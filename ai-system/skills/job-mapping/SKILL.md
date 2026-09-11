---
name: job-mapping
category: market
description: "Map every step of the job, including the parts our product never touches."
output: "job-map.md"
used_by:
  - jtbd-analyst
---

# Job Mapping

`market` · produces `job-map.md` · used by `jtbd-analyst`

Map every step of the job, including the parts our product never touches.

## Procedure
1. List the steps from the customer's first awareness of the need to their final outcome.
2. Mark friction, cost, and time at each step.
3. Identify the steps nobody currently serves well.
4. Check whether the biggest friction is inside or outside our product's scope.
5. Use the map to find where value is unclaimed.

## Output contract
`job-map.md` → `workspace/<venture-id>/market/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/market.tsv`.

## Quality bar
- Full job mapped beyond our product boundary
- Friction quantified per step
- The output states its confidence grade and names the evidence behind every load-bearing claim.
