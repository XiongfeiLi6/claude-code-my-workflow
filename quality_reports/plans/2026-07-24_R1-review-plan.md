# Plan: Round-2 (Revision-Stage) Referee Review — JEEM-D-26-00040R1

## Context

You refereed JEEM-D-26-00040 ("Monitoring the Monitors") in March 2026 with a Major Revision recommendation (6 major + 6 secondary comments). The authors have resubmitted (now titled "Environmental Governance and Bureaucratic Incentives in China's Clean-Air Campaign"). Your task now is the revision-stage review: audit whether each round-1 concern was addressed, evaluate the new material, and deliver a round-2 recommendation.

**You are Referee 2** — the point-by-point response on pp. 13–22 of the R1 file mirrors your report's numbering exactly.

## Source documents (all in the parent Dropbox folder)

| Document | Path / pages |
|----------|--------------|
| Your round-1 report | `Reviewer Report.pdf` (5 pp: §3.1–3.6 major, §4.1–4.6 secondary) |
| Initial submission | `JEEM-D-26-00040.pdf` (36 pp) — reference for before/after checks |
| Cover letter to editor | `JEEM-D-26-00040_R1_reviewer.pdf` pp. 2–6 |
| Response to YOU (Ref 2) | same file, pp. 13–22 |
| Response to Referee 1 | same file, pp. 7–12 (context only) |
| Online appendix (revised) | same file, pp. 23–42 |
| Revised manuscript | same file, pp. 43–87 |

## Deliverables (agreed)

Same format as round 1:
1. `quality_reports/referee_reports/2026-07-24_JEEM-D-26-00040_R1_author_report.{md,qmd}` + `output/pdf/..._author_report.pdf`
2. `quality_reports/referee_reports/2026-07-24_JEEM-D-26-00040_R1_editor_report.{md,qmd}` + `output/pdf/..._editor_report.pdf`
- Rendered via `./scripts/render_referee_report.sh`; quality gate `python3 scripts/quality_score.py` ≥ 80.
- Anonymous reviewer identity throughout (Article IV).

## Depth (agreed): Standard R2 audit

Concern-by-concern verification + close review of new material. No full fresh-eyes rescan.

## Workflow

### Phase 1 — Concern matrix construction
Decompose your round-1 report into discrete tracked concerns (R2.1–R2.6 major from §3.1–3.6; S1–S6 secondary from §4.1–4.6). For each: the original ask, in one sentence.

### Phase 2 — Response + revised-text audit (core of the review)
For each concern, following the `/respond-to-referees` classification logic (referee-side):
1. Read the authors' response (pp. 13–22) — what they CLAIM they did.
2. Verify against the revised manuscript (pp. 43–87) and appendix (pp. 23–42) — what they ACTUALLY did. Never accept a response-letter claim without locating it in the revised text.
3. Classify: **Resolved / Partially resolved / Not addressed / Reasonable disagreement**, with page/table/figure anchors in the revised version.

Key items to verify closely (new material the revision hinges on):
- **Event study** (Figure 3, ~p. 67): flat pre-trends claim; gradual post-adoption slope emerging after ~3 event years; whether the reframing to "reduced-form effect of the monitoring-and-disclosure regime" is consistently carried through the paper's title/abstract/intro/conclusion claims.
- **Rewritten model**: CARA utility, risk-premium term, multitask W_t = π̄_t − γ_tS + δ_tG, Proposition 1 comparative statics in four primitives — check internal consistency and whether the model-empirical mapping now supports the interpretation.
- **Promotion coding** (your §3.3): sub-provincial/provincial-capital lateral moves coded as promotions; demoted/disciplined officials now IN baseline with exclusion as robustness — verify the robustness table exists and behaves as claimed.
- **IV exclusion** (your §3.4): Appendix Table 2 (inversions vs. visibility/dew point/min temperature); weather controls robustness — check magnitudes, not just existence.
- **Effort measure validation** (your §3.5): Appendix Figure 2 (category adoption trends); waste-gas investment proxy (Appendix Tables 4, 6) — note authors admit only provincial-level and not always significant at 95%; judge whether this meets your bar.
- **PPML replacement** of log(1+days) (your §4.2, Appendix Table 5).
- **Information-gains heterogeneity test** (115-city pre-existing network) — NEW analysis supporting the observability mechanism; scrutinize its identification logic (representativeness caveat the authors themselves flag).
- Spot-check the pre-period coefficient narrative (your §4.1) and whether "zero before" claims were tempered.

### Phase 3 — New-issues sweep (bounded)
The revision introduces new analyses that can carry new problems. Check only the new/changed sections for: internal consistency (text vs. table numbers), overclaiming relative to the event-study evidence, and whether the mechanism language ("at least part of this change occurred through an observability-and-incentives mechanism") stays within what the information-gains test can support.

### Phase 4 — Draft the two reports
- **Author report**: concern-by-concern table (status: Resolved/Partial/Not addressed) + detailed remaining requests with revised-manuscript anchors + any new concerns. Constructive tone; every remaining major ask includes "what would satisfy this."
- **Editor report**: bottom-line assessment of revision quality, which concerns remain publication-relevant, and recommendation. Recommendation vocabulary: Accept / Minor Revision / Major Revision / Reject — decided by the audit outcome, discussed with you before finalizing (milestone check-in).

### Phase 5 — Verification & delivery (Article III + V)
1. `claim-verifier` (forked, fresh context) checks every evidence anchor in the drafted reports against the R1 PDF — page/table/figure/coefficient citations.
2. Optional `/humanize` pass on report prose.
3. Render both QMDs → PDFs; quality score ≥ 80 each; confirm PDFs exist and are readable.
4. Per your deliverable policy: regenerate the current PDF set in `output/pdf/` (the two R1 PDFs are added; March PDFs remain unless you say to remove them — will ask at delivery).

## Milestone check-ins

1. After Phase 2: concern matrix with classifications — **you review before drafting** (this is the substantive judgment step where we work together).
2. After Phase 4 draft: recommendation discussion.
3. Final: PDFs + scores.

## Files to create

- `quality_reports/plans/2026-07-24_R1-review-plan.md` (copy of this plan, per repo convention)
- `quality_reports/referee_reports/2026-07-24_JEEM-D-26-00040_R1_concern_matrix.md` (Phase 2 working artifact)
- The four report artifacts + two PDFs listed under Deliverables
- Session log `quality_reports/session_logs/2026-07-24_R1-review.md`

## Verification

- Every classification in the concern matrix carries a revised-manuscript anchor (page/section/table).
- claim-verifier PASS (or explicit uncertainty flags) on both reports before rendering.
- Both PDFs render, score ≥ 80, non-zero size.
