---
name: scope-cut-justification
category: product
description: "Record why something was cut so the decision survives argument."
output: "scope-cuts.md"
used_by:
  - mvp-scoper
---

# Scope Cut Justification

`product` · produces `scope-cuts.md` · used by `mvp-scoper`

Record why something was cut so the decision survives argument.

## Procedure
1. State what was cut and who asked for it.
2. State the criterion applied: does it change what we learn now?
3. Record the trigger that would bring it back.
4. Record the risk accepted by cutting it.
5. Publish so the cut does not have to be re-argued weekly.

## Output contract
`scope-cuts.md` → `workspace/<venture-id>/product/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/product.tsv`.

## Quality bar
- Revisit trigger recorded per cut
- Accepted risk stated
- The output states its confidence grade and names the evidence behind every load-bearing claim.
