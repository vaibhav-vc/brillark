---
name: hiring-plan
category: people
description: "Sequence hiring against the constraint that is actually binding."
output: "hiring-plan.md"
used_by:
  - chro-agent
---

# Hiring Plan

`people` · produces `hiring-plan.md` · used by `chro-agent`

Sequence hiring against the constraint that is actually binding.

## Procedure
1. Identify the binding constraint on output today.
2. Determine whether hiring is the right fix, or whether process or tooling is.
3. Sequence roles by which constraint each removes.
4. Check the plan against the financial model and runway.
5. Define the trigger for each hire rather than fixed dates.

## Output contract
`hiring-plan.md` → `workspace/<venture-id>/people/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/people.tsv`.

## Quality bar
- Binding constraint identified first
- Plan reconciled with the financial model
- The output states its confidence grade and names the evidence behind every load-bearing claim.
