---
paths:
  - "**/*.tex"
  - "**/*.qmd"
  - "manuscript/**"
  - "paper/**"
  - "drafts/**"
---

# Manuscript Writing Style

**Target audience:** top-journal referees and editors. The manuscript is a finished argument, not a lab notebook. Apply when editing manuscript prose (Results, Introduction, Conclusion, abstracts, discussion sections).

## Calibration

Top-5 empirical papers publish in at least two stylistic registers: the **minimalist register** (Chetty, Levitt, Dell, Autor–Dorn–Hanson, Kleven–Landais–Søgaard — short subsections, table-led, direct claims, sparing on synthesis) and the **discursive register** (Goldin, Card, Acemoglu, Krueger — longer subsections, expository discussion, narrative and institutional framing). Both are publishable.

This rule prescribes the **minimalist register**. The result is prose that reads as clean and direct but can read as undersupported if expository content the reader needs is cut. If a paper's contribution depends on framing or historical context that requires expository writing (institutional detail papers, surveys, narrative-heavy work), this rule is too restrictive — override on those subsections.

## Core principle

Writing decisions distinguish **claims about the world** (keep, state directly) from **claims about how the reader should think about your analysis** (cut or rewrite). The latter category includes apologetic, defensive, and meta-narrative prose. Substantive logical explanation — what the design is, why the comparison is structured a certain way, what the channels mean — is *not* in this category. Keep it.

### The self-excusing test

Before cutting any sentence, ask: *"Does this sentence make a claim about the world, or a claim about how the reader should think about my analysis?"*

- World-claim → keep. *"Coresidence absorbs roughly half of the employment decline."*
- Reader-direction → cut or rewrite. *"We caution the reader to interpret these results as suggestive."*

A world-claim can be confident, declarative, and substantive. A reader-direction is, by construction, apologetic.

## Positive templates

### Introduction architecture: where numbers go

Top-5 empirical intros follow a consistent arc. The numerical-content
discipline is:

| Paragraph | Role | Numerical content |
|---|---|---|
| 1–2 | Motivation + research question | None |
| 3 | High-level finding | One headline magnitude (e.g., the central per-SD effect) and the qualitative shape of the result |
| 4–5 | Why-not-obvious + identification | None |
| 6–8 | Detailed results | Per-spec ranges, per-outcome magnitudes, comparisons to literature benchmarks |
| 9+ | Policy + literature | Magnitudes where load-bearing |

**The failure mode to avoid:** all headline numbers in P3, no numbers in
P6–8. Referees skip number-free detail paragraphs as filler. The
detailed paragraphs are precisely where specific magnitudes, per-spec
ranges, and benchmark comparisons should live; if you cut them out of
the detail paragraphs, the detail paragraphs read as restatement.

**Test:** for each of P6, P7, P8, ask whether the paragraph contains at
least one specific number that does not appear in P3. If no, the
detail paragraph is doing no work.

### Abstract: state the inferential step

Policy claims in the abstract should unfold the logic from result to
conclusion, not assert the conclusion alone. The reader of an abstract
should be able to reconstruct the inferential chain without reading the
policy section.

- Asserts the conclusion (cut or rewrite): *"The asymmetry between
  regulated-pollutant and CO₂ enforcement provides a precise rationale
  for CBAM targeted at greenhouse gases rather than broad environmental
  standards."*
- Unfolds the bridge (use): *"Because Chinese enforcement already
  closes much of the regulated-pollutant gap but leaves the CO₂ gap
  open, a CBAM targeted narrowly at greenhouse gases (as the EU
  mechanism is designed) is appropriately calibrated, while a CBAM
  extended to broad environmental standards would over-correct."*

The "Because X, Y" structure forces you to write the bridge. The
"X provides a rationale for Y" structure lets you skip it.

### Subsection opener

One paragraph that names what the subsection covers, in what order, and at what level of aggregation. Optionally one sentence of design context (why the comparison is structured a certain way). **Do not state the finding.**

Example:
> *This section presents the labor-market response to the policy in three steps: the pooled DD on the four headline outcomes, the cohort heterogeneity by age in 2010, and the descriptive decomposition by realized fertility. The unit of analysis throughout is the woman-year, with always-eligible women as the comparison group.*

### Result paragraph

(i) State the finding with the **interpreted magnitude** in one sentence, citing the table column. (ii) One or two sentences of substantive interpretation — what the magnitude means economically, or how it compares to a literature benchmark. (iii) Move on.

