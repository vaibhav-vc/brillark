---
name: comparison-matrix
category: market
description: "Compare alternatives on the dimensions that decide purchases."
output: "comparison-matrix.md"
used_by:
  - competitor-intel-analyst
---

# Comparison Matrix

`market` · produces `comparison-matrix.md` · used by `competitor-intel-analyst`

Compare alternatives on the dimensions that decide purchases.

## Procedure
1. Derive dimensions from customer interviews, not from our feature list.
2. Score each alternative honestly, including where we lose.
3. Weight dimensions by how much they influence the decision.
4. Show the weighted result and the dimension that decides most cases.
5. Update when a competitor ships something material.

## Output contract
`comparison-matrix.md` → `workspace/<venture-id>/market/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/market.tsv`.

## Quality bar
- Dimensions derived from customer language
- Losses recorded honestly
- The output states its confidence grade and names the evidence behind every load-bearing claim.
