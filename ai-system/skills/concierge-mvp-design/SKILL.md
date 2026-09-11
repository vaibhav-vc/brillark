---
name: concierge-mvp-design
category: product
description: "Deliver the outcome manually before building the machine."
output: "concierge-design.md"
used_by:
  - mvp-scoper
---

# Concierge Mvp Design

`product` · produces `concierge-design.md` · used by `mvp-scoper`

Deliver the outcome manually before building the machine.

## Procedure
1. Identify the outcome the customer wants, separate from the interface.
2. Design a manual process that delivers it end to end.
3. Set the volume ceiling at which manual becomes untenable.
4. Instrument what you learn from doing it by hand.
5. Automate only the steps the manual run proves are needed.

## Output contract
`concierge-design.md` → `workspace/<venture-id>/product/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/product.tsv`.

## Quality bar
- Outcome delivered before automation
- Manual run instrumented for learning
- The output states its confidence grade and names the evidence behind every load-bearing claim.
