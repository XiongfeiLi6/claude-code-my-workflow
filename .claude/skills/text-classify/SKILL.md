---
name: text-classify
description: |
  Use an LLM API to classify text documents at scale, producing a clean
  CSV/DTA/RDS keyed to your unit ID that you can merge into a regression
  dataset. Implements Susan Athey's "Level 1" workflow from the Stanford
  IRiSS 2026 panel: write a prompt, hand-label 200 docs for ground truth,
  measure type-1/type-2 error, iterate, then call the API on the full
  corpus. Cost ballpark: $0.35–$3 per 100k short documents on Together.ai
  or Anthropic API depending on model + length.
  Use when: you have a corpus of text (tweets, court rulings, job ads,
  news articles, contracts, congressional speech, patent text) and you
  want a measured variable for each unit (sentiment, topic, presence of
  X, severity, slant, language).
argument-hint: "[corpus path or description of classification task]"
allowed-tools: ["Read", "Grep", "Glob", "Write", "Edit", "Bash", "Task", "Monitor", "WebFetch"]
effort: medium
---

# Text Classification as Measurement

Turn a corpus of unstructured text into a clean variable on each unit,
ready to merge into a regression dataset. LLM classification replaces
manual coding for tasks like "is this tweet about war?", "does this
contract have an arbitration clause?", "what topic is this news article?".

**Core idea (Susan Athey, Stanford IRiSS 2026):**
> *Write classification prompt → test on ~200 samples → refine based on
> type-1/type-2 error → upload full dataset → call API. 35 cents per
> 100,000 tweets.*

The skill is structured around the same five-phase pipeline.

---

## When to Use

- **Measuring a variable from text.** Sentiment, topic, presence/absence,
  severity, target audience, slant, language, named entity.
- **Sample restriction at scale.** "Keep only filings that mention X."
  Can be done as a binary classification before the substantive analysis.
- **Coding a survey open-end response.** Replace a small army of RAs.
- **Replicating a paper that uses NLP measures.** Build the measure, then
  feed into `/audit-estimator` or `/replicate-paper`.
- **Building a measure for a project's first paper.** This is the
  cheapest new measurement tool in applied micro right now.

**Not for:** generative tasks (writing summaries, drafting prose); use the
relevant skill for that. Not for: classification where ground truth is
itself ambiguous or culturally contested (e.g., "is this hate speech?")
without an explicit codebook the prompt encodes.

---

## Inputs

- `$ARGUMENTS` — corpus path (`data/raw/tweets.csv`,
  `data/court_rulings/*.txt`) or task description (`"classify tweets in
  data/raw/tweets.csv for whether they discuss war"`).

The skill prompts for clarification on:
- The classification target (binary? multi-class? ordinal scale?)
- The unit ID (so output merges cleanly)
- The text column (if CSV) or the file-name convention (if separate files)
- Budget envelope (number of documents × estimated cost)

---

## The Five-Phase Pipeline

### Phase 1: Spec the classification task

Write `quality_reports/text_classify_{taskname}_spec.md`:

```markdown
# Text-Classify Task Spec: {taskname}

**Corpus:** [path]
**N documents:** [count]
**Unit ID column:** [e.g., `tweet_id`]
**Text column:** [e.g., `text`]
**Target variable:** [name, type, levels]

## Classification rule (codebook)

[Plain-English rule the prompt will implement.]

- Class 0 ("not about war"): [definition + 2 positive examples + 2 negative]
- Class 1 ("about war"): [definition + 2 positive examples + 2 negative]

## Edge cases the codebook resolves

- Metaphorical use ("war on drugs"): class 0
- Historical references (WW2): class 1
- Sports analogies ("battle for the title"): class 0

## Cost envelope

- Backend: [Anthropic / Together.ai / OpenAI]
- Model: [claude-haiku-4-5 / Llama-3-70b / gpt-4o-mini]
- Tokens per doc: ~[est]
- Estimated cost: [N × tokens × $/M-tokens]
```

### Phase 2: Hand-label a ground-truth sample

1. Random-sample 200 documents (`set.seed(YYYYMMDD)` per the relevant code
   convention rule).
2. **Stop and ask the user to label them** — there is no automating this
   step. Present a small interactive form (one doc per line, two-column).
3. Save `data/labels/{taskname}_handcoded.csv` with columns
   `unit_id, true_label, hand_coder_notes`.

If the user has existing hand labels, skip this phase.

### Phase 3: Prompt engineering

1. Draft an initial classification prompt. Template:

```
You are an expert document classifier. Read the document below and
classify it into one of the following classes:

{class definitions from codebook}

Resolve these edge cases as follows:
{edge cases from codebook}

Output ONLY a JSON object: {"label": <integer>, "confidence": <0-1>}

Document:
"""
{document text}
"""
```

2. Call the API on the 200-doc ground-truth sample.
3. Compute the confusion matrix vs hand labels:

