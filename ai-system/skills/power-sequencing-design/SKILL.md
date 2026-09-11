---
name: power-sequencing-design
category: hardware
description: "Specify what powers up when, and what every output does at reset."
output: "sequencing-spec.md"
used_by:
  - pcb-schematic-designer
---

# Power Sequencing Design

`hardware` · produces `sequencing-spec.md` · used by `pcb-schematic-designer`

Specify what powers up when, and what every output does at reset.

## Procedure
1. Collect each device's sequencing and ramp requirements from its datasheet.
2. Design the sequence to satisfy all of them, including at power-down.
3. Define the reset state of every output and configuration pin.
4. Design for brown-out and partial-rail conditions, not only clean power.
5. Verify the sequence on hardware with a scope, not from intent.

## Output contract
`sequencing-spec.md` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Power-down sequence specified, not just power-up
- Verified on hardware with measurement
- The output states its confidence grade and names the evidence behind every load-bearing claim.
