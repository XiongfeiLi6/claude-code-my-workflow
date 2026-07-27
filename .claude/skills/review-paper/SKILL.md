---
name: review-paper
description: Top-journal manuscript referee workflow with dual-section output (confidential editor comments + author comments), evidence anchors, and PDF-ready deliverables. Optional --peer mode runs a simulated editorial pipeline (editor + domain referee + methods referee, calibrated to a journal profile) to pressure-test the review before drafting. Evidence anchors are verified via forked claim-verifier before delivery.
argument-hint: "[path to manuscript PDF/TEX/QMD] [--peer <journal>] [--no-verify]"
allowed-tools: ["Read", "Grep", "Glob", "Write", "Bash", "Task"]
---

# Manuscript Referee Review (Paper-First)

Produce a rigorous, constructive review in journal-referee format — anonymous, evidence-anchored, delivered as a polished PDF.

> **Which review skill do I want?**
>
> - **`/review-paper`** (this skill) — the full referee deliverable: dual-section report + QMD + rendered PDF with quality gate. Best for an **actual referee assignment**.
> - **`/review-paper-light`** — fast 3-agent triage (~1–2 min): contribution, identification, overclaiming. Best **first pass** when the manuscript arrives.
> - **`/review-paper-full`** — 7-agent parallel deep scan (consistency, math, tables, claims). Best for **generating raw material** before drafting the report.
> - **`/seven-pass-review`** — seven independent lenses, maximum coverage. Best for **high-stakes or R&R-round** assignments.
> - **`/respond-to-referees`** — R&R rounds: audit whether your round-1 concerns were addressed in the resubmission.

## Inputs

- `$ARGUMENTS`: manuscript file path (external path allowed) or filename in `master_supporting_docs/supporting_papers/`
- `--peer <JOURNAL>` (optional): before drafting, run the simulated editorial pipeline calibrated to `<JOURNAL>` (default `JEEM`; see `.claude/references/journal-profiles.md`) to stress-test your assessment against independent referee personas.
- `--no-verify` (optional): skip the claim-verifier evidence-anchor check (not recommended for final delivery).

## Outputs (all required)

1. `quality_reports/referee_reports/YYYY-MM-DD_[paper]_report.md`
2. `quality_reports/referee_reports/YYYY-MM-DD_[paper]_report.qmd`
3. `output/pdf/YYYY-MM-DD_[paper]_referee_report.pdf`

## Workflow

1. Resolve manuscript path:
   - use direct path if provided (strip flags from `$ARGUMENTS` first)
   - fallback to `master_supporting_docs/supporting_papers/`
   - Glob for partial matches
2. Read manuscript end-to-end (chunk long PDFs with the `pages` parameter, e.g., 5 pages per chunk).
3. Evaluate across the 6 review dimensions (below); extract evidence-backed findings with manuscript anchors (section, page, table, figure, equation).
4. Generate 3–5 **referee objections** — the tough questions a top referee would ask (see below).
5. **If `--peer` is set:** run the simulated editorial pipeline (below) before drafting; fold robust cross-referee concerns into the report and discard disposition-idiosyncratic ones.
6. Draft structured report using `templates/referee-report.md`.
7. **Verify evidence anchors** (unless `--no-verify`): spawn `claim-verifier` via `Task` with `subagent_type=claim-verifier` and `context: fork`, passing each anchor claim ("Table 2 reports coefficient X", "Section 4.1 assumes Y") plus the manuscript path — never the draft report. Per `.claude/rules/post-flight-verification.md`: regenerate any section whose anchor FAILs; flag unverifiable anchors explicitly in the report.
8. Optionally run `/humanize` on the drafted report so the delivered prose reads as human referee writing.
9. Create PDF-ready QMD using `templates/referee-report.qmd`.
10. Render PDF via `./scripts/render_referee_report.sh <report.qmd>`.
11. Score quality via `python3 scripts/quality_score.py <report.qmd>`.
12. If score < 80, revise and re-run scoring.

## Review Dimensions

