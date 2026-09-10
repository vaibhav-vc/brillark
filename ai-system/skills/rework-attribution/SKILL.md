---
name: rework-attribution
category: orchestration
description: "Find out what caused work to be redone, so the cause can be fixed."
output: "rework-log.md"
used_by:
  - handoff-coordinator
---

# Rework Attribution

**Category:** `orchestration` · **Output artifact:** `rework-log.md`

## What this skill does
Find out what caused work to be redone, so the cause can be fixed.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `handoff-coordinator`.

## Procedure
1. Record every rework event with the artifact and the trigger.
2. Classify the cause: unclear requirement, missing context, bad handoff, or genuine learning.
3. Separate valuable rework (learning) from waste.
4. Attribute to the process step, not to the agent.
5. Feed the pattern into retrospectives and agent scorecards.

## Output contract
Write `rework-log.md` into `workspace/<venture-id>/orchestration/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** rework-attribution
- **Author agent:** <agent-id>
- **Date:** <ISO-8601>
- **Confidence:** measured | sourced | benchmarked | estimated | guessed

## Summary
<the answer in three sentences or fewer>

## Body
<the substance produced by the procedure above>

## Evidence
| Claim | Source | Grade |
|---|---|---|

## Open questions
<what remains unknown, and who could answer it>

## Next action
<the single next step and its owner>
```

## Quality bar
- Learning distinguished from waste
- Attribution to process, not person
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `orchestration` category
- Assigning a task to a group instead of one accountable agent.
- Reporting progress as a percentage instead of as artifacts that exist.
- Adding a review layer to fix a problem that a clearer definition of done would solve.
