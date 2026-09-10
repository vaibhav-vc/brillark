---
name: schedule-optimisation
category: orchestration
description: "Improve the schedule without pretending work takes less time than it does."
output: "schedule.md"
used_by:
  - dependency-scheduler
---

# Schedule Optimisation

**Category:** `orchestration` · **Output artifact:** `schedule.md`

## What this skill does
Improve the schedule without pretending work takes less time than it does.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `dependency-scheduler`.

## Procedure
1. Attack the critical path first; optimising slack changes nothing.
2. Look for tasks that can start on partial inputs rather than complete ones.
3. Rebalance load away from over-committed agents.
4. Add buffer where variance is historically high, not uniformly.
5. Publish the revised schedule with what changed and why.

## Output contract
Write `schedule.md` into `workspace/<venture-id>/orchestration/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** schedule-optimisation
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
- Only critical-path changes claimed as gains
- Buffers placed by measured variance
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `orchestration` category
- Assigning a task to a group instead of one accountable agent.
- Reporting progress as a percentage instead of as artifacts that exist.
- Adding a review layer to fix a problem that a clearer definition of done would solve.
