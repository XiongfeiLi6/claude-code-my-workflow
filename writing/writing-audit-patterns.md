# Writing Audit Patterns (grep list)

Moved verbatim from the pre-2026-09-23 `manuscript-writing-style.md` (§7.2). Used by step 5 of the revision checklist in that rule. These catch surface tells only; they are a floor, not the standard.

## Over-defensive expressions

Cut or rewrite as a single positive caveat sentence (§4.4):

| Trigger | Why | Fix |
|---|---|---|
| `we caution\b`, `we emphasize\b`, `we cannot rule out` | Reader-direction (§1.1). Verb tells the reader how to react. | Drop the verb; state the claim directly. *"We cannot rule out that X"* → *"X is consistent with the data."* |
| `it should be noted that`, `it is important to note that`, `it bears emphasizing that` | Empty meta-introduction. | Drop the introduction; state the claim. |
| `should be interpreted as suggestive rather than\|definitive` | Verbose hedging. | One positive sentence stating the limit. See §4.4. |
| `this is suggestive evidence that`, `the results are suggestive of` | The data either identify the parameter or do not. "Suggestive" is reader-direction. | Either commit to the identification claim or rewrite as a partial-correlation statement. |
| `may / might / could possibly\|could potentially` stacks | Hedge-stacking; one hedge is enough. | Pick one modal. *"may potentially affect"* → *"may affect."* |
| Trailing repeated-caveat paragraphs after the result | The section-opener caveat already covers this. | Cut the trailing paragraph. Caveats have one home (§4.4). |

## Inline statistical reporting

These belong in the table, not in the prose:

| Trigger | Why | Fix |
|---|---|---|
| `\(p\s*[<=]\s*0\.[0-9]+\)`, `(p = 0.03)` inline | $p$-values live in the table via significance stars. Inline $p$-values clutter the prose and signal anxiety about the result. | Drop. The reader sees significance from the table. |
| `\(\\hat\\beta\s*=`, `(β = X, SE = Y)` inline when the table is directly below | Duplicates the table. | Drop, or reserve for cases where the coefficient itself is the argumentative object (§4.2). |
| Significance stars in prose: *"the effect is significant\*\*\*"* | Stars are a table convention. | *"statistically significant at the one percent level"* or just *"statistically significant."* |
| Reporting $t$-statistics or $F$-statistics inline when the table provides them | Same as above. | Drop unless the statistic is the argumentative object. |

## Punctuation overuse

| Trigger | Why | Fix |
|---|---|---|
| Em-dash overuse — three or more per paragraph | Em-dashes are for one essential aside per paragraph. Overuse signals poor sentence structure. | Restructure as separate sentences or convert to commas/parentheses. The em-dash should be load-bearing, not a decorative substitute for a comma. |
| Parenthetical asides used to bury qualifications | If you have to parenthesize the qualification, the sentence structure needs to change. | Promote the qualification to its own sentence, or drop it. |
| Semicolon-comma chains (a; b; c, d; e) | Hard to parse. | Break into separate sentences. |
| Double parentheticals: *"(a few studies (Smith 2020) have found ...)"* | Nested parentheses are hard to read. | Restructure or use a footnote. |

## Restatement patterns

| Trigger | Why | Fix |
|---|---|---|
| *"We find ... we show ... we document"* in adjacent sentences | One usage per finding is standard top-5; repetition is the violation. | Vary the construction; let one finding stand per paragraph. |
| Pre-announcing results in section openers: *"We find that X."* in P1 of a Results subsection. | The result belongs in the result paragraph, not the opener. | Subsection opener describes scope and order; the result paragraph delivers the magnitude. See §4.1. |
| Restating the table column-by-column: *"Column 1 shows X. Column 2 shows Y. Column 3 shows Z."* | The table shows it. The prose interprets it. | One result paragraph per outcome (§4.2); skip the column tour. |
| Restating the previous paragraph in different words | Restatement is not argument. | Cut. |

## Empty intensifiers and transition words

| Trigger | Why | Fix |
|---|---|---|
| `\b(clearly\|obviously\|importantly\|notably\|interestingly)\b` | These adverbs tell the reader how to feel rather than what to think. | Drop. If the claim is clear, the reader knows; if it isn't, the adverb won't help. |
| `\b(very\|quite\|rather\|extremely\|highly\|fairly)\b` as intensifier | Empty intensifiers dilute the magnitude. | Drop, or replace with a quantitative comparison. *"very large"* → *"twice the size of X."* |
| Sentence-start `Furthermore,\|Moreover,\|Additionally,\|In addition,` | Often used when the connection between sentences is already clear. | Drop the connector and let the sentences sit adjacent; or rewrite the connection substantively (*"This implies..."* instead of *"Moreover,..."*). |
| Sentence-start `In particular,\|Specifically,\|That is,` when the elaboration is already implicit | Empty signposting. | Drop. |

## Verbose constructions

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

## Formatting and visual noise

| Trigger | Why | Fix |
|---|---|---|
| Parenthetical italicized narrative labels in intro chain summaries: `(\textit{the leakage channel})` after each "First/Second/..." link | Not AER/QJE convention; redundant with sentence-level signposting. | Drop. Reserve `(\emph{...})` for inline variable/abbreviation definitions: `(\emph{count})`, `(\textbf{Exp})`, `(\textit{a priori})`. |
| Bold for emphasis in body prose | Bold in body prose reads as a textbook, not a journal article. | Use italic sparingly, or restructure the sentence so the emphasis is structural. |
| Underline | Not used in econ typography. | Italic. |
| ALL CAPS | Not used in econ prose. | Italic or restructure. |
| Footnotes longer than 5 sentences | Footnote is overrunning the body discipline. | Promote to appendix or robustness subsection. |

## Citation hygiene

| Trigger | Why | Fix |
|---|---|---|
| Citation clusters with more than 4–5 entries: `\citep{A,B,C,D,E,F,G}` | The reader cannot retain that many citations. | Drop to the 3–4 most important; move the rest to a footnote. |
| `\citet{X}` mid-sentence when grammatical | Inconsistent with the rest of the document. | `\citep{X}` if parenthetical; `\citet{X}` only when X is a grammatical subject or object. |
| Citing a paper whose bib key you haven't verified | Invented keys break compile. | Verify the bib key exists before adding. |
| Citing without page number for a direct quote | Top-5 convention requires page number for quotes. | Add the page number: `\citep[p.~187]{X}`. |

