---
name: cash-threshold-alerting
category: finance
description: "Make the cash position trigger action automatically."
output: "cash-alert-policy.md"
used_by:
  - burn-runway-analyst
---

# Cash Threshold Alerting

`finance` · produces `cash-alert-policy.md` · used by `burn-runway-analyst`

Make the cash position trigger action automatically.

## Procedure
1. Set thresholds in months of runway, not in currency.
2. Define the specific action each threshold triggers.
3. Assign the person or agent who executes on each trigger.
4. Wire the alert to the actual data source so it cannot be forgotten.
5. Test the alert once to confirm it fires.

## Output contract
`cash-alert-policy.md` → `workspace/<venture-id>/finance/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/finance.tsv`.

## Quality bar
- Thresholds in months of runway
- Alert tested, not just configured
- The output states its confidence grade and names the evidence behind every load-bearing claim.
