---
paths:
  - "**/*.tex"
  - "**/*.qmd"
  - "manuscript/**"
  - "paper/**"
  - "drafts/**"
---

# Manuscript Writing Style — Constitutional Standard for Economics

**Status:** Constitutional. This document is the foundational writing-style standard for every economics paper the author writes, regardless of submission target. The standard is calibrated to top-5 best practice. Aiming at this standard is not the same as submitting to a top-5 journal; it is what guarantees that the paper is *publishable* at the highest level.

**Scope:** all manuscript prose (Abstract, Introduction, Context, Framework, Data, Empirical Strategy, Results, Discussion, Conclusion), all table and figure captions, all appendix material. Applies to empirical papers; theory-specific conventions are flagged.

## 0. Calibration and scope

### 0.1 Two stylistic registers

Top-5 economics papers publish in two registers:

- **Minimalist register:** short subsections, table-led, direct claims, sparing on synthesis. Exemplars: Chetty, Levitt, Dell, Autor–Dorn–Hanson, Kleven–Landais–Søgaard.
- **Discursive register:** longer subsections, expository discussion, narrative and institutional framing. Exemplars: Goldin, Card, Acemoglu, Krueger.

Both are publishable. The default for this constitutional standard is the **minimalist register**, because it is the harder discipline and the easier register to back away from when expository content is needed. If a paper's contribution depends on framing or institutional context that requires expository writing (institutional-detail papers, surveys, narrative-heavy work, theory papers), override at the section level — but keep the foundational principle (§1) in force.

### 0.2 Empirical, theory, hybrid

Most of this document applies to empirical papers; theory-specific conventions are flagged "[theory]." Hybrid papers (theory + empirical) follow empirical conventions in the empirical sections and theory conventions in the theory sections.

### 0.3 Audience model

The constitutional reader is an associate editor at a top-5 economics journal — time-pressed and well-trained. Optimize the manuscript for the AE's reading pattern, then for the referee's deeper read.

| Section | AE reading time | What the AE looks for |
|---|---|---|
| Abstract | 1–2 min | Question, gap, contribution, headline result, inferential implication |
| Introduction | 10–15 min | Whether the contribution clears the bar |
| Tables + captions | 10–15 min | Identification, magnitudes, robustness |
| Conclusion | 5 min | Policy implication and broader contribution |
| Body prose | sampled | Whether the identification narrative survives a careful read |
| Footnotes | only if body raises a question | Methodological detail |

Every word in the Abstract, Introduction, Conclusion, and table/figure captions is read by the AE. Body prose is sampled. Footnotes are read only if the body raises a question. Plan word-economy accordingly.

## 1. Foundational principle

### 1.1 World-claim vs reader-direction

Every sentence makes one of two kinds of claim:

- A **world-claim** describes a fact about the world, the data, the model, or the mechanism — a coefficient, a magnitude, an institutional fact, a model prediction. World-claims are confident, declarative, substantive. Keep them.
- A **reader-direction** describes how the reader should react — how to interpret the claim, what caveat to apply, what tone to adopt. Reader-directions are apologetic, defensive, or meta-narrative. Rewrite as world-claims, or cut.

When in doubt, ask: *"Is this sentence about the world, or about how I want the reader to think about my analysis?"* If it's about the reader's thinking, rewrite it as a world-claim or cut. The substance carries the meta-message; spelling out the meta-message is reader-direction.

### 1.2 Three derived rules

1. **Declarative, not defensive.** State the finding directly. The reader judges precision from the table; do not qualify in prose.
2. **Substance, not signposting.** Every paragraph advances the argument. Paragraphs that announce what's coming, restate what's just been said, or self-explain the section architecture are signposts, not arguments.
3. **Substantive logic stays.** The world-vs-meta distinction is not a license to cut design explanation, mechanism interpretation, or channel framing. Substantive logic explains the design choices and tells the reader what they mean economically — keep it.

### 1.3 The self-excusing test (concrete)

> World-claim → keep. *"Coresidence absorbs roughly half of the employment decline."*
>
> Reader-direction → cut or rewrite. *"We caution the reader to interpret these results as suggestive."*

