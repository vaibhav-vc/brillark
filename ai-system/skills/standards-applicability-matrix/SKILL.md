---
name: standards-applicability-matrix
category: hardware
description: "Know which rules apply before designing, not before submitting."
output: "standards-matrix.md"
used_by:
  - compliance-emc-engineer
---

# Standards Applicability Matrix

`hardware` · produces `standards-matrix.md` · used by `compliance-emc-engineer`

Know which rules apply before designing, not before submitting.

## Procedure
1. List target markets and the product's classification in each.
2. Identify emissions, immunity, safety, radio, and environmental standards per market.
3. Record which apply, which do not, and why.
4. Identify the test regime and lead time for each.
5. Re-check when a market or a product function is added.

## Output contract
`standards-matrix.md` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Non-applicability recorded with a reason
- Test lead times identified early
- The output states its confidence grade and names the evidence behind every load-bearing claim.
