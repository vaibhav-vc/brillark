---
name: jtbd-analysis
category: market
description: "Frame the problem as the job a customer hires a solution to do."
output: "jtbd.md"
used_by:
  - business-head
  - jtbd-analyst
---

# Jtbd Analysis

`market` · produces `jtbd.md` · used by `business-head`, `jtbd-analyst`

Frame the problem as the job a customer hires a solution to do.

## Procedure
1. Write jobs as: when [situation], I want to [motivation], so I can [outcome].
2. Ground every job in a quoted customer statement.
3. Distinguish functional, emotional, and social dimensions of the job.
4. Identify what the customer currently hires and what they would have to fire.
5. Rank jobs by importance and current dissatisfaction.

## Output contract
`jtbd.md` → `workspace/<venture-id>/market/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/market.tsv`.

## Quality bar
- Every job traced to a quote
- Current solution being fired identified
- The output states its confidence grade and names the evidence behind every load-bearing claim.
