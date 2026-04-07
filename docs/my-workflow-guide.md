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

### Step 1 (Variant): Existing folder with data/code/manuscript already in place

Use this variant when you're adding Claude Code to a project that **already exists** — for example, a paper repository with `data/`, `code/`, and `manuscript/` folders already populated.

**Why not use the regular Step 1?** The regular Step 1 uses `git checkout -b main template/my-customizations`, which replaces the working directory with the template's tree. For an existing folder, that would either fail (untracked files present) or risk overwriting your work. Instead, we **copy infrastructure paths only** from a local clone of the template.

```bash
cd ~/Documents/my-existing-project

# 1. Initialize git IF NOT already a repo (no-op if already initialized)
git init

# 2. Snapshot existing work first (so template copy can't silently damage it)
git add -A
git commit -m "Snapshot existing project state before adding workflow" || true

# 3. Check for collisions BEFORE copying anything
for path in .claude CLAUDE.md MEMORY.md templates quality_reports; do
  if [ -e "$path" ]; then
    echo "COLLISION: $path already exists — review before overwriting"
  fi
done

# 4. Make sure your local template clone is on my-customizations and up to date
TEMPLATE=~/Documents/GitHub/claude-code-my-workflow
(cd $TEMPLATE && git checkout my-customizations && git pull origin my-customizations)

# 5. Copy ONLY the infrastructure — never data/, code/, manuscript/
cp -r $TEMPLATE/.claude .
cp $TEMPLATE/CLAUDE.md .
[ -f $TEMPLATE/MEMORY.md ] && cp $TEMPLATE/MEMORY.md .
[ -d $TEMPLATE/templates ] && cp -r $TEMPLATE/templates .
[ -d $TEMPLATE/quality_reports ] && cp -r $TEMPLATE/quality_reports .

# 6. Commit the workflow infrastructure as a separate labeled commit
git add .claude CLAUDE.md MEMORY.md templates quality_reports 2>/dev/null
git commit -m "Add Claude Code workflow infrastructure from my-customizations template"

# 7. GitHub remote — ONLY if project doesn't already have one
if ! git remote get-url origin &>/dev/null; then
  gh repo create my-existing-project --private --source=. --remote=origin --push
else
  echo "Remote 'origin' already exists — push manually when ready"
fi
```

**Key differences from the fresh-folder Step 1:**

| Fresh folder (original Step 1) | Existing folder (this variant) |
|---|---|
| `mkdir` + `cd` | `cd` only |
| `git init` on empty folder | `git init` + snapshot existing work first |
| `git checkout -b main template/my-customizations` **replaces** working tree | `cp -r` **adds** specific infrastructure paths only |
| `gh repo create --push` unconditionally | Conditional on no existing `origin` |
| One commit | Two commits: (1) existing state snapshot, (2) infrastructure added |

**Why copy instead of `git merge --allow-unrelated-histories`?** The merge approach would:
- Pollute your project history with Pedro's + Backman's + Moore's template commits
- Risk merge conflicts if any path collides (e.g., `data/`, `.gitignore`)
- Make it harder to see "what did I add from the template" in a clean diff

The copy approach gives you one clean, labeled commit — easy to revert, easy to audit.

**Adjust Step 2's starter prompt for this variant.** Add this line to the prompt so Claude knows the state:

> "This is an **existing** project. I already have `data/`, `code/`, and `manuscript/` folders with content in them. Read CLAUDE.md and configure it for this existing structure — do NOT create new data/code/manuscript folders or assume empty state. Then tell me which skills to remove based on the project type."

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
