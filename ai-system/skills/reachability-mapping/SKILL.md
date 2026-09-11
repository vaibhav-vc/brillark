---
name: reachability-mapping
category: market
description: "Establish where the ICP actually is and what it costs to get there."
output: "reachability.md"
used_by:
  - icp-persona-builder
---

# Reachability Mapping

`market` · produces `reachability.md` · used by `icp-persona-builder`

Establish where the ICP actually is and what it costs to get there.

## Procedure
1. List the channels where this ICP demonstrably gathers or can be targeted.
2. Estimate reachable volume and cost per contact for each.
3. Check for gatekeepers and access constraints.
4. Test one channel cheaply before assuming access.
5. Report reachable volume against the SOM claim.

## Output contract
`reachability.md` → `workspace/<venture-id>/market/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/market.tsv`.

## Quality bar
- Access tested, not assumed
- Reachable volume compared to SOM
- The output states its confidence grade and names the evidence behind every load-bearing claim.