Example:
> *Column 1 of Table 4 reports a 10.6 percentage-point decline in labor force participation among newly eligible women, or 14.8 percent of the pre-reform mean. The magnitude is roughly twice the median child penalty estimate in Kleven et al. (2019) at the corresponding event horizon, consistent with the policy shock binding on a margin that voluntary-fertility settings cannot identify.*

Avoid: $(\hat\beta = -0.106, \text{SE} = 0.017, p < 0.01)$ inline. The coefficient, SE, and significance star live in the table. The prose reports the interpreted magnitude (here: percentage-point change, percent of pre-reform mean).

### Caveat

One direct positive sentence stating the methodological limit. No "we caution," no "we emphasize," no "should be interpreted as." If the caveat needs more than one sentence, the rest goes in a footnote on the subsection title or in the table notes.

Example:
> *Because realized fertility is itself an outcome of the policy, within-panel comparisons describe correlations between policy-induced labor changes and realized fertility rather than causal effects on a fixed subpopulation.*

The reader knows what "describe correlations rather than causal effects" means. No further hedging needed in the body.

### Transition between subsections

A connecting sentence is fine when the next subsection genuinely depends on the previous one (*"Section 3.2 extends the pooled DD with cohort heterogeneity..."*). It is self-excusing when it just announces what you're about to do (*"In this subsection, we will document..."*). Test: does the sentence add information the reader couldn't infer from the section title? If yes, keep. If no, drop.

### Robustness summary table

A robustness-summary table reports the headline coefficient across
alternative specifications in a single column. Standard layout:
*Specification, Estimate, SE, N*. When alternative specifications
produce raw coefficients on different scales (e.g., alternative
weighting schemes whose underlying regressors have different units),
the raw-coefficient column is misleading — a reader cannot compare
β = 0.0077 to β = 2.92 even though both correspond to the same per-SD
effect.

**Fix:** add a *Per-SD (%)* column that translates each raw coefficient
to a single interpretable scale (coefficient × regressor SD × 100).
Mark off-scale rows with a footnote dagger pointing to the per-SD
column as the apples-to-apples comparison.

For specifications where the per-SD translation does not apply (e.g.,
the regressor uses a different functional form, such as a Kanzig shock
in units of EU policy surprise rather than a carbon-cost rate), enter
*--* in the per-SD column and document the omission in the table note.

### Policy claims acknowledge the policy's actual mechanism

When making a policy claim in the abstract, introduction, or policy
discussion about a specific instrument — a CBAM, an EITC, a Pigouvian
tax, an emissions cap — the claim must address the mechanism's actual
design. Examples of mechanism details to address:

- *CBAM:* the credit-for-carbon-price-paid mechanism (no double
  taxation when the destination has carbon pricing); the destination
  country's existing carbon pricing (pilot ETS, national ETS, carbon
  tax).
- *EITC:* the phase-in and phase-out rates; the disincentive on the
  intensive margin in the phase-out region.
- *Pigouvian tax:* the difference between the tax base and the
  externality scope.
- *Emissions cap:* the allocation method (auctioning vs free
  allocation); the cost-containment mechanism (price floor, ceiling).

Policy claims that ignore the mechanism's actual design are fragile —
any referee who knows the policy will reject the claim. State the
mechanism, then state how your finding interacts with it.

### Promised robustness checks must be delivered

