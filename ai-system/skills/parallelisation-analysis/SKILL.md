---
name: parallelisation-analysis
category: orchestration
description: "Find what can run at the same time and what genuinely cannot."
output: "parallelisation-plan.md"
used_by:
  - planning-decomposer
  - workflow-optimizer
---

# Parallelisation Analysis

**Category:** `orchestration` · **Output artifact:** `parallelisation-plan.md`

## What this skill does
Find what can run at the same time and what genuinely cannot.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `planning-decomposer`, `workflow-optimizer`.

## Procedure
1. Map each task's true inputs; a dependency exists only where an output is consumed.
2. Separate hard dependencies from habitual sequencing.
3. Identify shared mutable state that would make parallel runs unsafe.
4. Group independent branches into parallel tracks with separate owners.
5. Estimate the schedule gain, and drop parallelisation that adds coordination cost for little gain.

## Output contract
Write `parallelisation-plan.md` into `workspace/<venture-id>/orchestration/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** parallelisation-analysis
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
- Only true input dependencies retained
- Shared-state hazards identified
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `orchestration` category
- Assigning a task to a group instead of one accountable agent.
- Reporting progress as a percentage instead of as artifacts that exist.
- Adding a review layer to fix a problem that a clearer definition of done would solve.
