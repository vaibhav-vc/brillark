---
name: total-cost-of-ownership
category: research
description: "Cost the whole life, not the sticker."
output: "tco-analysis.md"
used_by:
  - technology-evaluator
---

# Total Cost Of Ownership

`research` · produces `tco-analysis.md` · used by `technology-evaluator`

Cost the whole life, not the sticker.

## Procedure
1. Include licence, integration, migration, and training.
2. Include ongoing operation, support, and version upgrades.
3. Include the engineering time to maintain the integration.
4. Include the cost of leaving, and of staying on an unsupported version.
5. Compare candidates over a realistic horizon, not the first year.

## Output contract
`tco-analysis.md` → `workspace/<venture-id>/research/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/research.tsv`.

## Quality bar
- Exit and maintenance costs included
- Compared over a realistic horizon
- The output states its confidence grade and names the evidence behind every load-bearing claim.