A world-claim can be confident, declarative, and substantive. A reader-direction is, by construction, apologetic.

## 2. Document architecture

### 2.1 Empirical paper section sequence

| # | Section | Pages | Purpose |
|---|---|---|---|
| Abstract | 1 | 150–200 words | Sell the contribution and the implication |
| 1 | Introduction | 4–6 | Frame question, summarize finding, position in literature |
| 2 | Institutional Context | 1–3 | Setting-specific detail the empirical reader needs |
| 3 | Conceptual Framework | 1–2 | Optional; useful when multiple mechanisms are plausible |
| 4 | Data | 2–3 | Sources, variable construction, summary statistics |
| 5 | Empirical Strategy / Identification | 2–4 | Specification, identifying assumption, threats and mitigations |
| 6 | Results | 10–15 | Per-link findings, per-outcome magnitudes, dynamics |
| 7 | Mechanisms / Robustness | 3–5 | Channel decomposition, sensitivity, falsifications |
| 8 | Discussion / Policy / Conclusion | 3–5 | Inferential implications + broader meaning |
| A | Appendix | 10–30 | Data appendix, theory appendix, full robustness battery |

Weights in the AE's mind: the Introduction and Results together carry 60–70% of the verdict. The Empirical Strategy section determines whether the paper survives the referee's identification audit. The other sections must be present and clean.

### 2.2 Theory paper sequence [theory]

| # | Section | Purpose |
|---|---|---|
| Abstract | Sell the result and the framework |
| Introduction | Frame the question and the contribution to theory |
| Model | State the environment, agents, equilibrium concept |
| Analysis | Propositions, comparative statics, optional proofs in body or appendix |
| Application / Extensions | Calibration or special cases |
| Conclusion | Implications |

### 2.3 Hybrid sequence

Empirical-leaning hybrid: insert Conceptual Framework after Context. Theory-leaning hybrid: empirical evidence becomes a "Quantification" or "Application" section after the Analysis.

## 3. Section templates

### 3.1 Abstract template

Five components, 150–200 words total:

1. **Motivation** (1 sentence): the question or vulnerability the literature opens.
2. **Gap** (1 sentence): what the literature has not done.
3. **Contribution** (1–2 sentences): what this paper does, including the setting and the method.
4. **Headline result** (2–3 sentences): the central finding with one or two headline magnitudes.
5. **Inferential implication** (1–2 sentences): why this matters, in **"Because X, Y"** form.

The "Because X, Y" structure is required for the inferential implication: it forces the writer to spell out the bridge from result to implication. "X provides a rationale for Y" lets the writer skip the bridge.

Example skeleton (substantive content from a carbon-leakage / enforcement paper):
> *Does carbon leakage provoke a regulatory response in the destination country? [Motivation.] The literature documents that leakage occurs but treats the destination as a passive absorber. [Gap.] We provide the first evidence tracing each link of the chain from foreign carbon pricing to domestic enforcement, using a shift-share design that maps EU~ETS embodied carbon costs to Chinese city-sectors. [Contribution + method.] A one-standard-deviation rise in export-weighted carbon exposure raises Chinese environmental penalty counts by approximately one percent, with the response strategic, institutionally mediated by the 2016 centralization of inspection, and asymmetric across pollutants. [Result.] Because Chinese enforcement already closes much of the regulated-pollutant gap but leaves the CO_2 gap open, a CBAM targeted narrowly at greenhouse gases is appropriately calibrated, while a CBAM extended to broad environmental standards would over-correct. [Inferential implication, in "Because X, Y" form.]*

### 3.2 Introduction template

**Architecture.** A top-5 introduction has the following paragraph structure. Numerical-content discipline is strict:

| Paragraph | Role | Numerical content |
|---|---|---|
| P1–2 | Motivation + research question | None |
| P3 | High-level finding + headline magnitude | One headline number |
| P4–5 | Why-not-obvious + identification strategy | None |
| P6–8 | Detailed results | Per-spec ranges, per-outcome magnitudes, benchmark comparisons |
| P9 | Back-of-the-envelope / quantification | Specific magnitudes |
| P10 | Policy implications | Magnitudes where load-bearing |
| P11+ | Related literature / contributions | None (or one number per literature when load-bearing) |

