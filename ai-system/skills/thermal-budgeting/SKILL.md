---
name: thermal-budgeting
category: hardware
description: "Account for every watt before designing the cooling."
output: "thermal-budget.md"
used_by:
  - thermal-engineer
---

# Thermal Budgeting

`hardware` · produces `thermal-budget.md` · used by `thermal-engineer`

Account for every watt before designing the cooling.

## Procedure
1. List every dissipating component with its real duty-cycle power.
2. Identify the worst-case operating scenario, not the typical one.
3. State each component's junction and case temperature limits.
4. Compare total dissipation against what the enclosure can shed.
5. Publish the budget so electrical and mechanical design work from one number.

## Output contract
`thermal-budget.md` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Power at real duty cycle, not nameplate
- Worst-case scenario used, not typical
- The output states its confidence grade and names the evidence behind every load-bearing claim.
