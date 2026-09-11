---
name: revenue-recognition-mapping
category: finance
description: "Determine when revenue may actually be recognised, not when cash arrives."
output: "rev-rec-policy.md"
used_by:
  - billing-systems-designer
---

# Revenue Recognition Mapping

`finance` · produces `rev-rec-policy.md` · used by `billing-systems-designer`

Determine when revenue may actually be recognised, not when cash arrives.

## Procedure
1. Identify each distinct performance obligation in the contract.
2. Determine when control transfers for each obligation.
3. Allocate the transaction price across obligations.
4. Define the recognition schedule and how it is automated.
5. Document the treatment and flag anything requiring professional advice.

## Output contract
`rev-rec-policy.md` → `workspace/<venture-id>/finance/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/finance.tsv`.

## Quality bar
- Obligations identified separately
- Advice-grade items flagged
- The output states its confidence grade and names the evidence behind every load-bearing claim.
