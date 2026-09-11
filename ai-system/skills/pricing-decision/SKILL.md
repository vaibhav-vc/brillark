---
name: pricing-decision
category: finance
description: "Decide what to charge and be able to defend it from both directions."
output: "pricing-decision.md"
used_by:
  - finance-head
  - pricing-strategist
---

# Pricing Decision

`finance` · produces `pricing-decision.md` · used by `finance-head`, `pricing-strategist`

Decide what to charge and be able to defend it from both directions.

## Procedure
1. Establish the floor from unit economics and the ceiling from value delivered.
2. Gather willingness-to-pay evidence from real prospects.
3. Choose the position within the band and state the reason.
4. Model the revenue effect at the chosen point, including volume response.
5. Define the migration path for existing customers before changing anything.

## Output contract
`pricing-decision.md` → `workspace/<venture-id>/finance/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/finance.tsv`.

## Quality bar
- Floor and ceiling both established
- Migration path defined before change
- The output states its confidence grade and names the evidence behind every load-bearing claim.
