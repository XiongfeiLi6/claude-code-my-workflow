---
name: question-quality
description: |
  Apply Matt Gentzkow's six-criterion research-taste lens (from his
  Stanford IRiSS 2026 talk) to interrogate a research question — your own
  or a student's — before you invest paper-writing time. Distinct from
  `devils-advocate` (which critiques design decisions on an existing
  draft) and from `research-ideation` (which generates new questions).
  This skill PRESSURE-TESTS a question that has already been formulated
  but not yet committed to.
  Use when: deciding which of your draft ideas to actually pursue;
  reviewing a thesis student's proposed dissertation question; evaluating
  a co-author's pitch; reading a working paper and asking "did this
  question deserve the firepower spent on it?"; auditing a referee report
  that praised method over substance.
argument-hint: "[research question or path to a one-pager]"
allowed-tools: ["Read", "Grep", "Glob", "Write", "Task"]
effort: medium
---

# Research-Question Quality Audit

A structured Socratic critique that applies six criteria — distilled from
Matt Gentzkow's talk on research judgment in an AI era — to a stated
research question. The output is not a yes/no verdict; it is six diagnostic
scores plus three sharpened alternative formulations of the question.

**Core idea (Matt Gentzkow, Stanford IRiSS 2026):**
> *Figuring out how to evaluate what is a good question is the hardest
> thing you learn in grad school, and it's the most important thing.
> As tool power grows, the return to directing it well grows quadratically.*

The skill makes that evaluation explicit and replicable.

---

## When to Use

- **Mid-prospect:** You have 3–5 candidate paper ideas. You need to pick
  one. Run all of them through this skill; pick by relative score.
- **Pre-PAP:** Before writing a pre-analysis plan, audit the question the
  PAP is built around.
- **Thesis supervision:** A PhD or MA student presents a dissertation
  question. Run it through this skill *with the student in the room*
  — the criteria are the teaching content.
- **Co-author pitch:** Your collaborator pitches a project. Audit before
  committing your time.
- **Working paper reading:** Audit the *question* of a paper you're
  reading. If it scores low, the rest of the paper may be clever-method
  fluff.
- **Referee-report quality control:** If your draft referee report praises
  methodology, this skill checks whether the question itself was worth
  praising too.

**Not for:** evaluating a question that hasn't been formulated yet (use
`/research-ideation`). Not for: critiquing the execution of a stated
question (use `/devils-advocate` or `/review-paper-light`).

---

## Inputs

- `$ARGUMENTS` — one of:
  - The question as a single sentence
  - Path to a one-pager / abstract / proposal
  - Path to a draft paper

If the input is longer than a paragraph, the skill first extracts the
research question into a single sentence and asks the user to confirm:
*"Is this the question you want audited? [Y/n/edit]"*

---

## The Six Criteria

Each criterion gets a 1–5 score plus a one-paragraph justification.

### 1. Decision-relevance

> What concrete decision changes if the answer is X versus Y?

A 5 names a real decision-maker (policymaker, firm, household, donor,
researcher) and describes precisely how their choice changes in the
two states of the world. A 1 is "this would be interesting to know."

**Test:** Can you write the sentence "if the answer is X, [agent] should
do Y; if the answer is W, [agent] should do Z"? If no, you don't have
decision-relevance.

### 2. Audience prior tightness

> How tight is the prior of the audience that will evaluate this?

A 5 audience is genuinely split (50/50). A 1 audience already agrees with
your hypothesized answer — your paper changes no one's mind. Note: a
*tight* but *wrong* audience prior is also a 5 (overturning consensus is
maximally informative).

**Test:** Survey three economists in your field. Ask them what they expect
the answer to be. If all three predict the same number within ±10%, your
audience prior is tight on a known answer — low informativeness.

### 3. Simplest interesting version

> If you stripped this to its minimum, would it still be interesting?

A 5 has a clean baseline question that would be a paper on its own. A 1
requires the full complex apparatus to be even minimally interesting —
suspicious signal that the complexity is hiding a weak core.

**Test:** Describe the question in two sentences to a smart undergraduate.
If they can't see why the answer would matter, the simplest version is
not interesting.

### 4. Credibility cost of identification

> How big is the credibility tax on your identification strategy?

A 5 has a transparent, defensible strategy (RCT, sharp regression
discontinuity, well-validated IV). A 1 has a research design where the
critical reader has to swallow a heavy assumption (parallel trends in a
4-period DiD with one treated unit; a "shift-share" IV without convincing
exogeneity argument).

**Test:** Imagine the worst-case referee. What is their headline objection?
Can you defend against it without adding apparatus that costs the paper
clarity?

### 5. External validity / portability

> Does the answer travel beyond the specific sample?

A 5 has a theoretically-grounded reason to expect the result holds beyond
the empirical context. A 1 is a one-place, one-time finding whose
applicability you cannot defend.

