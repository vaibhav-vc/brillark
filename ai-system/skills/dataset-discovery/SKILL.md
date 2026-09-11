---
name: dataset-discovery
category: research
description: "Find the data that could answer the question."
output: "dataset-candidates.md"
used_by:
  - data-sourcing-analyst
---

# Dataset Discovery

`research` · produces `dataset-candidates.md` · used by `data-sourcing-analyst`

Find the data that could answer the question.

## Procedure
1. Identify who would collect this data and why they would publish it.
2. Search primary statistical sources before aggregators.
3. Check for official, academic, industry, and open-data sources.
4. Record what exists and, importantly, what does not.
5. Prefer the source closest to the measurement.

## Output contract
`dataset-candidates.md` → `workspace/<venture-id>/research/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/research.tsv`.

## Quality bar
- Primary sources searched before aggregators
- Non-existence recorded as a finding
- The output states its confidence grade and names the evidence behind every load-bearing claim.
