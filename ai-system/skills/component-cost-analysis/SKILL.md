---
name: component-cost-analysis
category: hardware
description: "Know what the parts really cost at the volume you will actually build."
output: "component-cost.md"
used_by:
  - electronics-component-engineer
---

# Component Cost Analysis

`hardware` · produces `component-cost.md` · used by `electronics-component-engineer`

Know what the parts really cost at the volume you will actually build.

## Procedure
1. Price at the real annual volume with real packaging and minimum quantities.
2. Include tariffs, freight, and finance cost of inventory.
3. Identify the parts that dominate cost and attack those first.
4. Compare against the target and report the gap honestly.
5. Re-price when volume assumptions change.

## Output contract
`component-cost.md` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Priced at real volume with real packaging
- Inventory and freight cost included
- The output states its confidence grade and names the evidence behind every load-bearing claim.
