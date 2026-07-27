---
paths:
  - "master_supporting_docs/**"
  - "quality_reports/referee_reports/**"
  - "output/pdf/**"
---

# PDF Processing Protocol (Paper Review)

Use robust, chunked PDF workflows for long manuscripts and publication-grade outputs.

## Input Processing

1. Resolve manuscript path in this order:
   - direct path supplied by user (can be outside repo)
   - `master_supporting_docs/supporting_papers/`
2. Inspect basic properties using Python (`pypdf`) when `pdfinfo` is unavailable.
3. For long manuscripts, extract/read in chunks (for example 5 pages at a time).
4. Track uncertainty if text extraction is noisy.

## Output Processing

1. Render referee report QMD to PDF.
2. Validate using Python:
   - file exists
   - non-zero size
   - page count >= 1
3. Generate raster preview for layout QA:
   - `pdftoppm` if available
   - Ghostscript fallback otherwise

## Quality Requirements

- Consistent typography and section hierarchy
- No clipped/overlapping text
- Clear separation of editor vs author sections
- Human-readable references and labels
- ASCII hyphens only

## Error Handling

If parsing or rendering fails:
1. capture exact error
2. retry with fallback method
3. if still failing, report blocker and partial progress with clear next action
