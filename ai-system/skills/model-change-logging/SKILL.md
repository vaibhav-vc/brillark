---
name: model-change-logging
category: market
description: "Record how the business model evolved and what caused each change."
output: "model-change-log.md"
used_by:
  - business-model-canvas-agent
---

# Model Change Logging

`market` · produces `model-change-log.md` · used by `business-model-canvas-agent`

Record how the business model evolved and what caused each change.

## Procedure
1. Record the previous state, the new state, and the date.
2. State the evidence or event that triggered the change.
3. Note which blocks were affected downstream.
4. Record what the change invalidates in existing plans.
5. Keep the history readable so the pattern of pivots is visible.

## Output contract
`model-change-log.md` → `workspace/<venture-id>/market/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/market.tsv`.

## Quality bar
- Trigger evidence recorded per change
- Downstream invalidations noted
- The output states its confidence grade and names the evidence behind every load-bearing claim.
