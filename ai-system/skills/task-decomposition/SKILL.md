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

`orchestration` · produces `task-graph.yaml` · used by `orchestration-head`, `planning-decomposer`

Break an objective into tasks one agent can finish in one run with a checkable output.

## Procedure
1. Decompose by deliverable, not by activity — each node must produce an artifact.
2. Split any task an agent cannot finish in a single run.
3. Write the definition of done for each node before assigning it.
4. Name the inputs each node needs and where they come from.
5. Hand the resulting graph to dependency scheduling rather than ordering it yourself.

## Output contract
`task-graph.yaml` → `workspace/<venture-id>/orchestration/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/orchestration.tsv`.

## Quality bar
- Every node produces a named artifact
- Every node carries a definition of done
- The output states its confidence grade and names the evidence behind every load-bearing claim.
