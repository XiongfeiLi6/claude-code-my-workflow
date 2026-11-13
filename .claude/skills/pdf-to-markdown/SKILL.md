---
name: pdf-to-markdown
description: Split a PDF into chunks and convert it to readable markdown text. Use when the user wants to read, extract, or convert a PDF document.
user-invocable: true
argument-hint: [path/to/file.pdf]
allowed-tools: Read, Bash(mdls *), Bash(pdftotext *), Bash(which *), Write
---

# PDF Split & Convert

Convert a PDF file to readable markdown text. Handles large PDFs efficiently.

## Input

- `$ARGUMENTS[0]` — Path to the PDF file (required)

## Select coverage from the request

Default to the complete document, including references, appendices and supplements.
For a specified page range, extract that range. Use main-text-only trimming only
when the user requests it; a request to read or review a paper does not imply it.
Record source filename, total pages, selected pages and omissions. Preserve the
original PDF and any existing extracted file; use a distinct output name when needed.

## Choose the method first

Before reading anything, check whether `pdftotext` (part of poppler) is available:

```bash
which pdftotext
```

- **If available** → use the **pdftotext path** below. It extracts text mechanically without rendering every page. Inspect the actual PDF pages when equations, tables, figures or layout are important; extracted text alone can lose structure.
- **If not available** → fall back to the **Read-tool path**. Use the available PDF reader in bounded page ranges and report unreadable pages. Runtime limits depend on the installed tools; do not assume fixed timeout limits.

## Resolve the path and get page count

1. If the path is relative, resolve it relative to the current working directory.
2. Run `mdls -name kMDItemNumberOfPages "<pdf_path>"` to get the total page count. If `mdls` is unavailable or returns `(null)`, use `pdftotext` or Read to probe.

## Method A — pdftotext (preferred)

For an explicit page range, add `-f FIRST -l LAST` to `pdftotext` and set the marker start to FIRST. Otherwise extract the full PDF to text in one shot, retain all sections and add page markers. Trim only for an explicit main-text-only request. `pdftotext` emits a form-feed character (`\f`) at every page break — use that for pagination.

Reference implementation (bash + awk):

```bash
set -e
set -o noclobber  # Preserve any existing output; choose another OUT path if needed
PDF="$1"
OUT="${PDF%.pdf}.md"
TITLE=$(basename "${PDF%.pdf}")
MAIN_TEXT_ONLY=0  # Set to 1 only for an explicit main-text-only request
TMPTXT=$(mktemp)
trap 'rm -f "$TMPTXT"' EXIT

pdftotext -layout "$PDF" "$TMPTXT"

awk -v title="$TITLE" -v main_text_only="$MAIN_TEXT_ONLY" '
BEGIN {
    print "# " title
    print ""
    page = 1
    printf "---\n## Pages %d-%d\n---\n", page, page+19
    next_marker = page + 20
}
{
    # Convert form-feed page breaks to newlines and count pages
    n = gsub(/\f/, "\n")
    if (n > 0) {
        page += n
        if (page >= next_marker) {
            printf "\n---\n## Pages %d-%d\n---\n", next_marker, next_marker+19
            next_marker += 20
        }
    }

    # Build a stripped copy for heading detection.
    # CRITICAL: strip both form feeds AND embedded newlines — gsub above inserts
    # newlines into $0, which will defeat regex anchors like ^ and $ if you skip this.
    stripped = $0
    gsub(/[\f\n]/, "", stripped)
    sub(/^[ \t]+/, "", stripped)
    sub(/[ \t]+$/, "", stripped)

    if (main_text_only && length(stripped) > 0) {
        # References / Bibliography — standalone word, optionally numbered, short, no prose punctuation
        if (length(stripped) < 50 && stripped !~ /[(),;]/) {
            if (stripped ~ /^([0-9]+\.?[ \t]+)?(References|REFERENCES|Bibliography|BIBLIOGRAPHY)$/) exit
            if (stripped == "Works Cited") exit
        }

        # Appendix — length up to ~120 chars (some titles are long), no prose punctuation
        if (length(stripped) < 120 && stripped !~ /[(),;]/) {
            # "Appendix A" alone (bare letter, no title)
            if (stripped ~ /^Appendix[ \t]+[A-Z][0-9]*$/) exit
            # "Appendix A. Title" or "Appendix A: Title" — punctuation REQUIRED to avoid
            # matching body-text references like "Appendix H examines the effect..."
            if (stripped ~ /^Appendix[ \t]+[A-Z][0-9]*[.:][ \t]+[A-Z].*$/) exit
            # "APPENDIX A" variants
            if (stripped ~ /^APPENDIX[ \t]+[A-Z][0-9]*([ \t]+.*)?$/) exit
            # "Online Appendix [A]"
            if (stripped ~ /^Online[ \t]+Appendix([ \t]+[A-Z].*)?$/) exit
            # "Supplemental/Supplementary/Internet Appendix"
            if (stripped ~ /^(Supplement(al|ary)|Internet)[ \t]+Appendix([ \t]+.*)?$/) exit
        }
    }

    print
}
' "$TMPTXT" > "$OUT"

rm -f "$TMPTXT"
echo "Wrote $OUT ($(wc -l < "$OUT") lines)"
```

