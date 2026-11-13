# Data definitions and harmonization

Read when ingesting, joining or harmonizing sources. Use existing project metadata
and codebooks; extend them rather than creating a competing source of truth.

- Record source/version, unit of observation, key, variable meaning, units, valid
  values and missing-value codes, time/geographic coverage and access restrictions.
  Distinguish documented definitions from inferred ones; flag unknowns explicitly.
- Check key uniqueness, join cardinality, unmatched cases and before/after counts
  against the intended sample. Inspect metadata or approved aggregates without
  putting restricted raw records into model context or exported reports.
- Document each harmonization: source field -> target definition, transformation,
  units, affected observations, source evidence and approval where needed. Do not
  silently equate different survey questions, scales, periods or geographic units.
- Keep a discovered discrepancy visible. An undocumented missing code or ambiguous
  definition blocks the dependent transformation, not all independent work. Do not
  resolve it by dropping rows or choosing the version that gives a preferred result.
- Preserve raw inputs and implement approved transformations in code. Keep existing
  scientific choices; new measurement/sample decisions require owner resolution.
- Select storage/query tools from the actual scale and project environment; no
  particular format or database is required by this reference.

See the [source review](../../docs/ACADEMIC_WORKFLOW_REVIEW.md).
