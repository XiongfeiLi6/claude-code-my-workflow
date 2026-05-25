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
