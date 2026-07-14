---
name: commit
description: Stage and commit (quick mode, default); push + PR + merge to main only on request ('full'). Use ONLY on explicit commit intent — user says "commit", "ship it", "push this", "open a PR", "merge to main", "let's commit this", or prefixes with `/commit`. Do NOT auto-invoke on vague end-of-task phrases ("we're done", "wrap up") — those require explicit confirmation first. Never force-pushes or skips hooks.
argument-hint: "[optional: commit message | 'full' for the PR+merge cycle]"
allowed-tools: ["Bash", "Read", "Glob", "Task"]
model: sonnet
effort: medium
---

# Commit (quick by default; PR + merge on request)

Two modes:

- **Quick mode (DEFAULT):** run the pre-commit gates (Step 0 quality score + Step 0b surface-sync —
  both cheap scripts), then stage and commit on the current branch (Steps 1, 3, 4). Skip the verifier
  spawn, branching, PR, and merge. Read `git diff --stat`, never full diffs; open individual files only
  if the message genuinely needs it. If the current branch is `main`, create a branch first (Step 2).
- **Full mode** (`$ARGUMENTS` contains `full`, or the user explicitly asks for a push, PR, or merge):
  run ALL steps below, including the verifier agent, branch, PR, and merge.

The `model:`/`effort:` pins follow `.claude/rules/model-routing.md` (commit-message writing is
mechanical-tier work; the token cost of committing is the ceremony, not `git commit`). The verifier
agent spawned in full mode carries its own tier pin.

## Steps

### Step 0: Quality Gate (Pre-Commit)

**Run before branching.** For every changed `.qmd`, `.tex`, or `.R` file that has quality rubrics, run:

```bash
python3 scripts/quality_score.py <changed-file-paths>
```

- If any file scores below **80**, halt and report the findings. The user must either fix the issues or explicitly override with phrases like *"commit anyway"* or *"skip quality gate"*.
- If all files score 80+, continue.

**Full mode only:** spawn the **verifier** agent (via `Task` with `subagent_type=verifier`) to run compilation/render checks on the changed files. Report pass/fail before committing. (Quick mode relies on the two script gates above; the verifier runs when work is headed for `main`.)

### Step 0b: Surface-Sync Gate (Pre-Commit)

**Runs unconditionally.** Enforces that count claims (`"14 agents, 28 skills, 24 rules, 6 hooks"` and siblings) across README.md, CLAUDE.md, the guide source + rendered HTML, the landing page, and the skill template all agree with the on-disk counts of `.claude/{skills,agents,rules,hooks}`:

```bash
./scripts/check-surface-sync.sh
```

- **Exit 0:** all counts consistent — continue.
- **Exit 1:** drift detected — print the diff and halt. Fix the stale counts, then re-run. Do NOT proceed past this gate on drift, even with "commit anyway" — the purpose is to catch the exact class of issue that produced PRs #70, #76, and #78.
- **Exit 2:** script error (missing surface file, unreadable directory) — investigate before proceeding.

### Step 1: Check current state

```bash
git status
git diff --stat
git log --oneline -5
```

### Step 2: Create a branch (full mode; or quick mode when currently on `main`)

```bash
git checkout -b <short-descriptive-branch-name>
```

### Step 3: Stage files

Add specific files (never use `git add -A`):

```bash
git add <file1> <file2> ...
```

Do NOT stage `.claude/settings.local.json` or any files containing secrets.

### Step 4: Commit with a descriptive message

If `$ARGUMENTS` is provided, use it as the commit message. Otherwise, analyze the staged changes and write a message that explains *why*, not just *what*.

```bash
git commit -m "$(cat <<'EOF'
<commit message here>
EOF
)"
```

### Step 5: Push and create PR (full mode only)

```bash
git push -u origin <branch-name>
gh pr create --title "<short title>" --body "$(cat <<'EOF'
## Summary
<1-3 bullet points>

## Test plan
<checklist>

🤖 Generated with [Claude Code](https://claude.com/claude-code)
EOF
)"
```

### Step 6: Merge and clean up (full mode only)

```bash
gh pr merge <pr-number> --merge --delete-branch
git checkout main
git pull
```

### Step 7: Report

Quick mode: report the commit hash and a one-line summary. Full mode: report the PR URL and what was merged.

## Important

- **Never skip Step 0.** Quality gates catch broken compilation, bad citations, and hardcoded paths before they reach `main`. If the user insists on skipping, record their override reason in the commit message.
- Never commit directly to `main` — quick mode commits on the current working branch; full mode (and quick mode invoked from `main`) creates a new branch.
- Exclude `settings.local.json` and sensitive files from staging.
- Use `--merge` (not `--squash` or `--rebase`) unless asked otherwise.
- If the commit message from `$ARGUMENTS` is provided, use it exactly.
