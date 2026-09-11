---
name: impedance-planning
category: hardware
description: "Set impedance targets and make them achievable."
output: "impedance-plan.md"
used_by:
  - signal-integrity-engineer
---

# Impedance Planning

`hardware` · produces `impedance-plan.md` · used by `signal-integrity-engineer`

Set impedance targets and make them achievable.

## Procedure
1. Identify every interface with an impedance requirement.
2. Compute trace geometry from the real stack-up and material properties.
3. Check the geometry is manufacturable at the fabricator's tolerance.
4. Specify the impedance requirement and test coupon in the fab package.
5. Verify on fabricated boards rather than assuming.

## Output contract
`impedance-plan.md` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Geometry computed from the real stack-up
- Verified on fabricated boards
- The output states its confidence grade and names the evidence behind every load-bearing claim.