### 1. Argument Structure
- Is the research question clearly stated and well motivated?
- Is the logical flow sound (question → method → results → conclusion)?
- Are the conclusions supported by the evidence? Are limitations acknowledged?

### 2. Identification Strategy
- Is the causal claim credible? Are the key identifying assumptions stated explicitly?
- Threats: omitted variables, reverse causality, measurement error, spillovers/SUTVA (for environmental settings: pollution transport, leakage, spatial reallocation).
- Are robustness checks responsive to the obvious threats, or theater?
- Is the estimator appropriate for the research design?

### 3. Econometric Specification
- Correct standard errors (clustered at the right level? robust? bootstrap?)?
- Appropriate functional form? Sample selection issues? Multiple testing concerns?
- Are point estimates economically meaningful (not just statistically significant)?
- Exposure/outcome measurement credible (monitor coverage, satellite validation, coding reliability)?

### 4. Literature Positioning
- Are the key papers cited, and prior work characterized accurately?
- Is the contribution clearly differentiated from existing work?
- Any missing citations a referee would flag?

### 5. Writing Quality
- Clarity, concision, academic tone, consistent notation.
- Abstract effectively summarizes the paper.
- Tables and figures self-contained (labels, notes, sources). See `.claude/rules/manuscript-writing-style.md` as the evaluation rubric.

### 6. Presentation
- Table/figure design, notation consistency, typos, formatting.
- Is the paper the right length for the contribution?

## Referee Objections

For each of the 3–5 toughest questions:
- **Why it matters:** why this could be fatal to the paper.
- **What would change my mind:** the specific analysis, evidence, or argument that would resolve it. Every Major concern in the final report must carry this.

## `--peer` Mode (simulated editorial pipeline)

Uses the agent trio (adapted from Hugo Sant'Anna's clo-author): `.claude/agents/editor.md`, `.claude/agents/domain-referee.md`, `.claude/agents/methods-referee.md`, calibrated by `.claude/references/journal-profiles.md` (a `JEEM` profile ships in this repo).

1. **Editor desk review** (forked subagent): fit, contribution, desk-reject criteria → `quality_reports/peer_review_[paper]/desk_review.md`. WebSearch novelty-probe claims must pass claim-verifier before entering the narrative.
2. **Referee selection:** editor draws 2 different dispositions from the journal's referee-pool weights (STRUCTURAL / CREDIBILITY / MEASUREMENT / POLICY / THEORY / SKEPTIC) plus pet peeves.
3. **Two blind referees in parallel** (forked): `domain-referee` → `referee_domain.md`; `methods-referee` → `referee_methods.md`. Each MAJOR concern includes "What would change my mind".
4. **Editor synthesis:** classify concerns FATAL / ADDRESSABLE / TASTE → `editorial_decision.md`.
5. **Use, don't copy:** treat pipeline output as raw material. Concerns raised by multiple personas are robust — anchor and adopt them. Single-persona concerns are disposition-dependent — adopt only with your own judgment. The delivered report is yours, in your voice, under your recommendation.

## Required Report Structure

- Recommendation: Reject / Major Revision / Minor Revision / Accept
- Confidential Comments to Editor (fit, contribution significance, key risks, bottom line)
- Comments to Authors (never reveals confidential content or recommendation rationale meant for the editor)
- Major Concerns (actionable, evidence-anchored, each with severity, suggested fix, and "what would change my mind")
- Minor Concerns

## Issue Taxonomy

Use this severity scale:
- **Fatal**: publication-blocking identification/validity issue
- **Major**: core design, inference, or interpretation weakness
- **Moderate**: important but fixable clarity/robustness issue
- **Minor**: style, phrasing, formatting, small omissions

## Principles

- No fabricated claims, numbers, or references — every anchor verified before delivery (Article III).
- If evidence is uncertain, state uncertainty directly.
- Keep editor comments confidential and distinct from author-facing tone (Article IV).
- Be rigorous and specific; each major concern needs a suggested fix and a "what would change my mind".
- Be constructive; acknowledge what is done well.
- Preserve reviewer anonymity in all artifacts.
