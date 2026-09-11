---
name: hardware-cost-rollup
category: hardware
description: "Know what a unit actually costs to make."
output: "cost-rollup.md"
used_by:
  - hardware-head
---

# Hardware Cost Rollup

`hardware` · produces `cost-rollup.md` · used by `hardware-head`

Know what a unit actually costs to make.

## Procedure
1. Roll up BOM, assembly labour, test time, and yield loss.
2. Include tooling amortisation and packaging.
3. Include freight, duty, and warranty reserve.
4. Compare against the target and identify the dominant contributors.
5. Re-roll at every build phase as real numbers replace estimates.

## Output contract
`cost-rollup.md` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Yield loss and warranty reserve included
- Re-rolled as estimates become real numbers
- The output states its confidence grade and names the evidence behind every load-bearing claim.
