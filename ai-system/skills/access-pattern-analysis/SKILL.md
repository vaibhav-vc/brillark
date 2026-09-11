---
name: access-pattern-analysis
category: engineering
description: "Establish how data will actually be read and written."
output: "access-patterns.md"
used_by:
  - data-model-designer
---

# Access Pattern Analysis

`engineering` · produces `access-patterns.md` · used by `data-model-designer`

Establish how data will actually be read and written.

## Procedure
1. List every query the application makes, with its frequency and latency need.
2. List every write pattern and its consistency requirement.
3. Identify the patterns that will dominate at scale.
4. Check the model serves them without full scans or fan-out.
5. Re-check when a new feature adds an access pattern.

## Output contract
`access-patterns.md` → `workspace/<venture-id>/engineering/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/engineering.tsv`.

## Quality bar
- Frequency and latency captured per query
- Dominant patterns identified
- The output states its confidence grade and names the evidence behind every load-bearing claim.
