# Upstream refresh — 2026-11-13

Owner requested updates to both reusable workflows locally and on GitHub. Work was
reconciled in isolated checkouts; existing shared-writing edits are outside this change.

| Source | Reviewed head | Result |
|---|---|---|
| Pedro | fe7077463c06e6d1572bb6c13d1b00525a4ff28e | Latest reviewed snapshot integrated in Claude; relevant procedures/helpers adapted in Codex |
| Backman | 4c1aef514cf4aa520937131a54830b4af0e403db | Three optional explorable presentation skills and their resources added |
| Moore | 33a7efc85e92cd30edc7b907f1deb9d7038397bc | No change |
| oil-oil | 9e20bea3dda969de7fcd120f5176b585ea172cc5 | Checked; remains retired |

Codex retains full native skills, not Pedro's generated wrappers. Claude-specific
permission modes, model routing, plugin/mod behavior, hook retirement and UI commands
do not become Codex instructions. Native context reporting already uses actual evidence.
The upstream optional AI detector recommendation is not adopted as a writing target.
Existing scientific choices and the single external personal writing source take precedence.
Codex's per-path review ledger is workflow/upstream-review-2026-11-13.json.

The complete-folder method remains the default for papers, proposals and lectures.
Use each repository's own branch: Claude my-customizations; Codex main. Fetch/checkout
retains template history; copying without .git starts fresh. Copy hidden folders, but
exclude local state, old project reports, releases, personal writing and credentials.

Codex fixes: harmless read commands no longer trigger the broad shell-write regex;
native gate destinations use the token-aware parser; patch/MCP content is distinguished
from destination paths; empty passport warnings are suppressed. Setup diagnostics cover
all tool groups in a full copy, with explicit --profile filtering. New release exports
include MEMORY.md and the project contract; the old immutable 0.1.0 snapshot is historical.

These are source/configuration and fixture checks. They do not certify every presentation
renderer, account integration, actual Codex hook trust or a new project's scientific pipeline.
Review changed hook definitions through the application's normal trust interface.

Deck scaffolders also refuse existing destinations rather than cleaning their build folders.
