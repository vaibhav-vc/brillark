---
name: model-reconciliation
category: finance
description: "Check the model against reality and fix the model, not the reality."
output: "reconciliation.md"
used_by:
  - financial-model-builder
---

# Model Reconciliation

`finance` · produces `reconciliation.md` · used by `financial-model-builder`

Check the model against reality and fix the model, not the reality.

## Procedure
1. Pull actuals for the closed period from the source systems.
2. Compare each driver against its modelled value, not just the totals.
3. Explain every variance above the materiality threshold.
4. Correct the model's assumptions where the variance is structural rather than noise.
5. Record the reconciliation and the resulting model version.

## Output contract
`reconciliation.md` → `workspace/<venture-id>/finance/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/finance.tsv`.

## Quality bar
- Driver-level comparison, not totals only
- Structural variances corrected in the model
- The output states its confidence grade and names the evidence behind every load-bearing claim.
