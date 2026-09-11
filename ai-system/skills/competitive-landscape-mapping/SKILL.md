---
name: competitive-landscape-mapping
category: market
description: "Map everyone competing for the same budget, including the ones nobody counts."
output: "competitive-map.md"
used_by:
  - competitor-intel-analyst
---

# Competitive Landscape Mapping

`market` · produces `competitive-map.md` · used by `competitor-intel-analyst`

Map everyone competing for the same budget, including the ones nobody counts.

## Procedure
1. List direct competitors, indirect alternatives, and the status quo.
2. Include internal tools, spreadsheets, and doing nothing — usually the real incumbent.
3. Position each on the dimensions customers actually use to choose.
4. Note each competitor's apparent segment focus and business model.
5. Identify the whitespace and check whether it is empty for a good reason.

## Output contract
`competitive-map.md` → `workspace/<venture-id>/market/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/market.tsv`.

## Quality bar
- Status quo included as a competitor
- Whitespace tested for why it is empty
- The output states its confidence grade and names the evidence behind every load-bearing claim.
