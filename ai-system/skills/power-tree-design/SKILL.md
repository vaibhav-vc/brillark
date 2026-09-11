---
name: power-tree-design
category: hardware
description: "Lay out every rail, its source, and its headroom."
output: "power-tree.md"
used_by:
  - power-electronics-engineer
---

# Power Tree Design

`hardware` · produces `power-tree.md` · used by `power-electronics-engineer`

Lay out every rail, its source, and its headroom.

## Procedure
1. List each rail with its voltage, tolerance, and measured or datasheet load.
2. Add real headroom for transients and future scope, and state it.
3. Choose the conversion path for each rail and its efficiency.
4. Check sequencing and dependencies between rails.
5. Compute total input power and confirm the source can supply it.

## Output contract
`power-tree.md` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Headroom stated explicitly per rail
- Input source verified against total demand
- The output states its confidence grade and names the evidence behind every load-bearing claim.
