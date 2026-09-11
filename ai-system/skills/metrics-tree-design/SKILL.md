---
name: metrics-tree-design
category: orchestration
description: "Connect the top-level goal to metrics each domain can actually move."
output: "metrics-tree.md"
used_by:
  - coo-agent
---

# Metrics Tree Design

`orchestration` · produces `metrics-tree.md` · used by `coo-agent`

Connect the top-level goal to metrics each domain can actually move.

## Procedure
1. State the single top-level outcome metric.
2. Decompose it multiplicatively into drivers until each driver has an owner.
3. Check that moving a leaf metric provably moves the root.
4. Remove vanity metrics that no decision depends on.
5. Assign one owner per node and publish the tree.

## Output contract
`metrics-tree.md` → `workspace/<venture-id>/orchestration/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/orchestration.tsv`.

## Quality bar
- Leaves provably connected to the root
- One owner per node
- The output states its confidence grade and names the evidence behind every load-bearing claim.
