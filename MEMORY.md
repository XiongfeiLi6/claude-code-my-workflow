# Project Memory

Corrections and learned facts that persist across sessions.
When a mistake is corrected, append a `[LEARN:category]` entry below.

---

<!-- Append new entries below. Most recent at bottom. -->

## Workflow Patterns

[LEARN:workflow] Requirements specification phase catches ambiguity before planning → reduces rework 30-50%. Use spec-then-plan for complex/ambiguous tasks (>1 hour or >3 files).

[LEARN:workflow] Spec-then-plan protocol: AskUserQuestion (3-5 questions) → create `quality_reports/specs/YYYY-MM-DD_description.md` with MUST/SHOULD/MAY requirements → declare clarity status (CLEAR/ASSUMED/BLOCKED) → get approval → then draft plan.

[LEARN:workflow] Context survival before compression: (1) Update MEMORY.md with [LEARN] entries, (2) Ensure session log current (last 10 min), (3) Active plan saved to disk, (4) Open questions documented. The pre-compact hook displays checklist.

[LEARN:workflow] Plans, specs, and session logs must live on disk (not just in conversation) to survive compression and session boundaries. Quality reports only at merge time.

## Documentation Standards

[LEARN:documentation] When adding new features, update BOTH README and guide immediately to prevent documentation drift. Stale docs break user trust.

[LEARN:documentation] Always document new templates in README's "What's Included" section with purpose description. Template inventory must be complete and accurate.

[LEARN:documentation] Guide must be generic (framework-oriented) not prescriptive. Provide templates with examples for multiple workflows (LaTeX, R, Python, Jupyter), let users customize. No "thou shalt" rules.

[LEARN:documentation] Date fields in frontmatter and README must reflect latest significant changes. Users check dates to assess currency.

## Design Philosophy

[LEARN:design] Framework-oriented > Prescriptive rules. Constitutional governance works as a TEMPLATE with examples users customize to their domain. Same for requirements specs.

[LEARN:design] Quality standard for guide additions: useful + pedagogically strong + drives usage + leaves great impression + improves upon starting fresh + no redundancy + not slow. All 7 criteria must hold.

[LEARN:design] Generic means working for any academic workflow: pure LaTeX (no Quarto), pure R (no LaTeX), Python/Jupyter, any domain (not just econometrics). Test recommendations across use cases.

## File Organization

[LEARN:files] Specifications go in `quality_reports/specs/YYYY-MM-DD_description.md`, not scattered in root or other directories. Maintains structure.

[LEARN:files] Templates belong in `templates/` directory with descriptive names. Currently have: session-log.md, quality-report.md, exploration-readme.md, archive-readme.md, requirements-spec.md, constitutional-governance.md.

## Constitutional Governance

[LEARN:governance] Constitutional articles distinguish immutable principles (non-negotiable for quality/reproducibility) from flexible user preferences. Keep to 3-7 articles max.

[LEARN:governance] Example articles: Primary Artifact (which file is authoritative), Plan-First Threshold (when to plan), Quality Gate (minimum score), Verification Standard (what must pass), File Organization (where files live).

[LEARN:governance] Amendment process: Ask user if deviating from article is "amending Article X (permanent)" or "overriding for this task (one-time exception)". Preserves institutional memory.

## Skill Creation

[LEARN:skills] Effective skill descriptions use trigger phrases users actually say: "check citations", "format results", "validate protocol" → Claude knows when to load skill.

[LEARN:skills] Skills need 3 sections minimum: Instructions (step-by-step), Examples (concrete scenarios), Troubleshooting (common errors) → users can debug independently.

[LEARN:skills] Domain-specific examples beat generic ones: citation checker (psychology), protocol validator (biology), regression formatter (economics) → shows adaptability.

## Memory System

[LEARN:memory] Two-tier memory solves template vs working project tension: MEMORY.md (generic patterns, committed), personal-memory.md (machine-specific, gitignored) → cross-machine sync + local privacy.

[LEARN:memory] Post-merge hooks prompt reflection, don't auto-append → user maintains control while building habit.

## Meta-Governance

[LEARN:meta] Repository dual nature requires explicit governance: what's generic (commit) vs specific (gitignore) → prevents template pollution.

[LEARN:meta] Dogfooding principles must be enforced: plan-first, spec-then-plan, quality gates, session logs → we follow our own guide.

[LEARN:meta] Template development work (building infrastructure, docs) doesn't create session logs in quality_reports/ → those are for user work (slides, analysis), not meta-work. Keeps template clean for users who fork.

[LEARN:workflow] This project runs in paper-first mode by default. Slide/Beamer/TikZ assets remain available but dormant unless explicitly requested.

[LEARN:workflow] Early sessions use milestone check-ins at stage boundaries: spec, plan, first draft, verification, final artifact.

[LEARN:governance] Reviewer identity is anonymous by default. Do not include personal or institutional identifiers in referee outputs.

[LEARN:files] Canonical report paths: quality_reports/referee_reports/ for source artifacts and output/pdf/ for final PDF deliverables.

[LEARN:pdf] For PDF QA in this environment, prefer Quarto render + pypdf validation, with Ghostscript raster preview fallback when pdftoppm is unavailable.

[LEARN:workflow] User preference: always generate PDF outputs after each completed work batch, not only source markdown/qmd artifacts.

[LEARN:workflow] Deliverable policy: maintain exactly the currently requested PDF set in `output/pdf/` (regenerate required PDFs each work batch and remove obsolete ones).

[LEARN:pdf] The render_referee_report.sh XeLaTeX fallback silently drops non-ASCII characters (unicode minus, en/em dashes -> negatives vanish from rendered numbers) and restarts markdown ordered-list numbering per item. Keep referee-report sources pure ASCII and use bold-paragraph numbering ("**1. Title.**") instead of markdown ordered lists.

[LEARN:pdf] Referee report delivery format: hand-authored .tex in the March 2026 template (12pt article, margin 1in, setstretch 1.5, tgpagella = Palatino, centered bold title block, numbered sections, itemize with bold labels), compiled with PDFLATEX. xelatex silently ignores tgpagella and produces Latin Modern; verify with pdffonts that TeXGyrePagella is embedded. md/qmd remain the quality-scored sources; the .tex is the styled delivery source.

[LEARN:workflow] Quality scorer requires the combined master report artifact (Category: line + "Confidential Comments to Editor" + "Comments to Authors" + "Major Concerns" + "Minor Concerns" headings) — score the combined _report.qmd; split author/editor PDFs are delivery artifacts derived from it (March 2026 and July 2026 rounds both follow this pattern).
