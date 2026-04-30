# My Workflow: Starting New Projects from the Customized Template

**Author:** Xiongfei Li
**Template branch:** `my-customizations` on `XiongfeiLi6/claude-code-my-workflow`
**Last updated:** 2026-04-06

---

## Overview

You maintain a **forked workflow template** with two branches:

- **`main`** — clean mirror of Pedro Sant'Anna's upstream
- **`my-customizations`** — `main` + your curated additions (Backman's review skills, Moore's Stata skill, Codex, etc.)

Every new project starts by copying from `my-customizations`, then gets tailored to that specific project.

---

## Part A: Starting a New Project

### Step 1: Create the project repo

```bash
# Create a new directory for your project
mkdir ~/Documents/my-new-project
cd ~/Documents/my-new-project

# Initialize git
git init

# Pull the template content (without fork history)
git remote add template https://github.com/XiongfeiLi6/claude-code-my-workflow.git
git fetch template my-customizations
git checkout -b main template/my-customizations
git remote remove template

# Create your own GitHub repo and push
gh repo create my-new-project --private --source=. --remote=origin --push
```

This gives you a clean repo with all the infrastructure but no fork relationship to maintain.

### Step 1 (Variant): Subdirectory inside a larger project tree

This is the layout you actually use for research projects: the data, analysis code, and manuscript already live in a parent folder (often Dropbox-synced and shared with co-authors), and you want a writable Claude Code workspace as a *subdirectory* inside that tree. The data/code/manuscript folders are siblings of the workspace, not children — so the workspace itself is empty when you start.

**Layout this variant assumes:**

```
~/path/to/your-research-project/    ← read-only or co-author-shared, NOT a git repo
├── Data/                           ← read-only inputs
├── Analysis/                       ← read-only inputs (legacy code)
├── manuscript/                     ← read-only inputs (Overleaf-synced .tex)
└── ClaudeCode/                     ← writable workspace — THIS is your git repo
    └── (empty before you run the commands below)
```

CLAUDE.md will then carry a "Top Rule — Upstream Files Are READ-ONLY" section pointing at the parent's `Data/`, `Analysis/`, `manuscript/` paths.

**Commands** (works for any empty subdirectory; no `mkdir` since the folder already exists):

```bash
cd ~/path/to/your-research-project/ClaudeCode    # workspace folder (must be empty)
git init

# Pull the template content (no GitHub fork relationship — git history IS preserved)
git remote add template https://github.com/XiongfeiLi6/claude-code-my-workflow.git
git fetch template my-customizations
git checkout -b main template/my-customizations
git remote remove template

# Create your own private GitHub repo and push
gh repo create your-project-name --private --source=. --remote=origin --push
```

**What "without fork history" actually means.** The new repo is *not* a GitHub-level fork (so it's independent on GitHub — PRs and issues stay in your repo, not the template's). The full git commit history of `my-customizations` IS preserved — every commit from Pedro, Backman, Moore, and your own customizations comes along. That's a feature, not a bug: future `git log` calls show why a skill exists.

**Pre-flight check** — before running these commands, make sure the workspace folder won't collide with the template:

```bash
cd ~/path/to/your-research-project/ClaudeCode
ls -A    # should show nothing, or only files that don't appear in the template
```

If the folder is empty, you're safe. If it has files, check whether any name appears in the template's tree (e.g., `CLAUDE.md`, `.claude/`, `README.md`) — if so, `git checkout -b main template/my-customizations` will refuse with `"error: The following untracked working tree files would be overwritten by checkout"`. In that rare case, see the **fallback** below.

**Fallback: existing folder with tracked files that collide with the template**

If you really need to fold the template into a folder that already has `CLAUDE.md` or `.claude/` (e.g., you started ad-hoc and now want to formalize), don't fight `git checkout`. Snapshot the existing folder, then copy only the infrastructure paths from a local clone of the template:

