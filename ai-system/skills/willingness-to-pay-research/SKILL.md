---
name: willingness-to-pay-research
category: finance
description: "Find out what customers will actually pay, not what they say they like."
output: "wtp-research.md"
used_by:
  - pricing-strategist
---

# Willingness To Pay Research

`finance` · produces `wtp-research.md` · used by `pricing-strategist`

Find out what customers will actually pay, not what they say they like.

## Procedure
1. Screen for real buyers with budget authority.
2. Use forced trade-offs or price-sensitivity techniques rather than a single yes/no question.
3. Anchor against the alternative they use today and its cost.
4. Probe the budget line the purchase would come from.
5. Report the range and the segment differences, not a single number.

## Output contract
`wtp-research.md` → `workspace/<venture-id>/finance/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/finance.tsv`.

## Quality bar
- Forced trade-offs used, not stated intent
- Segment differences reported
- The output states its confidence grade and names the evidence behind every load-bearing claim.
