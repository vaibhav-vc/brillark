---
name: thermal-path-analysis
category: hardware
description: "Follow the heat from junction to ambient."
output: "thermal-analysis.md"
used_by:
  - thermal-engineer
---

# Thermal Path Analysis

`hardware` · produces `thermal-analysis.md` · used by `thermal-engineer`

Follow the heat from junction to ambient.

## Procedure
1. Map each path: junction, case, interface, spreader, enclosure, ambient.
2. Compute thermal resistance for every step in the chain.
3. Identify the dominant resistance — usually an interface, not a material.
4. Model the sealed case if the product ships sealed.
5. Verify with thermocouples on real hardware at worst-case ambient.

## Output contract
`thermal-analysis.md` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Every step's resistance computed
- Verified on real hardware at worst case
- The output states its confidence grade and names the evidence behind every load-bearing claim.
