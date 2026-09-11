---
name: hardware-abstraction-design
category: hardware
description: "Keep the product code independent of the parts underneath it."
output: "hal-spec.md"
used_by:
  - embedded-firmware-engineer
---

# Hardware Abstraction Design

`hardware` · produces `hal-spec.md` · used by `embedded-firmware-engineer`

Keep the product code independent of the parts underneath it.

## Procedure
1. Define the interface the product logic needs, not the one the chip offers.
2. Put every register access behind that interface.
3. Make the abstraction testable without hardware present.
4. Keep timing-critical behaviour visible rather than hidden in the abstraction.
5. Verify a component substitution touches only the driver layer.

## Output contract
`hal-spec.md` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Interface defined from product need, not chip features
- Component substitution confined to the driver layer
- The output states its confidence grade and names the evidence behind every load-bearing claim.
