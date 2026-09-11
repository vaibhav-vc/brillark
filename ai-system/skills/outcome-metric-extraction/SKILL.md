---
name: outcome-metric-extraction
category: market
description: "Capture how the customer measures success, in their own terms."
output: "outcome-metrics.md"
used_by:
  - jtbd-analyst
---

# Outcome Metric Extraction

`market` · produces `outcome-metrics.md` · used by `jtbd-analyst`

Capture how the customer measures success, in their own terms.

## Procedure
1. Ask what number changes if the problem is solved.
2. Capture their unit, their baseline, and their target.
3. Distinguish the metric they are measured on from the one they care about.
4. Check whether our product can actually move that number.
5. Use it as the success criterion in the value proposition.

## Output contract
`outcome-metrics.md` → `workspace/<venture-id>/market/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/market.tsv`.

## Quality bar
- Metric expressed in the customer's own terms
- Product's ability to move it verified
- The output states its confidence grade and names the evidence behind every load-bearing claim.