```bash
cd ~/path/to/existing-folder

# 1. Init + snapshot existing state in case anything goes wrong
git init && git add -A && git commit -m "Snapshot before adding workflow" || true

# 2. Copy infrastructure paths from a local clone of the template
TEMPLATE=~/Documents/GitHub/claude-code-my-workflow
(cd $TEMPLATE && git checkout my-customizations && git pull --ff-only)
cp -r $TEMPLATE/.claude .
cp    $TEMPLATE/CLAUDE.md .
[ -f $TEMPLATE/MEMORY.md ]            && cp    $TEMPLATE/MEMORY.md .
[ -d $TEMPLATE/templates ]            && cp -r $TEMPLATE/templates .
[ -d $TEMPLATE/quality_reports ]      && cp -r $TEMPLATE/quality_reports .

# 3. Commit infrastructure as one labeled commit
git add .claude CLAUDE.md MEMORY.md templates quality_reports 2>/dev/null
git commit -m "Add Claude Code workflow infrastructure from my-customizations"

# 4. Push (only create remote if missing)
git remote get-url origin &>/dev/null \
  || gh repo create your-project-name --private --source=. --remote=origin --push
```

Tradeoff: the fallback gives you one clean infrastructure commit but does **not** preserve the template's commit history. Use the main subdirectory variant whenever you can.

### Step 2: Launch Claude Code and run the starter prompt

```bash
cd ~/Documents/my-new-project
claude
```

Paste this prompt (fill in the brackets):

```
I am starting to work on [PROJECT NAME] in this repo. [Describe your project
in 2-3 sentences — e.g., "This is an applied micro paper studying the effect
of X on Y using difference-in-differences with staggered treatment adoption.
The data is from [source] covering [years]. We use Stata for all analysis."]

I've set up the Claude Code academic workflow from my template. Please:
1. Read CLAUDE.md, MEMORY.md, and the rules in .claude/rules/
2. Fill in the [BRACKETED PLACEHOLDERS] in CLAUDE.md with my project details
3. Delete skills and agents I won't need for this project type
4. Enter plan mode and show me what you've configured
```

### Step 3: Claude configures your project

Claude will:
- Fill in `CLAUDE.md` with your project name, institution, folder structure
- Identify which skills to keep vs remove based on project type
- Set up `MEMORY.md` with project-specific context
- Present a plan for your approval

**What to remove by project type:**

| Project Type | Keep | Remove |
|-------------|------|--------|
| **Research paper** | review-paper-full, review-paper-light, review-paper-code, stata, lit-review, research-ideation, data-analysis, commit | compile-latex, create-lecture, pedagogy-review, slide-excellence, deploy, qa-quarto, translate-to-quarto, extract-tikz, visual-audit, devils-advocate |
| **Course materials** | compile-latex, create-lecture, slide-excellence, pedagogy-review, visual-audit, proofread, stata, commit | review-paper-full, review-paper-light, review-paper-code, review-pap, review-grant, lit-review, research-ideation |
| **Grant proposal** | review-grant, review-paper-light, lit-review, research-ideation, commit | compile-latex, create-lecture, slide-excellence, deploy, qa-quarto, extract-tikz |
| **Pre-analysis plan** | review-pap, research-ideation, stata, data-analysis, commit | compile-latex, create-lecture, slide-excellence, deploy |

### Step 4: Set up your .gitignore

Claude will help, but here's what to think about:

```gitignore
# Always exclude
*.log *.aux *.bbl *.blg *.out *.nav *.snm *.toc *.synctex.gz
.DS_Store
.claude/state/
.claude/settings.local.json

# Project-specific decisions:
# - PDFs: exclude if you rebuild from source, keep if distributing
# - Data: exclude large .dta files, keep small reference datasets
# - Private: student data, copyrighted materials, API keys
```

### Step 5: Initial commit and push

```bash
git add -A
git commit -m "Initialize project from workflow template"
git push -u origin main
```

---

## Part B: Daily Workflow Within a Project

### Starting a work session

```bash
cd ~/Documents/my-new-project
claude
```

Claude reads `CLAUDE.md` and `MEMORY.md` automatically. If resuming after a break, it checks the most recent session log and git history.

### The work loop

1. **Describe what you want** — natural language is fine
   - "Write the introduction section of the paper"
   - "Create a Stata script that runs the main DiD regression"
   - "Review this draft before I send it to my coauthor"

2. **Claude plans** (for non-trivial tasks) — you approve or adjust

