---
name: scope-boundary-definition
category: product
description: "Draw the line around what this work includes."
output: "scope.md"
used_by:
  - product-requirements-agent
---

# Scope Boundary Definition

`product` · produces `scope.md` · used by `product-requirements-agent`

Draw the line around what this work includes.

## Procedure
1. List what is in scope, concretely.
2. List what is out of scope and why each exclusion is safe.
3. Identify the adjacent work this depends on or enables.
4. Name the person who may change the boundary.
5. Record boundary changes as decisions, not as drift.

## Output contract
`scope.md` → `workspace/<venture-id>/product/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/product.tsv`.

## Quality bar
- Exclusions justified individually
- Boundary changes recorded as decisions
- The output states its confidence grade and names the evidence behind every load-bearing claim.