```
              Pred 0   Pred 1
True 0          178       6     (false positives = 6)
True 1            4      12     (false negatives = 4)

Accuracy:    95.0%
Sensitivity: 75.0% (of true 1s, what fraction caught)
Specificity: 96.7%
```

4. Inspect the misclassified documents. Iterate prompt to address
   systematic errors. Re-run on the 200-doc sample.
5. **Stop iterating** when the confusion matrix is acceptable for your use
   case OR after 5 rounds (whichever comes first). Going further usually
   over-fits the prompt to the hand-coded sample.

### Phase 4: Call API at scale

Once the prompt is stable, run on the full corpus. The skill generates a
deterministic script `scripts/text_classify/{taskname}_classify.{py,R}`:

```python
# Concrete pattern; the skill writes language-appropriate version.
import anthropic
import json, csv, time
from pathlib import Path

client = anthropic.Anthropic()
PROMPT = Path("prompts/{taskname}.txt").read_text()

with open("data/raw/tweets.csv") as fin, \
     open("output/{taskname}_labels.csv", "w") as fout:
    w = csv.writer(fout)
    w.writerow(["unit_id", "label", "confidence"])
    for row in csv.DictReader(fin):
        resp = client.messages.create(
            model="claude-haiku-4-5",
            max_tokens=64,
            messages=[{"role": "user",
                       "content": PROMPT.format(document=row["text"])}],
        )
        out = json.loads(resp.content[0].text)
        w.writerow([row["tweet_id"], out["label"], out["confidence"]])
```

Background-launch this via `Bash` with `run_in_background: true` and
stream via `Monitor` — full-corpus runs typically take minutes to hours.

### Phase 5: Validation + merge

After the full-corpus run:

1. **Hold-out check.** Random-sample 50 newly-labeled docs (not in the
   200-doc training sample); hand-check 10–20 of them to confirm the
   API performs in the wild as it did in Phase 3.
2. **Save final outputs:**
   - `output/{taskname}_labels.csv` — the full labeled corpus
   - `output/{taskname}_labels.{rds,dta}` — language-appropriate companion
   - `quality_reports/text_classify_{taskname}_report.md` — confusion
     matrix, cost, prompt history
3. **Merge into analysis dataset.** Document in the report exactly how to
   join (`left_join` on `unit_id`).

---

## Output

```
✓ Text classification complete: {taskname}
  N docs labeled:       N
  Hand-validated:       50 (50 / 50 match → 100% agreement)
  Confusion matrix:     [accuracy / sens / spec on 200-doc training]
  Cost:                 $X.XX
  Labels:               output/{taskname}_labels.{csv,rds,dta}
  Report:               quality_reports/text_classify_{taskname}_report.md
  Prompt:               prompts/{taskname}.txt (saved verbatim for repro)
```

---

## Cost guidance (as of April 2026, subject to change)

| Backend | Model | $ per 1M input tokens | Tweets (~30 tok each) per dollar |
|---------|-------|-----------------------|----------------------------------|
| Anthropic | claude-haiku-4-5 | $0.80 | ~40,000 |
| Anthropic | claude-sonnet-4-6 | $3.00 | ~10,000 |
| Together.ai | Llama-3-70b | $0.90 | ~35,000 |
| OpenAI | gpt-4o-mini | $0.15 | ~220,000 |

For long documents (court rulings, contracts) the per-doc cost grows
roughly linearly in tokens. Always print an estimated total cost in
Phase 1 before launching Phase 4.

---

## Reproducibility requirements

- **Seed the random sample** in Phase 2 with `set.seed(YYYYMMDD)`.
- **Save the prompt** verbatim in `prompts/{taskname}.txt` and commit it.
- **Save the model identifier** (e.g., `claude-haiku-4-5-20251001`) in
  the report. Models drift; pinned versions don't.
- **Re-running tomorrow:** the same prompt + the same pinned model
  produces the same labels (LLM outputs are sampled, so labels may
  flip on ~1% of docs at default temperature — set `temperature=0`
  for stricter reproducibility, document the tradeoff).

---

## Cross-references

- [`.claude/skills/replicate-paper/SKILL.md`](../replicate-paper/SKILL.md) — when replicating a paper that uses an LLM-classified variable, this skill rebuilds the classified column.
- [`.claude/skills/audit-estimator/SKILL.md`](../audit-estimator/SKILL.md) — once labels are merged into a regression, test the downstream estimator.
- [`.claude/rules/r-code-conventions.md`](../../rules/r-code-conventions.md) / Stata conventions — followed for the generated script.

## What this skill does NOT do

- **Build the codebook for you.** The classification rule is yours;
  the skill scaffolds the prompt around it.
- **Replace IRB / ethics review.** If the text is human-subjects data
  (interviews, private messages), the skill stops at Phase 1 and prompts
  the user to confirm IRB coverage.
- **Generate embeddings.** That's the Level-2 use case Athey describes;
  worth a future sibling skill `/embeddings-as-covariates`.
- **Fine-tune a model.** That's Level 2/3; see Athey's slide deck and
  Together.ai / Hugging Face fine-tuning docs.
