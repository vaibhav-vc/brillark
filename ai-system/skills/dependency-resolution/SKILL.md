---
name: dependency-resolution
category: orchestration
description: "Turn a set of tasks into a valid execution order."
output: "dependency-graph.yaml"
used_by:
  - dependency-scheduler
---

# Dependency Resolution

`orchestration` · produces `dependency-graph.yaml` · used by `dependency-scheduler`

Turn a set of tasks into a valid execution order.

## Procedure
1. Build the directed graph of producer-to-consumer relationships.
2. Detect cycles and break them by splitting a task or relaxing an input.
3. Topologically sort the remaining graph.
4. Mark external dependencies that the organisation does not control.
5. Publish the order with the reason each edge exists.

## Output contract
`dependency-graph.yaml` → `workspace/<venture-id>/orchestration/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/orchestration.tsv`.

## Quality bar
- Graph is acyclic before execution
- External dependencies flagged separately
- The output states its confidence grade and names the evidence behind every load-bearing claim.
