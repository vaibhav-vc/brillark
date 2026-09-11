---
name: cost-baseline
category: finance
description: "Establish what things currently cost before trying to optimise."
output: "cost-baseline.md"
used_by:
  - cost-optimization-analyst
---

# Cost Baseline

`finance` · produces `cost-baseline.md` · used by `cost-optimization-analyst`

Establish what things currently cost before trying to optimise.

## Procedure
1. Pull twelve months of actual spend by vendor and category.
2. Normalise for one-offs and seasonality.
3. Attribute costs to drivers — per customer, per request, per employee.
4. Identify the largest three lines and their growth rates.
5. Publish the baseline as the reference point for all savings claims.

## Output contract
`cost-baseline.md` → `workspace/<venture-id>/finance/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/finance.tsv`.

## Quality bar
- Costs attributed to drivers
- Baseline published before optimisation begins
- The output states its confidence grade and names the evidence behind every load-bearing claim.
