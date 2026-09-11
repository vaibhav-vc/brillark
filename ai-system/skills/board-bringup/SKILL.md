---
name: board-bringup
category: hardware
description: "Get the first board alive, in a defined order."
output: "bringup-log.md"
used_by:
  - embedded-firmware-engineer
---

# Board Bringup

`hardware` · produces `bringup-log.md` · used by `embedded-firmware-engineer`

Get the first board alive, in a defined order.

## Procedure
1. Check power rails with the processor held in reset before anything else.
2. Bring up one subsystem at a time, in dependency order.
3. Use a known-good test firmware rather than the product application.
4. Record every finding, including the ones fixed with a wire.
5. Feed every fix back into the schematic and layout for the next revision.

## Output contract
`bringup-log.md` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Power verified before releasing reset
- Every bodge fed back into the design
- The output states its confidence grade and names the evidence behind every load-bearing claim.
