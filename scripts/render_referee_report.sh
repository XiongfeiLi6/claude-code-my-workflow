#!/bin/bash
# Render a referee report QMD to PDF and place final artifact in output/pdf.
# Primary path: Quarto render
# Fallback path: local markdown->LaTeX conversion + XeLaTeX

set -euo pipefail

if [ $# -ne 1 ]; then
  echo "Usage: $0 <path-to-report.qmd>"
  exit 1
fi

REPORT_QMD="$1"
if [ ! -f "$REPORT_QMD" ]; then
  echo "Error: file not found: $REPORT_QMD"
  exit 1
fi

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
mkdir -p "$REPO_ROOT/output/pdf" "$REPO_ROOT/tmp/pdfs"

BASENAME="$(basename "$REPORT_QMD" .qmd)"
SOURCE_DIR="$(cd "$(dirname "$REPORT_QMD")" && pwd)"
SOURCE_FILE="$(basename "$REPORT_QMD")"
SOURCE_PDF="$SOURCE_DIR/${BASENAME}.pdf"

render_with_quarto() {
  pushd "$SOURCE_DIR" >/dev/null
  if quarto render "$SOURCE_FILE" --to pdf; then
    popd >/dev/null
    return 0
  fi
  popd >/dev/null
  return 1
}

render_with_xelatex_fallback() {
  local tmp_tex="$SOURCE_DIR/${BASENAME}_fallback.tex"
  local tmp_pdf="$SOURCE_DIR/${BASENAME}_fallback.pdf"

  python3 - "$REPORT_QMD" "$tmp_tex" <<'PY'
import re
import sys
from pathlib import Path

qmd_path = Path(sys.argv[1])
tex_path = Path(sys.argv[2])

raw = qmd_path.read_text(encoding="utf-8")
if raw.startswith("---\n"):
    parts = raw.split("\n---\n", 1)
    body = parts[1] if len(parts) == 2 else raw
else:
    body = raw

def latex_escape(text: str) -> str:
    text = text.replace("\\", r"\textbackslash{}")
    text = text.replace("&", r"\&")
    text = text.replace("%", r"\%")
    text = text.replace("$", r"\$")
    text = text.replace("#", r"\#")
    text = text.replace("_", r"\_")
    text = text.replace("{", r"\{")
    text = text.replace("}", r"\}")
    text = text.replace("^", r"\textasciicircum{}")
    text = text.replace("~", r"\textasciitilde{}")
    return text

def inline_format(text: str) -> str:
    # Basic support for bold and inline code.
    code_tokens = {}
    def store_code(match):
        token = f"__CODE_{len(code_tokens)}__"
        code_tokens[token] = match.group(1)
        return token

    text = re.sub(r"`([^`]+)`", store_code, text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"ZZBOLDSTARTZZ\1ZZBOLDENDZZ", text)
    text = latex_escape(text)
    text = text.replace("ZZBOLDSTARTZZ", r"\textbf{").replace("ZZBOLDENDZZ", "}")

    for token, code in code_tokens.items():
        text = text.replace(latex_escape(token), r"\texttt{" + latex_escape(code) + "}")
    return text

lines = body.splitlines()
out = []
in_itemize = False
in_enum = False

def close_lists():
    global in_itemize, in_enum
    if in_itemize:
        out.append(r"\end{itemize}")
        in_itemize = False
    if in_enum:
        out.append(r"\end{enumerate}")
        in_enum = False

for line in lines:
    s = line.rstrip()
    stripped = s.strip()

    if stripped == "":
        close_lists()
        out.append("")
        continue

    if stripped.startswith("#### "):
        close_lists()
        out.append(r"\subsubsection*{" + inline_format(stripped[5:]) + "}")
        continue
    if stripped.startswith("### "):
        close_lists()
        out.append(r"\subsection*{" + inline_format(stripped[4:]) + "}")
        continue
    if stripped.startswith("## "):
        close_lists()
        out.append(r"\section*{" + inline_format(stripped[3:]) + "}")
        continue
    if stripped.startswith("# "):
        close_lists()
        out.append(r"\section*{" + inline_format(stripped[2:]) + "}")
        continue

    ordered = re.match(r"^\d+\.\s+(.*)$", stripped)
    if ordered:
        if in_itemize:
            out.append(r"\end{itemize}")
            in_itemize = False
        if not in_enum:
            out.append(r"\begin{enumerate}[leftmargin=*, itemsep=0.25em, topsep=0.4em]")
            in_enum = True
        out.append(r"\item " + inline_format(ordered.group(1)))
        continue

    if stripped.startswith("- "):
        if in_enum:
            out.append(r"\end{enumerate}")
            in_enum = False
        if not in_itemize:
            out.append(r"\begin{itemize}[leftmargin=*, itemsep=0.25em, topsep=0.4em]")
            in_itemize = True
        out.append(r"\item " + inline_format(stripped[2:]))
        continue

    close_lists()
    out.append(inline_format(stripped))
    out.append("")

close_lists()

tex = r"""\documentclass[11pt]{article}
\usepackage[margin=1in]{geometry}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage{enumitem}
\usepackage{parskip}
\setlength{\parskip}{0.55em}
\setlength{\parindent}{0pt}
\begin{document}
""" + "\n".join(out) + "\n\\end{document}\n"

tex_path.write_text(tex, encoding="utf-8")
print(tex_path)
PY

  pushd "$SOURCE_DIR" >/dev/null
  xelatex -interaction=nonstopmode "$(basename "$tmp_tex")" >/dev/null || true
  popd >/dev/null

  if [ ! -s "$tmp_pdf" ]; then
    echo "Fallback XeLaTeX render failed: $tmp_pdf not produced"
    return 1
  fi

  mv "$tmp_pdf" "$SOURCE_PDF"
  rm -f "$SOURCE_DIR/${BASENAME}_fallback.aux" \
        "$SOURCE_DIR/${BASENAME}_fallback.log" \
        "$SOURCE_DIR/${BASENAME}_fallback.tex"
}

if ! render_with_quarto; then
  echo "Quarto render unavailable in this environment, using XeLaTeX fallback."
  render_with_xelatex_fallback
fi

if [ ! -s "$SOURCE_PDF" ]; then
  echo "Error: expected PDF not generated: $SOURCE_PDF"
  exit 1
fi

if [[ "$BASENAME" == *_report ]]; then
  TARGET_BASE="${BASENAME%_report}_referee_report"
else
  TARGET_BASE="$BASENAME"
fi

TARGET_PDF="$REPO_ROOT/output/pdf/${TARGET_BASE}.pdf"
cp "$SOURCE_PDF" "$TARGET_PDF"
rm -f "$SOURCE_PDF"

echo "Rendered PDF: $TARGET_PDF"
