---
name: converter-topology-selection
category: hardware
description: "Choose the right converter for each rail."
output: "converter-decision.md"
used_by:
  - power-electronics-engineer
---

# Converter Topology Selection

`hardware` · produces `converter-decision.md` · used by `power-electronics-engineer`

Choose the right converter for each rail.

## Procedure
1. Determine conversion ratio, load current, and transient requirement.
2. Compare linear, switching, and charge-pump options on efficiency, noise, and size.
3. Check noise sensitivity of the load before choosing a switcher.
4. Check thermal dissipation for the chosen topology at worst case.
5. Record the decision with the rejected options.

## Output contract
`converter-decision.md` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Load noise sensitivity assessed before choosing
- Thermal dissipation checked at worst case
- The output states its confidence grade and names the evidence behind every load-bearing claim.
