# Start a new academic project

Copy the complete customization branch with Git, then describe your project to Claude Code. No profile installer is needed.

## 1. Create the project from GitHub

Choose a new folder and an unused repository name. Replace `my-new-project` throughout, run in order, and stop on any error.

```bash
# Create a new directory for your project
mkdir ~/Documents/my-new-project
cd ~/Documents/my-new-project

# Initialize git
git init

# Copy the committed template, including its Git history
git remote add template https://github.com/XiongfeiLi6/claude-code-my-workflow.git
git fetch template my-customizations
git checkout -b main template/my-customizations
git remote remove template

# Use the external shared writing folder instead of keeping a project copy
git rm -r -- writing
git commit -m "Use external shared writing rules"

# Create your own GitHub repo and push
gh repo create my-new-project --private --source=. --remote=origin --push
```

This creates an independent private GitHub repository and retains the template’s Git history. The `writing` removal applies only inside the new project: your shared originals stay in the workflow repository. Earlier history still contains the historical template files. No research data or local uncommitted writing edits are copied from your working tree.

## 2. Open the project and paste this prompt

Run `claude` in the new directory, or open it in the Claude Code interface you use:

```text
I’m starting [PROJECT NAME] in this repository.
[Describe the project, available materials and preferred tools in 2–3 sentences.]

Read CLAUDE.md, MEMORY.md and the relevant .claude rules. Propose
the setup, then adapt the project instructions and configuration after my
approval. Keep the complete skill library available.

Work carefully, verify results, and record decisions and corrections so I
do not have to repeat them. Preserve my customized writing, table, figure
and presentation styles, using the single shared writing folder.

Plan substantial tasks first. Once I approve a plan, carry out the work
autonomously and ask when a substantive decision or ambiguity needs me.
Explain the workflow a little more during our first few sessions.

Start with the project setup plan.
```

Adapted from [Pedro Sant’Anna’s original starter prompt](https://github.com/pedrohcgs/claude-code-my-workflow/blob/fe7077463c06e6d1572bb6c13d1b00525a4ff28e/guide/workflow-guide.qmd#L305). Keep your project description general; Claude selects relevant procedures.

## 3. Keep the shared style

The single shared writing folder on this Mac is `~/Documents/GitHub/Codex-my-workflow/writing` (the same files as the Claude workflow’s writing folder). Project instructions should reference its `manuscript-writing-style.md`, `house-style-exemplars.md` and `exhibit-notes-style.md`, preserving your table, figure and presentation conventions. Do not create project-local copies.

Run `bash scripts/backtest.sh` for infrastructure checks, and verify a small actual project build. Review permissions and hooks normally; do not copy trust or enable automation as part of startup. Future commits, pushes and messages require their corresponding request.

OpenAI’s official Codex plugin for Claude Code is managed separately. Keep the installed official plugin; there is no community Codex helper to copy or refresh in this template.

See [the full guide](../guide/workflow-guide.qmd) and [template maintenance](my-workflow-guide.md).
