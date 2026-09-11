---
name: methodology-assessment
category: research
description: "Read how the number was made before using it."
output: "methodology-notes.md"
used_by:
  - data-sourcing-analyst
---

# Methodology Assessment

`research` · produces `methodology-notes.md` · used by `data-sourcing-analyst`

Read how the number was made before using it.

## Procedure
1. Find the sample: who was measured, how many, and how selected.
2. Find the definitions: what exactly was counted as what.
3. Find the date and the collection period.
4. Identify who funded it and any consequent incentive.
5. State the limits that matter for our specific use.

## Output contract
`methodology-notes.md` → `workspace/<venture-id>/research/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/research.tsv`.

## Quality bar
- Sample and definitions established
- Use-specific limits stated
- The output states its confidence grade and names the evidence behind every load-bearing claim.