3. **Claude implements** — the orchestrator handles:
   - Implementation
   - Verification (compiles, runs, checks output)
   - Review (specialized agents check quality)
   - Fix (applies fixes from review)
   - Score (quality gates: 80 to commit, 90 to teach/submit)

4. **You review the result** — approve, request changes, or iterate

### Key slash commands

**For research papers:**
```
/review-paper-full AER              # Full 6-agent review targeting AER
/review-paper-light                 # Quick 2-agent check (~1 min)
/review-paper-code                  # Check paper-code consistency
/lit-review [topic]                 # Literature search + synthesis
/research-ideation [topic]          # Generate research questions
```

**For course materials:**
```
/create-lecture [Lecture N: Topic]   # Full lecture creation
/compile-latex [file.tex]            # 3-pass XeLaTeX
/slide-excellence [file.tex]         # Multi-agent slide review
/proofread [file.tex]                # Grammar/typo check
```

**For grants and PAPs:**
```
/review-grant NSF                   # 6-agent grant review (NSF persona)
/review-pap AEA                     # PAP review (AEA registry standards)
```

**For Stata work:**
```
/stata                              # Stata coding reference (auto-triggers)
/data-analysis [dataset]            # End-to-end Stata analysis
```

**Always available:**
```
/commit                             # Stage, commit, PR, merge
/context-status                     # Check session health
/deep-audit                         # Repository-wide consistency check
```

### Committing and pushing

After completing a unit of work:

```
/commit
```

Or tell Claude: "commit and push what we've done." Claude stages the right files, writes a commit message, and pushes.

---

## Part C: Maintaining the Template

### When you find a new skill you want

```bash
cd ~/Documents/GitHub/claude-code-my-workflow
git checkout my-customizations

# Add the skill
mkdir -p .claude/skills/new-skill
# Copy or create SKILL.md

git add .claude/skills/new-skill/
git commit -m "Add new-skill: [description]"
git push origin my-customizations
```

The skill is now available for all future projects (but not retroactively added to existing ones — copy manually if needed).

### When Pedro updates upstream

```bash
cd ~/Documents/GitHub/claude-code-my-workflow

# Sync main with Pedro
git checkout main
git fetch upstream
git merge upstream/main
git push origin main

# Rebase your customizations on top
git checkout my-customizations
git rebase main
# If conflicts (rare): resolve, then git rebase --continue
git push origin my-customizations --force-with-lease
```

> **If `git push` is rejected after the rebase, DO NOT run `git pull`.** A rejected push is normal after a rebase (your local history was rewritten, so it no longer matches the remote). `git pull` will *merge* the old remote history back in and create a duplicate-commits mess. The correct fix is `git push --force-with-lease` (the command above already uses it).

### When other skills' authors update their skills

Your `my-customizations` branch carries skills authored by third parties (not Pedro). These **do not auto-update** when you sync with Pedro's upstream — you have to refresh them by hand.

**Step 0: Source registry**

Each third-party author uses a different layout in their repo. Here are the three sources and how their files map to ours:

| Skill family | Author | Source repo | Layout in source | Layout in your fork |
|---|---|---|---|---|
| `review-paper-full`, `review-paper-light`, `review-paper-code`, `review-pap`, `review-grant` | Backman | https://github.com/claesbackman/AI-research-feedback | flat `Skills/<name>.md` (one file per skill) | `.claude/skills/<name>/SKILL.md` (each wrapped in a directory) |
| `stata` (incl. `packages/` + `references/`) | Moore | https://github.com/dylantmoore/stata-skill | `plugins/stata/skills/stata/...` (plugin layout) | `.claude/skills/stata/...` |
| `codex` | oil-oil | https://github.com/oil-oil/codex | `SKILL.md` + `scripts/` at repo root | `.claude/skills/codex/SKILL.md` + `.claude/skills/codex/scripts/` |

**Important — the `review-paper` rename.** Backman ships his flagship skill as `review-paper`. Pedro's upstream also ships a skill called `review-paper` (different content, same name). To avoid the collision we renamed Backman's copy to `review-paper-full` in our fork. **Refreshing this one skill needs a special procedure** (below) — the simple `git checkout backman/main -- ...` pattern would overwrite Pedro's `review-paper` instead.

