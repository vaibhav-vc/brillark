---
name: business-model-canvas
category: market
description: "Describe the whole business model on one page with evidence per block."
output: "business-model-canvas.md"
used_by:
  - business-head
  - business-model-canvas-agent
---

# Business Model Canvas

`market` · produces `business-model-canvas.md` · used by `business-head`, `business-model-canvas-agent`

Describe the whole business model on one page with evidence per block.

## Procedure
1. Fill all nine blocks: segments, value proposition, channels, relationships, revenue, resources, activities, partners, costs.
2. Tag each block as measured, sourced, or assumed.
3. Check that the revenue model fits the segment, the channel, and the cost structure.
4. Identify the riskiest block and the test that would validate it.
5. Log what changed since the last version and why.

## Output contract
`business-model-canvas.md` → `workspace/<venture-id>/market/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/market.tsv`.

## Quality bar
- Every block carries an evidence tag
- Riskiest block identified with a test
- The output states its confidence grade and names the evidence behind every load-bearing claim.
