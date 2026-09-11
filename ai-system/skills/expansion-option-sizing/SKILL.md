---
name: expansion-option-sizing
category: council
description: "Size an expansion option honestly, including what it would require."
output: "expansion-options.md"
used_by:
  - council-expansion-scout
---

# Expansion Option Sizing

`council` · produces `expansion-options.md` · used by `council-expansion-scout`

Size an expansion option honestly, including what it would require.

## Procedure
1. Define the option concretely: which customers, which offer, which channel.
2. Size the opportunity with the same rigour as the core market.
3. State the prerequisite that must be true first.
4. Estimate the cost and the distraction risk to the core.
5. Recommend a sequence position, not immediate pursuit.

## Output contract
`expansion-options.md` → `workspace/<venture-id>/council/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/council.tsv`.

## Quality bar
- Prerequisite stated honestly
- Distraction risk to core estimated
- The output states its confidence grade and names the evidence behind every load-bearing claim.
