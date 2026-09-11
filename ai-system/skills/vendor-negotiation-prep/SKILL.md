---
name: vendor-negotiation-prep
category: finance
description: "Arrive at a vendor negotiation with data instead of hope."
output: "negotiation-brief.md"
used_by:
  - cost-optimization-analyst
---

# Vendor Negotiation Prep

`finance` · produces `negotiation-brief.md` · used by `cost-optimization-analyst`

Arrive at a vendor negotiation with data instead of hope.

## Procedure
1. Pull actual usage against the contracted commitment.
2. Benchmark the price against alternatives and published rates.
3. Identify the leverage: renewal timing, volume growth, or a credible alternative.
4. Decide the walk-away position before the conversation.
5. Prepare the specific ask, with the concession you are willing to trade.

## Output contract
`negotiation-brief.md` → `workspace/<venture-id>/finance/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/finance.tsv`.

## Quality bar
- Walk-away position set in advance
- Ask supported by usage data
- The output states its confidence grade and names the evidence behind every load-bearing claim.
