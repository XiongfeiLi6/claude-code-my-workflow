---
name: context-audit
description: |
  Periodic audit of .claude/ infrastructure to reduce context overhead from
  dead features, duplicate content, and noisy hooks. Retrospective practice —
  runs on mature projects where you have real evidence of what's unused.
  Use when: a project has been running for 2+ weeks and context feels bloated,
  OR after abandoning a format/tool (e.g., "Quarto is now dormant"),
  OR when you notice hooks firing for events you don't care about.
  DO NOT use on fresh projects — the scaffolding you'd delete hasn't been
  tried yet. Prevention (lean templates) beats cleanup.
author: Claude Code Academic Workflow
version: 1.0.0
allowed-tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep"]
---

# /context-audit — Infrastructure Context-Overhead Audit

Retrospectively audit `.claude/` to find and remove files that cost tokens on every message without earning their keep.

## When to Use

**USE when:**
- Project has been running for 2+ weeks with real usage
- You have concrete evidence a format/tool is dormant (e.g., you decided to abandon Quarto)
- Hooks are firing frequently with warnings you ignore
- CLAUDE.md and `.claude/rules/` contain duplicated content (notation tables, conventions)
- Context feels bloated and responses feel slow

**DO NOT USE when:**
- Project is fresh (< 1 week old) — you haven't tested the scaffolding yet
- You're unsure whether something is actually unused (absence of evidence ≠ evidence of absence)
- The template was just cloned from a workflow repo — wait for real usage signal

## Safety Principles

1. **Evidence-based deletion** — every removal must be justified by observed non-use, not speculation
2. **Consolidation beats deletion** — if content is unique, merge it into CLAUDE.md before deleting the source
3. **Protected names** — files containing `rule`, `protocol`, `convention`, or `governance` in the name require explicit user approval before deletion
4. **One commit per category** — never bundle all deletions into one commit; keep `git show` diagnostics easy
5. **Git is the safety net** — everything deleted lives in history forever, but labeled commits make recovery trivial

## Workflow

### PHASE 1: Evidence Gathering

Before deleting anything, collect signals:

```bash
# What formats does this project actually produce?
ls dist/ 2>/dev/null
ls Slides/*.tex 2>/dev/null
ls Slides/*.qmd 2>/dev/null

# What languages/tools are in active use?
find scripts/ -type f 2>/dev/null | head -20
grep -l "\.do" .claude/rules/ .claude/skills/ 2>/dev/null
grep -l "\.R\|\.r\b" .claude/rules/ .claude/skills/ 2>/dev/null

# What's in CLAUDE.md? (master reference for duplicate detection)
wc -l CLAUDE.md
```

Record:
- **Active formats:** (e.g., Beamer only, Quarto dormant)
- **Active languages:** (e.g., Stata only, no R)
- **Recent file activity:** which rules/skills have been touched in the last month

### PHASE 2: Dead Features Audit

List every agent, skill, and rule that references a format/tool/language this project does NOT use.

```bash
ls .claude/agents/ 2>/dev/null
ls .claude/skills/ 2>/dev/null
ls .claude/rules/ 2>/dev/null
```

For each candidate, verify it's actually dead:
- Grep the file for its target format/tool
- Cross-reference against the "active formats" list from Phase 1
- If it references ONLY dormant things → mark for deletion
- If it references a mix → mark for consolidation (strip dead parts)

**Common dead patterns:**
- Quarto agents/skills when project is Beamer-only
- R rules/reviewers when project is Stata-only
- Deploy/publish skills when project doesn't ship to web
- Translation skills between dormant formats

### PHASE 3: Duplicate Content Audit

Compare every file in `.claude/rules/` against CLAUDE.md and MEMORY.md:

```bash
# Extract headings/tables from rules
for f in .claude/rules/*.md; do
  echo "=== $f ==="
  head -30 "$f"
done
```

Flag any rule that:
- Repeats notation tables already in CLAUDE.md
- Repeats convention lists already in MEMORY.md
- Is a "rule about rules" (meta-governance) with no concrete task guidance
- Duplicates workflow references from CLAUDE.md

**Rule of thumb:** If the rule just restates CLAUDE.md content, delete the rule. If it has unique content, merge unique parts into CLAUDE.md and then delete.

### PHASE 4: Noisy Hooks Audit

Review `.claude/hooks/` and the `hooks` section of `.claude/settings.json`:

```bash
ls .claude/hooks/
```

For each hook, ask:
- **What event triggers it?** (frequency matters — `PostToolUse` on `Bash` fires on every shell call)
- **What does it do?** (protect files? nag? estimate something?)
- **Is the signal accurate?** (heuristics like "context % from tool count" are usually wrong)
- **Does it block Claude?** (Stop hooks with `decision: block` are maximally disruptive)

