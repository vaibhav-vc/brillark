---
name: metric-dictionary
category: data
description: "Define every metric once, with one owner."
output: "metric-dictionary.md"
used_by:
  - chief-data-officer-agent
---

# Metric Dictionary

`data` · produces `metric-dictionary.md` · used by `chief-data-officer-agent`

Define every metric once, with one owner.

## Procedure
1. Write the precise definition, including the filters and the time basis.
2. Name the source system and the exact calculation.
3. Assign one owner responsible for the definition.
4. Record known caveats and where the metric is misleading.
5. Reject any duplicate definition of an existing metric.

## Output contract
`metric-dictionary.md` → `workspace/<venture-id>/data/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/data.tsv`.

## Quality bar
- One definition and one owner per metric
- Caveats documented
- The output states its confidence grade and names the evidence behind every load-bearing claim.
