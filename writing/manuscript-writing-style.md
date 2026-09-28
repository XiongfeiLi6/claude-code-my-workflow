# Manuscript Writing Style

**Status:** the author's standard for all manuscript prose, captions, appendix text, and proposals,
in every project. **One copy only:** this file, loaded into every project through `~/.claude/CLAUDE.md`
(an `@` import). Do not copy it into a project. A project adds its own specifics in
`.claude/rules/writing-style-project.md`, which extends this file and never restates it.

**Shared files** (all in `~/Documents/GitHub/claude-code-my-workflow/writing/`):
- this rule;
- `house-style-exemplars.md`: approved and rejected passage pairs from every project. **Read it before
  drafting or revising manuscript prose**, and add to it as §4 says;
- `writing-audit-patterns.md`: the grep list of report tells used in §3.

**What this rule is for.** A research paper is an argument made by people to people. The standard is
the prose of good economics papers and the approved passages in the exemplars, not compliance with a
list. McCloskey's warning applies to this file too: rules are a floor, and applied mechanically they
make prose worse. When a rule below and a good sentence conflict, the sentence wins; say why in the
session log.

**The reader.** A well-trained economist with limited time: an editor who reads the abstract,
introduction, tables and conclusion closely and samples the rest, and a referee who then reads
everything. Write so that the editor can reconstruct the argument from topic sentences alone.

---

## 1. Principles

1. **Lead with the claim.** At every level (paper, section, paragraph, sentence) the point comes first
   and the support follows. A results paragraph opens with what the data show, in words about the
   economy, and cites the table in passing: *"Environmental enforcement rises with exposure to EU
   carbon costs. \Cref{tab: penalty} reports..."*, not *"\Cref{tab: penalty} reports the effect of..."*
   (example from a carbon-policy paper). Do not narrate what was done before saying what was found
   (Cochrane; McCloskey).

2. **State results as facts about the world.** *"Regulators sanction more often rather than more
   heavily"*, not *"the adjustment occurs primarily through the number of enforcement actions"*.
   Institutions and people are the subjects; actions are the verbs (Williams). Avoid nominalized
   subjects ("the adjustment", "the stability of the coefficient") when an actor exists.

3. **One idea per paragraph; the topic sentence carries it.** The rest of the paragraph supports,
   quantifies, or qualifies that one claim. If the topic sentences of a subsection, read in order, do
   not state its argument, rewrite the topic sentences before touching anything else.

4. **Paragraphs connect by logic, not by signposts.** Each paragraph answers the question the previous
   one raised: *how large? through which margin? compared with what? why?* Connectives carry content
   (*so, because, which implies, by contrast*); signposts (*Moreover, Additionally, Next we turn to,
   Overall*) do not. Within a sentence, put the familiar before the new (Williams).

5. **Every number gets a meaning.** Report the interpreted magnitude (per-SD percent, pp, elasticity),
   then say what it means: a comparison with a stated bridge (a ratio to a benchmark, a mechanism, a
   share of a total). A benchmark placed next to the estimate without a comparison is a list, not an
   argument. A policy implication is stated as a bridge from the result: *"Because X, Y"*. Discuss the
   numbers the argument needs; do not tour the table column by column (Cochrane).

6. **Declarative, not defensive.** Keep world-claims; cut or rewrite reader-directions (sentences about
   how the reader should take the result: *we caution, should be interpreted as, suggestive*). One hedge
   where the evidence needs it, none where it does not. A caveat is one positive sentence with one home
   (body, footnote, or table note), never two (McCloskey; Cochrane).

7. **Plain words.** The shortest accurate word; no five-dollar words; no self-praise (*striking, novel,
   very significant*). Let the magnitude carry the emphasis (McCloskey; Cochrane; Orwell).

8. **Let the argument set the shape.** No paragraph templates and no fixed paragraph counts. Sentence
   length and paragraph length vary because the content varies. Uniform, symmetric paragraphs,
   tricolons, and "not only X but also Y" frames read as generated text.

9. **A recognizable voice.** "We" for the authors' choices and for the argument's moves; the authors'
   judgment is visible where it is theirs (interpretation, the reading of a mechanism) and stated with
   the confidence the evidence supports. The voice to match is the voice in the exemplars.

10. **Brevity by revision.** Delete every sentence the argument survives without. Restating the
    previous paragraph, the table, or the section plan is not argument. A closing *"Overall, Table X
    establishes..."* paragraph is the commonest offender.

## 2. Mechanical conventions

- **Numbers.** Prose magnitudes to two significant figures (4.9%, 0.55%); coefficients and SEs live in
  tables. Inline $\hat\beta$/SE only when the coefficient itself is the object of the argument. Every
  prose number is recomputed from the current table before it is written, and one subsection uses one
  specification throughout. In tables, coefficients carry 2–4 decimals and per-SD effects 1–2;
  scientific notation only below $10^{-3}$ or above $10^{6}$.
- **Significance.** "statistically significant (at the X percent level)"; *large, substantial* are for
  economic size; no stars or p-values in prose.
