---
name: financial-controls-review
category: finance
description: "Check that money cannot leave the company without the right approvals."
output: "controls-review.md"
used_by:
  - cfo-agent
---

# Financial Controls Review

`finance` · produces `controls-review.md` · used by `cfo-agent`

Check that money cannot leave the company without the right approvals.

## Procedure
1. Map every path by which funds can be disbursed.
2. Check each path for approval thresholds and segregation of duties.
3. Test a sample of transactions for control compliance.
4. Identify paths with a single point of authorisation.
5. Report gaps with the specific control that would close each.

## Output contract
`controls-review.md` → `workspace/<venture-id>/finance/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/finance.tsv`.

## Quality bar
- All disbursement paths mapped
- Sample testing performed, not just policy review
- The output states its confidence grade and names the evidence behind every load-bearing claim.
