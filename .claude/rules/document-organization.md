# Document Organization: Where Working Markdown Goes

**No working `.md` files in the project root, in source/manuscript folders, or loose at the top of
`quality_reports/`.** Every working document has a typed home. This rule exists because review reports,
strategy docs, research memos, and roadmaps tend to accumulate wherever they were first written (the
repo root, a manuscript folder, the top of `quality_reports/`), which makes a project hard to navigate
and makes the next session waste time hunting for the current plan.

---

## The only `.md` files allowed in the project root

| File | Purpose |
|---|---|
| `CLAUDE.md` | Project instructions (loaded every session) |
| `MEMORY.md` | `[LEARN]` index (loaded every session) |
| `README.md` | Repo readme |

**Nothing else.** Any other `.md` created at the root is misplaced — move it to the right subdir below.

## `quality_reports/` taxonomy

All project working documents live under `quality_reports/` in a typed subdir:

| Subdir | What goes here | Naming |
|---|---|---|
| `strategy/` | Roadmaps, revision/research strategy, and the project's master task list (the session entry point) | `MASTER_TASK_LIST.md` (stable); other docs `YYYY-MM-DD_description.md` |
| `reviews/` | All review + proofread reports (referee reports, pre-submission reviews, review-of-reviews, code reviews) | `YYYY-MM-DD_description.md` or a skill-defined stable prefix |
| `research/` | Research memos (literature notes, institutional/background research, data-feasibility audits) | `YYYY-MM-DD_description.md` |
| `plans/` | Implementation plans (plan-first workflow) | `YYYY-MM-DD_short-description.md` |
| `specs/` | Requirements specs | `YYYY-MM-DD_description.md` |
| `session_logs/` | Session logs | `YYYY-MM-DD_description.md` |
| `audits/` | Consistency / data / infrastructure audits | `YYYY-MM-DD_description.md` |
| `merges/` | Merge quality reports (merge time only) | `YYYY-MM-DD_[branch].md` |

Create a subdir only when you have a document for it; don't scaffold empty folders. If a doc fits none of
the above, it usually belongs in `research/` (a finding) or `strategy/` (a plan of what to do).

## Naming convention

- **Dated working docs:** `YYYY-MM-DD_kebab-case-description.md`.
- **Stable canonical docs** (one per project, updated in place, never dated in the filename) — e.g. a
  master task list or a data inventory. Put the "Last updated" date *inside* the file, not in the name,
  so pointers to it never break.

## Optional: a master task list as the session entry point

For a long-running project, keep a single living to-do at a **stable path** (e.g.
`quality_reports/strategy/MASTER_TASK_LIST.md`) and point to it from `CLAUDE.md` so a new session reads
it first, then the docs it links, then works the highest-priority open task. Give it a short
"NEW SESSION? START HERE" header and a linked-context list. Update it in place as tasks complete. This is
what lets a fresh session resume without re-deriving the plan from git history.

## Skills and agents that generate reports

Any skill or agent that writes a report (a referee report, a proofread, an audit, a research memo) MUST
target the correct `quality_reports/` subdir — not the current working directory. A report skill that
defaults to the cwd is how documents end up in the repo root. When you author or edit such a skill, set
its save path to the matching subdir (reviews → `reviews/`, audits → `audits/`, etc.).

## Self-check before creating a doc

Before writing any `.md`, ask: *which typed subdir does this belong in?* If you're about to write to the
root, a source/manuscript folder, or the top of `quality_reports/`, stop and pick the right subdir.

## Adapting this rule

The folder names above (`quality_reports/...`) are this template's convention and are shared by the other
rules (`session-logging.md`, `proofreading-protocol.md`, etc.). If a project uses a different reports
root, rename consistently across rules and update `CLAUDE.md`. The principle is invariant across domains —
econ papers, biology lab protocols, CS project notes, a writing project — only the folder labels change.
