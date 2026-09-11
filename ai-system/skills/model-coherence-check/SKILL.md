---
name: model-coherence-check
category: market
description: "Check that the parts of the business model actually fit together."
output: "coherence-check.md"
used_by:
  - business-model-canvas-agent
---

# Model Coherence Check

`market` · produces `coherence-check.md` · used by `business-model-canvas-agent`

Check that the parts of the business model actually fit together.

## Procedure
1. Test whether the channel can reach the stated segment at the stated cost.
2. Test whether the price supports the cost structure and the sales motion.
3. Test whether the key resources exist or can be acquired in time.
4. Test whether the partners have an incentive to participate.
5. Report each incoherence with the two blocks that conflict.

## Output contract
`coherence-check.md` → `workspace/<venture-id>/market/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/market.tsv`.

## Quality bar
- Conflicts named as specific block pairs
- Motion-to-price fit tested
- The output states its confidence grade and names the evidence behind every load-bearing claim.
