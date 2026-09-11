---
name: dataset-licence-review
category: research
description: "Check we are allowed to use it the way we intend."
output: "licence-record.md"
used_by:
  - data-sourcing-analyst
---

# Dataset Licence Review

`research` · produces `licence-record.md` · used by `data-sourcing-analyst`

Check we are allowed to use it the way we intend.

## Procedure
1. Find the licence or terms of use for every dataset used.
2. Check whether commercial use, redistribution, and derivation are permitted.
3. Check attribution requirements and comply with them.
4. Flag datasets whose licence forbids the intended use before anyone builds on them.
5. Record the licence alongside the data in the repository.

## Output contract
`licence-record.md` → `workspace/<venture-id>/research/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/research.tsv`.

## Quality bar
- Intended use checked against the licence
- Licence recorded with the data
- The output states its confidence grade and names the evidence behind every load-bearing claim.
