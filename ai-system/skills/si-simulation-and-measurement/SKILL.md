---
name: si-simulation-and-measurement
category: hardware
description: "Check the signals, first in simulation and then on the bench."
output: "si-report.md"
used_by:
  - signal-integrity-engineer
---

# Si Simulation And Measurement

`hardware` · produces `si-report.md` · used by `signal-integrity-engineer`

Check the signals, first in simulation and then on the bench.

## Procedure
1. Simulate the interfaces where a failure would cost a board spin.
2. Use real device models and the real stack-up, not generic ones.
3. Measure on the first build with adequate probe bandwidth.
4. Compare measurement to simulation and resolve differences.
5. Record the results per interface as build evidence.

## Output contract
`si-report.md` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Real device models and stack-up used
- Measurement compared against simulation
- The output states its confidence grade and names the evidence behind every load-bearing claim.
