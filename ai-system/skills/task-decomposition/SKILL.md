---
name: task-decomposition
category: orchestration
description: "Break an objective into tasks one agent can finish in one run with a checkable output."
output: "task-graph.yaml"
used_by:
  - orchestration-head
  - planning-decomposer
---

# Task Decomposition

**Category:** `orchestration` · **Output artifact:** `task-graph.yaml`

## What this skill does
Break an objective into tasks one agent can finish in one run with a checkable output.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `orchestration-head`, `planning-decomposer`.

## Procedure
1. Decompose by deliverable, not by activity — each node must produce an artifact.
2. Split any task an agent cannot finish in a single run.
3. Write the definition of done for each node before assigning it.
4. Name the inputs each node needs and where they come from.
5. Hand the resulting graph to dependency scheduling rather than ordering it yourself.

## Output contract
Write `task-graph.yaml` into `workspace/<venture-id>/orchestration/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** task-decomposition
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
- Every node produces a named artifact
- Every node carries a definition of done
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `orchestration` category
- Assigning a task to a group instead of one accountable agent.
- Reporting progress as a percentage instead of as artifacts that exist.
- Adding a review layer to fix a problem that a clearer definition of done would solve.
