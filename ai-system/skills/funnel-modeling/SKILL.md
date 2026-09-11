---
name: funnel-modeling
category: finance
description: "Model the path from first contact to paying customer with real conversion rates."
output: "funnel-model.md"
used_by:
  - revenue-forecaster
---

# Funnel Modeling

`finance` · produces `funnel-model.md` · used by `revenue-forecaster`

Model the path from first contact to paying customer with real conversion rates.

## Procedure
1. Define each funnel stage by an observable event.
2. Measure conversion and time between stages from actual data.
3. Identify the stage with the largest drop and the largest delay.
4. Model how volume at the top translates to revenue at the bottom.
5. Flag stages where the sample is too small for the rate to be trusted.

## Output contract
`funnel-model.md` → `workspace/<venture-id>/finance/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/finance.tsv`.

## Quality bar
- Stages defined by observable events
- Small-sample rates flagged
- The output states its confidence grade and names the evidence behind every load-bearing claim.