**Audit test for each paragraph.** Each detail paragraph (P6, P7, P8) should contain at least one specific number that does not appear in P3. If not, the detail paragraph is restatement.

**Self-containment.** A reader who reads only the Introduction should leave with: the contribution, the method, the headline result, the inferential implication.

**Two failure modes to avoid:**
- All headline numbers in P3, no numbers in P6–8.
- Pre-announcing the result in P1 or P2 (the motivation paragraph sets up the question; the result belongs in P3).

### 3.3 Related Literature template

Three to four paragraphs, one per literature stream the paper contributes to. Each paragraph follows the same template:

1. **Name the literature** with a citation cluster.
2. **State what the literature has established.**
3. **State what this paper adds**, in "We extend X by Y" or "We open the black box of X by documenting Y" form.

Avoid the "we contribute to N literatures" opener — it is signposting. Open the section directly with the first literature.

### 3.4 Institutional Context template

One paragraph per relevant institution. Each paragraph names the institution, states the relevant facts (with citations to legal text or government documents), and states why the fact matters for identification.

The Context section is the discursive register inside an otherwise minimalist paper. Long paragraphs are acceptable; expository tone is acceptable; defensive prose is not.

### 3.5 Conceptual Framework template [optional]

Useful when (a) the result has multiple plausible mechanisms, (b) the empirical specification needs theoretical motivation, or (c) the paper's quantification step depends on a structural object. Skip if the headline result is robust to mechanism specification.

When present, the framework has three components:

1. **Environment** (1 paragraph): agents, choices, payoffs, equilibrium concept.
2. **Predictions** (1 paragraph per testable prediction): a numbered list. State each prediction in "X increases (decreases) in Y" form; defer derivation to a footnote or appendix.
3. **Mapping to empirics** (1 paragraph): how each prediction maps to a coefficient or sign in the empirical analysis.

### 3.6 Data template

Four standard subsections:

1. **Outcomes:** how the headline outcome variables are constructed, including units and transformations.
2. **Treatment / instrument:** how the identifying variation is constructed.
3. **Sample:** geography × time × unit; exclusions; final N.
4. **Summary statistics:** a single table with the headline variables; prose reports two or three round numbers that the reader needs to anchor magnitudes.

A "Comparison to existing data" paragraph is useful when the data source is new or controversial.

### 3.7 Empirical Strategy / Identification template

The most load-bearing section after the Introduction. Standard structure:

1. **Specification** (1 paragraph): write the regression equation. Define every term, including fixed effects. Cite the SE convention.
2. **Source of identifying variation** (1 paragraph): in one sentence, what cross-sectional or time-series comparison identifies the parameter?
3. **Identifying assumption** (1 paragraph): the formal exogeneity condition, with a citation to the relevant econometric framework (Borusyak-Hull-Jaravel 2022 for shift-share, Goldsmith-Pinkham-Sorkin-Swift 2020 for share-based identification, etc.).
4. **Threats and mitigations** (1 subsection per threat, ≤6 threats): for each threat, state the threat, state how the design handles it, state the robustness check that supports the handling.

**Promised-robustness discipline:** if §5 promises a robustness check, the appendix must deliver the table or the promise must come out of §5. Orphan promises hurt credibility because the referee will grep the appendix.

### 3.8 Results template

One subsection per link in the empirical chain. Each subsection has:

1. **Opener** (1 paragraph): what the subsection covers and in what order. Do not state the finding.
2. **Headline paragraph** (1 paragraph per outcome, see §4.2 result-paragraph template).
3. **Heterogeneity or mechanism paragraph** (1 paragraph): what differs across subgroups or specifications, with magnitudes.
4. **Caveat paragraph** (0 or 1 paragraph): one direct sentence; see §4.3.

### 3.9 Robustness template

A short paragraph per robustness check, plus a robustness-summary table (§6.1). Each robustness paragraph:

1. **Names the threat** the robustness addresses.
2. **Describes the modification** in one sentence.
3. **States the result** in one sentence with the per-SD comparison to the headline.

### 3.10 Discussion / Policy template

Three components:

