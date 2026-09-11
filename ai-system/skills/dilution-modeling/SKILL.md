---
name: dilution-modeling
category: finance
description: "Show what a financing actually costs in ownership."
output: "dilution-model.md"
used_by:
  - cap-table-steward
  - fundraising-strategist
---

# Dilution Modeling

`finance` · produces `dilution-model.md` · used by `cap-table-steward`, `fundraising-strategist`

Show what a financing actually costs in ownership.

## Procedure
1. Start from the current fully diluted cap table.
2. Model the new money, the pre-money valuation, and the option pool top-up.
3. Show whether the pool is created pre- or post-money and what that costs founders.
4. Project through the next round to show cumulative dilution.
5. Present ownership percentages, not just dollar values.

## Output contract
`dilution-model.md` → `workspace/<venture-id>/finance/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/finance.tsv`.

## Quality bar
- Pool timing effect made explicit
- Cumulative dilution projected forward
- The output states its confidence grade and names the evidence behind every load-bearing claim.
