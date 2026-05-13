---
name: audit-estimator
description: |
  Stress-test your own estimator against a known data-generating process
  (DGP). Implements the builder/tester two-agent pattern from Yiqing Xu's
  Stanford IRiSS 2026 talk: the BUILDER (you, or another agent) writes
  the estimator blind to true parameters; the TESTER simulates data from
  a DGP, runs the estimator, and verifies recovered estimates match the
  true parameters within tolerance. Use for: validating a new estimator
  package, regression of a custom GMM moment, ML-augmented inference,
  bootstrap pipelines, or any code that produces a numerical estimate
  you'll cite in a paper.
argument-hint: "[estimator file or function name + DGP description]"
allowed-tools: ["Read", "Grep", "Glob", "Write", "Edit", "Bash", "Task", "Monitor"]
effort: high
---

# Audit Estimator Against Known DGP

Builder/tester loop: simulate data where you know the true parameter,
run the estimator on that data, check that recovered estimates concentrate
around truth at the right rate.

**Core idea (Yiqing Xu, Stanford IRiSS 2026):**
> *Two agents: Builder writes package code; does NOT see true parameters.
> Tester is deterministic code that checks if builder's estimates match
> the DGP. Both agents spawn independently with distinct information.*

In this skill the "builder" is whatever produced the estimator (the user,
Claude in a prior session, an R package, a co-author). The skill is the
TESTER: it owns the DGP, owns the truth, and reports PASS/FAIL.

The separation is structural, not just stylistic. The tester writes code
that *generates* data; it does not borrow code from the builder. If the
builder's estimator passes tests it didn't see during development,
that's real evidence the estimator works.

---

## When to Use

- **You just wrote a new estimator** (custom GMM, ML-augmented IV, a
  bootstrap variance, a small package). You need simulation evidence
  before citing point estimates in a paper.
- **You're submitting an R or Stata package** to CRAN / SSC. Builder/
  tester is the minimum bar for replication-package quality.
- **You inherited code from a co-author** and want to verify it works
  before running it on real data.
- **You're refereeing a paper** that introduces a new estimator and the
  authors did not provide a DGP sanity check; this skill produces one
  you can run.
- **You modified an existing estimator** and want to confirm the change
  didn't break recovery of the original DGP.

**Not for:** linear OLS / standard GLM where the formula is closed-form
and uncontroversial (use the analytic derivation directly). Reserve this
skill for non-trivial estimators where DGP recovery is informative.

---

## Inputs

- `$ARGUMENTS` — either:
  - Path to an estimator function: `scripts/R/my_estimator.R`
  - Function name accessible from the project: `myPackage::estimate_att`
  - A description: `"the GMM estimator I just wrote in scripts/R/iv_gmm.R,
    expecting to recover beta=0.3 from the linear IV DGP"`

---

## Workflow

### Phase 1: Pin the estimator interface

1. **Read the estimator code.** Identify:
   - Function name
   - Input signature (data, formula, options)
   - Output signature (coefficient vector, SE vector, conf.int, p-value)
   - Stochastic elements (uses bootstrap? Monte Carlo? a seed?)
2. **Wrap the estimator** in a small adapter if its interface is unusual.
   The adapter must return a flat `{name → (point, se)}` map.
3. **Identify the parameters of interest** the test will recover. Usually
   one or a small number of coefficients, not the entire vector.

### Phase 2: Specify the DGP

The user specifies the DGP. The skill asks (only if not provided):

- **Sample size** `n` (or a grid: 100, 1000, 10000)
- **True parameter vector** for the parameters of interest
- **Nuisance structure** (variance, covariate distribution, correlation,
  clustering structure if relevant)
- **Number of simulations** `S` (default 500; 200 if fast, 2000 if slow)

The DGP code lives in
`scripts/{R,stata,python}/audit_estimator/{taskname}_dgp.{R,do,py}`. It
generates ONE simulated dataset given a seed.

### Phase 3: The builder/tester separation (architectural)

The skill enforces the separation by writing the tester as a separate
script that *imports* the estimator but does *not* import anything from
the estimator's internal helpers. This is a soft enforcement, not a
sandbox — the test of independence is procedural: did the builder see
the test code while developing?

```
scripts/R/my_estimator.R                ← builder's deliverable
scripts/R/audit_estimator/
  iv_test_dgp.R                         ← tester's DGP (independent)
  iv_test_runner.R                      ← tester's loop + comparison
  iv_test_report.md                     ← generated output
```

### Phase 4: Run the simulation

For each `s in 1..S`:

1. Set seed `s` (deterministic per-replication seed lets you re-run any
   single replication that fails).
2. Generate dataset from the DGP at the chosen `n`.
3. Call the estimator on the dataset.
4. Record the recovered point estimates and SEs.