If §5 ("Identification and Validity") promises a robustness check
("we verify robustness by excluding X cities"; "we control for Y at
the sector-year level"; "we use alternative weights from Z"), the
appendix must either deliver the table or the promise must come out of
§5. Orphan promises hurt credibility because referees who search the
appendix will catch the gap.

**Audit pattern:** after each round of edits, grep §5 for "robustness,"
"we verify," "we check," "we control for," and confirm each promised
check has a corresponding appendix table.

### Footnote

Footnotes hold (i) methodological choices the reader might worry about that the body doesn't have room for, (ii) institutional detail relevant to identification, (iii) data-construction nuance, (iv) references to closely-related literature where a fuller treatment would derail the body. Length up to ~5 sentences is normal; longer than that usually means the content belongs in the appendix or a robustness section.

A caveat already stated in the body should *not* be repeated in a footnote. Pick one home.

## Inline conventions

- **$\hat\beta$ and SEs live in the table**, not the prose. Stars and SEs in parentheses below the coefficient. No stars in prose.
- **Prose reports the *interpreted* magnitude** (per-SD percentage, elasticity, dollar effect, percentage-point change) and refers the reader to the relevant column.
- **Inline $(\hat\beta, \text{SE})$ is reserved for cases where the coefficient itself is the argumentative object** — comparing to a literature benchmark, emphasizing precision, or contrasting two coefficients where the contrast is the result.
- **Magnitude convention**: state once near the start of the Results section, then use consistently. For IHS or shift-share specs, specify the SD of the regressor and the translation to per-SD percentages.
- **Acceptable hedges**: "approximately X%", "roughly X%", "X to Y%". **Stacked hedges are unacceptable**: "approximately significant at the five-percent level."

References: [AER style guide](https://www.aeaweb.org/journals/aer/style-guide), [AEJ: Applied style guide](https://www.aeaweb.org/journals/app/style-guide).

## Anti-patterns to cut

In order of frequency:

1. **Trailing repeated-caveat paragraphs.** A "We caution against giving these patterns a strict causal interpretation..." paragraph *after* the result, restating what the section-opener caveat already said. Cut.
2. **Stale legacy paragraphs.** When a section is reframed (e.g., "child penalty / policy penalty" → "descriptive decomposition"), the original framing paragraphs often survive as artifacts and contradict the new framing. Search and cut.
3. **"We emphasize at the outset that..."** If it's important enough to emphasize, state it as fact.
4. **"We caution the reader against / that..."** Describes how the reader should react. Let substance carry that work.
5. **"We describe rather than attribute"** / **"our interpretive language reflects this"** — meta-commentary on your own interpretive style.
6. **"We cannot fully rule out the possibility that..."** Verbose hedging. State the caveat as one positive sentence.
7. **"The results should therefore be interpreted as suggestive rather than definitive evidence of..."** Same pattern, more verbose.
8. **Pre-announcing results in section openers.** "We find that X" two paragraphs before the table that shows X.
9. **"We find / we show / we document" in adjacent sentences.** One usage per finding is standard top-5; repeating in consecutive sentences is the violation. Banning these phrases outright is wrong.
10. **Inline $(\hat\beta = \ldots, \text{SE} = \ldots)$** that duplicates the table directly below.
11. **Defending dropped specifications in body prose.** Belongs in a footnote, robustness subsection, or data appendix. Defending the *chosen* specification is fine and often required.
12. **Stacked hedges** in one sentence.
13. **Parenthetical narrative labels in intro chain summaries**:
    `(\textit{the leakage channel})`, `(\textit{the production
    channel})` and similar after each "First/Second/..." link. Not
    common in AER or QJE intros — sentence-level signposting already
    structures the chain, so the parenthetical labels are visual noise.
    Reserve italicized parentheticals for inline variable or
    abbreviation definitions: `(\emph{count})`, `(\textbf{Exp})`,
    `(\textit{a priori})`.
14. **Asserting a policy conclusion without the inferential bridge**.
    "The asymmetry provides a precise rationale for CBAM targeted at
    greenhouse gases" — the reader cannot reconstruct why. See
    "Abstract: state the inferential step" above.

## Common over-application failures

The most common mistake is cutting substantive logic along with apologetic prose. Three patterns to avoid:

- **Cutting a design-establishing opener** because it contains the verb "we present." Edit the verb; keep the design content.
- **Burying a body-level caveat in a footnote** when the reader needs it as part of the opener's framing. One direct caveat sentence in the body is fine; the footnote holds the *additional* technical content.
- **Cutting "we find" / "we show" wholesale** because they appear on the anti-pattern list. The rule is no repetition in adjacent sentences; one usage per finding is standard.

When a sentence has both an apologetic wrapper and a substantive core, **edit the wrapper, keep the core**:

- Original: *"We caution that the patterns in Panel A are consistent with several non-exclusive explanations."*
- Surgical: *"The patterns in Panel A are consistent with several non-exclusive explanations."*
- Over-surgical (wrong): deleting the whole sentence and losing the substantive interpretation that follows.

## Sanity checks (run after editing)

1. **Fresh-reader test.** Read the revised section as if you'd never seen the prior version. Does it read as too sparse, unmotivated, or missing the *why*? If yes, you over-applied — restore the substantive logic.
2. **Substance-loss check.** For each paragraph deleted, ask: did this paragraph contain any world-claim (design, channel, interpretation) that no other paragraph carries? If yes, restore at least one substantive sentence.
3. **Length check.** If a 4-paragraph subsection collapsed to 2, you probably over-applied. The minimalist register is compact but not minimal — a typical top-5 subsection runs 3–5 paragraphs.
4. **Caveat-home check.** Each methodological caveat should have exactly one home: section opener, footnote, or table notes. If a caveat appears in two of these, drop one.
