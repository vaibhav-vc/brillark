---
name: metrics-tree-design
category: orchestration
description: "Connect the top-level goal to metrics each domain can actually move."
output: "metrics-tree.md"
used_by:
  - coo-agent
---

# Metrics Tree Design

**Category:** `orchestration` · **Output artifact:** `metrics-tree.md`

## What this skill does
Connect the top-level goal to metrics each domain can actually move.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `coo-agent`.

## Procedure
1. State the single top-level outcome metric.
2. Decompose it multiplicatively into drivers until each driver has an owner.
3. Check that moving a leaf metric provably moves the root.
4. Remove vanity metrics that no decision depends on.
5. Assign one owner per node and publish the tree.

## Output contract
Write `metrics-tree.md` into `workspace/<venture-id>/orchestration/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** metrics-tree-design
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
- Leaves provably connected to the root
- One owner per node
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `orchestration` category
- Assigning a task to a group instead of one accountable agent.
- Reporting progress as a percentage instead of as artifacts that exist.
- Adding a review layer to fix a problem that a clearer definition of done would solve.
