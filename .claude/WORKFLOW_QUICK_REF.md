# Workflow Quick Reference

**Model:** Plan-first contractor mode for anonymous manuscript referee work

---

## The Loop

```
Your instruction
    ↓
[SPEC] (if ambiguous) -> MUST/SHOULD/MAY + clarity status
    ↓
[PLAN] -> file-level implementation plan -> your approval
    ↓
[EXECUTE] autonomous implementation
    ↓
[MILESTONE CHECK-INS] draft, verification, final artifact
    ↓
[REPORT] outputs + quality score + open decisions (if any)
```

---

## I Ask You When

- Recommendation threshold is borderline (Major vs Minor Revision)
- A key manuscript section is unreadable/ambiguous and changes conclusions
- You need to choose between materially different framing choices
- Scope expansion is non-trivial (new analyses, extra documents, new templates)

---

## I Execute Autonomously When

- Report structure is already approved
- Evidence extraction and synthesis are straightforward
- Rendering, QA checks, and score evaluation are mechanical
- Fixes are clear and do not change substantive judgment

---

## Early Session Check-ins (Enabled)

For your first sessions, I check in at these boundaries:
1. Spec complete
2. Plan complete
3. First report draft complete
4. Verification complete
5. Final PDF complete

---

## Quality Gates (No Exceptions)

| Score | Action |
|-------|--------|
| >= 80 | Deliverable ready |
| < 80  | Block delivery and fix issues |

---

## Non-Negotiables

- Evidence-grounded critique only
- No fabricated claims, citations, or section references
- Anonymous reviewer identity in all report artifacts
- Confidential comments to editor are kept separate from author-facing comments
- PDF must pass render and visual sanity checks before delivery

---

## Canonical Paths

- Report sources: `quality_reports/referee_reports/`
- Final PDFs: `output/pdf/`
- Optional in-repo manuscript copies: `master_supporting_docs/supporting_papers/`
- Default manuscript source: external path provided by user

---

## Next Step

You provide task -> I spec/plan if needed -> you approve -> I execute autonomously with milestone check-ins.
