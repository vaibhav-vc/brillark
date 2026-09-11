---
name: firmware-architecture
category: hardware
description: "Structure the embedded software so hardware changes do not rewrite the product."
output: "firmware-architecture.md"
used_by:
  - embedded-firmware-engineer
---

# Firmware Architecture

`hardware` · produces `firmware-architecture.md` · used by `embedded-firmware-engineer`

Structure the embedded software so hardware changes do not rewrite the product.

## Procedure
1. Separate hardware access, device logic, and product behaviour into layers.
2. Define the boot sequence, state machine, and failure behaviour explicitly.
3. Decide what runs in interrupt context and keep it minimal.
4. Plan memory and flash budget with headroom for updates.
5. Define logging and diagnostics before they are needed in the field.

## Output contract
`firmware-architecture.md` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Hardware access isolated behind an abstraction
- Memory and flash headroom planned
- The output states its confidence grade and names the evidence behind every load-bearing claim.
