---
name: Skill Promotion Policy
description: |
  Threshold-based policy for promoting an in-context pattern into a
  formal `.claude/skills/<name>/SKILL.md` skill. Read by `/learn` and
  by anyone considering whether to crystallize a workflow. Codifies
  the "12 painful rounds before promoting" heuristic from Yiqing Xu's
  Stanford IRiSS 2026 talk.
---

# Skill Promotion Policy

**Core question:** when should a recurring pattern in your work become a
formal `.claude/skills/<name>/SKILL.md` skill versus a one-off note?

The repo already has 30+ skills. Adding more has real costs:
- Every skill consumes a small amount of context window when its keywords
  trigger.
- Skill discovery (`ls .claude/skills/`) gets noisier.
- Maintenance cost grows linearly with skill count.
- Future-Pedro-upstream-merge surface area grows.

So promotion should be deliberate. This rule codifies a three-tier
threshold based on observed repetition.

---

## The three-tier policy

### Tier 1: < 5 occurrences → keep inline

If you've encountered the pattern fewer than five times across all your
projects:
- **Do not create a skill file.**
- Document the pattern inline in `MEMORY.md` under `[LEARN:topic]` tags.
- The pattern is not yet stable; you don't know which parts are
  essential versus accidental to the first few cases.

### Tier 2: 5–12 occurrences → draft, don't promote

If you've hit the pattern 5–12 times:
- **Draft a candidate skill** in
  `quality_reports/draft-skills/<candidate-name>.md`. This is a working
  file, not a real skill — it doesn't live in `.claude/skills/` and so
  doesn't trigger.
- Each new occurrence: open the draft, refine the steps, log the variant.
- Keep refining until the steps stabilize. If 4 of the next 5 invocations
  follow the draft as written, the skill is stable.

### Tier 3: 12+ occurrences, stable steps → promote

If you've hit the pattern 12+ times AND the steps have been stable across
the last several occurrences:
- **Promote** by moving the draft to `.claude/skills/<name>/SKILL.md`.
- Apply the `/learn` skill's quality gates (description has specific
  triggers; solution was verified; no sensitive info).
- Remove the draft from `quality_reports/draft-skills/`.
- Commit the new skill on `my-customizations`.

---

## Why the 12-rounds threshold

The number is from Yiqing Xu's Stanford IRiSS 2026 panel:

> *Start with painful tasks, iterate ~12–24 rounds, ask the LLM "is this
> worth making a skill?" Only formalize if frequently reused and not too
> idiosyncratic.*

Empirically, patterns that survive 12 invocations tend to survive
indefinitely. Patterns promoted earlier are over-fit to the first few
cases and need rework.

If you're tempted to promote sooner: do the draft instead, and let the
next 5–7 occurrences refine it. Drafts are cheap; rewriting a published
skill is expensive (existing project copies have to be reconciled).

---

## Exceptions: when to bypass the threshold

Three legitimate cases for direct promotion without the 12-round trial:

1. **The skill is a wrapper for an external tool** with a stable API
   (e.g., a new third-party LLM service, a new statistical package).
   The skill is documenting the tool, not crystallizing a personal
   workflow. Just write it.

2. **The skill enforces a hard rule the user wants from day one**
   (e.g., "always set `set seed 20260513` before any simulation in this
   project"). Promote immediately; the threshold is irrelevant when the
   pattern is a policy choice, not an emergent pattern.

3. **The skill imports a colleague's published skill from another repo**
   (Backman, Moore, etc.). The 12-round trial happened in their repo;
   you're just adopting it.

---

## What `/learn` should do

When `/learn` is invoked:

1. **Check this rule.** If the pattern in question hasn't been seen 5+
   times (i.e., `grep -rl "<pattern>" MEMORY.md` returns fewer than 5
   `[LEARN:]` entries), recommend inline documentation in `MEMORY.md`,
   not a new skill.
2. **Check `quality_reports/draft-skills/`.** If a draft exists for the
   same topic, recommend updating the draft rather than creating
   a parallel skill.
3. **Apply the threshold only after** the existing `/learn` self-assessment
   in Phase 1.

The `/learn` skill is not modified by this rule (its body is owned by
Pedro upstream); this rule is consulted by the orchestrator at the
moment `/learn` runs.

---

## Pruning: the inverse policy

Skill graveyard: if a skill has not been invoked in 12+ months AND the
project that motivated it is dormant:

1. Move the skill to `.claude/skills/_archived/<name>/`.
2. Document the archival date and reason in
   `.claude/skills/_archived/README.md`.
3. The skill no longer triggers but its history is preserved.

This is handled by `/context-audit` (existing skill); this rule defines
the threshold (12 months no use).

---

## Cross-references

- [`.claude/skills/learn/SKILL.md`](../skills/learn/SKILL.md) — invokes
  this rule during Phase 1 self-assessment.
- [`.claude/skills/context-audit/SKILL.md`](../skills/context-audit/SKILL.md)
  — handles archival of unused skills.
- `MEMORY.md` — `[LEARN:topic]` entries are the Tier-1 documentation
  layer this rule recommends.

---

## A worked example

> You've noticed that every time you run a panel DiD, you need to
> double-check whether `feols` is clustering at the right level. You've
> caught this bug three times.

**Tier-1 response:** add to `MEMORY.md`:

```markdown
## [LEARN:fixest] cluster level on multi-way panel
- `feols(y ~ x | id^year, cluster = ~id)` — cluster matches treatment
  assignment, NOT the absorbed FE structure.
- Trap: defaults to clustering at the highest-order absorbed FE,
  which is often wrong for staggered DiD.
- Caught 2026-05-13, 2026-05-21, 2026-06-02.
```

After two more catches, this becomes a Tier-2 draft. After 7 more, with
stable steps, it becomes a Tier-3 skill `fixest-cluster-check`.
