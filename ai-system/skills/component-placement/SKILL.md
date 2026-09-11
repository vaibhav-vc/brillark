---
name: component-placement
category: hardware
description: "Place parts for the signal path, the mechanics, and the build."
output: "placement.md"
used_by:
  - pcb-layout-designer
---

# Component Placement

`hardware` · produces `placement.md` · used by `pcb-layout-designer`

Place parts for the signal path, the mechanics, and the build.

## Procedure
1. Place mechanically fixed items first: connectors, mounting, and user-facing parts.
2. Place by signal flow and keep critical paths short.
3. Keep switching and sensitive analogue apart, with defined return regions.
4. Place decoupling where it works, not where it fits after routing.
5. Check assembly and rework access, and component orientation consistency.

## Output contract
`placement.md` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Mechanically constrained parts placed first
- Decoupling placed for function, not convenience
- The output states its confidence grade and names the evidence behind every load-bearing claim.
