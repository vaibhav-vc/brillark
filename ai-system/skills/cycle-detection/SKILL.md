---
name: cycle-detection
category: orchestration
description: "Find circular dependencies before they deadlock execution."
output: "cycle-report.md"
used_by:
  - dependency-scheduler
---

# Cycle Detection

**Category:** `orchestration` · **Output artifact:** `cycle-report.md`

## What this skill does
Find circular dependencies before they deadlock execution.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `dependency-scheduler`.

## Procedure
1. Traverse the graph depth-first, tracking the active path.
2. Report every cycle with the full loop, not just the closing edge.
3. Classify each cycle: genuine mutual need, or accidental over-specification.
4. Propose a break: split a task, stub an interface, or stage the work.
5. Re-run detection after the fix to confirm the graph is acyclic.

## Output contract
Write `cycle-report.md` into `workspace/<venture-id>/orchestration/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** cycle-detection
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
- Full loops reported, not single edges
- Re-verified acyclic after the break
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `orchestration` category
- Assigning a task to a group instead of one accountable agent.
- Reporting progress as a percentage instead of as artifacts that exist.
- Adding a review layer to fix a problem that a clearer definition of done would solve.
