---
name: watchlist-design
category: research
description: "Decide what to watch, from what would break the plan."
output: "watchlist.md"
used_by:
  - horizon-scanner
---

# Watchlist Design

`research` · produces `watchlist.md` · used by `horizon-scanner`

Decide what to watch, from what would break the plan.

## Procedure
1. List the assumptions whose failure would invalidate the strategy.
2. For each, identify the earliest observable indicator.
3. Choose indicators that are measurable now, not in principle.
4. Assign a source and a check cadence to each.
5. Keep the list short enough to actually monitor.

## Output contract
`watchlist.md` → `workspace/<venture-id>/research/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/research.tsv`.

## Quality bar
- Indicators derived from plan-invalidating assumptions
- Each indicator measurable today
- The output states its confidence grade and names the evidence behind every load-bearing claim.