Stash results in `scripts/R/audit_estimator/{taskname}_sims.rds`.

For large `S` or large `n`, background-launch via `Bash` with
`run_in_background: true` and stream stdout via `Monitor`.

### Phase 5: Tester checks

For each parameter of interest:

1. **Mean bias** = `mean(point - truth)`. PASS if `|bias| < 0.05 × truth`
   (or absolute < 0.01 if truth is near zero). Document threshold.
2. **RMSE** = `sqrt(mean((point - truth)^2))`. Report.
3. **Coverage** = fraction of replications where the reported 95% CI
   covers truth. PASS if coverage ∈ [0.92, 0.97]. Persistent under- or
   over-coverage indicates wrong SEs.
4. **SE calibration** = `mean(se) / sd(point)`. PASS if ∈ [0.9, 1.1].
   Deviations indicate the analytic SE is mis-specified.
5. **Distribution shape** = histogram of (point - truth) / se. Should be
   roughly N(0, 1) under correct specification. Plot and save.

Each parameter gets its own row in the report table.

### Phase 6: Report

Write `scripts/R/audit_estimator/{taskname}_test_report.md`:

```markdown
# Estimator Audit Report: {taskname}

**Estimator under test:** [function name, file path, git hash]
**DGP:** [one-paragraph description]
**Simulations:** S = [count], n = [grid]

## Per-parameter recovery

| Param | Truth | Mean point | Bias | RMSE | Coverage | SE calib. | Status |
|-------|-------|-----------|------|------|----------|-----------|--------|
| β₁ | 0.30 | 0.302 | +0.002 | 0.041 | 0.948 | 1.02 | PASS |
| β₂ | -0.50 | -0.491 | +0.009 | 0.067 | 0.881 | 0.83 | FAIL (coverage low; SE under-estimated) |

## Diagnostics

- [Histogram of standardized errors per parameter]
- [Bias-vs-n trajectory if multiple n's tested]

## Verdict

[PASS / PARTIAL / FAIL]. If FAIL: which parameter, which diagnostic,
specific suspected cause (analytic SE, missing finite-sample correction,
mis-specified moment condition).

## Reproduce

```r
source("scripts/R/audit_estimator/{taskname}_test_runner.R")
```

Seeds 1..S are pinned; re-running produces the same numbers.
```

### Phase 7: Iterate

If FAIL, the report tells the builder what to fix. The builder iterates;
the tester is not modified to make the test pass — that defeats the
purpose. The tester is only modified if the DGP itself was wrong.

---

## Output

```
✓ Estimator audit complete: {taskname}
  Parameters tested:    M
  PASS:                 P
  FAIL:                 F
  Verdict:              PASS / PARTIAL / FAIL
  Report:               scripts/R/audit_estimator/{taskname}_test_report.md
  Sims data:            scripts/R/audit_estimator/{taskname}_sims.rds
  Next:                 [if FAIL, fix the estimator and rerun; if PASS, commit]
```

---

## Architectural notes

**Why this is different from `methods-referee`.**
`methods-referee` reviews substantive design choices in someone else's
paper (identification, clustering, robustness). This skill verifies that
*your own code* recovers known parameters from synthetic data. They
compose: pass this skill first, then run `methods-referee` on the
manuscript.

**Why this is different from `claim-verifier`.**
`claim-verifier` is a fresh-context fact-checker for claims that have
already been written. This skill *generates* claims (about recovery)
from a controlled experiment.

**Why deterministic SE calibration matters even when point estimates pass.**
Yiqing's panel session emphasized that the tester catches what the builder
didn't think to check. A typical failure mode for hand-rolled estimators:
the point estimate is fine but the analytic SE doesn't account for some
nuisance (clustering, two-step estimation, parameter dependence). The
SE-calibration diagnostic surfaces this without needing to derive the
analytic SE by hand.

---

## Cross-references

- [`.claude/skills/replicate-paper/SKILL.md`](../replicate-paper/SKILL.md) — once your estimator passes this audit, replicate a published paper to confirm it produces the same numbers on real data.
- [`.claude/agents/methods-referee.md`](../../agents/methods-referee.md) — substantive review once estimator + paper are both in hand.
- [`.claude/rules/replication-protocol.md`](../../rules/replication-protocol.md) — tolerance language reused.

## What this skill does NOT do

- **Prove the estimator is correct.** Passing recovery on one DGP doesn't
  rule out failure on a different DGP. Run multiple DGPs.
- **Replace asymptotic theory.** A passing simulation at n=10,000 doesn't
  imply consistency at n=∞; that's a math problem.
- **Catch coding bugs unrelated to the parameter.** If the estimator
  silently rounds the dataset, this skill won't notice unless the rounding
  affects recovery.