1. **Refinement of the policy claim** (1 paragraph): unfold the inferential bridge from result to policy implication; state the mechanism details the implication depends on.
2. **Quantification or back-of-the-envelope** (1 paragraph): translate the regression coefficient to a policy-relevant magnitude.
3. **Limitations and extensions** (1 paragraph): what would change the conclusion; what the next paper does.

### 3.11 Conclusion template

Two to three paragraphs. The Conclusion is NOT a summary of the paper; it is a synthesis.

1. **What the paper showed** (1 paragraph): one sentence per major link, with one headline magnitude.
2. **Why it matters** (1 paragraph): the broader implication, beyond the specific setting.
3. **Open questions** (optional 1 paragraph): the most important next-paper question.

Avoid restating the paper section by section. The reader has already read the paper.

### 3.12 Appendix template

The appendix has up to four standard sections, in order:

| § | Title | Contents |
|---|---|---|
| A | Data Appendix | Variable definitions, additional summary stats, data-cleaning detail |
| B | Theory Appendix | Proofs, additional propositions [theory] |
| C | Robustness Tables | Every robustness regression promised in the body, plus inference diagnostics |
| D | Figures | Event studies, IRFs, balance plots |

Place all regression-results tables in §C (or whatever the Tables section is called). Inline placement of result tables in data-construction subsections is the worst-of-both-worlds layout: the reader does not know where to look. Description in §A → forward reference to §C.

## 4. Paragraph-level templates

### 4.1 Subsection opener

One paragraph that names what the subsection covers, in what order, and at what level of aggregation. Optionally one sentence of design context (why the comparison is structured a certain way). **Do not state the finding.**

> *This section presents the labor-market response to the policy in three steps: the pooled DD on the four headline outcomes, the cohort heterogeneity by age in 2010, and the descriptive decomposition by realized fertility. The unit of analysis throughout is the woman-year, with always-eligible women as the comparison group.*

### 4.2 Result paragraph

(i) State the finding with the **interpreted magnitude** in one sentence, citing the table column. (ii) One or two sentences of substantive interpretation — what the magnitude means economically, or how it compares to a literature benchmark. (iii) Move on.

> *Column 1 of Table 4 reports a 10.6 percentage-point decline in labor force participation among newly eligible women, or 14.8 percent of the pre-reform mean. The magnitude is roughly twice the median child penalty estimate in Kleven et al. (2019) at the corresponding event horizon, consistent with the policy shock binding on a margin that voluntary-fertility settings cannot identify.*

Coefficients, standard errors, and significance stars live in the table. The prose reports the interpreted magnitude (per-SD percent, percentage-point change, dollar effect, elasticity). Inline $(\hat\beta, \text{SE})$ is reserved for cases where the coefficient itself is the argumentative object — comparing to a literature benchmark, emphasizing precision, contrasting two coefficients where the contrast is the result.

### 4.3 Mechanism / channel paragraph

When the result has more than one plausible mechanism, write a paragraph that:

1. **States the candidate mechanisms** as a list.
2. **States the empirical signature** of each.
3. **Reports which signature the data show**, with the magnitude.
4. **States the inference** — which mechanism the data support, and which they cannot rule out.

> *The strategic-enforcement interpretation predicts that the headline coefficient survives controls for output and sector-level pollution; the mechanical-scaling interpretation predicts the coefficient collapses. Column 4 of Table 7 reports a coefficient of 0.0013 (SE 0.0008) after both controls, statistically indistinguishable from the unconditional headline 0.0070 and economically a 0.17% per-SD effect. The data are consistent with strategic enforcement; mechanical scaling is rejected.*

### 4.4 Caveat

One direct positive sentence stating the methodological limit. No "we caution," no "we emphasize," no "should be interpreted as." If the caveat needs more than one sentence, the rest goes in a footnote on the subsection title or in the table notes.

> *Because realized fertility is itself an outcome of the policy, within-panel comparisons describe correlations between policy-induced labor changes and realized fertility rather than causal effects on a fixed subpopulation.*

Each methodological caveat has exactly one home: section opener, footnote, or table notes. If a caveat appears in two places, drop one.

### 4.5 Transition between subsections

