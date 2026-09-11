---
name: high-speed-routing
category: hardware
description: "Route the fast signals so they still work when they arrive."
output: "routing-report.md"
used_by:
  - pcb-layout-designer
---

# High Speed Routing

`hardware` · produces `routing-report.md` · used by `pcb-layout-designer`

Route the fast signals so they still work when they arrive.

## Procedure
1. Route critical nets first, against the constraints from signal integrity.
2. Keep an unbroken reference plane under every high-speed trace.
3. Control impedance, spacing, and length matching to the stated budgets.
4. Avoid stubs, plane splits, and layer changes without a return via.
5. Verify against the constraint set rather than by eye.

## Output contract
`routing-report.md` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Unbroken reference plane under every fast trace
- Verified against the constraint set
- The output states its confidence grade and names the evidence behind every load-bearing claim.
