---
name: enclosure-architecture
category: hardware
description: "Decide how the housing splits, closes, and holds itself together."
output: "enclosure-architecture.md"
used_by:
  - enclosure-designer
---

# Enclosure Architecture

`hardware` · produces `enclosure-architecture.md` · used by `enclosure-designer`

Decide how the housing splits, closes, and holds itself together.

## Procedure
1. Choose split lines for tooling, assembly, and appearance together.
2. Decide the closure method: screws, snaps, welding, or adhesive, and why.
3. Plan the assembly order and what becomes inaccessible after each step.
4. Provide for service access where the product requires it.
5. Check the architecture against the sealing and thermal requirements.

## Output contract
`enclosure-architecture.md` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Split lines justified for tooling and appearance
- Post-assembly accessibility mapped
- The output states its confidence grade and names the evidence behind every load-bearing claim.