A connecting sentence is acceptable when the next subsection genuinely depends on the previous one (*"Section 3.2 extends the pooled DD with cohort heterogeneity..."*). It is self-excusing when it just announces what's coming (*"In this subsection, we will document..."*). Test: does the sentence add information the reader cannot infer from the section title?

### 4.6 Footnote

Footnotes hold (i) methodological choices the reader might worry about that the body does not have room for, (ii) institutional detail relevant to identification, (iii) data-construction nuance, (iv) references to closely-related literature where a fuller treatment would derail the body. Length up to ~5 sentences is normal; longer than that usually means the content belongs in the appendix or a robustness section. A caveat already stated in the body should not be repeated in a footnote.

## 5. Sentence-level conventions

### 5.1 Voice and agency

- **"We"** for substantive choices the authors made (design, sample, specification, robustness): *"We restrict the sample to..."*, *"We use city-clustered standard errors..."*.
- **Impersonal** for technical descriptions and findings: *"The specification is..."*, *"Column 3 reports..."*.
- **Avoid first-person agency for the result itself.** "We find" / "we show" / "we document" are acceptable once per finding but not in adjacent sentences. The result is in the data, not in the authors' agency.

### 5.2 Tense

- **Present tense for findings:** *"Column 1 reports a 10.6 pp decline."*
- **Past tense for institutional and historical facts:** *"The EU ETS began trading in 2005."*
- **Present tense for conceptual statements:** *"Regulators face a trade-off between growth and enforcement."*

### 5.3 Hedging language

- **Acceptable:** "approximately X%", "roughly X%", "X to Y%", "consistent with X", "in the range of X."
- **Unacceptable:**
  - Stacked hedges in one sentence ("approximately significant at the five-percent level"; "roughly approximately one percent").
  - "We cannot rule out that..." — rewrite as one positive caveat sentence.
  - "This is suggestive evidence that..." — either it identifies the parameter or it does not; pick one.
  - "May / might / could possibly" stacks.

### 5.4 Statistical significance language

- **"Statistically significant at the X percent level"** — the standard formulation.
- **"Significant" alone** — ambiguous between statistical and economic; reserve for statistical context only.
- **"Substantial / meaningful / large"** — reserve for economic significance.
- **Stars in tables**, never in prose; SE in tables, never inline unless the SE itself is the argumentative object.

### 5.5 Number presentation

- **Coefficients in tables:** 2–4 decimal places, consistent within a single table.
- **Per-SD percentages in prose:** 1 decimal place typically, 2 for very small effects.
- **Magnitudes in prose:** round to no more than 2 significant figures (4.1%, not 4.06%).
- **Standard errors in tables:** same precision as the coefficient.
- **Scientific notation in tables:** only when the magnitude is below $10^{-3}$ or above $10^{6}$.

## 6. Visual conventions

### 6.1 Table captions and notes

**Caption** (one sentence): describes the table's content in a single declarative sentence. Do not state the finding.

**Notes** (multiple sentences, starting with "Note:" or "Notes:"): describes the specification, the fixed effects, the sample, the standard-error convention, the significance codes, and any non-obvious construction.

**Standard table-note skeleton:**
> *Notes: The table reports estimates from Equation~(X) at the [unit] level. Outcomes are [list]. [Specification details: regressor transformations, FE structure, control set.] Standard errors clustered at the [unit] level in parentheses. Significance levels: $^{***}$ $p<0.01$, $^{**}$ $p<0.05$, $^{*}$ $p<0.10$.*

### 6.2 Robustness summary tables

A robustness-summary table reports the headline coefficient across alternative specifications in a single column. Standard layout: *Specification, Estimate, SE, N*.

**When raw coefficients are on different scales** (e.g., alternative weighting schemes whose regressors have different units), add a **Per-SD (%) column** that translates each raw coefficient to a single interpretable scale (coefficient × regressor SD × 100). Mark off-scale rows with a footnote dagger pointing to the per-SD column as the apples-to-apples comparison. For specifications where the per-SD translation does not apply (e.g., a shock measure in different units), enter "—" and document in the note.

### 6.3 Figure captions and notes

Caption: one sentence describing what the figure shows.

Notes: data source, unit of observation, axis definitions, confidence-band definition, reference year/group for event studies or IRFs, any normalization.

