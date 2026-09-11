---
name: value-proposition-canvas
category: market
description: "Connect specific customer pains and gains to specific product capabilities."
output: "value-proposition.md"
used_by:
  - value-proposition-designer
---

# Value Proposition Canvas

`market` · produces `value-proposition.md` · used by `value-proposition-designer`

Connect specific customer pains and gains to specific product capabilities.

## Procedure
1. List the customer's jobs, pains, and gains from evidence.
2. List the product's pain relievers and gain creators.
3. Map each reliever to a named, evidenced pain; unmatched capabilities are scope to cut.
4. Identify pains with no reliever — these are the roadmap.
5. Rate the fit and state where it is weakest.

## Output contract
`value-proposition.md` → `workspace/<venture-id>/market/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/market.tsv`.

## Quality bar
- Unmatched capabilities identified as cuttable
- Unrelieved pains routed to the roadmap
- The output states its confidence grade and names the evidence behind every load-bearing claim.
