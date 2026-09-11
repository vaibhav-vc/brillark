---
name: opportunity-scoring
category: market
description: "Rank problems by how much unclaimed value they contain."
output: "opportunity-scores.md"
used_by:
  - jtbd-analyst
---

# Opportunity Scoring

`market` · produces `opportunity-scores.md` · used by `jtbd-analyst`

Rank problems by how much unclaimed value they contain.

## Procedure
1. Score each job or outcome on importance and current satisfaction.
2. Compute opportunity as importance plus unmet gap.
3. Weight by the number of customers who share it.
4. Cross-check high scores against willingness to pay.
5. Rank and recommend the top two, with the reason the rest wait.

## Output contract
`opportunity-scores.md` → `workspace/<venture-id>/market/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/market.tsv`.

## Quality bar
- Scores validated against willingness to pay
- Ranked with explicit deferrals
- The output states its confidence grade and names the evidence behind every load-bearing claim.
