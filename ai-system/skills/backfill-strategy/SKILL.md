---
name: backfill-strategy
category: engineering
description: "Populate new structures over existing data safely."
output: "backfill-plan.md"
used_by:
  - data-model-designer
---

# Backfill Strategy

`engineering` · produces `backfill-plan.md` · used by `data-model-designer`

Populate new structures over existing data safely.

## Procedure
1. Estimate the data volume and the time the backfill will take.
2. Design it to be resumable and idempotent.
3. Throttle to protect production load.
4. Track progress and verify a sample for correctness as it runs.
5. Define how new writes are handled while the backfill is in flight.

## Output contract
`backfill-plan.md` → `workspace/<venture-id>/engineering/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/engineering.tsv`.

## Quality bar
- Resumable and idempotent by design
- In-flight writes handled explicitly
- The output states its confidence grade and names the evidence behind every load-bearing claim.
