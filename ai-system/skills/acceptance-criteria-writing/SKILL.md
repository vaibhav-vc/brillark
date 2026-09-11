---
name: acceptance-criteria-writing
category: product
description: "Write conditions that decide unambiguously whether the work is done."
output: "acceptance-criteria.md"
used_by:
  - cpo-agent
  - product-requirements-agent
---

# Acceptance Criteria Writing

`product` · produces `acceptance-criteria.md` · used by `cpo-agent`, `product-requirements-agent`

Write conditions that decide unambiguously whether the work is done.

## Procedure
1. Express each criterion as given, when, then.
2. Cover the unhappy paths, the empty states, and the error states.
3. Make each criterion independently testable.
4. Remove anything subjective or unmeasurable.
5. Agree them with engineering and QA before build starts.

## Output contract
`acceptance-criteria.md` → `workspace/<venture-id>/product/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/product.tsv`.

## Quality bar
- Unhappy paths covered
- Agreed before build begins
- The output states its confidence grade and names the evidence behind every load-bearing claim.
