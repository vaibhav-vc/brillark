---
name: power-protection-design
category: hardware
description: "Define what happens when power goes wrong."
output: "power-protection-spec.md"
used_by:
  - power-electronics-engineer
---

# Power Protection Design

`hardware` · produces `power-protection-spec.md` · used by `power-electronics-engineer`

Define what happens when power goes wrong.

## Procedure
1. Specify behaviour for reverse polarity, overvoltage, overcurrent, and short circuit.
2. Design inrush limiting for hot insertion and capacitive loads.
3. Define brown-out behaviour and ensure the system recovers cleanly.
4. Check protection component ratings against the real fault energy.
5. Test every fault mode on hardware rather than reasoning about it.

## Output contract
`power-protection-spec.md` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Every fault mode has specified behaviour
- All fault modes tested on hardware
- The output states its confidence grade and names the evidence behind every load-bearing claim.
