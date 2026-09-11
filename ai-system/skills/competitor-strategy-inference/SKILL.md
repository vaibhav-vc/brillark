---
name: competitor-strategy-inference
category: market
description: "Work out what a competitor is trying to do from observable signals."
output: "competitor-strategy.md"
used_by:
  - competitor-intel-analyst
---

# Competitor Strategy Inference

`market` · produces `competitor-strategy.md` · used by `competitor-intel-analyst`

Work out what a competitor is trying to do from observable signals.

## Procedure
1. Track hiring, pricing changes, positioning shifts, and product releases.
2. Infer the segment and motion they are optimising for.
3. Identify their constraint — what they cannot easily do.
4. Predict their next two moves and state your confidence.
5. Set watch indicators that would confirm or refute the inference.

## Output contract
`competitor-strategy.md` → `workspace/<venture-id>/market/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/market.tsv`.

## Quality bar
- Inference supported by observable signals
- Watch indicators defined
- The output states its confidence grade and names the evidence behind every load-bearing claim.
