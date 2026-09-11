---
name: alternative-comparison
category: market
description: "Compare against what the customer would actually do instead."
output: "alternative-comparison.md"
used_by:
  - value-proposition-designer
---

# Alternative Comparison

`market` · produces `alternative-comparison.md` · used by `value-proposition-designer`

Compare against what the customer would actually do instead.

## Procedure
1. Identify the real alternative for each segment, including doing nothing.
2. Compare on cost, effort, risk, and outcome — not on features.
3. Be honest where the alternative is better.
4. Quantify the net advantage.
5. State the conditions under which the alternative wins.

## Output contract
`alternative-comparison.md` → `workspace/<venture-id>/market/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/market.tsv`.

## Quality bar
- Doing nothing included
- Conditions where we lose stated
- The output states its confidence grade and names the evidence behind every load-bearing claim.
