---
name: data-quality-scoring
category: data
description: "Measure whether the data can be trusted."
output: "data-quality-report.md"
used_by:
  - chief-data-officer-agent
---

# Data Quality Scoring

`data` · produces `data-quality-report.md` · used by `chief-data-officer-agent`

Measure whether the data can be trusted.

## Procedure
1. Define quality dimensions: completeness, validity, timeliness, and consistency.
2. Set a check per dimension per critical dataset.
3. Score and publish, rather than assuming quality.
4. Alert on degradation, not just on absolute failure.
5. Fix the worst-scoring source each cycle.

## Output contract
`data-quality-report.md` → `workspace/<venture-id>/data/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/data.tsv`.

## Quality bar
- Checks defined per dimension
- Degradation alerts, not just failures
- The output states its confidence grade and names the evidence behind every load-bearing claim.
