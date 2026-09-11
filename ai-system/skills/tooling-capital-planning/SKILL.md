---
name: tooling-capital-planning
category: hardware
description: "Plan the money that gets locked into steel and inventory."
output: "tooling-capital-plan.md"
used_by:
  - chief-hardware-officer-agent
---

# Tooling Capital Planning

`hardware` · produces `tooling-capital-plan.md` · used by `chief-hardware-officer-agent`

Plan the money that gets locked into steel and inventory.

## Procedure
1. Estimate tooling cost per part and the total for the product.
2. Time the spend against the design freeze, not against the launch date.
3. Model inventory cash: the build is paid for long before units sell.
4. Include the cost of a tooling change if the design moves.
5. Compare against runway and flag the risk explicitly.

## Output contract
`tooling-capital-plan.md` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Spend timed against design freeze
- Inventory cash impact modelled against runway
- The output states its confidence grade and names the evidence behind every load-bearing claim.
