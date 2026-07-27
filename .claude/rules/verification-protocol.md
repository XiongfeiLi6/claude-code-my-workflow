---
paths:
  - "quality_reports/referee_reports/**"
  - "templates/referee-report.*"
  - "output/pdf/**"
---

# Task Completion Verification Protocol (Referee Workflow)

Every non-trivial task must include explicit verification before delivery.

## For Manuscript Review Artifacts (.md/.qmd)

1. Structural validation:
   - recommendation category exists
   - confidential comments to editor section exists
   - comments to authors section exists
2. Evidence validation:
   - major concerns include explicit manuscript anchors (section/page/table/figure)
3. Consistency validation:
   - recommendation aligns with concern severity

## For PDF Rendering (.qmd -> .pdf)

1. Render using:
   - `./scripts/render_referee_report.sh <report.qmd>`
   - fallback: `quarto render <report.qmd> --to pdf`
2. Confirm output file exists and size > 0.
3. Confirm page count >= 1 via `pypdf`.
4. Run visual sanity check:
   - preferred: raster preview with `pdftoppm`
   - fallback: Ghostscript PNG preview (`gs`) when `pdftoppm` unavailable
5. Verify no obvious clipping/overlap or unreadable sections in preview images.

## For Manuscript Inputs

- Default source may be external path outside repo.
- Optional in-repo source location: `master_supporting_docs/supporting_papers/`.
- If file cannot be parsed cleanly, document limitations explicitly.

## Verification Checklist

```
[ ] Required report sections present
[ ] Recommendation category explicit
[ ] Evidence anchors included for major concerns
[ ] PDF render successful
[ ] PDF exists and is non-empty
[ ] Visual sanity preview checked
[ ] Quality score >= 80
```
