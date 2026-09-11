---
name: bom-management
category: hardware
description: "Own the list of everything that goes into the product."
output: "bom.csv"
used_by:
  - electronics-component-engineer
---

# Bom Management

`hardware` · produces `bom.csv` · used by `electronics-component-engineer`

Own the list of everything that goes into the product.

## Procedure
1. Maintain one BOM of record with revision, reference designators, and approved parts.
2. Record manufacturer part numbers, not just descriptions.
3. Record an approved alternate for every line where one exists.
4. Keep the BOM synchronised with the schematic and the CAD assembly.
5. Cost the BOM at real volume with real packaging and minimums.

## Output contract
`bom.csv` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- One BOM of record synchronised with design
- Manufacturer part numbers, not descriptions
- The output states its confidence grade and names the evidence behind every load-bearing claim.
