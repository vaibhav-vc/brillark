---
name: schematic-capture
category: hardware
description: "Draw the circuit so it can be reviewed, built, and debugged."
output: "schematic"
used_by:
  - pcb-schematic-designer
---

# Schematic Capture

`hardware` · produces `schematic` · used by `pcb-schematic-designer`

Draw the circuit so it can be reviewed, built, and debugged.

## Procedure
1. Settle the block architecture before capturing symbols.
2. Organise sheets by function with clear inter-sheet connections.
3. Name every net meaningfully; unnamed nets make debugging guesswork.
4. Annotate values, tolerances, ratings, and anything non-obvious.
5. Keep the schematic readable — it is the document every later problem returns to.

## Output contract
`schematic` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Architecture settled before capture
- Every net meaningfully named
- The output states its confidence grade and names the evidence behind every load-bearing claim.
