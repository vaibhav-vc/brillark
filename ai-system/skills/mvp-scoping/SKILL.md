---
name: mvp-scoping
category: product
description: "Find the smallest build that answers the riskiest question."
output: "mvp-scope.md"
used_by:
  - engineering-head
  - mvp-scoper
---

# Mvp Scoping

`product` · produces `mvp-scope.md` · used by `engineering-head`, `mvp-scoper`

Find the smallest build that answers the riskiest question.

## Procedure
1. State the riskiest assumption the venture depends on.
2. Design the smallest artifact that could disprove it.
3. Cut everything that does not change what we learn.
4. Prefer a manual step over building automation before demand is proven.
5. Estimate time to first real user and treat it as the binding constraint.

## Output contract
`mvp-scope.md` → `workspace/<venture-id>/product/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/product.tsv`.

## Quality bar
- Scope tests the riskiest assumption
- Time to first user treated as the constraint
- The output states its confidence grade and names the evidence behind every load-bearing claim.
