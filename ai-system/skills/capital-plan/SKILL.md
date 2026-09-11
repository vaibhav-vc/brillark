---
name: capital-plan
category: finance
description: "Decide how much money to raise, when, and against what milestone."
output: "capital-plan.md"
used_by:
  - cfo-agent
---

# Capital Plan

`finance` · produces `capital-plan.md` · used by `cfo-agent`

Decide how much money to raise, when, and against what milestone.

## Procedure
1. Define the milestone that justifies the next round.
2. Compute the capital needed to reach it plus a buffer for slippage.
3. Set the raise start date at least nine months before cash-out.
4. Model the dilution at plausible valuations.
5. Define the alternative if the raise does not happen.

## Output contract
`capital-plan.md` → `workspace/<venture-id>/finance/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/finance.tsv`.

## Quality bar
- Raise anchored to a milestone
- Non-raise alternative defined
- The output states its confidence grade and names the evidence behind every load-bearing claim.