- **Tense and person.** Present for findings and concepts; past for historical and institutional facts;
  "we" for choices; "we find/show" once per finding, not in adjacent sentences.
- **Hedges.** One per claim at most: *approximately, roughly, consistent with*.
- **Citations.** `\citet` when the citation is a grammatical part of the sentence, `\citep` otherwise;
  verified keys only. A citation cluster is in alphabetical (or chronological, consistently) order and
  holds at most four or five works; a direct quotation carries a page number.
- **Equations.** Introduce with "is given by" or "satisfies", not "is the following:"; define every
  symbol once, at first use; number only equations referenced later; punctuate displayed equations.
- **LaTeX.** `\Cref` at sentence start, `\cref` mid-sentence, never hard-coded numbers. `.tex` source is
  one paragraph per line.
- **Footnotes.** For a methodological choice, an institutional detail, a data nuance, or related
  literature that would break the argument's line; about five sentences at most; never a second copy
  of a caveat stated elsewhere.
- **Promises.** Every robustness check the text promises is in the appendix; if it is not, the promise
  goes.
- **Emphasis.** Italic, rarely; no bold, underline, or caps in body prose; no italic parenthetical labels
  for channels.
- **Tables and figures.** Captions describe, never state the finding; notes give specification, sample,
  inference. A robustness-summary table reports each coefficient's per-SD effect in its own column, and
  marks an off-scale entry with a dagger explained in the note. Layout and sizing follow the project's
  exhibit rule, where one exists.

## 3. Revising a subsection

Run this on every subsection, in order.

1. **Map it.** Write each paragraph's single claim in one line. Merge paragraphs that share a claim; cut
   paragraphs that only describe a table, restate, or summarize.
2. **Topic sentences.** Each states something about the economy or the actors studied. Read them in
   order: they should be the subsection's argument.
3. **Numbers.** Recompute each from the current table; two significant figures; one specification across
   the subsection.
4. **Bridges.** Every comparison says how large the estimate is relative to it, or why it matters.
5. **Report tells.** Cut *Overall, establishes the result, suggests... associated with,* column tours,
   closing summaries, signpost connectives. Grep list: `writing-audit-patterns.md` (shared folder).
6. **Voice.** Read it next to the exemplars and the paper's best-written section. It should sound like
   the same authors.

**Guard against over-cutting.** Cutting apology must not cut design logic, mechanism, or interpretation.
When a sentence has an apologetic wrapper and a substantive core, remove the wrapper and keep the core.
If a revised subsection reads as too sparse to a fresh reader, restore the reasoning that was cut.

**After an AI-assisted pass**, run `/humanize` on the edited files where the project has it, and have the
authors rewrite the topic sentences that carry the argument.

## 4. Keeping this rule alive

This rule is deliberately short and grows from the authors' own judgments, not from templates. **No
section-by-section layouts** (Results templates, numbered Introduction paragraphs, per-section recipes)
belong here: they produce 八股文, prose that fills slots instead of making an argument.

It grows through `house-style-exemplars.md` in the shared folder:

1. **Every time the authors approve or reject a passage, in any project**, add a pair there: the
   disliked version, the approved version, and a one-line reason in the authors' words, with the entry
   heading `date · [project] · section · who judged`. Record rejections of Claude-drafted text too;
   they are the most informative entries. Write to the shared file directly, never to a project copy.
2. **When the same reason appears in three or more pairs**, distill it into a principle in §1 (or sharpen
   an existing one), citing the pairs. Remove any principle the pairs contradict.
3. **Date every change** to this file in the log below.
4. **Commit** changes to the shared folder in the workflow repo (`git -C
   ~/Documents/GitHub/claude-code-my-workflow add writing && git commit`), one line, no PR; push when
   convenient. No project needs to fetch anything.

### Change log

- **2026-09-23** — Restructured (in Regulation_Coordination_ClaudeCode) from a 42 KB template-and-checklist
  rule. Section templates removed; principles rewritten around leading with the claim, logic between
  paragraphs, interpreted numbers, and voice; grep tables moved to `writing-audit-patterns.md`;
  unverified statistics and model abstracts dropped.
- **2026-09-28** — Made the single shared copy for all projects (workflow repo `writing/`, loaded via
  `~/.claude/CLAUDE.md`). Paper-specific lines generalized. Carried over from the old version the
  general conventions it lacked: table decimals and scientific notation, citation clusters and quote
  pages, the "Because X, Y" bridge, equation introduction and symbol definition, footnotes, promised
  robustness, the per-SD column in robustness-summary tables.

## Sources

Verified against the primary text (Regulation_Coordination_ClaudeCode,
`quality_reports/research/2026-09-23_economics-writing-guides.md`): McCloskey, "Economical Writing,"
*Economic Inquiry* 1985; Cochrane, "Writing Tips for Ph.D. Students"; Head, "The Introduction Formula";
Bellemare, "How to Write Applied Papers in Economics." Standard references, existence confirmed but text
not re-read: Williams, *Style: Lessons in Clarity and Grace*; Pinker, *The Sense of Style*; Thomson,
*A Guide for the Young Economist*.
