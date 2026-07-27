# Plan: Import Referee-Relevant Assets from Reusable Workflow Repo

**Date:** 2026-07-24
**Source:** `/Users/xiongfei/Documents/GitHub/claude-code-my-workflow` (my-customization reusable workflow)
**Destination:** this repo (JEEM referee workflow, paper-first mode)
**Trigger:** User request — compare skills/rules/agents and import relevant ones (writing rules, review rules, skills).

## Selection Rationale

Two parallel assessment agents read all source-only candidates. Selection criteria:
relevant to manuscript refereeing / report writing / evidence integrity; skip
slide-specific, grant/PAP, prompt-engineering, and source-repo-maintenance assets.

## Import List

### Agents (new) — the referee agent cluster
- `agents/claim-verifier.md` — CoVe fresh-context evidence verifier (enforces Article III)
- `agents/domain-referee.md` — contribution/fit referee persona
- `agents/methods-referee.md` — paper-type-aware methodology referee with sanity-check blockers
- `agents/editor.md` — desk review + editorial synthesis persona
- `agents/humanize-auditor.md` — AI-voice audit of report prose

### Rules (new)
- `rules/manuscript-writing-style.md` — writing standard; doubles as referee evaluation rubric
- `rules/post-flight-verification.md` — CoVe anti-hallucination protocol
- `rules/document-organization.md` — quality_reports taxonomy (adapt: referee_reports/)
- `rules/summary-parity.md` — summary/body drift prevention
- `rules/model-routing.md` — model-tier routing (slide agents exist here, dormant)
- `rules/skill-promotion-policy.md` — [LEARN] → draft skill → skill thresholds

### References (new directory)
- `references/journal-profiles.md` — + add a JEEM field-journal profile
- `references/discipline-cards.md` — econ method conventions

### Skills (new)
- review-paper-full, review-paper-light, review-paper-code
- seven-pass-review (adapt lens 3 → domain-referee)
- verify-claims, respond-to-referees, humanize (adapt all-mode globs), question-quality
- checkpoint, audit-reproducibility

### Templates (new)
- journal-profile-template.md, response-to-referees.md, decision-record.md

### Merge (not overwrite)
- `skills/review-paper/SKILL.md`: keep JEEM shell (dual-section output, Reject/Major/Minor/Accept,
  qmd→PDF pipeline, quality gate ≥80, anonymity, external manuscript path) and import from source:
  itemized 6-dimension rubric, referee objections, `--peer` editor+referee pipeline, CoVe verification step.

### Explicitly NOT imported
- content-invariants (slide/R-specific), cross-artifact-review (no-op without author code, and
  depends on review-r pathways already present if needed later), audit-pet-peeves (source-repo PR history),
  prompt-formatting-core + prompt/prompt-only (orphaned), review-grant, review-pap, stata suite,
  codex, compress-session, context-audit, permission-check, preregister, promote-memory (+council),
  new-diagram, text-classify, simulation-study, stata-replication, r-package-check (+conventions),
  tikz-measurement/prevention (slide), and all files that already exist locally with paper-first
  customizations (no overwrites of locally modified shared files).

## Verification
1. All copied files exist and are readable.
2. Adapted files: humanize globs, seven-pass lens 3, document-organization subdir names, JEEM journal profile added.
3. CLAUDE.md Skill Quick Reference updated with new commands.
4. Cross-references in imported files resolve to files present in this repo (spot check).
