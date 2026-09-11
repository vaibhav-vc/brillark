---
name: power-measurement-validation
category: hardware
description: "Measure the power system rather than quoting the datasheet."
output: "power-measurement.md"
used_by:
  - power-electronics-engineer
---

# Power Measurement Validation

`hardware` · produces `power-measurement.md` · used by `power-electronics-engineer`

Measure the power system rather than quoting the datasheet.

## Procedure
1. Measure efficiency across the full load range, not at one point.
2. Measure ripple and noise at the load, with correct probing technique.
3. Measure at temperature extremes and at input voltage extremes.
4. Measure start-up, shutdown, and fault recovery behaviour.
5. Compare against the design targets and record the margins.

## Output contract
`power-measurement.md` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Measured across load, temperature, and input range
- Probing technique appropriate for ripple measurement
- The output states its confidence grade and names the evidence behind every load-bearing claim.
