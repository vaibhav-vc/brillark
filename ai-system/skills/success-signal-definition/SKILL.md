---
name: success-signal-definition
category: product
description: "Define in advance what would show a feature worked."
output: "success-signal.md"
used_by:
  - product-requirements-agent
---

# Success Signal Definition

`product` · produces `success-signal.md` · used by `product-requirements-agent`

Define in advance what would show a feature worked.

## Procedure
1. Name the single metric that should move if this succeeds.
2. State the baseline and the threshold that counts as success.
3. Set the measurement window and the required sample.
4. Define what would show it failed, and what happens then.
5. Instrument before launch, not after.

## Output contract
`success-signal.md` → `workspace/<venture-id>/product/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/product.tsv`.

## Quality bar
- Threshold and window set in advance
- Failure response defined
- The output states its confidence grade and names the evidence behind every load-bearing claim.
