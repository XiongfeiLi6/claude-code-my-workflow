# CLAUDE.MD -- JEEM Referee Workflow (Paper-First)

**Project:** Anonymous JEEM Referee Workflow (JEEM-D-26-00040)
**Institution:** Anonymous Reviewer
**Branch:** main

---

## Core Principles

- **Plan first** -- enter plan mode before non-trivial tasks; save plans to `quality_reports/plans/`
- **Spec before plan for ambiguity** -- create a MUST/SHOULD/MAY spec when scope is unclear
- **Contractor mode after approval** -- execute autonomously after plan approval, ask only on ambiguity/decisions
- **Milestone check-ins (early sessions)** -- report at stage boundaries: spec, plan, draft, verification, final
- **Evidence-grounded critique** -- every major claim in a review must map to manuscript text, table, or design choice
- **No fabrication** -- if content is uncertain or unreadable, state uncertainty explicitly
- **Anonymity by default** -- reports and artifacts use anonymous reviewer identity
- **Verify before delivery** -- no report is delivered without quality scoring + PDF rendering checks
- **[LEARN] tags** -- when corrected, save `[LEARN:category] wrong -> right` to MEMORY.md

---

## Folder Structure

```
claude-code-my-workflow/
├── CLAUDE.md                              # This file
├── .claude/                               # Rules, skills, agents, hooks
├── templates/                             # Report and workflow templates
├── scripts/                               # Utility scripts
├── quality_reports/
│   ├── specs/                             # Requirements specs
│   ├── plans/                             # Implementation plans
│   ├── session_logs/                      # Session logs
│   ├── merges/                            # Merge reports
│   └── referee_reports/                   # Referee report source artifacts
├── output/
│   └── pdf/                               # Final PDF deliverables
├── master_supporting_docs/
│   ├── supporting_papers/                 # Optional in-repo paper copies
│   └── supporting_slides/
└── docs/                                  # Existing docs assets
```

---

## Canonical Artifact Paths

- **Source manuscript (default):** external path allowed (outside repo root)
- **Optional manuscript copy (if requested):** `master_supporting_docs/supporting_papers/`
- **Structured review report (markdown):** `quality_reports/referee_reports/YYYY-MM-DD_[paper]_report.md`
- **PDF-ready source (quarto):** `quality_reports/referee_reports/YYYY-MM-DD_[paper]_report.qmd`
- **Final polished PDF:** `output/pdf/YYYY-MM-DD_[paper]_referee_report.pdf`

---

## Commands

```bash
# Quality score
python3 scripts/quality_score.py quality_reports/referee_reports/file_report.qmd

# Render polished referee report PDF
./scripts/render_referee_report.sh quality_reports/referee_reports/file_report.qmd

# Optional direct render (fallback)
quarto render quality_reports/referee_reports/file_report.qmd --to pdf
```

---

## Quality Thresholds

| Score | Gate | Meaning |
|-------|------|---------|
| 80 | Deliverable | Ready to share |
| 90 | Strong | Journal-grade rigor |
| 95 | Excellence | Exceptional clarity and polish |

---

## Skill Quick Reference

| Command | What It Does |
|---------|-------------|
| `/review-paper [file]` | Full manuscript referee review with dual-section output; `--peer JEEM` adds the simulated editor + referee pipeline |
| `/review-paper-light [file]` | Fast 3-agent triage: contribution, identification, overclaiming (~1-2 min) |
| `/review-paper-full [file] [journal]` | 7-agent deep scan: consistency, claims, math, tables, contribution |
| `/review-paper-code [dir]` | Review a replication package: code quality + paper-to-code mapping |
| `/seven-pass-review [file]` | 7 parallel lenses (abstract, intro, methods, results, robustness, prose, citations) |
| `/verify-claims [file]` | CoVe fact-check of evidence anchors via forked claim-verifier |
| `/respond-to-referees` | R&R rounds: audit whether prior concerns were addressed |
| `/humanize [file]` | AI-voice audit of report prose before delivery |
| `/question-quality [question]` | Gentzkow six-criterion lens on the paper's research question |
| `/audit-reproducibility` | Cross-check manuscript numbers against replication outputs |
| `/checkpoint` | Session-handoff snapshot for multi-session review work |
| `/proofread [file]` | Grammar/typo/style review of report artifacts |
| `/lit-review [topic]` | Literature search + synthesis support |
| `/context-status` | Session health + context usage |
| `/learn [skill-name]` | Persist reusable workflow lessons |
| `/deep-audit` | Repository-wide consistency audit |

**Referee agent cluster** (used by `--peer` mode and verification): `editor`, `domain-referee`, `methods-referee`, `claim-verifier`, `humanize-auditor`. Journal calibration in `.claude/references/journal-profiles.md` (includes a JEEM profile).

---

## Referee Report Standard (Default)

1. **Recommendation:** Reject / Major Revision / Minor Revision / Accept
2. **Confidential comments to editor:** publication fit, contribution significance, key risks
3. **Comments to authors:** actionable major + minor issues
4. **Evidence anchors:** page/section/table/figure references wherever possible
5. **Tone:** rigorous, constructive, professionally neutral

---

## Current Project State

| Item | Status | Notes |
|------|--------|-------|
| Workflow mode | Paper-first | Slide/TikZ/Beamer workflows retained but dormant |
| Reviewer identity | Anonymous | No personal/institutional signature in outputs |
| Check-in policy | Milestone | Extra stage-boundary updates in early sessions |
| Primary manuscript | `JEEM-D-26-00040.pdf` | Located outside repo root by user preference |
