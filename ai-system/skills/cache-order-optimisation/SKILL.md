---
name: cache-order-optimisation
category: efficiency
description: "Order the prompt so the stable part stays cacheable."
output: "cache-order.md"
used_by:
  - token-efficiency-analyst
---

# CAChe Order Optimisation

`efficiency` · produces `cache-order.md` · used by `token-efficiency-analyst`

Order the prompt so the stable part stays cacheable.

## Procedure
1. Place the most stable content first: base prompt, tier prompt, agent charter.
2. Place skill definitions next, since they change per task but not per turn.
3. Place the context package and the task last, where variability belongs.
4. Never interleave variable content into the stable prefix.
5. Verify cache reuse after any reordering.

## Output contract
`cache-order.md` → `workspace/<venture-id>/efficiency/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/efficiency.tsv`.

## Quality bar
- No variable content inside the stable prefix
- Cache reuse verified after reordering
- The output states its confidence grade and names the evidence behind every load-bearing claim.
