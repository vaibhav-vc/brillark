---
name: fit-analysis
category: market
description: "Assess honestly whether the offer matches the customer profile."
output: "fit-analysis.md"
used_by:
  - value-proposition-designer
---

# Fit Analysis

`market` · produces `fit-analysis.md` · used by `value-proposition-designer`

Assess honestly whether the offer matches the customer profile.

## Procedure
1. Compare the ranked pains against the ranked relievers.
2. Check that the top pain has a strong reliever, not just any pain.
3. Identify mismatches where we solve problems nobody ranked highly.
4. Rate the overall fit and name the weakest link.
5. Recommend either a product change or a segment change.

## Output contract
`fit-analysis.md` → `workspace/<venture-id>/market/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/market.tsv`.

## Quality bar
- Top-ranked pain addressed, not just any pain
- Weakest link named
- The output states its confidence grade and names the evidence behind every load-bearing claim.
