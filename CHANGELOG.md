# Changelog

All notable changes to this template are documented here. We follow [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and use loose semantic versioning: **major** when fork upgrades require manual migration, **minor** for new skills or features that are additive, **patch** for fixes and docs.

If you have forked this template, see the **Upgrading** section at the bottom for how to pull updates without losing your customizations.

---

## v1.9.1 — 2026-06-03

A **balance correction** patch release. Restores the tactical audit
checklist that v1.9.0 had compressed to a single 5-item high-level
list. Positive templates (§§3–6) remain the primary constitutional
framing; the tactical "what specifically not to write" content is now
recorded as a subsidiary audit checklist under §7.2.

User feedback after the v1.9.0 constitutional rewrite: the
high-level failure-mode list (5 items) was correct in spirit but
lost too much grep-able specificity. Writers need both the
architectural framing (§§1–6) AND a tactical checklist that
catalogs the specific phrases, punctuation, and inline conventions to
audit before submission.

### Added

`manuscript-writing-style.md` §7 split into two sub-sections:

- **§7.1 The five high-level failures** — unchanged from v1.9.0.
- **§7.2 Specific patterns to grep and cut** — new tactical audit
  checklist organized into eight categories:
  - 7.2.1 Over-defensive expressions (we caution, it should be noted
    that, this is suggestive evidence that, may/might/could stacks,
    trailing repeated-caveat paragraphs).
  - 7.2.2 Inline statistical reporting (p-values in parens, inline
    β/SE duplicating the table, significance stars in prose,
    inline t/F-statistics).
  - 7.2.3 Punctuation overuse (em-dash overuse — three or more per
    paragraph; parenthetical asides burying qualifications;
    semicolon-comma chains; double parentheticals).
  - 7.2.4 Restatement patterns (adjacent "we find/we show/we
    document"; pre-announcing results in section openers;
    restating the table column-by-column).
  - 7.2.5 Empty intensifiers and transition words (clearly,
    obviously, importantly, notably, very, quite, rather; sentence-
    start Furthermore/Moreover/Additionally/In addition).
  - 7.2.6 Verbose constructions (the fact that; in order to; due to
    the fact that; at this point in time; a number of; is able to;
    make use of; with respect to/with regard to).
  - 7.2.7 Formatting and visual noise (parenthetical italicized
    narrative labels; bold for emphasis in body prose; underline;
    ALL CAPS; over-long footnotes).
  - 7.2.8 Citation hygiene (citation clusters > 4–5 entries; citet
    vs citep consistency; verifying bib keys; page numbers for
    direct quotes).

Each row of each sub-checklist has: the trigger (regex-friendly
phrase or pattern), the rationale, and the recommended fix. The
structure supports running a mechanical grep pass over the manuscript
before submission.

### Motivation

User feedback: "I respect your idea on 'not Too much negative
framing', and this rule should be more about positive templates, but
we need to make sure the expression we definitely do not want is
recorded, including but not limited to, over-defensive sentences,
p-values in parethesis, too much unnecessary double dash, and so on.
Find the balance."

The balance: positive templates as the primary teaching content,
tactical audit checklist as the subsidiary enforcement mechanism. Both
visible; neither dominant. The §7.2 checklist is explicitly a
"tactical audit" subsidiary to the §7.1 structural failure modes,
preserving the constructive primary framing of v1.9.0.

### Net effect

Rule file: 412 → 501 lines. All v1.9.0 content retained.

---

## v1.9.0 — 2026-06-03

A **manuscript-writing constitutional rewrite** minor release.
`manuscript-writing-style.md` promoted from a style sheet (with
positive templates + a long anti-pattern list) to a **constitutional
standard** for every economics paper the writer produces, regardless
of submission target. The standard is calibrated to top-5 best
practice; the framing is that aiming at the constitutional standard
guarantees a publishable paper at the highest level, even when the
specific submission target is lower.

The rewrite is motivated by user feedback that the v1.8.x series had
drifted back toward "what not to do, what to drop" framing — exactly
the framing the v1.8.0 baseline was supposed to move away from. The
v1.9.0 rewrite reorganizes content around **positive templates** and
trims the negative content to a short, ranked **common failure modes**
section.

### Structural changes

The rule grew from 228 to 412 lines and gained five new top-level
sections. The new structure:

0. **Calibration and scope** — minimalist vs discursive register;
   empirical vs theory vs hybrid; **AE audience model with reading-
   time table** (NEW).
1. **Foundational principle** — world-claim vs reader-direction;
   three derived rules; self-excusing test.
2. **Document architecture** — empirical, theory, hybrid section
   sequences (NEW; the empirical section sequence is the implicit
   reference structure for every other template in the document).
3. **Section templates** — Abstract, Introduction, Related
   Literature, Institutional Context, Conceptual Framework, Data,
   Empirical Strategy, Results, Robustness, Discussion/Policy,
   Conclusion, Appendix. Each section has a short template; most
   include an example skeleton. (PRIOR VERSION had templates only
   for Subsection Opener, Result Paragraph, Caveat, Transition,
   Footnote — paragraph-level only. NEW VERSION has section-level
   templates that codify what each major manuscript section should
   contain.)
4. **Paragraph-level templates** — Subsection Opener, Result
   Paragraph, **Mechanism / Channel Paragraph** (NEW), Caveat,
   Transition, Footnote.
5. **Sentence-level conventions** — Voice/agency, Tense, Hedging,
   Statistical-significance language, Number presentation (NEW
   section; the prior version only mentioned voice in passing).
6. **Visual conventions** — Table captions/notes, Robustness summary,
   Figure captions, Equations, Emphasis, Citation style,
   Cross-references (NEW section; the prior version had no
   equation-numbering, citation-style, or cross-reference
   conventions).
7. **Common failure modes** — short ranked list of the five
   highest-frequency failures (PRIOR VERSION had 14 anti-patterns;
   NEW VERSION compresses to 5 and reframes each toward the
   constructive fix).
8. **Over-application failures** — the existing "edit the wrapper,
   keep the core" guidance, retained.
9. **Sanity checks** — expanded from 4 to 8 items, including the
   new "inferential-bridge check," "promised-robustness check," and
   "mechanism-acknowledgement check."

### Content additions

- **Abstract template:** five-component skeleton (motivation, gap,
  contribution, headline result, inferential implication) with a
  worked example. Inferential implication required in "Because X, Y"
  form.
- **Introduction architecture:** paragraph-by-paragraph numerical-
  content table extended from the v1.8.2 patch. Added the
  Back-of-the-Envelope (P9) and Related Literature (P11+) rows.
  Added the self-containment test ("a reader who reads only the
  Introduction should leave with the contribution, the method, the
  headline result, the inferential implication").
- **Empirical Strategy template:** four-component skeleton
  (specification, source of variation, identifying assumption,
  threats and mitigations). Adds the "promised-robustness discipline"
  audit.
- **Robustness paragraph template:** three-component skeleton.
- **Discussion / Policy template:** three-component skeleton
  (refinement, quantification, limitations). Codifies that policy
  claims must acknowledge the policy's actual mechanism.
- **Conclusion template:** distinguishes conclusion from summary;
  three components (what we showed, why it matters, open questions).
- **Appendix template:** four-section skeleton (Data, Theory,
  Tables, Figures) with single-canonical-Tables-section discipline.
- **Mechanism / channel paragraph template:** four-step skeleton
  (candidate mechanisms, empirical signatures, observed signature,
  inference).
- **Voice / tense / hedging / number presentation:** explicit rules
  for each of these sentence-level conventions.
- **Equation conventions:** numbering policy, introduction
  ("is given by" / colon), punctuation, symbol-definition discipline.
- **Citation and cross-reference style:** `\citet` vs `\citep`,
  citation-cluster alphabetization, `\Cref` capitalization rules,
  hard-coded vs labeled cross-references.

### Constitutional framing

The "constitutional" framing is explicit at the top of the document.
The standard is the same for every paper — not because every paper
will be submitted to a top-5 journal, but because the constitutional
standard guarantees quality regardless of journal. Calibration to top-5
best practice provides a single fixed reference.

### No content removed

Every positive template in the v1.8.2 version is retained verbatim or
edited only for clarity. The "Anti-patterns to cut" section is the
only material that was substantially compressed — from 14 items to 5
common failure modes, with the cut items either folded into the
positive templates they motivated or quietly retired.

### Motivation

User asked for a constitutional rewrite after auditing the v1.8.x
series: "treat this writing style as a constitutional file for all
papers I am gonna write in Economics study. The standard should the
highest, as high as the best practice in Top 5 papers."

---

## v1.8.2 — 2026-06-03

A **manuscript-writing convention** patch release. Expands
`manuscript-writing-style.md` with five new positive templates and two
new anti-patterns drawn from a real top-5 revision sprint on an
empirical economics paper. The rule grew from 117 to 227 lines; all
additions are universally applicable principles tested against AER and
QJE intro arcs, robustness-summary conventions, and policy-section
norms.

### Added

- **Introduction architecture: where numbers go.** New positive
  template. Codifies the top-5 intro arc: P1–2 motivation + question
  (no numbers); P3 high-level finding + headline magnitude (one
  headline number); P4–5 why-not-obvious + identification (no
  numbers); P6–8 detailed-results paragraphs (specific per-spec ranges
  + per-outcome magnitudes); P9+ policy + literature. Failure mode to
  catch: all numbers in P3 and no numbers in P6–8 (referees skip
  number-free detail paragraphs as filler). Includes a
  per-detail-paragraph audit test.
- **Abstract: state the inferential step.** New positive template.
  Policy claims in the abstract should unfold the logic from result to
  conclusion in "Because X, Y" form, not assert the conclusion alone.
  Side-by-side example contrasts "asserts the conclusion" (cut) with
  "unfolds the bridge" (use).
- **Robustness summary table.** New positive template. When
  alternative specifications produce raw coefficients on different
  scales (e.g., alternative weighting schemes whose underlying
  regressors have different units), add a *Per-SD (%)* column so all
  rows are comparable on a single interpretable scale. Footnote-mark
  off-scale rows pointing to the per-SD column as the apples-to-apples
  comparison. Document Kanzig-shock-style specs where per-SD doesn't
  apply with "--" in the column.
- **Policy claims acknowledge the policy's actual mechanism.** New
  positive template. When making a policy claim about a specific
  instrument (CBAM, EITC, Pigouvian tax, emissions cap), the claim
  must address the mechanism's actual design. Examples of mechanism
  details to address for each policy.
- **Promised robustness checks must be delivered.** New positive
  template. If §5 promises a robustness check, the appendix must
  deliver the table or the promise must come out of §5. Includes an
  audit-pattern grep for §5 promise verbs ("we verify," "we check,"
  "we control for").
- **Anti-pattern #13: parenthetical narrative labels in intro chain
  summaries.** Adds to the existing anti-pattern list.
  `(\textit{the leakage channel})`, `(\textit{the production channel})`
  etc. after each "First/Second/..." link. Not common in AER/QJE intros
  — sentence-level signposting already structures the chain. Reserve
  italicized parentheticals for inline variable/abbreviation
  definitions like `(\emph{count})`, `(\textbf{Exp})`, `(\textit{a priori})`.
- **Anti-pattern #14: asserting a policy conclusion without the
  inferential bridge.** Cross-refs the new "Abstract: state the
  inferential step" template.

### Motivation

Tested in a June 2026 revision sprint on a top-5-target carbon leakage
/ Chinese environmental enforcement paper for the LSE–Yale Firms, Trade,
and Development conference. The intro had six parenthetical narrative
labels (dropped); P3 carried all magnitudes and P6–7 carried none
(rebalanced); the abstract asserted a CBAM conclusion without the
inferential bridge (rewritten); the robustness summary had two rows on
different scales without a per-SD comparison column (added); and the
empirical-strategy section promised three robustness checks that the
appendix did not deliver (one was added, two are queued for a follow-up).
Each of these five fixes generalizes beyond the project setting.

---

## v1.8.1 — 2026-05-22

A **manuscript-writing convention** patch release. Adds one path-scoped rule that codifies a top-journal prose convention (declarative, not defensive; $\hat\beta$/SE in tables not prose; per-SD magnitudes; no result pre-announcement in section openers). Motivated by a real review cycle in which a defensive subsection opener was rewritten from 16 lines to 1, and the cleaner pattern was identified as belonging in the template, not just one project.

### Added

- **`.claude/rules/manuscript-writing-style.md`** — path-scoped rule loading on `.tex`, `.qmd`, and any path matching `manuscript/`, `paper/`, or `drafts/`. Core principle: **declarative, not defensive.** Forbids in body prose: result pre-announcement in section openers, defending dropped specifications, self-explaining the section architecture, hedge-stacking ("approximately roughly about"). Encourages: one-sentence subsection openers; interpreted magnitudes (per-SD %, elasticity, dollar effect) + table column reference in result paragraphs; inline $(\hat\beta, \text{SE})$ only when the coefficient itself is the argumentative object. References the AER and AEJ:Applied style guides for the in-prose-coefficient convention. Includes a "common targets for cleanup" checklist (subsection openers, redundant $(\hat\beta, \text{SE})$ parentheticals, restating-the-result "Interpretation" paragraphs, 3+ sentence footnotes, repeated "we find / we show / we document" phrases).

### Changed

- **`README.md`** path-scoped rules table now lists `manuscript-writing-style`.

---

## v1.8.0 — 2026-04-27

A **disciplinary breadth + audit-hardening + Apr 2026 incorporation** minor release. The cycle landed in two passes: (1) infrastructure-only audit-hardening (mechanical parity checks via `check-skill-integrity.py`, living pet-peeves catalogue, PreCompact blocking, Routines awareness) and (2) capability work (two new skills `/checkpoint` and `/preregister`, political-science breadth via three journal profiles + two paper types + a discipline-cards reference, and Apr 2026 documentation: auto mode promotion, protected-paths gate explainer, session-management commands, Computer Use sidebar, Monitor tool integration, `disable-model-invocation` discipline). No breaking changes; counts updated across all monitored surfaces.

### Added — new skills

- **`.claude/skills/checkpoint/`** — `/checkpoint` produces a structured state snapshot (active plan, recent decisions, file pointers with line numbers, open questions, next 1–3 actions) into `quality_reports/checkpoints/YYYY-MM-DD_<slug>.md`. Companion to (NOT replacement for) the narrative session-log workflow under `quality_reports/session_logs/`. Carries `disable-model-invocation: true` (writes to a persistent state file — must be user-intent). Pattern adapted from Hugo Sant'Anna's [clo-author v4.2.0](https://github.com/hugosantanna/clo-author) with permission; reimplemented in original prose against this template's narrative-session-log + plan-on-disk + auto-memory architecture. Attribution header on the SKILL.md.
- **`.claude/skills/preregister/`** + **`templates/preregistration-template.md`** — `/preregister` drafts a registry-ready preregistration document in OSF, AsPredicted, or AEA RCT Registry style. Extracts hypotheses, design, sampling plan, exclusions, and analysis plan from a research spec (`/interview-me` output) or free-form description. MUST/SHOULD/MAY clarity annotation per section. Pre-flight cross-checks: directional hypothesis, named estimator, ex-ante exclusion rules, sample-size stopping rule. Post-flight CoVe verification of any cited literature (re-uses `/verify-claims`). Output: `quality_reports/preregistrations/YYYY-MM-DD_<slug>.md` (gitignored). Refuses retrospective preregistration (description containing realised results). Greenfield — not ported.

### Added — political-science breadth

- **`.claude/references/journal-profiles.md`** +3 profiles: **APSR** (highest theoretical bar; THEORY-disposition pool weight 0.30; methods-referee tilts toward formal-theory comparative-static sharpness), **AJPS** (methods-emphasis; CREDIBILITY 0.30, replication policy enforced), **JOP** (clarity-of-contribution bar; SKEPTIC 0.25). Each profile is ~40–45 lines following the existing schema.
- **`.claude/agents/methods-referee.md`** +2 paper types: **`formal-theory`** (pure theory; weights tilt toward model originality and comparative-static sharpness; sanity checks include equilibrium existence, assumption tractability, robustness to assumption relaxation) and **`survey-experiment`** (vignette/conjoint/list/factorial; weights tilt toward design, sampling, and attrition+manipulation checks; sanity checks include balance, manipulation-check pass rate, attrition asymmetry, sampling-frame validity). The 4 prior paper types (reduced-form / structural / theory+empirics / descriptive) are unchanged — additions are purely additive.
- **`.claude/agents/domain-reviewer.md`** template-marker comment now ships **two** customization examples (econ + poli-sci) to illustrate that the 5-lens structure is field-agnostic. Lens content under each example reflects field-specific norms (poli-sci: ignorability, conjoint AMCE algebra, Hainmueller-Hopkins-Yamamoto for cross-reference, `cjoint`/`survey::svyglm` package defaults).
- **`.claude/references/discipline-cards.md`** — new reference. Two cards: `econ` and `poli-sci`. Each card: paper-type frequency table, dominant journals (cross-referenced to `journal-profiles.md`), preregistration norms (cross-referenced to `/preregister --style`), method conventions (significance-stars conventions, SE conventions, dominant code language). Read by `/research-ideation`, `/interview-me`, `/preregister`, and the `editor` agent when paper-type or discipline is given without a target journal. Forkers extend for psych / sociology / public-health / etc.

### Changed — research-side skill paper-type awareness

- **`.claude/skills/research-ideation/SKILL.md`** — new Step 3 tags each generated RQ with a likely paper type from the 6-type taxonomy. Output format adds a `**Paper type:**` field per RQ. `discipline-cards.md` informs the default distribution.
- **`.claude/skills/interview-me/SKILL.md`** — Phase 1 ("Big Picture") now optionally asks the researcher what kind of paper they envision (same 6-type taxonomy). Saved to spec frontmatter as `paper_type:` so downstream skills (`/preregister`, `/data-analysis`, `/review-paper --peer`) can read it.

### Added — Apr 2026 feature documentation

- **`TROUBLESHOOTING.md`** +2 sections under Permissions:
  - **Bypass mode still prompts on protected paths** — explains the protected-path list (`.git`, `.vscode`, `.idea`, `.husky`, `.claude` with carve-outs for `commands/agents/skills/worktrees`) and that **auto mode** is the only mode that routes protected paths through the classifier instead of prompting. Documents the auto-mode requirements (Max/Team/Enterprise/API + Sonnet 4.6 / Opus 4.6 / Opus 4.7 + Anthropic API). Includes two workarounds for users without auto-mode access: edit through Bash (`python3` heredoc) or move edits out of `.claude/`.
  - **`.vscode/settings.json` key typo** — `claudeCode.allowDangerouslySkipPermissions` is silently ignored; the canonical key is `allowDangerouslySkipPermissions` (no `claudeCode.` prefix). The typo leaves the protected-paths gate active even with broad CLI bypass. Reload window after fixing.
- **`.vscode/settings.json`** — fixed the typo: `allowDangerouslySkipPermissions: true` (was incorrectly prefixed). Takes effect on next VSCode window reload.

### Changed — `disable-model-invocation` audit

- **`.claude/skills/create-lecture/`**, **`.claude/skills/new-diagram/`**, **`.claude/skills/learn/`** — added `disable-model-invocation: true` to frontmatter. Rationale: each writes a load-bearing persistent file (a new lecture `.tex`, a new TikZ source, a new SKILL.md respectively) that should only be created on explicit user intent. `/deep-audit` also gains the flag in this release (its body writes audit reports + applies fixes). The new `/checkpoint` and `/preregister` skills carry the flag too.

### Added — Apr 2026 doc additions (guide + onboarding)

- **`guide/workflow-guide.qmd`** — new `### Session Management` subsection under "Settings — Permissions and Hooks": `/btw` for side questions outside conversation history, `/rewind` and `Esc+Esc` for checkpoint navigation, `/clear` and `/compact <instruction>` for context resets, `Ctrl+G` for in-editor plan editing, `claude --continue` / `--resume` / `/rename` for cross-session continuity, plus `/checkpoint <slug>` (this template). Three composition patterns documented.
- **`guide/workflow-guide.qmd`** — added `auto` mode row to the permission-modes table; documented bypass mode's protected-path gate inline (`.git`, `.vscode`, `.idea`, `.husky`, `.claude` minus `commands/agents/skills/worktrees` carve-outs).
- **`guide/workflow-guide.qmd`** — Computer Use callout in the Adversarial Pattern section (Apr 2026 Week 14, research preview, optional). Frames Computer Use as the *visual loop* extension when text-level `/qa-quarto` and `/visual-audit` aren't enough.
- **`guide/workflow-guide.qmd`** — Monitor-tool subsection in "Cost-Conscious Parallelism" (Apr 2026 Week 15). Replaces polling-loop anti-pattern for long-running R fits, replication batch reruns, etc.
- **`guide/workflow-guide.qmd`** — new "Anthropic-Shipped Apr 2026 Utilities" section in the ecosystem area: `/team-onboarding`, `/autofix-pr`, `/powerup`, Ultraplan, `/less-permission-prompts`. Framed as off-ramps when this template's scope doesn't fit.
- **`README.md`** — Quick Start callout pointing forkers heavily diverging from academic content at Anthropic's `/init` to re-derive `CLAUDE.md`.
- **`templates/skill-template.md`** — new "When to set `disable-model-invocation: true`" subsection codifying the rule (write-load-bearing-persistent-file → set the flag) and the new "CLAUDE.md `@import` syntax" subsection documenting the Anthropic Apr 2026 import feature, with explicit guidance that this template's CLAUDE.md deliberately does NOT use it (under-150-line CLAUDE.md is better monolithic).
- **`.claude/skills/data-analysis/SKILL.md`**, **`.claude/skills/audit-reproducibility/SKILL.md`** — new "Long-running fits / batch reruns: use the Monitor tool" subsections. Document the background-launch + Monitor pattern for jobs that take more than a couple of minutes.

### Surface-sync

- Skills 28 → 30 (`/checkpoint`, `/preregister`). Agents unchanged at 14. Rules unchanged at 24. Hooks unchanged at 6. Counts updated across all 6 monitored surfaces (README, CLAUDE.md, guide `.qmd` + rendered `.html`, `docs/index.html`, `docs/workflow-guide.html`, `templates/skill-template.md`). `scripts/check-surface-sync.sh` clean; `scripts/check-skill-integrity.py` clean. Guide re-rendered with Quarto 1.8.x; `docs/workflow-guide.html` synced.

### Attribution

`/checkpoint` shape: adapted from Hugo Sant'Anna's [clo-author v4.2.0](https://github.com/hugosantanna/clo-author) with permission. Attribution header on `.claude/skills/checkpoint/SKILL.md`.

---

### Pre-v1.8.0 infrastructure (folded into this release)

Two themes that landed in the working tree before the v1.8.0 capability work: audit-hardening (mechanical parity checks + living pet-peeves catalogue that close classes of bug the agent-based `/deep-audit` was missing) and selective incorporation of Claude Code Apr 2026 features (Routines for AFK scheduling, PreCompact blocking, `/less-permission-prompts` as a sibling to our `/permission-check`).

### Added — mechanical integrity checks

- **`scripts/check-skill-integrity.py`** — deterministic parity checks that run in under a second. Four checks: (1) frontmatter `allowed-tools` ↔ body tool-invocation parity — catches the v1.7.0 PR #92 class of bug where 4 skills promised `Task` in their body but had no `Task` permission; (2) `argument-hint` ↔ body flag parity — documented flags advertised in the one-line hint; (3) internal markdown anchor resolution — no broken `[text](path#anchor)` links (the `#category-11-numerical-discipline` miss on PR #87); (4) rule `paths:` ↔ skill implementation parity — rule claims skill follows protocol, so skill body must reference the protocol's keywords (the `/interview-me` miss on PR #92).
- **`scripts/check-surface-sync.sh`** now runs both `check-surface-sync.py` (count assertions) and `check-skill-integrity.py` (parity). Either gate failing blocks `/commit` Step 0b.
- **`.claude/skills/slide-excellence/SKILL.md`** `argument-hint` updated to advertise `--fast`, `--skip-substance`, `--acknowledge-template-domain-reviewer` — the first real P2 the new check caught on baseline.

### Added — living pet-peeves catalogue

- **`.claude/references/audit-pet-peeves.md`** — 12-entry seed document cataloguing classes of bug review bots (Copilot / Codex) have caught on recent PRs that `/deep-audit` missed. Each entry: example + how to catch + why deep-audit missed it + when to apply. Grows with each PR — the meta-fix for the "audit agents keep missing this one thing" pattern.
- **`.claude/skills/deep-audit/SKILL.md`** now has a Phase 0 that runs the mechanical checks first (cheapest, most precise), and every agent in Phase 1 is instructed to read the pet-peeves file before reporting clean.

### Changed — documentation

- MEMORY.md `[LEARN:audit]` entry on the mechanical-vs-agent tradeoff (catch classes of bug where precision matters with deterministic checks; use agents for judgment calls).
- TROUBLESHOOTING.md section for `check-skill-integrity` failures — what each P0/P1/P2 means, how to resolve or tune.

### Fixed

- Self-referential false positive in the pet-peeves doc: example `[text](path#anchor)` markdown inside prose was matched by the anchor-resolution check. Script now strips inline code spans and fenced code blocks before scanning, so illustrative examples don't trigger the check.

### Added — Apr 2026 Claude Code incorporation

- **PreCompact hook can now block compaction** (`.claude/hooks/pre-compact.py`). Opt-in via env var `CLAUDE_PRECOMPACT_BLOCK_ON_DRAFT=1`: blocks once per DRAFT plan so the user can approve before losing mid-plan context. Uses the modern Claude Code block protocol (exit 0 + JSON `{"decision":"block","reason":"..."}` on stdout). Fires at most once per plan path — no lock-out loops. Default off; existing users get no change.
- **MEMORY.md `[LEARN:scheduling]` + `[LEARN:hooks]`** capturing two lessons from Apr 2026: (a) `CronCreate` is session-only in practice — use Claude Code Routines (launched Apr 14) for any autonomous work that must survive session termination; (b) PreCompact hooks can now block, which is the right primitive for "don't lose this context."
- **`.claude/references/audit-pet-peeves.md` entry 17** — don't use `CronCreate` for long-delay autonomous work; Routines is the right primitive.
- **TROUBLESHOOTING.md scheduling section** — explains `CronCreate` vs Routines tradeoff (short-delay in-session vs AFK work on web infra) and documents the PreCompact blocking guard. Plus a pointer to the built-in `/less-permission-prompts` skill as a sibling to our `/permission-check` (diagnose with `/permission-check`, remediate with `/less-permission-prompts`).

No stale model references audited — all 14 agents already use `model: inherit`, so they auto-adapt to Opus 4.7 / Sonnet 4.6 / Haiku 4.5 without changes.

---

## v1.7.0 — 2026-04-16

A **discipline-patterns** minor release. Additive infrastructure for anti-drift (summary-parity) and anti-hallucination (Post-Flight Verification / Chain-of-Verification). Full details below; no breaking changes for forks.

### Added — Post-Flight Verification (Chain-of-Verification)

Mirror of v1.6.0's Pre-Flight Reports, at the output side. Where Pre-Flight proves inputs were read before work, Post-Flight proves factual claims hold after drafting — before the skill returns to the user. Adapted from **Dhuliawala et al. 2023, "Chain-of-Verification Reduces Hallucination in Large Language Models" ([arXiv:2309.11495](https://arxiv.org/abs/2309.11495))**. The core CoVe idea — answer verification questions in a context that does NOT contain the original draft — is architecturally enforced here via `context: fork` on the verifier agent.

- **`.claude/rules/post-flight-verification.md`** — new path-scoped rule. Defines the 4-step CoVe protocol (draft → extract claims → generate verification questions → answer independently in fresh context → reconcile). Scoped to skills that generate factual claims. Fail-closed: if the verifier errors or times out, the draft is surfaced as provisional rather than shipped silently. Opt-out via `--no-verify`.
- **`.claude/agents/claim-verifier.md`** — new forked agent. Never sees the draft (enforced by `context: fork` at the Task boundary). Receives only: claims, verification questions, source-material pointers. Uses `Read`, `Grep`, `Glob`, `WebFetch`, `WebSearch`, `Bash`. Returns a structured verification report (PASS / PARTIAL / FAIL per claim, with evidence quotes + source locations).
- **`.claude/skills/verify-claims/`** — new user-facing skill. Runs Post-Flight on any draft the user hands to it (a `.md`, `.qmd`, `.tex`, `.txt` file). Accepts `--source <path-or-url>` to point at source material. Callable directly by users or spawned by other skills via `Task`.
- **Four skill integrations** — `/lit-review`, `/research-ideation`, `/respond-to-referees`, `/review-paper` (novelty probe in `--peer` mode). Each now runs Post-Flight internally before returning. Skip conditions documented per skill (e.g., `--no-verify`, user pre-verifies).

Rationale: `/lit-review` citations from WebSearch were hallucination-prone (already flagged in SKILL.md); `/research-ideation` negative-literature claims (e.g., "no prior work studies X") and dataset-structure claims are classic hallucination vectors; `/respond-to-referees` "we added X on page Y" claims can be wrong or out-of-date after revision; `/review-paper --peer` editor novelty probe depends on WebSearch.

### Added — anti–whack-a-mole rule (from earlier in v1.7.0 cycle)

- **`.claude/rules/summary-parity.md`** — path-scoped rule preventing surgical word-level fixes on summary paragraphs from introducing new drift elsewhere in the same paragraph. Triggers on CHANGELOG ledes, README taglines, PR `## Summary` blocks, skill/rule/agent frontmatter `description` fields, guide section abstracts, MEMORY.md `[LEARN]` headlines. Core heuristic: two review-bot flags on the same paragraph = rewrite structurally (abstract up), don't patch. Motivated by 3 consecutive Copilot findings on the v1.6.1 CHANGELOG opening (PRs #88–#90), each surgical fix introducing a new drift elsewhere.

### Added — audit learnings

- **`MEMORY.md`** new `[LEARN:audit]` entries capturing the whack-a-mole anti-pattern (summary-parity) and the CoVe vs critic-fixer vs cross-artifact distinction (three complementary verification mechanisms at three different architectural levels). Future sessions inherit both lessons on fresh context.

### Added — guide coverage

- `/verify-claims` and the new `claim-verifier` agent added to the guide's "All Skills" / "All Agents" tables. `post-flight-verification.md` and `summary-parity.md` added to "All Rules." Pre-existing gap in the rules table closed as well: `content-invariants.md` and `cross-artifact-review.md` were on disk but missing from the table; now listed. Path-scoped rule callout updated (16 → 20 path-scoped rules total).

### Changed — counts

- Skills 27 → 28 (`/verify-claims`). Agents 13 → 14 (`claim-verifier`). Rules 22 → 24 (`summary-parity.md` + `post-flight-verification.md`). Hooks unchanged at 6. Surface-sync gate propagates the new counts across all 6 monitored surfaces (README, CLAUDE.md, guide `.qmd` + `.html`, `docs/index.html`, `docs/workflow-guide.html`, `templates/skill-template.md`, `/commit` SKILL internal example).

### Changed — drift-proofing the v1.6.1 CHANGELOG lede (applied the new summary-parity rule)

- Rewrote the v1.6.1 opening paragraph abstraction-first ("No breaking changes. No new directories were added to `.claude/`; existing infrastructure was revised …"). First test of the new summary-parity rule on an existing entry. GitHub release notes for v1.6.1 synced to match.

### Governance note

v1.7.0 establishes the **discipline-pattern trilogy**:

1. **v1.6.0 Pre-Flight** (input discipline) — inputs were read before work.
2. **v1.6.1 summary-parity** (framing discipline) — summaries don't drift from bodies.
3. **v1.7.0 Post-Flight** (output discipline) — factual claims hold before work ships.

All three share a shape: **fail-closed, structured output block, honest fallbacks**. All three address classes of bugs a human reviewer would catch but the agent loop should catch earlier.

---

## v1.6.1 — 2026-04-16

A **framing honesty + hook friction** patch release. No breaking changes. No new directories were added to `.claude/`; existing infrastructure was revised to address two classes of issue surfaced by a multi-round audit:

1. **Claim-vs-reality drift:** v1.6.0 docs and rules described the "orchestrator" as if it were a repo-wide daemon that activates automatically after plan approval. In reality, the 6-step loop (IMPLEMENT → VERIFY → REVIEW → FIX → RE-VERIFY → SCORE) is a **pattern** implemented by specific skills (`/commit`, `/qa-quarto`, `/review-paper --adversarial`, `/slide-excellence`, `/create-lecture`, `/data-analysis`, `/review-paper --peer`). Plan approval does NOT trigger an auto-loop. Similarly, quality thresholds are **advisory inside `/commit`**, not enforced by a repo-wide git pre-commit hook.

2. **Hook blocking fatigue:** the Stop hook `log-reminder.py` used `{"decision": "block"}` to force session-log creation. Effective for discipline, disruptive for autonomous flows. Now exits 0 with stderr-only advisories.

### Changed — honest framing

- **`.claude/rules/orchestrator-protocol.md`** rewritten: opens with "This rule describes the contract that skills implement. The 6-step loop is a *pattern*, not a runtime." Adds a skill-by-skill implementation table (which skill covers which steps; notes where auto-fixing happens and where it doesn't). "Just Do It" mode clarified to explicitly NOT authorize commits on its own — `/commit` invocation is still required.
- **`.claude/rules/quality-gates.md`** renamed to **"Quality Review & Scoring Rubrics"** in practice (header kept for URL stability). Opens with an advisory-framing callout: enforcement is by the `/commit` skill only (halt + ask to override); a direct `git commit` bypasses the review.
- **`.claude/rules/cross-artifact-review.md`** clarifies that detection is **pattern-based** (`\input{scripts/...}` / `%% source:` / filename matches). If the manuscript has none of those signals, nothing auto-invokes — and `--no-cross-artifact` is a no-op. Removed a reference to an unimplemented `--with-scripts` forcing flag.
- **`.claude/rules/beamer-quarto-sync.md`** adds a **precedence-with-SSOT** section for the case where the Quarto file has manual post-translation edits: Beamer remains authoritative; presentation-only divergence (HTML-specific callouts) is allowed; structural drift is a bug.
- **`guide/workflow-guide.qmd`** 4 sections rewritten: "The Orchestrator" → "A Pattern, Not a Daemon"; "Quality Scoring" now advisory; the "Skills vs Orchestrator" callout acknowledges both paths invoke the pattern inside a skill. Removed 5 occurrences of "automatic orchestrator" overselling across the document.
- **`README.md`** contractor-mode framing updated: "runs the orchestrator pattern internally" instead of "runs autonomously." Quality Review section adds an explicit framing-honesty note: "advisory at the harness level — if you bypass the skill, you bypass the review."
- **`docs/index.html`** landing-page bullets reworded: "Contractor mode via skills" (not "Contractor mode orchestrator"), quality-scoring bullet describes halt-and-override inside `/commit`.
- **`CLAUDE.md`** Quality Thresholds table title now reads "(advisory)" with a one-line footnote clarifying `/commit`-only enforcement.

### Changed — hook friction relief

- **`.claude/hooks/log-reminder.py`** no longer blocks. Both block-return branches (no-log-exists and 15-response-counter) converted to stderr-only advisories. `THRESHOLD` raised from 15 → 50. Docstring updated to match the new semantics. The old blocking behavior was effective but disrupted `/loop` and batched-fix flows — stderr reminders preserve the nudge without halting execution.
- **`.claude/hooks/verify-reminder.py`** throttle bumped from 60s → 300s (5 minutes). Same reminder, less noise during iterative `.tex` / `.qmd` / `.R` edits.

### Added — orphan wiring + skill disambiguation

- **`templates/decision-record.md`** (v1.6.0 addition) now wired into `/interview-me`: when the researcher explicitly chooses among alternatives during an interview (e.g. DiD vs IV vs RDD, admin vs survey data), the skill produces an ADR alongside the research spec. Skipped when there's a single uncontested path.
- **Decision trees** added to the top of `/review-paper`, `/seven-pass-review`, and `/slide-excellence` SKILL.md files. Users can now pick the right skill at a glance: review-paper = most drafts; seven-pass = submission-ready / R&R; slide-excellence = slides; plus pointers to single-lens skills.
- **`.claude/agents/domain-reviewer.md`** and **`domain-referee.md`** both prefixed with a scope-disambiguation block. `domain-reviewer` is the general (not disposition-primed) substance reviewer used by `/slide-excellence` and `/seven-pass-review`. `domain-referee` is the disposition-primed variant used by `/review-paper --peer`. Same domain expertise, different calibration.
- **`.claude/rules/r-code-conventions.md`** adds **Section 8: Numerical Discipline** with the project epsilon (`eps <- 1e-12`) for CDF clamping plus 7 headline rules, cross-referenced to `r-reviewer` Category 11. The checklist gains a "numerical discipline" row.

### Added — documentation

- **`TROUBLESHOOTING.md`** +5 sections for v1.5/v1.6 features:
  - **Permissions / bypass / statusline** (6-layer stack diagnosis, why `/permission-check` gates host-global reads, statusline parse-failure recovery)
  - **Peer-review pipeline** (missing journal profile, cloned referee reports, R&R continuation chain breaks)
  - **Surface-sync gate** (count drift resolution, adding a new skill breaks the gate by design)
  - **Pre-Flight Reports** (fail-closed semantics, first-lecture fallback in `/create-lecture`)
  - **Decision records** (where to save, gitignore behavior)
- **`README.md`** Quick Start adds two callouts: Python/R/markdown-only users can skip XeLaTeX/Quarto; `MEMORY.md` vs `personal-memory.md` distinction introduced early (was previously session-2 discovery only).
- **`MEMORY.md`** +6 new `[LEARN]` entries: framing (orchestrator is pattern, quality gates advisory, cross-artifact pattern-based), dogfooding (empty `quality_reports/` dirs is a red flag — Stop hook caught it mid-session), audit (claim-vs-reality is the highest-ROI lens for a governance-heavy template repo). Template inventory refreshed from 6 → 10 files + `tikz-snippets/`.
- **`guide/workflow-guide.qmd`** "All Skills" table adds `/seven-pass-review` and `/permission-check` (were missing).

### Fixed — review-driven polish (from Copilot + Codex on PR #87)

- **Broken anchor:** `r-code-conventions.md` linked to `#category-11-numerical-discipline`, but the actual heading in `r-reviewer.md` is `### 11. NUMERICAL DISCIPLINE`. Dropped the anchor, references by name.
- **Unimplemented flag:** `beamer-quarto-sync.md` advised running `/translate-to-quarto --diff [file]`, but the skill has no `--diff` option. Replaced with "regenerate into a scratch path, diff manually."
- **Contradictory scope:** `domain-reviewer.md` claimed "slides only" while also stating "used by `/seven-pass-review`" (a manuscript skill). Reframed as general reviewer for both artifacts; `domain-referee.md` is the disposition-primed manuscript variant.
- **Stale docstring:** `log-reminder.py` docstring described blocking behavior after the code had been converted to advisory. Updated.
- **Stale docstring:** `verify-reminder.py` said "within 60s" after throttle was bumped to 5 min. Updated.
- **Daemon phrasing in TROUBLESHOOTING:** `sessionInfo.txt` fix referenced "the orchestrator" as if it were a daemon. Points at `00_run_all.R` via `/data-analysis` or the user's pipeline runner instead.
- **`/context-status` regression averted:** intermediate commit had unwired `context-monitor.py` from `PostToolUse`, but `/context-status` reads the cache that hook writes. Codex flagged the dependency; the hook was re-wired before merge.
- **CHANGELOG upgrade example:** pin example updated from `v1.3.0` (2026-04-13) to `v1.6.0` (2026-04-15) to reflect current state.
- **Guide frontmatter date:** stale `2026-03-20` → `2026-04-15` (v1.6.0 release date).
- **v1.6.0 Pre-Flight claim:** CHANGELOG line about "fail-closed if inputs can't be read" now acknowledges `/create-lecture`'s first-lecture fallback (documented exception, not a contradiction).

### Governance note

v1.6.1 establishes the **"claim-vs-reality" audit lens** as a first-class review category going forward. When a template repo oversells itself, the gap is the first thing forkers notice when reality bites. The [LEARN:audit] entry in MEMORY.md captures this: for any governance-heavy feature, the audit question "is the claim mechanically enforced, or is it prose?" catches more real bugs than skill/doc consistency checks.

The Stop hook's conversion from blocking to advisory is a **philosophical tradeoff**: discipline vs. autonomy. v1.6.0 chose discipline (block until the user complies); v1.6.1 chooses autonomy (nudge but don't halt) because the blocking version disrupted `/loop`, batched audits, and autonomous-ship flows. The nudge survives in stderr, the discipline now depends on the user's own habit. If a future release finds this has quietly caused session-log neglect, the blocking form can be restored behind an opt-in setting.

### Verification

Pre-merge deep audit launched 4 parallel agents (guide content, hook code, skills/rules consistency, cross-doc). 1 genuine finding (stale docstring), 1 false alarm (log-reminder fail-open is correct). Fixed on branch before merge.

Surface-sync gate: 27 skills / 13 agents / 22 rules / 6 hooks matched across 6 surfaces. `quality_score.py` on `guide/workflow-guide.qmd`: 100/100.

---

## v1.6.0 — 2026-04-15

A **discipline-layer release**: the template's infrastructure now actively catches the class of bugs that produced reviewer-driven fix PRs in v1.5.x. Also adds two observability/diagnosis tools (statusline, `/permission-check`), doubles the referee pet-peeve pools, and ports three quality patterns from clo-author (Pre-Flight Reports, Content Invariants, Numerical Discipline). No breaking changes.

### Added — observability + diagnostics

- **`.claude/scripts/statusline.sh`** — always-visible mode badge (`[BYPASS] / [PLAN] / [AUTO-EDIT] / [PROMPT]`) + model + git branch. Renders on every turn. Wired via `.claude/settings.json` `statusLine`. Parses session JSON in a single `python3` invocation (per-turn perf).
- **`.claude/skills/permission-check/`** — new `/permission-check` skill. Read-only diagnostic: reads repo-local settings layers auto, requires explicit user confirmation before reading host-global (`~/.claude/settings.json`, VSCode user settings). Redacts unrelated keys. Surfaces drift across the 6-tier permission stack (VSCode user / workspace / CLI user / project / project-local / in-session runtime).
- **Six-Layer Permission Stack + Plan→Bypass Handoff** in the guide. Troubleshooting checklist for "prompts fire despite bypass." Explicit `callout-warning` that plan approval is NOT an enforcement boundary — exiting plan mode returns to `defaultMode` with full bypass authority.

### Added — surface-sync gate

- **`scripts/check-surface-sync.py` + `scripts/check-surface-sync.sh`** — cross-document count consistency gate. Counts `.claude/{skills,agents,rules,hooks}` on disk, scans 6 surfaces (README, CLAUDE.md, guide .qmd + .html, docs/index.html, skill-template) for count assertions using compound regex patterns (avoids false positives on unrelated phrases like "3 parallel agents" or attribution lines). Fails closed on drift — no `"commit anyway"` override. Wired into `/commit` as Step 0b.
- Addresses the systemic drift pattern that produced PRs #70, #76, #78 in v1.5.x (adding a skill updated `.claude/` but left stale counts in prose).

### Added — referee quality polish

- **Expanded editor pet-peeve pools:** 25 → 29 critical peeves (added: notation drift, seed-dependent results, covariate balance absent, overlap/common-support missing); 20 → 25 constructive peeves (added: "what this paper does not show" paragraph, raw-data figures, alternative specs, notation tables, careful attribution). Now exceeds clo-author v3.1 baseline (27/24).
- **`quality_reports/decisions/` + `templates/decision-record.md`** — ADR-style decision records. Template with Status / Problem / Options considered / Decision + rationale / Consequences / Rejected alternatives. Gitignored like plans/specs.

### Added — discipline patterns (ported from clo-author, adapted)

- **Pre-Flight Reports** in `/data-analysis`, `/create-lecture`, `/review-paper --peer`. Each skill now requires a structured output block proving inputs were read before doing work (dataset fields, project conventions, notation registry checks, journal profile, cross-artifact status). Fail-closed if inputs can't be read, **with a documented first-lecture fallback** in `/create-lecture` (proposes a minimal knowledge base when the template is still empty, to avoid deadlocking fresh forks).
- **`.claude/rules/content-invariants.md`** — new rule, path-scoped to `Slides/**/*.tex`, `Quarto/**/*.qmd`, `Quarto/**/*.scss`, `Preambles/header.tex`, `scripts/R/**/*.R`. Defines **INV-1 through INV-12**: palette sync, Beamer↔Quarto notation parity, Quarto CSS override contract, TikZ-as-SVG, single bibliography, no `\pause`, max 2 boxes per slide, motivation-before-formalism, `set.seed` once, relative paths only, transparent-bg figures, project theme on all plots. Critics can now cite invariants by number.
- **`r-reviewer` agent — category 11 "Numerical Discipline":** no float `==`, CDF clamping to open interval with named epsilon (not `[0,1]` — exact 0/1 to `qnorm` yields ±Inf), integer literals for counts (`1L`), pre-allocated vectors, deterministic bootstrap seeding, explicit `na.rm`, no `T`/`F` shorthands.

### Changed — skill trigger descriptions

- **17 `.claude/skills/*/SKILL.md` frontmatter rewrites** for reliable auto-invocation. Verb+object + "Use when: …" trigger phrases + disambiguation from sibling skills (e.g., `/interview-me` explicitly says NOT for lit review, pairs with `/research-ideation`). Follows the `deep-audit` gold-standard pattern. Cold-prompt auto-invocation is now reliable for `/commit`, `/deploy`, `/proofread`, `/data-analysis`, and siblings.
- **`commit` skill triggers tightened** after Codex flagged vague end-of-task phrases as risky: now only explicit commit intent ("commit", "ship it", "push this", "open a PR", "merge to main", "let's commit this"). Removed "wrap up these changes" and end-of-task-signal trigger.
- **Guide: "Writing Effective Trigger Descriptions"** expanded with the 3-part pattern (verb+object → "Use when:" phrases → disambiguation), A/B rewrite example, and a pre-ship checklist.

### Changed — documentation

- **Counts:** skills 26 → 27 (added `/permission-check`), rules 21 → 22 (added `content-invariants`). Agents and hooks unchanged. Synced across all 6 surfaces via the new sync gate.
- **Guide re-rendered** with the new sections (statusline, permission stack, Plan→Bypass handoff, expanded trigger-description guidance). `docs/workflow-guide.html` synced.

### Fixed — systemic quality during development

This release absorbed an unusual volume of reviewer-driven fixes from Codex and Copilot. Representative samples:

- **Count drift:** a single `replace_all` on `"26 skills"` missed `"26 skills, and 21 rules"` (extra "and"), missed `"26 slash commands"`, missed `"template's 26"`. The deep-audit skill now documents the phrasing-variant trap; the surface-sync gate prevents the class of bug.
- **Stop-hook block protocol:** some audit guidance implied non-zero exit codes are required to block. Actually, modern Claude Code accepts BOTH `exit 2 + stderr reason` (legacy) AND `exit 0 + JSON {"decision":"block","reason":"..."}` on stdout (modern — what `log-reminder.py` uses). Deep-audit skill now documents both protocols explicitly so future audit agents don't re-flag `log-reminder.py`.
- **Statusline parse-failure fallback:** parse error emitted `cwd="."` which wasn't empty, bypassing the `pwd` fallback. Fixed to emit empty third line and tightened the bash guard to treat `"."` as invalid.
- **`notify.sh` robustness:** best-effort notification now fails open on missing `jq` AND on malformed JSON input (defaults before jq attempt, silent stderr on parse).
- **Plan→Bypass framing:** initial guide text said "combines safety and prompt-free execution." Codex correctly flagged this as overselling — plan approval doesn't bind later execution to the approved plan. Reworded as "review-before-execute convenience" with a callout warning.
- **`/permission-check` privacy boundary:** first draft read `~/.claude/` and VSCode user settings unconditionally on ambiguous prompts like "why am I getting prompts?". In a shared/corporate environment this could leak host-global config. Restructured into Phase A (repo-local, auto) + Phase B (host-global, explicit user confirmation + key redaction).
- **CDF clamping math bug** in the new Numerical Discipline checklist: initial draft said `pmin(1, pmax(0, p))` but exact 0/1 to `qnorm` yields ±Inf. Fixed to open interval with named `eps`.
- **Content-invariants path globs:** initial frontmatter used bare directories; other rule files use quoted glob patterns. Aligned.
- **Seed format conflict** in `/data-analysis`: Phase 1 required YYYYMMDD (per `r-code-conventions.md`) but the template example still showed `set.seed(42)`. Made self-consistent.

### Attribution

The discipline patterns in this release (Pre-Flight Reports, Content Invariants, Numerical Discipline rules) are **ported from [Hugo Sant'Anna's clo-author](https://github.com/hugosantanna/clo-author) with adaptation to our lecture-shaped surface**. Hugo's v4.1.x has moved to a 10-verb skill consolidation + full paper-type branching we deliberately didn't port (doesn't fit our primary artifact). Invariants have lecture-specific codes (INV-1..INV-12) rather than clo-author's paper-centric ones.

### Governance note

v1.6.0 establishes the "discipline layer" as a first-class template concern. The surface-sync gate makes count drift a pre-commit error, not a reviewer catch. The statusline + `/permission-check` turn permission debugging from detective work into a 2-second glance. The Pre-Flight Report pattern makes "agent hallucinated your variable names" a category of failure that can't happen silently.

---

## v1.5.0 — 2026-04-14

### Added — Simulated peer review

A new `--peer [journal]` mode for `/review-paper` that runs a full editorial pipeline: **editor desk review → referee selection (2 different dispositions from a 6-way taxonomy) → 2 blind referees in parallel → editorial synthesis (FATAL / ADDRESSABLE / TASTE)**. Calibrated per journal.

- **`.claude/agents/editor.md`** — journal editor persona. Desk-reviews (with optional WebSearch novelty probe, ON by default — opt out with `--no-novelty-check`), selects two referees with *deliberately different* dispositions from the 6-way taxonomy (STRUCTURAL / CREDIBILITY / MEASUREMENT / POLICY / THEORY / SKEPTIC), assigns each referee 1 critical + 1 constructive pet peeve, then synthesizes their reports into an editorial decision with classification and "MUST / SHOULD / MAY push back" response-planning block.
- **`.claude/agents/domain-referee.md`** — substance referee. 5 weighted dimensions (contribution 30 / lit positioning 25 / substance 20 / external validity 15 / journal fit 10). Disposition-primed. Requires "What would change my mind: [specific ask]" on every MAJOR concern — a discipline that separates adversarial review from productive review.
- **`.claude/agents/methods-referee.md`** — methodology referee with **paper-type branching**: reduced-form / structural / theory+empirics / descriptive. Each type has its own dimension weights and mandatory pre-scoring sanity checks (sign / magnitude / parameter plausibility / construct validity / etc.). Same "What would change my mind" requirement.
- **`.claude/references/journal-profiles.md`** — NEW directory. Ships with **5 econ journals** (AER / QJE / JPE / ECMA / ReStud), each with Focus / Bar / Domain-referee adjustments / Methods-referee adjustments / Typical concerns / Referee-pool weights / optional Table-format override. Plus a "Field adaptation" section with detailed instructions for non-econ users.
- **`templates/journal-profile-template.md`** — skeleton for adding your own journal/field. Includes a disposition reference and field-specific paper-type guidance (e.g., biology: observational/experimental/computational/review; political science: case-study/comparative/formal-model/survey).

### Changed

- **`/review-paper`** — now supports three modes: default (single-pass), `--adversarial` (critic-fixer loop from v1.4.0), and the new `--peer <journal>` pipeline. Sub-flags: `--peer --r2` / `--peer --r3` (R&R continuation — reloads prior reports, classifies concerns Resolved / Partial / Not addressed, max 3 rounds), `--peer --stress` (hostile editor — forces SKEPTIC dispositions, doubles critical peeves), `--no-novelty-check` (skip WebSearch probes). Output directory: `quality_reports/peer_review_[paper]/` with `desk_review.md`, `referee_domain.md`, `referee_methods.md`, `editorial_decision.md`.
- **`.claude/rules/cross-artifact-review.md`** — adds `--peer` ordering clause: in `--peer` mode, cross-artifact review runs **before** the editor's desk review so reproducibility FAIL can be cited as desk-reject grounds. In default and `--adversarial` modes, cross-artifact still runs at Step 6b (after the paper review).
- **Counts:** **10 → 13 agents** (editor, domain-referee, methods-referee). Skills (26) and rules (21) unchanged. Synced across README, docs/index.html, guide, templates, CLAUDE.md.

### Attribution

The simulated-peer-review pipeline is **adapted from [Hugo Sant'Anna's clo-author](https://github.com/hugosantanna/clo-author) with his explicit permission**. Hugo's work contributed:
- The pipeline shape (editor desk → 2 referees → editorial synthesis).
- The 6-way disposition taxonomy (STRUCTURAL / CREDIBILITY / MEASUREMENT / POLICY / THEORY / SKEPTIC).
- The journal-calibration schema (Focus / Bar / Typical concerns / Referee-pool weights / Table-format overrides).
- The paper-type branching in the methods referee (reduced-form / structural / theory+empirics / descriptive) with per-type dimension weights and sanity checks.
- The "What would change my mind" requirement on every major concern.
- The R&R continuation pattern (reload prior round, classify Resolved / Partial / Not addressed).

We reimplemented all files rather than copying verbatim (clo-author has no LICENSE file at time of adaptation; our version is original text under MIT). All new files carry an attribution header pointing back to clo-author.

Thanks to Hugo for both the inspiration and the permission. The fork is doing great work on the authoring side of the pipeline — complementary to our template's authoring + review orientation.

### Governance note

With v1.5.0, the template's review story is now the strongest single feature: single-pass review (fast feedback), adversarial loop (iterative revision), seven-pass parallel review (broad coverage), simulated peer review (journal-calibrated editorial pipeline), R&R continuation (R&R rehearsal), stress mode (hostile editor). Four complementary review modes, one skill.

---

## v1.4.0 — 2026-04-14

### Added — review-skills hardening

- **`.claude/skills/audit-reproducibility/`** — enforces `replication-protocol.md` by cross-checking numeric claims in a manuscript (`ATT = -1.632 (0.584)`, `N = 2,847`, p-values, percentages) against the actual R / Stata / Python outputs. Tolerance-graded PASS/FAIL per claim. Usable as a `/commit` gate (exit 1 on FAIL). Addresses the "I updated the analysis but forgot to update Table 2" bug.
- **`.claude/skills/seven-pass-review/`** — mechanizes Pattern 15. Seven forked subagents, one per lens (abstract, intro, methods, results, robustness, prose, citations), run in parallel, then a synthesizer produces a prioritized revision checklist with cross-lens contradictions surfaced.
- **`.claude/rules/cross-artifact-review.md`** — paper ↔ code dependency-graph protocol. When `/review-paper` runs, auto-invokes `/review-r` on referenced scripts and `/audit-reproducibility` on the pair. Surfaces critical cross-artifact findings (code bug invalidates paper claim) at the top of the review report. Opt-out: `--no-cross-artifact`.

### Changed

- **`/review-paper`** — new `--adversarial` mode runs the critic-fixer loop from `/qa-quarto` (up to 5 rounds). Single-pass default unchanged. Now also auto-invokes cross-artifact review (Step 6b).
- **`/slide-excellence`** — conditional dispatch: only spawns subagents that can produce useful output (`tikz-reviewer` only on TikZ-bearing files, content-parity only when both `.tex` and `.qmd` counterparts exist, R reviewer only when R chunks are present). Pre-flight check refuses to run `domain-reviewer` if the agent is still the shipped template. New flags: `--skip-substance`, `--acknowledge-template-domain-reviewer`, `--fast`. Cuts token cost ~50% on typical `.qmd`-only files.
- **`/validate-bib`** — new `--semantic` mode: citation-drift detection (duplicate `.bib` entries for the same paper), crossref DOI verification with caching and rate limiting, within-file citation-style consistency, optional `--cite-claim` abstract surfacing. Structural mode unchanged. `--skip-doi` for offline.
- **`.claude/agents/domain-reviewer.md`** — adds `AUTO-DETECT-TEMPLATE-MARKER` so `/slide-excellence` can detect un-customized templates and warn before running generic substance review.
- **Counts:** 24 → 26 skills, 20 → 21 rules. Synced across README, `docs/index.html`, guide, templates, and `docs/workflow-guide.html`.

### Fixed — Codex round-2 regressions

- **Trust-boundary porousness (PR U1):** The `permissions.deny` on `.claude/settings.json` and `.claude/hooks/**` was bypassable via allowlisted shell tools (`Bash(python3 *)`, `Bash(cp *)`, etc.). Narrowed the broad shell allows and added a `PreToolUse` guard. *(Later removed in the bypass-mode directive — see "Removed" below.)*
- **TikZ prevention bypasses (PR U2):** `check_p3` missed `scale={0.8}` and `scale=\myscale`; `check_p4` incorrectly flagged `align=left` (treated `left` as a direction). Rewrote with a brace/bracket-balanced tokenizer that matches standalone option keys. Parse errors now exit 2 (visible) instead of silent 0.
- **R stale-state leak (PR U3):** `scripts/R/03_analyze.R` used `exists("df")` without `inherits = FALSE`, allowing a stale globalenv to satisfy the guard. Added `inherits = FALSE` to match the contract already applied to `02_clean.R` and `05_figures.R`.
- **R template silent-skip (PR U4):** `05_figures.R` silently switched to base-R PDF if `ggplot2` was missing and silently skipped SVG if `svglite` was missing. Made `ggplot2` a hard dependency (fail loudly); kept `svglite` optional but emits an explicit "SKIPPED" warning. Rewrote `scripts/R/README.md` to document hard vs. optional deps.

### Removed

- **`.claude/hooks/protect-sensitive-paths.sh`** — added in PR U1, removed the same release under explicit user directive: "bypass mode means bypass." Bypass permissions (`defaultMode: bypassPermissions`) is the user's chosen high-autonomy workflow; re-adding approval gates during autonomous runs is a regression. Persisted to memory as `feedback_bypass_permissions.md` so this decision isn't re-litigated.

### Governance note

When adversarial reviewers (Codex, Copilot) flag the absence of approval gates as a risk under bypass mode, the template now treats that as a documented tradeoff, not a bug. Hardening under bypass mode is limited to non-blocking signals (PostToolUse reminders, notifications, logging). See `feedback_bypass_permissions.md` in the project's memory directory.

---

## v1.3.0 — 2026-04-13

### Added — TikZ story overhaul

Ported the best parts of Scott Cunningham's [MixtapeTools](https://github.com/scunning1975/MixtapeTools) TikZ infrastructure and wired them into our pipeline end-to-end.

- **`.claude/rules/tikz-prevention.md`** — 6 authoring rules (P1–P6) that stop collisions at write-time: explicit node dimensions, coordinate-map comments, prohibition on `scale=`, directional keyword on every edge label, use the snippet gallery, one tikzpicture per idea.
- **`.claude/rules/tikz-measurement.md`** — six-pass protocol with concrete formulas: Bézier `max_depth = (chord/2)·tan(bend/2)`, character-width table by font size, label-gap calculation, 0.4 cm shape-boundary rule, matplotlib `arc3` Bézier helpers, full margin matrix.
- **`templates/tikz-snippets/`** — 8 production-ready standalone `.tex` diagrams (DAG basic, DAG mediation, two-period DiD, event study, timeline, regression scatter, 3-step flowchart, supply-demand). Every snippet compiles on the first try and passes the prevention grep checks.
- **`Preambles/header.tex`** — production-ready Beamer preamble (previously empty): 11-color palette matching the SCSS, shared TikZ styles (`dag-node`, `decision-node`, `observed-edge`, `counterfactual-edge`, `confound-edge`, `observed-dot`, `counterfactual-dot`), Beamer theme assignments, convenience macros (`\muted`, `\key`, `\good`, `\bad`, `\transitionslide`).
- **`Preambles/README.md`** — usage + palette contract + inventory.
- **`scripts/check-palette-sync.sh`** — greps `Preambles/header.tex` and `Quarto/theme-template.scss`, enforces that the five core palette names exist on both sides. Wired into `validate-setup.sh`.
- **`.claude/skills/new-diagram/`** — scaffold a new TikZ diagram from the gallery with prevention checks pre-applied; compiles standalone, invokes `tikz-reviewer` with measurement citations, loops until APPROVED (max 5 rounds).

### Changed

- **`/extract-tikz`** — mandatory Step 1 prevention pre-check (greps for bare edge labels and `scale=`) before the expensive compile + SVG cycle.
- **`tikz-reviewer`** agent now requires citing the specific pass and formula from `tikz-measurement.md` for every CRITICAL/MAJOR finding. Vague reports are rejected.
- **`settings.json`** allowlist expanded substantially (+23 Bash tools, +36 Edit/Write path rules): read-only tools (grep/cat/head/tail/awk/find/tree/basename/dirname/file), file ops (cp/mv/touch/mktemp), pipeline tools (pandoc/docx2txt/pdftotext), missing git/gh subcommands (tag/rm/mv/remote, issue/release), and Edit/Write pre-approvals for every directory we normally edit (.claude/**, templates/**, guide/**, docs/**, scripts/**, Preambles/**, Slides/**, Quarto/**, Figures/**, quality_reports/**, explorations/**, master_supporting_docs/**, .github/**, plus CLAUDE.md, README.md, CHANGELOG.md, MEMORY.md, .gitignore).
- **Counts:** 23 → 24 skills, 18 → 20 rules, 7 → 6 hooks. Synced across README, `docs/index.html`, guide body, guide appendix, and CLAUDE.md.
- **Guide** Step 3 "Adapt Your Theme" rewritten to document the two-surface palette contract and the sync script.

### Removed

- **`.claude/hooks/protect-files.sh`** and its `PreToolUse` registration. The hook used to block `Edit`/`Write` on `Bibliography_base.bib` and `settings.json` unless bypass was signalled. With the explicit `Edit(...)` / `Write(...)` allow-rules added to `settings.json` (above), Claude Code's permission system handles this cleanly and the extra hook was redundant friction. Removing it also cuts a failure mode (earlier sessions had to work around the hook with `python3 -c` writes).

### Attribution

TikZ prevention + measurement rules adapted from `tikz_rules.md` in [scunning1975/MixtapeTools](https://github.com/scunning1975/MixtapeTools). The source repo has no LICENSE file; its README says "Use freely. Attribution appreciated but not required." Both ported rule files cite Scott at the top.

### Copilot review follow-up (same day)

This release shipped as a sequence of small PRs (#53–#56) plus an end-of-day Copilot-review cleanup PR that fixed 15 issues Copilot caught across those four PRs, removed `protect-files.sh` per user preference, and unified cross-skill grep patterns. Summary of the biggest catches:

- LaTeX load order in `Preambles/header.tex` (xcolor before hyperref; `\makeatletter` around `\@ifclassloaded`; `inputenc` gated by `\ifPDFTeX`).
- `protect-files.sh` env-var bypass moved above `$(cat)` so it exits immediately.
- `/extract-tikz` and `/new-diagram` grep patterns unified character-for-character.
- P1 scoped to boxed nodes; P3 reconciled with the `scale=1.1` convention.
- `check-palette-sync.sh` uses absolute paths (`$(dirname "$0")/..`) and a stable exit-code contract.
- Removed `Bash(npm *)` from the allowlist (too broad — npm run executes arbitrary scripts).

---

## v1.2.0 — 2026-04-13

### Added

- **`/respond-to-referees` skill** — parses a referee report, classifies each concern (addressed / partially / deferred / disagreement), points to specific revisions, and drafts a complete response document using `templates/response-to-referees.md`. Use during the R&R stage of paper revision.
- **HelloWorld sample** — `Slides/HelloWorld.tex` and `Quarto/HelloWorld.qmd` — minimal decks that compile/render on a fresh fork before any project customization.
- **`scripts/validate-setup.sh`** — colored dependency checker for Claude Code, XeLaTeX, Quarto, R, Python, git, gh, and hook permissions.
- **GitHub templates** — `.github/CONTRIBUTING.md`, issue templates, and PR template.
- **CHANGELOG.md** — this file.

### Changed

- **`/commit` skill** — now runs `scripts/quality_score.py` and the `verifier` agent on changed files as a pre-commit gate. Halts on score < 80 unless the user explicitly overrides.
- **`/extract-tikz` skill** — now invokes the `tikz-reviewer` agent after SVG generation and loops on revisions to the Beamer source until APPROVED.
- **`/slide-excellence` skill** — `domain-reviewer` agent is now MANDATORY for `.tex` files (was optional).
- **`CLAUDE.md`** — example rows in the Beamer environments and Quarto CSS classes tables are now visible (not hidden in HTML comments). Added links to `MEMORY.md` and `quality_reports/` so Claude knows where cross-session context lives.
- **`README.md`** — added "Verify Your Setup" step in the Quick Start; replaced "Work in progress" disclaimer; added badges and CHANGELOG link.
- **`docs/index.html`** — added SEO metadata (description, keywords, Open Graph, JSON-LD `SoftwareApplication` schema).
- **Skill count: 22 → 23** across all surfaces.

### Fixed

- `scripts/quality_score.py` — Quarto compilation check no longer doubles the path when `cwd` is set to the file's parent (was producing spurious 0/100 scores).
- `scripts/validate-setup.sh` — git config check now guards behind `command -v git` to avoid misleading warnings when git is missing.
- `Slides/HelloWorld.tex` — added a citation and bibliography slide so `/compile-latex`'s 3-pass + bibtex pipeline completes cleanly on the onboarding sample.

---

## v1.1.0 — 2026-03-20

### Added

- **`/deep-audit` skill** — repository-wide consistency audit (4 parallel specialist agents).
- **2026 Claude Code feature support** — effort levels (`/effort low|medium|high|max`), 5 permission modes, 4 hook handler types, 11 new hook events documented.
- **Skill frontmatter reference** — `effort`, `context: fork`, `agent`, `hooks`, dynamic `!\`command\`` injection.
- **Pattern 15: Sequential Adversarial Audits** — seven-audit protocol for paper review (inspired by ClaudeCodeTools).
- **Ecosystem section** — autoresearch (Karpathy), ClaudeCodeTools, clo-author, claudeblattman, MixtapeTools.
- **Prerequisites section** — install command (`curl -fsSL https://claude.ai/install.sh | bash`), Node.js, Claude account, cost notes.
- **`plansDirectory` setting** — explicit `quality_reports/plans/` location.
- **Automatic "Last Modified" date** — `date-modified: last-modified` in guide YAML.

### Changed

- Major guide refresh: 2400+ lines, all 25 factual claims verified against official docs across two deep-audit rounds.
- Template cleanup for fork-friendliness — removed project-specific session logs, emptied `Bibliography_base.bib`, renamed Emory SCSS to generic `theme-template.scss`.

### Fixed

- All 5 Python hooks: `from __future__ import annotations`, fail-open `try/except`, `~/.claude/sessions/` storage, hash length consistency.
- `pre-compact.py` exit code (2 → 0) and stdout → stderr (PreCompact ignores stdout).
- `post-compact-restore.py` reads `source` field (was reading `type`, never ran).

---

## v1.0.0 — 2026-02-28

### Initial Release

- 10 specialized agents: proofreader, slide-auditor, pedagogy-reviewer, r-reviewer, tikz-reviewer, beamer-translator, quarto-critic, quarto-fixer, verifier, domain-reviewer.
- 22 skills covering LaTeX, Quarto, R, reproducibility, research, and meta-workflows.
- 18 rules (4 always-on, 14 path-scoped) for quality gates, verification, and domain standards.
- Hooks for notifications, context monitoring, session logging, and compaction state.
- Orchestrator protocol (contractor mode) with adversarial critic-fixer loop (max 5 rounds).
- Plan-first workflow with on-disk plan persistence across context compaction.
- Three-tier memory system: `CLAUDE.md` (project), `MEMORY.md` (auto-memory), session logs.
- GitHub Pages deployment via `scripts/sync_to_docs.sh`.

---

## Upgrading Your Fork

If you forked this repo and want to pull our updates:

```bash
git remote add upstream https://github.com/pedrohcgs/claude-code-my-workflow.git
git fetch upstream
git merge upstream/main           # or: git rebase upstream/main
```

Files you almost certainly customized — `CLAUDE.md`, `Bibliography_base.bib`, `Quarto/theme-template.scss`, your lecture files in `Slides/` and `Quarto/`, `.claude/agents/domain-reviewer.md` — may produce merge conflicts. Resolve in favor of your customizations; pull only the infrastructure improvements.

To pin to a specific version: `git checkout v1.8.0` (latest as of 2026-04-27).
