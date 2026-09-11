---
name: investor-targeting
category: finance
description: "Build a target list of investors who could actually say yes."
output: "investor-list.md"
used_by:
  - fundraising-strategist
---

# Investor Targeting

`finance` · produces `investor-list.md` · used by `fundraising-strategist`

Build a target list of investors who could actually say yes.

## Procedure
1. Filter by stage, cheque size, and sector thesis.
2. Check portfolio for conflicts and for pattern fit.
3. Identify the specific partner, not just the fund.
4. Find the warmest credible introduction path to each.
5. Rank by fit and prioritise, rather than contacting everyone at once.

## Output contract
`investor-list.md` → `workspace/<venture-id>/finance/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/finance.tsv`.

## Quality bar
- Targeted at partner level
- Conflicts checked in portfolio
- The output states its confidence grade and names the evidence behind every load-bearing claim.
