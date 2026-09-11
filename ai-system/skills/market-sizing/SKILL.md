---
name: market-sizing
category: market
description: "Size a market bottom-up from countable inputs and sanity-check it top-down."
output: "market-sizing.md"
used_by:
  - market-researcher
---

# Market Sizing

`market` · produces `market-sizing.md` · used by `market-researcher`

Size a market bottom-up from countable inputs and sanity-check it top-down.

## Procedure
1. Define the buyer unit and count how many exist in the target geography.
2. Estimate realistic annual spend per buyer from observed pricing or budgets.
3. Multiply to TAM, narrow to SAM by segment fit, and to SOM by actual channel reach.
4. Cross-check against a top-down source and explain any gap larger than 2x.
5. Name the three inputs the estimate is most sensitive to and grade each source.

## Output contract
`market-sizing.md` → `workspace/<venture-id>/market/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/market.tsv`.

## Quality bar
- Every figure traceable to a counted input
- SOM justified by a real channel
- The output states its confidence grade and names the evidence behind every load-bearing claim.
