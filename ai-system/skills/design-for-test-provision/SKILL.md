---
name: design-for-test-provision
category: hardware
description: "Build in the access debugging and production will need."
output: "dft-spec.md"
used_by:
  - pcb-schematic-designer
---

# Design For Test Provision

`hardware` · produces `dft-spec.md` · used by `pcb-schematic-designer`

Build in the access debugging and production will need.

## Procedure
1. Add test points on power rails, clocks, resets, and critical signals.
2. Provide a debug interface and keep it accessible after assembly.
3. Provide test access for in-circuit or boundary-scan coverage.
4. Design the board so a failing unit can be diagnosed, not just rejected.
5. Agree access requirements with production test before layout.

## Output contract
`dft-spec.md` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Test access agreed before layout
- Debug interface accessible after assembly
- The output states its confidence grade and names the evidence behind every load-bearing claim.
