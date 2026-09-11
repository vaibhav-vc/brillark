---
name: failure-cost-estimation
category: improvement
description: "Put a number on what each failure pattern costs."
output: "failure-costs.md"
used_by:
  - failure-miner
---

# Failure Cost Estimation

`improvement` · produces `failure-costs.md` · used by `failure-miner`

Put a number on what each failure pattern costs.

## Procedure
1. Count the rework hours or agent runs consumed.
2. Add the delay imposed on downstream work.
3. Add the cost of decisions made on corrupted information.
4. Note where the cost is unknown rather than assuming it is small.
5. Rank patterns by total cost per cycle.

## Output contract
`failure-costs.md` → `workspace/<venture-id>/improvement/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/improvement.tsv`.

## Quality bar
- Decision-corruption cost included
- Unknown costs marked rather than assumed small
- The output states its confidence grade and names the evidence behind every load-bearing claim.
