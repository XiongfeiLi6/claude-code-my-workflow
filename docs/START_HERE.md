# Start a project with the complete Claude workflow

Use this template for a paper, proposal, lecture series, or a combination. No profile installer is required.

## Copy the local folder with fresh Git history

Choose a directory that does not exist. Run each step separately and stop on errors.

```sh
mkdir ~/Documents/my-new-project
```

```sh
rsync -a --exclude='/.git/' --exclude='/quality_reports/' --exclude='/writing/' --exclude='/.claude/state/' --exclude='/.claude/settings.local.json' --exclude='__pycache__/' --exclude='.DS_Store' ~/Documents/GitHub/claude-code-my-workflow/ ~/Documents/my-new-project/
```

```sh
cd ~/Documents/my-new-project
git init -b main
```

Keep the hidden .claude folder. The optional .agents bridge is also copied; the separate Codex workflow has full native skills. Personal writing stays in its shared external folder. Do not use this copy command to overwrite an existing research project.

## Your Git-fetch method

This uses the committed customization branch and retains its history:

```sh
mkdir ~/Documents/my-new-project
cd ~/Documents/my-new-project
git init
git remote add template https://github.com/XiongfeiLi6/claude-code-my-workflow.git
git fetch template my-customizations
git checkout -b main template/my-customizations
git remote remove template
```

Removing the remote does not remove template history. Use the folder copy if you want a fresh history.

## First-session prompt

Open the new project in Claude Code and adapt this prompt:

```text
I am starting [PROJECT NAME], a [paper / proposal / lecture series / mixed project].
[Describe the objective, audience, materials and expected tools in 2–3 sentences.]

I copied my complete academic workflow. Read CLAUDE.md and the relevant rules,
inspect the files, and propose a concise setup plan. After approval, replace
template placeholders with this project's objectives, deliverables, file layout,
data boundaries, entry points, build commands and verification requirements.
Ask about missing substantive decisions; do not invent scientific choices.
Keep the full skill library available and preserve my single external writing source.
Plan substantial work, record decisions and corrections, and save checkpoints.
Verify a small real build using the tools this project needs. Do not alter hook
trust, local permission settings or protected gates during routine customization.
Commit, push, publish, send messages or create GitHub items only when I request
the corresponding action. Explain the workflow briefly in our first sessions.
```

For a paper, record approved samples, estimands and inference. For a proposal,
record the funder, call and deadline. For lectures, record prerequisites, learning
objectives and the chosen presentation format. New explorable skills are optional.

## GitHub

Ask for a reviewed initial commit with explicit paths, excluding restricted data,
credentials and local state. Then create the private repository when ready:

```sh
gh repo create my-new-project --private --source=. --remote=origin --push
```

See the [full guide](../guide/workflow-guide.qmd) and [refresh record](UPSTREAM_REFRESH_2026-11-13.md).
