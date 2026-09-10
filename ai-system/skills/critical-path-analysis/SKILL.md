---
name: critical-path-analysis
category: orchestration
description: "Identify the chain of work that actually determines the finish date."
output: "critical-path.md"
used_by:
  - dependency-scheduler
---

# Critical Path Analysis

**Category:** `orchestration` · **Output artifact:** `critical-path.md`

## What this skill does
Identify the chain of work that actually determines the finish date.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `dependency-scheduler`.

## Procedure
1. Estimate duration for each task from historical throughput, not optimism.
2. Compute earliest and latest start for every node.
3. Identify the zero-slack chain and mark it as the critical path.
4. Name the single binding constraint on that path.
5. Re-compute whenever a task on the path slips.

## Output contract
Write `critical-path.md` into `workspace/<venture-id>/orchestration/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** critical-path-analysis
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
- Estimates drawn from actual throughput
- Binding constraint named explicitly
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `orchestration` category
- Assigning a task to a group instead of one accountable agent.
- Reporting progress as a percentage instead of as artifacts that exist.
- Adding a review layer to fix a problem that a clearer definition of done would solve.