**Delete hooks that:**
- Fire on every Bash/Edit/Write/Stop event with marginal value
- Use inaccurate heuristics to estimate state
- Block Claude to nag about optional tasks (session logs, memory updates)
- Duplicate functionality already in CLAUDE.md instructions

**Keep hooks that:**
- Protect specific files from overwrites (fast, targeted)
- Run fast syntax checks after Write/Edit (catch real errors)
- Restore state after compaction

When removing a hook file, also remove its reference in `settings.json`.

### PHASE 5: Triage and Approval

Present findings to the user in this format:

```
## Context Audit Findings

### Dead Features (safe to delete)
- [ ] .claude/agents/quarto-critic.md — Quarto is dormant per MEMORY.md
- [ ] .claude/skills/deploy/ — no web deployment target exists

### Duplicate Content (merge then delete)
- [ ] .claude/rules/knowledge-base-template.md — notation table duplicates CLAUDE.md §Notation

### Noisy Hooks (delete hook file + settings.json entry)
- [ ] .claude/hooks/log-reminder.py — blocks every Stop event to nag about session logs

### PROTECTED — requires explicit approval
- [ ] .claude/rules/meta-governance.md — contains "rule" in name, 251 lines

Proceed with non-protected deletions? (y/n)
Approve protected deletions individually? (list names)
```

**Wait for user response before proceeding.**

### PHASE 6: Execute Deletions (Separate Commits)

For each category, use a separate commit:

```bash
# Category 1: Dead features
git rm .claude/agents/quarto-critic.md .claude/skills/deploy/SKILL.md
git commit -m "Remove dead Quarto/deploy infrastructure (format dormant)"

# Category 2: Duplicate content (after merging unique parts into CLAUDE.md)
git add CLAUDE.md
git rm .claude/rules/knowledge-base-template.md
git commit -m "Consolidate notation table into CLAUDE.md, remove duplicate rule"

# Category 3: Noisy hooks
git rm .claude/hooks/log-reminder.py
# edit settings.json to remove hook reference
git add .claude/settings.json
git commit -m "Remove log-reminder hook (blocked every Stop for optional nag)"
```

Labeled commits make `git log` readable and recovery easy.

### PHASE 7: Verify and Report

After all deletions:

```bash
# Confirm settings.json is still valid JSON
python3 -m json.tool .claude/settings.json > /dev/null && echo "settings.json OK"

# Count lines removed
git log --stat HEAD~N..HEAD | tail -5

# Sanity check: try compiling a slide deck to confirm nothing broke
cd Slides && TEXINPUTS=../Preambles:$TEXINPUTS xelatex -interaction=nonstopmode Lecture01_*.tex | tail -5
```

Report:

```
## Audit Summary

- Lines removed: N
- Files deleted: M
- Files consolidated (content merged): K
- Commits created: P (one per category)

### Verification
- [ ] settings.json is valid JSON
- [ ] Sample slide compiles successfully
- [ ] No broken references in CLAUDE.md

### Rollback
Anything deleted can be recovered via:
  git show HEAD~N:path/to/file.md > path/to/file.md
```

## Anti-Patterns to Avoid

| Anti-Pattern | Why It's Bad | Fix |
|--------------|--------------|-----|
| Running on day-1 project | Deletes untested scaffolding | Wait for 2+ weeks of real usage |
| One giant "cleanup" commit | `git show` becomes unreadable | Separate commit per category |
| Deleting rules without reading them | Might contain unique content | Read fully, merge unique parts first |
| Speculative deletion ("probably unused") | Regret later when needed | Require concrete evidence of non-use |
| Deleting protected files without approval | Breaks user's mental model of the workflow | Always ask for rules/protocols/conventions |

## Prevention Beats Cleanup

This skill exists because templates accumulate cruft. The better long-term fix is:

1. **Lean templates** — ship only the tools for the format/language you actually use
2. **Single source of truth** — notation, conventions, and workflows live in ONE file (CLAUDE.md)
3. **Minimal hooks** — only protect-files and fast syntax checks; never nag
4. **Explicit track selection** — when cloning a template, immediately delete the "wrong track" (e.g., delete R if you're using Stata)

If your template is already lean, this skill has nothing to do.

## References

- Inspired by the Econ 301 cleanup that removed 1,767 lines across two commits:
  - `01cca7a` Trim dormant/unused infrastructure (1,242 lines)
  - `13f3645` Remove noisy hooks and duplicate rule (525 lines)
- Template repo: consider promoting this skill to a `my-customization` branch
  of your Claude Code workflow template on GitHub.
