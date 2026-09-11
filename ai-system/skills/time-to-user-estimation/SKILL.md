---
name: time-to-user-estimation
category: product
description: "Estimate honestly when a real user will touch this."
output: "time-to-user.md"
used_by:
  - mvp-scoper
---

# Time To User Estimation

`product` · produces `time-to-user.md` · used by `mvp-scoper`

Estimate honestly when a real user will touch this.

## Procedure
1. Break the path to first user into its required steps.
2. Estimate each from historical throughput, not optimism.
3. Include the non-build steps: review, deploy, and access.
4. State the estimate as a range with the assumptions behind each end.
5. Track the actual against the estimate to calibrate the next one.

## Output contract
`time-to-user.md` → `workspace/<venture-id>/product/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/product.tsv`.

## Quality bar
- Non-build steps included
- Estimate calibrated against past actuals
- The output states its confidence grade and names the evidence behind every load-bearing claim.
