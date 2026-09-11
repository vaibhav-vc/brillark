---
name: data-model-design
category: engineering
description: "Design the data structure around how it will actually be used."
output: "data-model.md"
used_by:
  - data-model-designer
---

# Data Model Design

`engineering` · produces `data-model.md` · used by `data-model-designer`

Design the data structure around how it will actually be used.

## Procedure
1. Model the entities and relationships in the domain first.
2. Enumerate the queries and write patterns the system must support.
3. Choose the storage technology from those patterns, not from preference.
4. Define integrity constraints and enforce them at the storage layer.
5. Classify every field for privacy and retention at creation.

## Output contract
`data-model.md` → `workspace/<venture-id>/engineering/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/engineering.tsv`.

## Quality bar
- Access patterns enumerated before design
- Constraints enforced at the storage layer
- The output states its confidence grade and names the evidence behind every load-bearing claim.
