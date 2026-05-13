---
name: replicate-paper
description: |
  Reproduce an EXTERNAL paper's published numbers from scratch — given its
  replication package (or just its PDF + a data source). Implements the
  three-layer pattern from Yiqing Xu's Stanford IRiSS talk: (1) LLM extracts
  targets + materials, (2) markdown skill-notes accumulate cross-paper edge
  cases, (3) deterministic R/Stata/Python code is version-controlled.
  Distinct from `/audit-reproducibility`, which compares YOUR manuscript to
  YOUR code; this skill compares THEIR paper to YOUR re-implementation of
  their analysis.
  Use when: preparing to extend a paper, writing a referee report, auditing
  a literature claim, building a meta-analysis, or onboarding a co-author
  onto an existing literature.
argument-hint: "[paper citation or DOI or replication-package path]"
allowed-tools: ["Read", "Grep", "Glob", "Write", "Edit", "Bash", "Task", "WebFetch", "Monitor"]
effort: high
---

# Replicate an External Paper

Reproduce a published paper's reported numbers from scratch. Goal: a
versioned `scripts/{R,stata,python}/replicate_{author}_{year}.{R,do,py}`
that, when run, regenerates Table X to within the tolerances in
[`.claude/rules/replication-protocol.md`](../../rules/replication-protocol.md).

**Core idea (Yiqing Xu, Stanford IRiSS 2026):**
> *Minimize LLM involvement in final output; use it to teach skills and
> update deterministic code.*

The LLM's job is the semantic part (read the paper, locate Table 3,
identify the spec, find the data column). The deterministic code's job
is the numerical part (run the regression, save the .rds/.dta, compare).

---

## When to Use

- **Before extending a paper.** Replicate the headline result so the
  baseline you build on is verified.
- **Writing a referee report.** Check whether the paper's headline number
  survives the simplest alternative spec the authors didn't run.
- **Auditing a literature claim.** A meta-analysis citation says "the
  elasticity is 0.42"; verify by re-running their main spec.
- **Onboarding a co-author / RA.** Hand them the replicate script as the
  fastest possible way to understand the original paper.
- **Reading-group preparation.** Run the paper before discussing it.

**Not for:** verifying your OWN paper against your OWN code (use
`/audit-reproducibility` instead). The distinction matters because
this skill assumes the gold standard is the *paper's printed value*,
not your code's output.

---

## Inputs

- `$ARGUMENTS` — one of:
  - A DOI: `10.1257/aer.84.4.772`
  - A working-paper URL: `https://www.nber.org/papers/w12345`
  - A local PDF path: `master_supporting_docs/card_krueger_1994.pdf`
  - A replication-package path: `~/Downloads/CK_1994_replication/`
  - A free-text citation: `"Card and Krueger 1994 AER"` (skill will resolve)

---

## The Three Layers

```
┌─────────────────────────────────────────────────────────────────┐
│ Layer 1 — Semantic extraction (LLM-driven, non-deterministic)   │
│   • Read paper PDF                                              │
│   • Locate replication package (Journal site, Dataverse, ICPSR) │
│   • Extract target numbers from Table X (or your specified loc) │
│   • Parse README / .do / .R files to identify the main spec     │
└─────────────────────────────────────────────────────────────────┘
                                ↓
┌─────────────────────────────────────────────────────────────────┐
│ Layer 2 — Skill-notes (markdown, append-only)                   │
│   .claude/skills/replicate-paper/notes/{author}_{year}.md       │
│   • Edge cases encountered (clustering choice, sample restrict) │
│   • Translation pitfalls (Stata-to-R, R-to-Python)              │
│   • Tolerance overrides (this paper rounds aggressively)        │
│   Accumulates across papers — read by Layer 1 next time.        │
└─────────────────────────────────────────────────────────────────┘
                                ↓
┌─────────────────────────────────────────────────────────────────┐
│ Layer 3 — Deterministic code (versioned, reruns identically)    │
│   scripts/{R,stata,python}/replicate_{author}_{year}.{R,do,py}  │
│   • Runs end-to-end from raw data → saved RDS → comparison      │
│   • Re-running tomorrow produces the same numbers                │
│   • Lives in git; PR-able; can be cited in your own paper        │
└─────────────────────────────────────────────────────────────────┘
```

---

## Workflow

### Phase 0: Inputs and ground truth

1. Resolve `$ARGUMENTS` to a paper. If just a citation, search for the DOI
   and an accessible PDF (NBER, journal page, or `master_supporting_docs/`).
2. **Ask the user once, only if ambiguous**: "Which table/figure is the
   replication target? Default: the headline table from the abstract."
3. Read `.claude/rules/replication-protocol.md` for tolerance thresholds.
4. Read any existing `notes/{author}_{year}.md` if present.

### Phase 1: Extract targets

Write `quality_reports/replicate_{author}_{year}_targets.md`:

```markdown
# Replication Targets: [Author Year]

**Source:** [paper title, journal, DOI]
**Date extracted:** YYYY-MM-DD
**Replication package:** [URL or "none — extracting from PDF text only"]

## Targets

| ID | Location | Quantity | Reported value | SE / CI | Significance | Sample N |
|----|----------|----------|----------------|---------|--------------|----------|
| T1 | Table 3, row 4 ("DiD") | ATT, FTE per store | +2.76 | (1.36) | ** | 410 |
| T2 | Table 3, row 1 ("NJ FTE Feb") | mean | 20.44 | (0.51) | — | 331 |

## Specification (from paper text / their .do file)

- **Outcome:** FTE per store (defined as full-time + 0.5 × part-time)
- **Treatment:** NJ indicator
- **Control:** PA indicator
- **Period:** Feb 1992 (pre) vs Nov 1992 (post)
- **Estimator:** OLS on interaction `i.treat##i.post`
- **SE:** classical (paper does not cluster)
- **Sample restrictions:** stores answering both waves; drop temporary closures
```

### Phase 2: Locate and prepare the data

Order of preference:
1. **Official replication package** (Dataverse, ICPSR, journal data archive,
   author website).
2. **Public mirror** (NBER, AEA, Inter-university Consortium).
3. **Source data** (BLS, IPUMS, CPS, World Bank) — if the paper's data is
   derived from public sources, re-derive it.
4. **Last resort: contact the authors.** Pause skill execution; ask user.

If the package is in Stata and your project is R (or vice versa), translate
**after** replicating in the original language — Yiqing's rule: *replicate
first in the original tool, translate second*. This isolates language-
specific issues from substantive specification issues.

### Phase 3: Layer 3 — Deterministic code

Generate `scripts/{R,stata,python}/replicate_{author}_{year}.{R,do,py}`
following the language-specific conventions rule
(`r-code-conventions.md`, etc.). The script must:

1. Load raw data from a single documented path.
2. Apply the paper's sample restrictions in order.
3. Run the main spec exactly as described.
4. Save the regression object (`.rds` for R, `est save` for Stata).
5. Print a comparison block to stdout:

```
Target T1 (ATT, Table 3 row 4):
  Reported by paper:    +2.76 (1.36)
  Reproduced by code:   +2.76 (1.36)
  Diff:                 +0.00 (0.00)
  Tolerance:            0.01 / 0.05
  Status:               PASS
```

### Phase 4: Iterate to tolerance

If any target fails, **do not "improve" the spec to match.** Follow
`replication-protocol.md` Phase 3: isolate the source of disagreement.
Common causes documented in the Stata→R pitfalls table of the rule file.

Log every fix attempt to `notes/{author}_{year}.md` so the next person
(or next paper) benefits.

### Phase 5: Generate the report

Write `quality_reports/replicate_{author}_{year}_report.md` following the
template in `replication-protocol.md` Phase 3. Mark overall verdict
`REPLICATED | PARTIAL | FAILED`.

### Phase 6: Update skill notes

Append to `.claude/skills/replicate-paper/notes/{author}_{year}.md`:

```markdown
# Notes: [Author Year]

**Replicated:** YYYY-MM-DD by Claude Code session (commit hash X)
**Verdict:** REPLICATED | PARTIAL | FAILED

## Edge cases discovered

- The paper uses classical SEs; replication with `robust` would give SE = 0.94.
- "FTE" excludes managers but the README is ambiguous; matches paper only
  after dropping `manager == 1`.

## Translation pitfalls (Stata original → R)

- Stata `tab y81 nearinc, sum(rprice)` includes missing as a separate row;
  R `dplyr::group_by() %>% summarize()` drops them silently. Add
  `filter(!is.na(rprice))` to match.

## Files produced

- `scripts/R/replicate_card_krueger_1994.R`
- `scripts/R/_outputs/replicate_card_krueger_1994_main.rds`
- `quality_reports/replicate_card_krueger_1994_report.md`
```

---

## Output

```
✓ Replication complete: [Author Year]
  Targets:   M / N matched within tolerance
  Verdict:   REPLICATED | PARTIAL | FAILED
  Script:    scripts/R/replicate_{author}_{year}.R
  Report:    quality_reports/replicate_{author}_{year}_report.md
  Notes:     .claude/skills/replicate-paper/notes/{author}_{year}.md
  Next:      [commit + push, OR extend with your own modifications]
```

---

## Cross-references

- [`.claude/rules/replication-protocol.md`](../../rules/replication-protocol.md) — tolerance contract.
- [`.claude/skills/audit-reproducibility/SKILL.md`](../audit-reproducibility/SKILL.md) — sibling skill for YOUR-paper-vs-YOUR-code audits.
- [`.claude/skills/audit-estimator/SKILL.md`](../audit-estimator/SKILL.md) — sibling skill for testing your own estimator against a known DGP.
- [`.claude/skills/methods-referee/`] (via agent) — for substantive critique once replication is verified.

## What this skill does NOT do

- **Critique the paper.** Verdict is numeric (PASS / FAIL on tolerance),
  not substantive. For that: `/review-paper-full` or the `methods-referee`
  agent.
- **Acquire restricted data.** If the paper uses confidential data (admin
  files, IRS, FBI), the skill stops at Phase 2 and prompts the user.
- **Replicate from PDF text alone.** If no replication package and the
  data isn't public, the skill produces only Layer 1+2 (a structured
  read of the paper), not Layer 3 code.

## Long replication runs: Monitor tool

For replications whose main spec takes >2 minutes (large panel data, GMM,
bootstrap), background-launch the deterministic script via `Bash` with
`run_in_background: true`, then stream stdout via the `Monitor` tool. The
comparison block prints to stdout, so Monitor surfaces PASS/FAIL the moment
it's available — no polling needed.
