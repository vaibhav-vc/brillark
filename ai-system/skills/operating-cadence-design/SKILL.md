---
name: operating-cadence-design
category: orchestration
description: "Design the rhythm of planning, review, and decision for the organisation."
output: "operating-cadence.md"
used_by:
  - coo-agent
---

# Operating Cadence Design

`orchestration` · produces `operating-cadence.md` · used by `coo-agent`

Design the rhythm of planning, review, and decision for the organisation.

## Procedure
1. List the decisions the organisation must make repeatedly and how often.
2. Design one ritual per recurring decision, and delete rituals with no decision.
3. Set the cadence from the decision's natural frequency, not from habit.
4. Define the input required and the output produced by each ritual.
5. Review quarterly and cut anything that stopped producing decisions.

## Output contract
`operating-cadence.md` → `workspace/<venture-id>/orchestration/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/orchestration.tsv`.

## Quality bar
- Every ritual has a decision output
- Rituals without decisions removed
- The output states its confidence grade and names the evidence behind every load-bearing claim.
