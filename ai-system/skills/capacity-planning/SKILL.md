---
name: capacity-planning
category: engineering
description: "Ensure capacity exists before demand arrives."
output: "capacity-plan.md"
used_by:
  - performance-engineer
---

# Capacity Planning

`engineering` · produces `capacity-plan.md` · used by `performance-engineer`

Ensure capacity exists before demand arrives.

## Procedure
1. Project demand from the growth forecast, not from current load.
2. Identify the resource that saturates first.
3. Determine lead time to add capacity for each resource.
4. Set the trigger point that accounts for that lead time.
5. Re-plan when the growth forecast changes materially.

## Output contract
`capacity-plan.md` → `workspace/<venture-id>/engineering/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/engineering.tsv`.

## Quality bar
- Lead time built into the trigger point
- First saturating resource identified
- The output states its confidence grade and names the evidence behind every load-bearing claim.
