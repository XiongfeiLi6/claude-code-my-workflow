---
paths:
  - "quality_reports/referee_reports/**"
  - "templates/referee-report.*"
  - "output/pdf/**"
---

# Quality Gates and Scoring Rubric (Referee Reports)

## Thresholds

- 80/100 = deliverable threshold
- 90/100 = strong journal-grade quality
- 95/100 = excellence

## Referee Report Artifacts (.md / .qmd)

### Critical Issues

| Issue | Deduction |
|-------|-----------|
| Missing recommendation category | -25 |
| Missing confidential editor section | -20 |
| Missing author comments section | -20 |
| Fabricated or unverifiable evidence claim | -30 |
| Render failure for PDF-ready QMD | -100 (auto-fail) |

### Major Issues

| Issue | Deduction |
|-------|-----------|
| Major concern lacks evidence anchor | -8 each |
| Internal inconsistency across sections | -8 |
| Recommendation not aligned with concerns | -10 |
| Overly vague major concern (non-actionable) | -5 each |
| Formatting hierarchy unclear | -5 |

### Minor Issues

| Issue | Deduction |
|-------|-----------|
| Typos/grammar issues | -1 each (cap 10) |
| Inconsistent terminology | -2 |
| Minor style/punctuation drift | -1 each |

## Enforcement

- Score < 80: block delivery and fix issues.
- Score >= 80: deliverable allowed.
- Score >= 90: strong quality.

## Required Checks Before Delivery

- [ ] Recommendation present and explicit
- [ ] Editor/author split present
- [ ] Evidence anchors included for major points
- [ ] PDF render succeeds for QMD artifacts
- [ ] Final score >= 80
