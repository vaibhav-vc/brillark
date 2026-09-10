---
name: dependency-resolution
category: orchestration
description: "Turn a set of tasks into a valid execution order."
output: "dependency-graph.yaml"
used_by:
  - dependency-scheduler
---

# Dependency Resolution

**Category:** `orchestration` · **Output artifact:** `dependency-graph.yaml`

## What this skill does
Turn a set of tasks into a valid execution order.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `dependency-scheduler`.

## Procedure
1. Build the directed graph of producer-to-consumer relationships.
2. Detect cycles and break them by splitting a task or relaxing an input.
3. Topologically sort the remaining graph.
4. Mark external dependencies that the organisation does not control.
5. Publish the order with the reason each edge exists.

## Output contract
Write `dependency-graph.yaml` into `workspace/<venture-id>/orchestration/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** dependency-resolution
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
- Graph is acyclic before execution
- External dependencies flagged separately
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `orchestration` category
- Assigning a task to a group instead of one accountable agent.
- Reporting progress as a percentage instead of as artifacts that exist.
- Adding a review layer to fix a problem that a clearer definition of done would solve.