### 6.4 Equations

- **Number equations that are referenced later in the text.**
- **Don't number** equations used only for one-shot definition or explanation.
- **Introduce** equations with a colon or with "is given by" / "satisfies"; not "is the following:".
- **Punctuate** displayed equations as sentences (period or comma at the end based on the grammar of the surrounding paragraph).
- **Define every symbol** the first time it appears. If a symbol appears in more than one section, the first definition is canonical; later sections can reuse without redefinition.

### 6.5 Emphasis

- **Italic** for emphasis, used sparingly (no more than once per page).
- **Bold** rarely, primarily in table notes for substantive sub-headings or panel labels.
- **Double quotes** for terms of art being introduced (*"carbon leakage,"* *"strategic enforcement"*); not for emphasis.
- **Parenthetical italic narrative labels** (e.g., *(the leakage channel)*) are not AER/QJE convention. Reserve italicized parentheticals for inline variable or abbreviation definitions: *(count)*, *(Exp)*, *(a priori)*.

### 6.6 Citation style

- **Use `\citet{...}` for in-text grammatical citations** ("Following \citet{X}, we...").
- **Use `\citep{...}` for parenthetical citations** at the end of a clause.
- **Citation clusters** at the end of a clause should be alphabetical and contain at most 4–5 entries; longer lists go in a footnote.
- **Verify every citation key exists** in the bib before adding. Do not invent keys.

### 6.7 Cross-references

- **Use `\Cref{...}` (capitalized) at sentence start.**
- **Use `\cref{...}` (lowercase) mid-sentence.**
- **Tables, figures, sections, equations all use `\Cref`** — the package decides the prefix.
- **Never hard-code "Table 3"** — use the label; renumbering will break the hard-code.

## 7. Common failure modes

### 7.1 The five high-level failures

The five highest-frequency *structural* failures, ranked:

1. **Defensive prose.** The result is hedged so heavily the reader cannot tell what is claimed. Apply the world-claim test (§1.1).
2. **Restatement instead of argument.** Paragraphs restate the table or the previous paragraph in different words. Cut.
3. **Number-free detail paragraphs in the Introduction.** P6–P8 read as filler if they have no specific magnitudes. Add benchmark comparisons.
4. **Self-excusing transitions.** "In this section we will..." Rewrite as a substantive bridge.
5. **Policy claims without inferential bridges.** "X provides a rationale for Y." Rewrite as "Because X, Y."

### 7.2 Specific patterns to grep and cut

Tactical audit checklist. Each pattern has a regex-friendly trigger, one explanation, and the recommended fix. Run a pass with each pattern before submission.

#### 7.2.1 Over-defensive expressions

Cut or rewrite as a single positive caveat sentence (§4.4):

| Trigger | Why | Fix |
|---|---|---|
| `we caution\b`, `we emphasize\b`, `we cannot rule out` | Reader-direction (§1.1). Verb tells the reader how to react. | Drop the verb; state the claim directly. *"We cannot rule out that X"* → *"X is consistent with the data."* |
| `it should be noted that`, `it is important to note that`, `it bears emphasizing that` | Empty meta-introduction. | Drop the introduction; state the claim. |
| `should be interpreted as suggestive rather than\|definitive` | Verbose hedging. | One positive sentence stating the limit. See §4.4. |
| `this is suggestive evidence that`, `the results are suggestive of` | The data either identify the parameter or do not. "Suggestive" is reader-direction. | Either commit to the identification claim or rewrite as a partial-correlation statement. |
| `may / might / could possibly\|could potentially` stacks | Hedge-stacking; one hedge is enough. | Pick one modal. *"may potentially affect"* → *"may affect."* |
| Trailing repeated-caveat paragraphs after the result | The section-opener caveat already covers this. | Cut the trailing paragraph. Caveats have one home (§4.4). |

#### 7.2.2 Inline statistical reporting

These belong in the table, not in the prose:

