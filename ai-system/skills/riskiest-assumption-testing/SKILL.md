---
name: riskiest-assumption-testing
category: product
description: "Test the belief that would hurt most if wrong, first."
output: "rat-test.md"
used_by:
  - mvp-scoper
---

# Riskiest Assumption Testing

`product` · produces `rat-test.md` · used by `mvp-scoper`

Test the belief that would hurt most if wrong, first.

## Procedure
1. Rank assumptions by how much of the plan collapses if each is false.
2. Take the top one and define what evidence would disprove it.
3. Design the cheapest test that could produce that evidence.
4. Set the decision threshold before running it.
5. Act on the result, including when it is inconvenient.

## Output contract
`rat-test.md` → `workspace/<venture-id>/product/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/product.tsv`.

## Quality bar
- Threshold set before the test runs
- Result acted on regardless of convenience
- The output states its confidence grade and names the evidence behind every load-bearing claim.
