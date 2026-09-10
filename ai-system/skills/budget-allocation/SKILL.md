---
name: budget-allocation
category: orchestration
description: "Give every task an explicit ceiling on time, tokens, and spend."
output: "budget-allocation.md"
used_by:
  - dependency-scheduler
---

# Budget Allocation

**Category:** `orchestration` · **Output artifact:** `budget-allocation.md`

## What this skill does
Give every task an explicit ceiling on time, tokens, and spend.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `dependency-scheduler`.

## Procedure
1. Derive the total budget from the stage gate's allowance.
2. Allocate proportionally to expected value, not to requester insistence.
3. Set a hard ceiling per task and the action to take when it is hit.
4. Reserve a contingency pool held by the head, not distributed in advance.
5. Track consumption and report overruns before they compound.

## Output contract
Write `budget-allocation.md` into `workspace/<venture-id>/orchestration/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** budget-allocation
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
- Every task has a hard ceiling
- Contingency held centrally, not pre-spent
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `orchestration` category
- Assigning a task to a group instead of one accountable agent.
- Reporting progress as a percentage instead of as artifacts that exist.
- Adding a review layer to fix a problem that a clearer definition of done would solve.