| Trigger | Why | Fix |
|---|---|---|
| `\(p\s*[<=]\s*0\.[0-9]+\)`, `(p = 0.03)` inline | $p$-values live in the table via significance stars. Inline $p$-values clutter the prose and signal anxiety about the result. | Drop. The reader sees significance from the table. |
| `\(\\hat\\beta\s*=`, `(β = X, SE = Y)` inline when the table is directly below | Duplicates the table. | Drop, or reserve for cases where the coefficient itself is the argumentative object (§4.2). |
| Significance stars in prose: *"the effect is significant\*\*\*"* | Stars are a table convention. | *"statistically significant at the one percent level"* or just *"statistically significant."* |
| Reporting $t$-statistics or $F$-statistics inline when the table provides them | Same as above. | Drop unless the statistic is the argumentative object. |

#### 7.2.3 Punctuation overuse

| Trigger | Why | Fix |
|---|---|---|
| Em-dash overuse — three or more per paragraph | Em-dashes are for one essential aside per paragraph. Overuse signals poor sentence structure. | Restructure as separate sentences or convert to commas/parentheses. The em-dash should be load-bearing, not a decorative substitute for a comma. |
| Parenthetical asides used to bury qualifications | If you have to parenthesize the qualification, the sentence structure needs to change. | Promote the qualification to its own sentence, or drop it. |
| Semicolon-comma chains (a; b; c, d; e) | Hard to parse. | Break into separate sentences. |
| Double parentheticals: *"(a few studies (Smith 2020) have found ...)"* | Nested parentheses are hard to read. | Restructure or use a footnote. |

#### 7.2.4 Restatement patterns

| Trigger | Why | Fix |
|---|---|---|
| *"We find ... we show ... we document"* in adjacent sentences | One usage per finding is standard top-5; repetition is the violation. | Vary the construction; let one finding stand per paragraph. |
| Pre-announcing results in section openers: *"We find that X."* in P1 of a Results subsection. | The result belongs in the result paragraph, not the opener. | Subsection opener describes scope and order; the result paragraph delivers the magnitude. See §4.1. |
| Restating the table column-by-column: *"Column 1 shows X. Column 2 shows Y. Column 3 shows Z."* | The table shows it. The prose interprets it. | One result paragraph per outcome (§4.2); skip the column tour. |
| Restating the previous paragraph in different words | Restatement is not argument. | Cut. |

#### 7.2.5 Empty intensifiers and transition words

| Trigger | Why | Fix |
|---|---|---|
| `\b(clearly\|obviously\|importantly\|notably\|interestingly)\b` | These adverbs tell the reader how to feel rather than what to think. | Drop. If the claim is clear, the reader knows; if it isn't, the adverb won't help. |
| `\b(very\|quite\|rather\|extremely\|highly\|fairly)\b` as intensifier | Empty intensifiers dilute the magnitude. | Drop, or replace with a quantitative comparison. *"very large"* → *"twice the size of X."* |
| Sentence-start `Furthermore,\|Moreover,\|Additionally,\|In addition,` | Often used when the connection between sentences is already clear. | Drop the connector and let the sentences sit adjacent; or rewrite the connection substantively (*"This implies..."* instead of *"Moreover,..."*). |
| Sentence-start `In particular,\|Specifically,\|That is,` when the elaboration is already implicit | Empty signposting. | Drop. |

#### 7.2.6 Verbose constructions

| Trigger | Replace with |
|---|---|
| `the fact that` | Drop or rewrite (*"The fact that X is Y"* → *"X is Y, which..."*). |
| `in order to` | `to` |
| `due to the fact that` | `because` |
| `at this point in time` | `now` or drop |
| `a number of` | `several` or a specific number |
| `is able to`, `has the ability to` | `can` |
| `make use of` | `use` |
| `with respect to`, `with regard to` | `for`, `about`, or drop |

#### 7.2.7 Formatting and visual noise

| Trigger | Why | Fix |
|---|---|---|
| Parenthetical italicized narrative labels in intro chain summaries: `(\textit{the leakage channel})` after each "First/Second/..." link | Not AER/QJE convention; redundant with sentence-level signposting. | Drop. Reserve `(\emph{...})` for inline variable/abbreviation definitions: `(\emph{count})`, `(\textbf{Exp})`, `(\textit{a priori})`. |
| Bold for emphasis in body prose | Bold in body prose reads as a textbook, not a journal article. | Use italic sparingly, or restructure the sentence so the emphasis is structural. |
| Underline | Not used in econ typography. | Italic. |
| ALL CAPS | Not used in econ prose. | Italic or restructure. |
| Footnotes longer than 5 sentences | Footnote is overrunning the body discipline. | Promote to appendix or robustness subsection. |

