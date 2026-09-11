---
name: fastener-and-joint-design
category: hardware
description: "Choose how parts are held together and whether they can come apart."
output: "joint-spec.md"
used_by:
  - mechanical-engineer
---

# Fastener And Joint Design

`hardware` · produces `joint-spec.md` · used by `mechanical-engineer`

Choose how parts are held together and whether they can come apart.

## Procedure
1. Select the joint for the load, the material, and the number of assembly cycles.
2. Specify torque, thread engagement, and any locking feature.
3. Design boss and rib geometry for the actual fastener and process.
4. Decide deliberately whether the joint must be serviceable.
5. Check the joint after thermal cycling and vibration, not just at build.

## Output contract
`joint-spec.md` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Torque and thread engagement specified
- Serviceability decided deliberately
- The output states its confidence grade and names the evidence behind every load-bearing claim.
