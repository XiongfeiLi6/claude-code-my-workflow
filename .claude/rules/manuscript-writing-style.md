---
paths:
  - "**/*.tex"
  - "**/*.qmd"
  - "manuscript/**"
  - "paper/**"
  - "drafts/**"
---

# Manuscript Writing Style

**Target audience:** top-journal referees and editors. The manuscript is a finished argument, not a lab notebook. Apply this rule whenever editing manuscript prose (Results, Introduction, Conclusion, abstracts, discussion sections).

## Core rule: declarative, not defensive

Top-journal prose **states what the section does and lets the result land**. It does not pre-announce findings, explain methodological choices in the opener, or enumerate what we excluded.

### Don't do this

- **Pre-announce results in section openers.** Do not write "we find that X" two paragraphs before the table that shows X. The opener says what the section covers; the result paragraph carries the finding.
- **Defend dropped specifications in body prose.** Do not write "we drop the city-level / firm-level / monthly X because Y" in the main text. If the choice is methodologically interesting, it belongs in (a) a footnote, (b) a robustness subsection, or (c) the data appendix. Body prose presents what we *did* report, not what we didn't.
- **Self-explain the section architecture.** Do not write "we report A and B because the contrast between them is the central finding." That is the reader's job to notice. State what A and B are; let them notice.
- **Hedge with future-tense road-mapping inside a subsection.** "In what follows, we will see..." is acceptable at the start of the entire Results section, not inside individual subsections that span half a page.
- **Stack hedges in the same sentence.** "approximately roughly about" or "approximately significant" or "the coefficient is approximately positive" — pick one hedge or zero.

### Do this instead

- **One opener sentence per subsection.** Tell the reader what the subsection covers and at what level of aggregation. Stop.
- **Let results land in the paragraph that reports them.** Interpreted magnitudes (per-SD percentages, elasticities, dollar effects, marginal effects), comparisons, and significance claims belong with the relevant table reference, not in the opener.
- **Methodological caveats go in footnotes.** If a coefficient is sensitive to a choice the reader might worry about, a one-line footnote is the right place — not a defensive paragraph in the body.
- **Justifications for analytical choices belong in the methods section or the data appendix**, not inside Results subsection openers.

## Cross-references and inline coefficients

Follow the prevailing top-journal convention (AER, QJE, *Econometrica*, JPE, *RES*, *AEJ*, *Journal of Public Economics*):

- **$\hat\beta$ and standard errors live in the table**, not the prose. Stars and SEs in parentheses below the coefficient. No stars in prose.
- **Prose reports the *interpreted* magnitude** (per-standard-deviation percentage, elasticity, dollar effect, percentage-point change) and refers the reader to the relevant column.
- **Inline $(\hat\beta, \text{SE})$ is reserved for cases where the coefficient itself is the argumentative object** — comparing to a literature benchmark, emphasizing precision, contrasting two coefficients where the contrast is the result, or where the raw number is downstream calibration input for an accounting calculation.

Reference: [AER style guide](https://www.aeaweb.org/journals/aer/style-guide), [AEJ: Applied style guide](https://www.aeaweb.org/journals/app/style-guide).

## Magnitude convention

For shift-share and Bartik designs, IHS-transformed regressors, or any specification where the raw coefficient is not directly interpretable:

- **State the convention once**, near the start of the Results section, as a footnote or short methods paragraph. Specify the standard deviation of the regressor and the formula for translating coefficients to per-SD percentages.
- **Use the convention throughout.** Do not switch between per-unit, per-SD, and elasticity interpretations within the same section.
- **Acceptable hedges**: "approximately X%", "roughly X%", "X to Y%" for a range. **Not acceptable**: stacked hedges, or hedges around already-uncertain quantities ("approximately statistically significant at the five-percent level").

## Tone

- **Confident, not defensive.** State the result. Significance claims appear once per result, not in every sentence that mentions the coefficient.
- **Declarative, not hedged**, except where genuine uncertainty exists (e.g., a coefficient that is borderline-significant or a magnitude that depends on a calibration assumption).
- **Active voice where possible.** "Exposure raises enforcement" > "enforcement is found to be raised by exposure".
- **No paragraph titles in continuous-argument subsections.** If the subsection is a single argument unfolding across 2–4 paragraphs, do not interrupt with `\paragraph{...}` titles. Paragraph titles are appropriate when each paragraph is a distinct sub-finding (typical of long Results sections like Strategic Enforcement or Heterogeneity).

## When in doubt, cut

If a sentence in body prose reads like *"we did X because Y, but not Z because W"* — cut it. The reader can see X in the table; W is irrelevant to a reader who came for the result.

If a paragraph opens with self-explanation — *"in this subsection we will document..."*, *"the contrast between A and B is central to our finding..."*, *"the natural concern with this specification is..."* — rewrite it to start with the substantive statement instead.

## Common targets for cleanup

When applying this rule to existing drafts, the highest-yield targets are usually:

1. **Subsection openers** that pre-announce results or defend choices.
2. **Inline $(\hat\beta = ..., \text{SE} = ...)$** parentheticals that duplicate the table directly below the paragraph.
3. **"Interpretation" paragraphs** at the end of result subsections that restate the result in different words.
4. **Footnotes that exceed three sentences** — usually a sign that the content belongs in the appendix.
5. **"We find / we show / we document" phrases** repeated in adjacent sentences — keep one.
