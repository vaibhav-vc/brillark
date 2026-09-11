---
name: rework-attribution
category: orchestration
description: "Find out what caused work to be redone, so the cause can be fixed."
output: "rework-log.md"
used_by:
  - handoff-coordinator
---

# Rework Attribution

`orchestration` · produces `rework-log.md` · used by `handoff-coordinator`

Find out what caused work to be redone, so the cause can be fixed.

## Procedure
1. Record every rework event with the artifact and the trigger.
2. Classify the cause: unclear requirement, missing context, bad handoff, or genuine learning.
3. Separate valuable rework (learning) from waste.
4. Attribute to the process step, not to the agent.
5. Feed the pattern into retrospectives and agent scorecards.

## Output contract
`rework-log.md` → `workspace/<venture-id>/orchestration/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/orchestration.tsv`.

## Quality bar
- Learning distinguished from waste
- Attribution to process, not person
- The output states its confidence grade and names the evidence behind every load-bearing claim.
