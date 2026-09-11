---
name: variance-analysis
category: finance
description: "Explain the gap between budget and actual in a way that changes behaviour."
output: "variance-analysis.md"
used_by:
  - cfo-agent
---

# Variance Analysis

`finance` · produces `variance-analysis.md` · used by `cfo-agent`

Explain the gap between budget and actual in a way that changes behaviour.

## Procedure
1. Compare actual to budget by line, at the level where someone owns it.
2. Separate price, volume, and timing effects.
3. Investigate every variance above the materiality threshold.
4. Distinguish one-off from structural variances.
5. Assign each structural variance an owner and a corrective action.

## Output contract
`variance-analysis.md` → `workspace/<venture-id>/finance/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/finance.tsv`.

## Quality bar
- Price, volume, and timing separated
- Structural variances have owners
- The output states its confidence grade and names the evidence behind every load-bearing claim.
