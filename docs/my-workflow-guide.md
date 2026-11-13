# My academic workflow

Use [START_HERE](START_HERE.md) for the canonical Git commands and short starter prompt. The reusable Claude branch is `my-customizations`; the separate Codex repository uses `main`. Both retain the complete academic skill library.

## Working in a project

Describe the task, approve substantive plans, let the agent carry out approved work, and review verified outputs. Keep current objectives and boundaries in project instructions, decisions in session logs, and a checkpoint before stopping. A quality score or successful build is not evidence that scientific results are correct.

Use the existing personal writing, table, figure and presentation rules. The shared writing source stays external. Keep approved examples and project-specific exhibit definitions with the project; do not silently change samples, estimands or inference.

For a workspace inside a larger research folder, create an empty subdirectory and use the same startup commands there. State which parent/sibling paths are read-only in your project description. For an existing populated project, reconcile files individually; do not overlay the template or reset local work.

## Maintaining both workflows

1. Read `docs/upstream-state.json` and the latest refresh record. Compare upstream changes against the recorded source revisions in an isolated checkout.
2. Preserve local customizations and shared writing files. Review each changed procedure and its helper resources before importing it.
3. Keep Backman’s flagship mapped to `review-paper-full`; Pedro’s `review-paper` is a different procedure. Backman’s other skills and Moore’s Stata reference remain separately sourced.
4. Run `bash scripts/backtest.sh`; render changed guide sources and synchronize the published HTML. For Codex also run its native validator and update reviewed provenance hashes.
5. Commit explicit paths and push only on the owner’s request. Never rewrite shared history to refresh the template. Existing research projects need a separate, scoped update.

Source pins: [current registry](upstream-state.json). Capabilities: [README](../README.md). General procedures: [full guide](../guide/workflow-guide.qmd).

## Codex in Claude Code

Use OpenAI’s official Codex plugin already installed for Claude Code. It is managed through the plugin system, separately from this template. Do not copy a community helper into `.claude/skills/` or maintain a helper-specific Git remote. Invoke the commands actually exposed by the installed official plugin.

## Keep improvements small

Start with a concrete recurring problem. Prefer improving an existing rule or skill over adding another wrapper. Record what failed, the proposed remedy and how it was checked; keep speculative advice optional. Retain the full skill library at startup and select procedures as needed instead of deleting skills by project category.
