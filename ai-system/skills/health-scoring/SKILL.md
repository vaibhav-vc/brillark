---
name: health-scoring
category: gtm
description: "Predict which customers are at risk before they leave."
output: "health-score-model.md"
used_by:
  - customer-success-agent
---

# Health Scoring

`gtm` · produces `health-score-model.md` · used by `customer-success-agent`

Predict which customers are at risk before they leave.

## Procedure
1. Build the score from behaviour: usage depth, breadth, and frequency.
2. Weight by what actually predicted past churn, not by intuition.
3. Validate the score against historical outcomes.
4. Define the intervention triggered at each score band.
5. Recalibrate as the product and the customer base change.

## Output contract
`health-score-model.md` → `workspace/<venture-id>/gtm/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/gtm.tsv`.

## Quality bar
- Weights validated against past churn
- Intervention defined per band
- The output states its confidence grade and names the evidence behind every load-bearing claim.
