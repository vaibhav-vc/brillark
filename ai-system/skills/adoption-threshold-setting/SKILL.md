---
name: adoption-threshold-setting
category: improvement
description: "Decide in advance what would justify adopting the change."
output: "adoption-threshold.md"
used_by:
  - improvement-head
  - prompt-optimizer
---

# Adoption Threshold Setting

`improvement` · produces `adoption-threshold.md` · used by `improvement-head`, `prompt-optimizer`

Decide in advance what would justify adopting the change.

## Procedure
1. Set the minimum improvement worth the churn of changing.
2. Set the maximum acceptable regression elsewhere.
3. Define the sample the result must be based on.
4. Record the threshold before seeing any result.
5. Refuse to move the threshold after the fact.

## Output contract
`adoption-threshold.md` → `workspace/<venture-id>/improvement/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/improvement.tsv`.

## Quality bar
- Threshold recorded before results are seen
- Post-hoc threshold changes refused
- The output states its confidence grade and names the evidence behind every load-bearing claim.