After extraction, compare coverage with the selected pages and inspect the beginning,
end and relevant dense pages. In full-document mode, references and appendices must
remain. In main-text-only mode, inspect the proposed cut point in the original PDF;
heading detection can match a contents entry or body text. Do not claim complete
coverage when pages were omitted or text extraction failed. The example markers
label nominal 20-page chunks; report the actual final page separately.

## Method B — Read tool (fallback when pdftotext unavailable)

1. Read the selected pages in bounded chunks supported by the available PDF reader, preserving page numbers.
2. Include references and appendices by default. Stop at the confirmed main-text boundary only when that scope was explicitly requested.
3. Compile output:
   - Save alongside the PDF with a `.md` extension.
   - Header: `# [Original Filename]`
   - Page markers between chunks: `---\n## Pages X-Y\n---`
   - Preserve extracted text as-is.

Use a local OCR tool if scanned pages have no usable text and it is available. Do not upload documents to an external conversion service without authorization. Check important equations, tables and figures against rendered pages.

## Heading-detection pitfalls (hard-won lessons)

These false positives broke earlier attempts — keep them in mind whether you use Method A or B:

- **Parenthetical references in body text** like `(see Appendix B.5)` — exclude lines containing `(`, `)`, `,`, or `;`.
- **Body text starting with "Appendix X ..."** like `Appendix H examines the differential effect...` — require punctuation (`.` or `:`) immediately after the appendix letter when a title follows. Bare "Appendix A" alone on a line is still valid.
- **Line-wrapped headings** — `pdftotext` can wrap `Online Appendix` across two lines if the PDF's layout is unusual. You'll see `Online` on one line and `Appendix` on the next. The regex above matches the joined form; if you see false trims at a lone `Appendix` line, inspect and tighten.
- **Form-feed at start of page** — `pdftotext` emits `\f` as the first character on every new page. After `gsub(/\f/, "\n")` on `$0`, the line has an embedded `\n` that defeats `^` / `$` anchors unless you also `gsub(/[\f\n]/, "", stripped)` on your detection copy.
- **Length thresholds** — simple "< 50 chars" is too tight for appendix titles. "Appendix A. Merging Mortgages with the Real Estate Database" is 59 chars. Use ~120 for appendix patterns, ~50 for bare References.
- **Numbered section headings** — some papers format as `7 References` or `7. References`. Allow an optional leading number.

## Report results

Tell the user:
- Method used (pdftotext vs Read tool)
- Total pages processed
- Output file path and final line count
- Selected scope and any exclusions; the confirmed trim point only if trimming was requested
- Any pages that were unreadable or empty

For batch conversions, print a summary table and note any files whose trim point looks suspicious (very short output, or output ending mid-sentence).