**Test:** State one other context (country, time period, industry) where
the result should hold. Can you defend that extension? If no, the
question is descriptive-of-this-sample, not informative-about-the-world.

### 6. Method-versus-question balance

> Is this a clever-method paper, or a tangible-question paper?

A 5 is motivated entirely by the question; the method serves the question.
A 1 is motivated by a method or natural experiment; the question was
back-fitted to use it.

**Test (Gentzkow's test):** Could the paper be re-described as "I solved
a really hard problem and this happens to be one application"? If yes,
score 1 or 2. The path of least resistance in modern empirical economics
is to find a clever quasi-experiment and ask whatever question it answers
— resist this when grading your own work.

---

## Workflow

### Phase 1: Restate the question

Read the input. Write a single-sentence statement of the question in the
form: *"What is the effect of [treatment] on [outcome] for [population],
identified by [strategy]?"* (or the appropriate equivalent for a
descriptive / theoretical question).

Ask the user to confirm.

### Phase 2: Score each criterion

For each of the six criteria:
- Assign a 1–5 score
- Write a one-paragraph justification grounded in the input
- Quote a specific phrase from the input if relevant

### Phase 3: Compute the headline

Report total score (6–30) plus categorical verdict:
- **27–30: Strong question.** Pursue.
- **22–26: Solid question.** Pursue with targeted strengthening on lowest
  criterion.
- **16–21: Weak in 2+ criteria.** Either reformulate or do not pursue.
- **6–15: Likely not worth the time investment.** Reformulate from
  scratch or drop.

### Phase 4: Generate three sharpened reformulations

This is the most valuable part of the skill. Even if the original
question scores 30, the sharpened versions illuminate the design space.

For each reformulation, write:
- The new one-sentence question
- Which criterion it strengthens (or trades off)
- What new data / strategy / scope it requires
- Why it might be better OR worse than the original

The reformulations should not all be "make it bigger" or "make it
smaller." Mix:
- One "narrower-but-sharper" version (better criteria 1, 4)
- One "broader-but-riskier" version (better criteria 5)
- One "different-mechanism" version (better criteria 2, 6)

### Phase 5: Report

Write `quality_reports/question_quality_{slug}.md`:

```markdown
# Question Quality Audit: {slug}

**Question audited:**
> [single-sentence restatement]

**Date:** YYYY-MM-DD
**Auditor:** Claude Code (question-quality skill)

## Headline score: [N/30] — [verdict]

## Per-criterion scores

| # | Criterion | Score | Justification |
|---|-----------|-------|---------------|
| 1 | Decision-relevance | [1-5] | ... |
| 2 | Audience prior tightness | [1-5] | ... |
| 3 | Simplest interesting version | [1-5] | ... |
| 4 | Credibility cost | [1-5] | ... |
| 5 | External validity | [1-5] | ... |
| 6 | Method-vs-question balance | [1-5] | ... |

## Three sharpened reformulations

### Reformulation A — Narrower but sharper
[question + analysis]

### Reformulation B — Broader but riskier
[question + analysis]

### Reformulation C — Different mechanism
[question + analysis]

## Recommendation

[One paragraph: pursue / reformulate / drop, with reasoning.]
```

---

## Output

```
✓ Question audited: "{single-sentence question}"
  Headline:  [N/30] — [Strong / Solid / Weak / Drop]
  Strongest: Criterion [#] ([name])
  Weakest:   Criterion [#] ([name])
  Report:    quality_reports/question_quality_{slug}.md
  Three reformulations attached. Pick one to pursue further.
```

---

## Anti-patterns to flag

When auditing, watch for these and call them out explicitly:

- **"Clever-quasi-experiment-in-search-of-a-question"** — the paper exists
  because the data/instrument is available, not because the answer
  matters. Common in modern empirical micro. Score criterion 6 low.
- **"It would be useful to know"** — vague decision-relevance.
- **"This is the first paper to..."** — novelty is not informativeness.
- **"Many policymakers care about..."** without naming any.
- **"Builds on" without saying which part of the prior literature was
  wrong or incomplete.** A good question identifies a specific gap.

---

## Cross-references

- [`.claude/skills/research-ideation/SKILL.md`](../research-ideation/SKILL.md) — generates questions from scratch; precedes this skill.
- [`.claude/skills/devils-advocate/SKILL.md`](../devils-advocate/SKILL.md) — pressure-tests an existing design, not the underlying question. Run after this skill.
- [`.claude/skills/interview-me/SKILL.md`](../interview-me/SKILL.md) — Socratic question-formalization; precedes this skill for ill-formed inputs.

## What this skill does NOT do

- **Tell you whether the answer exists.** That's an empirical / theoretical
  problem.
- **Critique the methodology.** Use `methods-referee` or `/devils-advocate`.
- **Reformulate every question into a winning one.** Some questions
  shouldn't be pursued; the recommendation can be "drop."
