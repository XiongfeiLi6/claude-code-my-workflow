# Token Economy — performance first, but the session must last

**Goal:** a five-hour working session on the main model without a compaction that loses the
thread, and without paying Fable prices for work a cheaper tier does as well. This is a balance
rule, not a saving rule: judgment stays on the best model; search, inventory, and mechanical
implementation do not.

Paid for on 2026-09-02 in a course repo forked from this template: the configuration session
reached 82 % of context on setup work alone. Most of the spend was avoidable (table at the end).

## 1. Subagents: tier by task, cap the report

| Subagent kind | Model to pass at launch | Why |
|---|---|---|
| `Explore`, `Plan`, file/asset inventories, PDF extraction | `sonnet` (`haiku` for pure listings) | search-and-summarize; inherits Fable otherwise |
| Review lenses (`domain-reviewer`, `claim-verifier`, `methods-referee`, `tikz-reviewer`, …) | as pinned in their frontmatter (`model-routing.md`) | judgment work; do not demote |
| `verifier` before a `main` commit | as pinned | gate |

Every subagent prompt ends with a **report contract**: a size cap (≤ 150 lines), tables with
paths and line numbers, no verbatim reproduction unless the text will be copied into a deliverable.
An unbounded report is paid for twice — once by the agent, once when it lands in the main context.

## 2. Reading: once, and only the part you need

- `grep -n` or `Read` with `offset`/`limit` before any whole-file read.
- A file is read once per session; note the facts you need in the plan or session log rather than
  re-reading.
- No whole-file `cat` above ~150 lines without a stated reason; a 30 KB tool result persisted to
  disk is a sign the read was too wide.

## 3. Editing: the tool that does not echo

- **Files already read → the Edit tool.** A script edit (`sed`, Python) on a file the harness has
  seen causes the whole changed file to be echoed back into context.
- **Files not yet read → a script**, batched, one Bash call.
- Resolve the write path and its constraints (was it read? is it a protected path?) before
  generating content. Every artifact is generated once; a rejected Write is a full re-generation.

## 4. Session shape

- **Fable for design turns**: planning, decisions, anything that needs judgment about the course.
- **`/model opus` (or `/effort medium`) for implementing an approved spec**: writing a batch of
  documents from a fixed table, applying a review's mechanical findings, building PDFs. Effort is the first
  lever, tier the second (`model-routing.md`).
- Back to Fable for the next decision. The owner switches; Claude says when a phase is mechanical.
- Batch independent tool calls in one message. Run single gates while iterating; the full
  `./scripts/backtest.sh` once at the end of a phase.

## 5. State discipline (what makes five hours safe)

| Context (from `context-monitor`) | Do |
|---|---|
| ~50 % | write the session log entry; set the plan's status and phase on disk |
| ~75 % | `/compress-session` (or `/checkpoint`); finish the current phase, do not start a new one |
| ~85 % | stop at the next phase boundary with everything on disk; compaction is fine from here |

Phase every long task so each phase ends with its files written and its plan status updated.
Compaction then costs a summary, not a decision.

## Anti-patterns (2026-09-02, one session)

| What happened | Cost | Rule |
|---|---|---|
| Five Explore agents and one Plan agent inherited Fable | 50–120k tokens each | §1 tier |
| Asked for verbatim extracts; two reports came back at ~12k tokens | doubled | §1 report contract |
| Python bulk edits on rules already read | full files echoed back | §3 |
| Wrote `CLAUDE.md`, Write refused (never Read), regenerated via Bash | 2× a 160-line file | §3 resolve path first |
| Plan agent stalled ten minutes, produced nothing | wall-clock + its tokens | §1 (Sonnet, tight scope) |
| `cat` of 30 KB of rules in one call | persisted to disk, still paid | §2 |

## Cross-references

- [`model-routing.md`](model-routing.md) — the fleet's pinned tiers and the effort axis.
- [`plan-first-workflow.md`](plan-first-workflow.md) — context-survival checklist before compaction.
- [`/compress-session`](../skills/compress-session/SKILL.md), [`/checkpoint`](../skills/checkpoint/SKILL.md), [`/context-status`](../skills/context-status/SKILL.md).
