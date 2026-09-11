---
name: adjacency-mapping
category: council
description: "Find the markets and use cases nearest to where we already stand."
output: "adjacency-map.md"
used_by:
  - council-expansion-scout
---

# Adjacency Mapping

`council` · produces `adjacency-map.md` · used by `council-expansion-scout`

Find the markets and use cases nearest to where we already stand.

## Procedure
1. Inventory the assets we are building: capability, data, relationships, and brand.
2. For each asset, list who else would value it.
3. Rate each adjacency by distance from our current position.
4. Identify what we would need to add to serve it.
5. Rank by value over distance, not by market size alone.

## Output contract
`adjacency-map.md` → `workspace/<venture-id>/council/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/council.tsv`.

## Quality bar
- Adjacencies derived from actual assets
- Ranked by value over distance
- The output states its confidence grade and names the evidence behind every load-bearing claim.