#### 7.2.8 Citation hygiene

| Trigger | Why | Fix |
|---|---|---|
| Citation clusters with more than 4–5 entries: `\citep{A,B,C,D,E,F,G}` | The reader cannot retain that many citations. | Drop to the 3–4 most important; move the rest to a footnote. |
| `\citet{X}` mid-sentence when grammatical | Inconsistent with the rest of the document. | `\citep{X}` if parenthetical; `\citet{X}` only when X is a grammatical subject or object. |
| Citing a paper whose bib key you haven't verified | Invented keys break compile. | Verify the bib key exists before adding. |
| Citing without page number for a direct quote | Top-5 convention requires page number for quotes. | Add the page number: `\citep[p.~187]{X}`. |

## 8. Over-application failures

The most common mistake when applying this rule is cutting substantive logic along with apologetic prose. Three patterns to avoid:

- **Cutting a design-establishing opener** because it contains "we present." Edit the verb; keep the design content.
- **Burying a body-level caveat in a footnote** when the reader needs it as part of the opener's framing. One direct caveat sentence in the body is fine; the footnote holds additional technical content.
- **Cutting "we find" / "we show" wholesale** because they appear on the failure-mode list. The rule is no repetition in adjacent sentences; one usage per finding is standard.

**When a sentence has both an apologetic wrapper and a substantive core, edit the wrapper and keep the core.**

> Original: *"We caution that the patterns in Panel A are consistent with several non-exclusive explanations."*
>
> Surgical: *"The patterns in Panel A are consistent with several non-exclusive explanations."*
>
> Over-surgical (wrong): deleting the whole sentence and losing the substantive interpretation that follows.

## 9. Sanity checks (run after editing)

1. **Fresh-reader test.** Read the section as if you had never seen the prior version. Does it read as too sparse, unmotivated, or missing the *why*? If yes, you over-applied — restore the substantive logic.
2. **Substance-loss check.** For each paragraph deleted, ask: did the paragraph contain any world-claim (design, channel, interpretation) that no other paragraph carries? If yes, restore at least one substantive sentence.
3. **Length check.** If a 4-paragraph subsection collapsed to 2, you probably over-applied. The minimalist register is compact but not minimal — a typical top-5 subsection runs 3–5 paragraphs.
4. **Caveat-home check.** Each methodological caveat has exactly one home. Drop duplicates.
5. **Number-discipline check.** Each detail paragraph of the Introduction (P6, P7, P8) contains at least one specific number that does not appear in P3.
6. **Inferential-bridge check.** Each policy claim in the Abstract is in "Because X, Y" form.
7. **Promised-robustness check.** Each robustness check promised in §5 has a corresponding appendix table.
8. **Mechanism-acknowledgement check.** Each policy claim in the Discussion section addresses the mechanism the policy uses (CBAM credit-for-price-paid; EITC phase-in/out; etc.).
9. **AI-voice audit.** After any AI-assisted revision pass, run `/humanize` on the edited files (or rely on `/review-paper-light` Agent C, which runs `humanize-auditor` automatically). The §7.2 tactical checklist catches the most common AI tells by grep, but `/humanize` also flags symmetric paragraph shapes, tricolon abuse, and lexical fingerprints (the LLM training-distribution markers) that grep cannot detect. Triggered automatically by the orchestrator when an AI-assisted edit touches a paper-like file; the writer should also run it explicitly before journal submission or working-paper posting.

---

**References:** [AER style guide](https://www.aeaweb.org/journals/aer/style-guide); [AEJ: Applied style guide](https://www.aeaweb.org/journals/app/style-guide); Borusyak-Hull-Jaravel (2022), "Quasi-Experimental Shift-Share Research Designs," *Review of Economic Studies*; Borusyak-Hull-Jaravel (2025), "A Practical Guide to Shift-Share Instruments," *Journal of Economic Perspectives*.
