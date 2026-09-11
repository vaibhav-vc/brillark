---
name: model-tier-assignment
category: efficiency
description: "Put each agent on the cheapest tier that holds quality."
output: "tier-assignment.md"
used_by:
  - model-router-tuner
  - token-efficiency-analyst
---

# Model Tier Assignment

`efficiency` · produces `tier-assignment.md` · used by `model-router-tuner`, `token-efficiency-analyst`

Put each agent on the cheapest tier that holds quality.

## Procedure
1. Classify the agent's work: mechanical, analytical, or judgement.
2. Run the golden cases at the candidate tier.
3. Compare quality against the rubric floor, not against the stronger tier's ceiling.
4. Assign the cheapest tier that clears the floor.
5. Keep judgement, arbitration, and Council work on the strongest tier.

## Output contract
`tier-assignment.md` → `workspace/<venture-id>/efficiency/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/efficiency.tsv`.

## Quality bar
- Quality verified against a rubric floor
- Judgement work never demoted
- The output states its confidence grade and names the evidence behind every load-bearing claim.
