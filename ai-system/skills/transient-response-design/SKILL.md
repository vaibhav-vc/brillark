---
name: transient-response-design
category: hardware
description: "Make the rail hold up when the load steps."
output: "transient-report.md"
used_by:
  - power-electronics-engineer
---

# Transient Response Design

`hardware` · produces `transient-report.md` · used by `power-electronics-engineer`

Make the rail hold up when the load steps.

## Procedure
1. Characterise the real load step: magnitude, rate, and repetition.
2. Design the control loop for stability with margin across the load range.
3. Size output capacitance for the transient, not just for ripple.
4. Check stability with the real capacitor characteristics at temperature.
5. Measure the step response on hardware across the load range.

## Output contract
`transient-report.md` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Real load step characterised
- Stability checked with real capacitor behaviour
- The output states its confidence grade and names the evidence behind every load-bearing claim.
