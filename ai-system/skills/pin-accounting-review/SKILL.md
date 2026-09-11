---
name: pin-accounting-review
category: hardware
description: "Account for every pin on every part."
output: "pin-review.md"
used_by:
  - pcb-schematic-designer
---

# Pin Accounting Review

`hardware` · produces `pin-review.md` · used by `pcb-schematic-designer`

Account for every pin on every part.

## Procedure
1. List every pin of every device and its intended connection.
2. Justify every unconnected pin explicitly against the datasheet.
3. Check pull-ups, pull-downs, and strapping against required boot states.
4. Check every supply and ground pin is connected and decoupled.
5. Have a second engineer repeat the check independently.

## Output contract
`pin-review.md` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Unconnected pins justified against the datasheet
- Independently repeated by a second engineer
- The output states its confidence grade and names the evidence behind every load-bearing claim.
