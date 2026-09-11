---
name: dunning-flow-design
category: finance
description: "Recover failed payments without losing the customer."
output: "dunning-flow.md"
used_by:
  - billing-systems-designer
---

# Dunning Flow Design

`finance` · produces `dunning-flow.md` · used by `billing-systems-designer`

Recover failed payments without losing the customer.

## Procedure
1. Map the failure reasons and which are recoverable.
2. Design the retry schedule around bank behaviour, not arbitrary intervals.
3. Write the customer communication for each stage, escalating in clarity not aggression.
4. Define the grace period and exactly what access is retained.
5. Measure recovery rate by failure reason and tune the sequence.

## Output contract
`dunning-flow.md` → `workspace/<venture-id>/finance/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/finance.tsv`.

## Quality bar
- Retry schedule matches failure reason
- Recovery measured by reason
- The output states its confidence grade and names the evidence behind every load-bearing claim.
