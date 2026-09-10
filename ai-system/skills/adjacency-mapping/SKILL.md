---
name: adjacency-mapping
category: council
description: "Find the markets and use cases nearest to where we already stand."
output: "adjacency-map.md"
used_by:
  - council-expansion-scout
---

# Adjacency Mapping

**Category:** `council` · **Output artifact:** `adjacency-map.md`

## What this skill does
Find the markets and use cases nearest to where we already stand.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `council-expansion-scout`.

## Procedure
1. Inventory the assets we are building: capability, data, relationships, and brand.
2. For each asset, list who else would value it.
3. Rate each adjacency by distance from our current position.
4. Identify what we would need to add to serve it.
5. Rank by value over distance, not by market size alone.

## Output contract
Write `adjacency-map.md` into `workspace/<venture-id>/council/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** adjacency-mapping
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
- Adjacencies derived from actual assets
- Ranked by value over distance
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `council` category
- An objection stated as an adjective rather than a concrete failure sequence.
- Criticism offered with no remedy at any cost level.
- Averaging two positions instead of testing which survives the evidence.
