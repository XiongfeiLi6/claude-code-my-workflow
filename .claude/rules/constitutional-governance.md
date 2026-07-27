# Constitutional Governance -- JEEM Referee Workflow

This file defines immutable principles for this project. Preferences can vary, but these articles are default non-negotiables unless explicitly amended.

## Article I: Primary Artifact

Referee reports are authoritative source artifacts.

- Markdown review: `quality_reports/referee_reports/*.md`
- PDF-ready Quarto source: `quality_reports/referee_reports/*.qmd`
- Final output: `output/pdf/*.pdf`

Why this matters: judgment reasoning and final PDF must remain synchronized.

## Article II: Plan-First Threshold

Enter plan mode for any task that is multi-step, multi-file, or affects substantive judgment.

Exceptions:
- Single typo fixes
- Trivial path updates

Why this matters: avoids silent scope drift and inconsistent review standards.

## Article III: Evidence Integrity

No fabricated evidence. Every major concern must be anchored to manuscript content (section, page, table, figure, equation, or explicit textual quote/paraphrase).

If evidence is unclear or missing, mark uncertainty directly.

Why this matters: reviewer credibility and editorial reliability depend on traceable claims.

## Article IV: Anonymity and Separation

Reports must maintain anonymous identity and separate:
- Confidential comments to editor
- Comments to authors

Why this matters: protects review process integrity and avoids accidental disclosure.

## Article V: Verification Before Delivery

No deliverable is complete without:
- render check (QMD -> PDF succeeds)
- artifact check (PDF exists, non-zero size, readable)
- quality score >= 80

Why this matters: prevents broken or low-quality outputs.

## User-Overridable Preferences

These are flexible per task:
- recommendation strictness in borderline cases
- narrative length/detail level
- wording style (direct vs nuanced)
- optional appendices/checklists

## Amendment Protocol

When a request conflicts with an article, ask whether this is:
1. Permanent amendment to the article, or
2. One-time task override.
