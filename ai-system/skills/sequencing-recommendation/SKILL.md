---
name: sequencing-recommendation
category: council
description: "Recommend an order rather than a wish list."
output: "sequence-plan.md"
used_by:
  - council-expansion-scout
---

# Sequencing Recommendation

`council` · produces `sequence-plan.md` · used by `council-expansion-scout`

Recommend an order rather than a wish list.

## Procedure
1. Identify the prerequisites linking the options.
2. Place options that unlock others earlier.
3. Check capacity — a sequence that requires doing everything at once is not a sequence.
4. State what must be true before each step begins.
5. Define the checkpoint between steps.

## Output contract
`sequence-plan.md` → `workspace/<venture-id>/council/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/council.tsv`.

## Quality bar
- Prerequisites drive the order
- Capacity checked against the sequence
- The output states its confidence grade and names the evidence behind every load-bearing claim.