**Baseline as of 2026-04-30** (so you can tell what's already in):

| Skill family | Source commit | Status |
|---|---|---|
| Backman skills (all 5) | `b2a42c3` | ✅ in sync |
| Moore stata | `33a7efc` | ✅ in sync |
| Codex | `0b9f1d0` | ⚠️ local has divergence (we copied an older version with edits — refresh later if you want oil-oil's newer wording, including a Windows PowerShell variant we currently don't ship) |

Update this table whenever you do a refresh.

**Step 1: Add source remotes once**

You only need to do this the first time:

```bash
cd ~/Documents/GitHub/claude-code-my-workflow
git checkout my-customizations

git remote add backman   https://github.com/claesbackman/AI-research-feedback.git
git remote add moore     https://github.com/dylantmoore/stata-skill.git
git remote add codex-src https://github.com/oil-oil/codex.git
```

These remotes stay in your repo permanently; they don't conflict with anything.

**Step 2: Refresh recipes — pick the one for the skill you're updating**

Always start each refresh with:
```bash
cd ~/Documents/GitHub/claude-code-my-workflow
git checkout my-customizations
git tag backup/pre-skill-refresh-$(date +%Y-%m-%d)   # safety net
```

#### Recipe A — Backman skills (the renamed `review-paper-full`)

Backman's `Skills/review-paper.md` lives in our repo as `.claude/skills/review-paper-full/SKILL.md`. We use `git show ... > destination` (NOT `git checkout`) to dump his file content into our renamed location without touching Pedro's `review-paper`:

```bash
git fetch backman

# See what Backman changed
git log --oneline -10 backman/main -- Skills/review-paper.md

# Overwrite OUR review-paper-full/SKILL.md with HIS review-paper.md content
git show backman/main:Skills/review-paper.md > .claude/skills/review-paper-full/SKILL.md

# Review BEFORE committing — Backman may have changed flags, defaults, agent counts
git diff .claude/skills/review-paper-full/SKILL.md

# If something looks wrong, abort:
# git checkout HEAD -- .claude/skills/review-paper-full/SKILL.md

# Otherwise, commit with his commit hash
HASH=$(git log -1 --format=%h backman/main)
git add .claude/skills/review-paper-full/SKILL.md
git commit -m "Refresh review-paper-full from Backman ${HASH}"
git push origin my-customizations
```

#### Recipe B — Backman skills (NOT renamed: `review-paper-light`, `review-paper-code`, `review-pap`, `review-grant`)

For these the names match, so the simple pattern works. Pick the skill name and run:

```bash
SKILL=review-paper-light    # or review-paper-code, review-pap, review-grant

git fetch backman

# See what changed
git log --oneline -10 backman/main -- "Skills/${SKILL}.md"

# Pull his version into our directory layout
git show "backman/main:Skills/${SKILL}.md" > ".claude/skills/${SKILL}/SKILL.md"

git diff ".claude/skills/${SKILL}/SKILL.md"

HASH=$(git log -1 --format=%h backman/main)
git add ".claude/skills/${SKILL}/SKILL.md"
git commit -m "Refresh ${SKILL} from Backman ${HASH}"
git push origin my-customizations
```

#### Recipe C — Moore stata (multi-file, plugin → flat path translation)

Moore keeps his skill at `plugins/stata/skills/stata/` but we keep ours at `.claude/skills/stata/`. Refresh the whole tree at once:

```bash
git fetch moore

# See what changed
git log --oneline -10 moore/main -- plugins/stata/skills/stata/

# Pull his entire stata tree into a temp dir, then move into place
git checkout moore/main -- plugins/stata/skills/stata/
rm -rf .claude/skills/stata
mkdir -p .claude/skills
mv plugins/stata/skills/stata .claude/skills/stata
rm -rf plugins                      # clean up the leftover plugin scaffold

# Review — this will be a big diff (50+ files); skim package/reference changes
git diff .claude/skills/stata/

HASH=$(git log -1 --format=%h moore/main)
git add .claude/skills/stata/ plugins
git commit -m "Refresh stata skill from Moore ${HASH}"
git push origin my-customizations
```

> Moore also ships `stata-c-plugins` and `stata-skill-contributor` plugins in his repo. We don't carry those — ignore unless you decide to add them.

#### Recipe D — Codex (small, root-level layout)

Codex's repo IS the skill — `SKILL.md` and `scripts/` sit at the repo root. We place them under `.claude/skills/codex/`:

```bash
git fetch codex-src

# See what changed
git log --oneline -10 codex-src/main

# Pull SKILL.md and scripts into our location
git show codex-src/main:SKILL.md > .claude/skills/codex/SKILL.md
git show codex-src/main:scripts/ask_codex.sh > .claude/skills/codex/scripts/ask_codex.sh
chmod +x .claude/skills/codex/scripts/ask_codex.sh

# (Optional) the upstream now ships a Windows PowerShell variant — pull it too if you want it
# git show codex-src/main:scripts/ask_codex.ps1 > .claude/skills/codex/scripts/ask_codex.ps1

git diff .claude/skills/codex/

HASH=$(git log -1 --format=%h codex-src/main)
git add .claude/skills/codex/
git commit -m "Refresh codex skill from oil-oil ${HASH}"
git push origin my-customizations
```

⚠️ Our local `codex/SKILL.md` currently has divergence from upstream (older base + your edits). Running Recipe D will overwrite both. If you want to keep your local edits, use the cherry-pick pattern below instead.

**If you've made local edits to a third-party skill**

The `git show ... > destination` pattern in the recipes above will overwrite your edits silently. Two options:

- **Accept theirs, redo your edits** — run the recipe, then re-apply your local changes by hand.
- **Keep yours, cherry-pick just their fix** — view the diff first and copy in only what you want:
  ```bash
  diff <(git show backman/main:Skills/review-paper.md) .claude/skills/review-paper-full/SKILL.md
  ```
  Edit `.claude/skills/review-paper-full/SKILL.md` manually with the parts you want.

**If something goes wrong after a refresh**

The `backup/pre-skill-refresh-YYYY-MM-DD` tag from Step 2 is your escape hatch:
```bash
git reset --hard backup/pre-skill-refresh-2026-04-30
git push --force-with-lease origin my-customizations
```

**Existing project repos do NOT auto-update from refreshed skills** — see the next section.

### When to update existing projects

Existing project repos are **independent copies** — they don't auto-update when the template changes. To bring in a new skill to an existing project:

```bash
cd ~/Documents/my-existing-project

# Copy a specific skill from the template
cp -r ~/Documents/GitHub/claude-code-my-workflow/.claude/skills/new-skill \
      .claude/skills/new-skill

git add .claude/skills/new-skill
git commit -m "Add new-skill from template"
```

---

## Part D: Example Walkthroughs

### Example 1: New research paper

```bash
# 1. Create project
mkdir ~/Documents/Research/minimum-wage-did
cd ~/Documents/Research/minimum-wage-did
git init
git remote add template https://github.com/XiongfeiLi6/claude-code-my-workflow.git
git fetch template my-customizations
git checkout -b main template/my-customizations
git remote remove template
gh repo create minimum-wage-did --private --source=. --remote=origin --push

# 2. Launch Claude
claude

# 3. Starter prompt:
# "I am starting a research paper on the effect of minimum wage increases on
#  employment using county-level data and staggered DiD (Callaway-Sant'Anna).
#  Data is from QCEW 2010-2023. Software: Stata. Please configure this project,
#  remove skills I don't need for a paper, and enter plan mode."

# 4. Claude configures, removes lecture/slide skills, keeps:
#    stata, review-paper-full, review-paper-light, review-paper-code,
#    lit-review, research-ideation, data-analysis, commit, deep-audit

# 5. Start working:
# "Run a literature review on minimum wage employment effects using DiD"
# "Create the main analysis .do file with csdid estimation"
# "Review my draft: /review-paper-full AER"
```

### Example 2: New course

```bash
# 1. Create project (same template pull)
mkdir ~/Documents/Teaching/micro-principles
cd ~/Documents/Teaching/micro-principles
git init
git remote add template https://github.com/XiongfeiLi6/claude-code-my-workflow.git
git fetch template my-customizations
git checkout -b main template/my-customizations
git remote remove template
gh repo create micro-principles --private --source=. --remote=origin --push

# 2. Launch Claude with:
# "I am starting Principles of Microeconomics at UIBE. Beamer slides,
#  14 lectures. Remove research/paper skills, keep teaching skills."

# 3. Start building:
# "/create-lecture Lecture 1: Supply and Demand"
# "/compile-latex Slides/Lecture01_SupplyDemand.tex"
# "/slide-excellence Slides/Lecture01_SupplyDemand.tex"
```

### Example 3: Grant proposal

```bash
# 1. Create project (same pattern)
# 2. Launch Claude with:
# "I am writing an NSF grant proposal on [topic]. Keep review-grant,
#  lit-review, research-ideation. Remove lecture/slide skills."

# 3. Work:
# "Draft the project description section"
# "/review-grant NSF"
# "Address the critical issues from the review"
```

---

## Quick Reference Card

| Task | Command |
|------|---------|
| Start new project | `git init` + pull from template + `gh repo create` |
| Configure project | Paste starter prompt in Claude |
| Full paper review | `/review-paper-full [journal]` |
| Quick paper check | `/review-paper-light` |
| Code reproducibility | `/review-paper-code` |
| Grant review | `/review-grant [funder]` |
| PAP review | `/review-pap [registry]` |
| Stata help | `/stata` (auto-triggers on Stata questions) |
| Build lecture | `/create-lecture [topic]` |
| Review slides | `/slide-excellence [file]` |
| Compile LaTeX | `/compile-latex [file]` |
| Commit + push | `/commit` |
| Sync template | `main`: merge upstream; `my-customizations`: rebase on main |
| Add skill to template | Commit to `my-customizations` branch |
| Add skill to project | Copy from template into project's `.claude/skills/` |

---

## Current Skill Inventory (my-customizations)

| Skill | Source | Slash Command | Use Case |
|-------|--------|---------------|----------|
| review-paper-full | Backman | `/review-paper-full` | 6-agent pre-submission review |
| review-paper-light | Backman | `/review-paper-light` | Quick 2-agent review |
| review-paper-code | Backman | `/review-paper-code` | Paper-to-code reproducibility |
| review-pap | Backman | `/review-pap` | Pre-analysis plan review |
| review-grant | Backman | `/review-grant` | Grant proposal review |
| stata | Moore | `/stata` | Comprehensive Stata reference |
| codex | — | `/codex` | Delegate coding to Codex CLI |
| compile-latex | Sant'Anna | `/compile-latex` | 3-pass XeLaTeX |
| create-lecture | Sant'Anna | `/create-lecture` | Full lecture creation |
| slide-excellence | Sant'Anna | `/slide-excellence` | Multi-agent slide review |
| proofread | Sant'Anna | `/proofread` | Grammar/typo review |
| visual-audit | Sant'Anna | `/visual-audit` | Slide layout audit |
| pedagogy-review | Sant'Anna | `/pedagogy-review` | Teaching quality review |
| review-r | Sant'Anna | `/review-r` | R code review |
| lit-review | Sant'Anna | `/lit-review` | Literature search |
| research-ideation | Sant'Anna | `/research-ideation` | Research question generation |
| interview-me | Sant'Anna | `/interview-me` | Research idea formalization |
| data-analysis | Sant'Anna | `/data-analysis` | End-to-end analysis |
| validate-bib | Sant'Anna | `/validate-bib` | Citation cross-reference |
| devils-advocate | Sant'Anna | `/devils-advocate` | Challenge design decisions |
| commit | Sant'Anna | `/commit` | Git commit workflow |
| learn | Sant'Anna | `/learn` | Extract discovery into skill |
| context-status | Sant'Anna | `/context-status` | Session health check |
| deep-audit | Sant'Anna | `/deep-audit` | Repository consistency audit |
| deploy | Sant'Anna | `/deploy` | Quarto to GitHub Pages |
| qa-quarto | Sant'Anna | `/qa-quarto` | Adversarial Quarto QA |
| translate-to-quarto | Sant'Anna | `/translate-to-quarto` | Beamer to Quarto |
| extract-tikz | Sant'Anna | `/extract-tikz` | TikZ to SVG |
