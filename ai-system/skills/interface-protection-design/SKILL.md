---
name: interface-protection-design
category: hardware
description: "Protect every connection to the outside world."
output: "protection-spec.md"
used_by:
  - pcb-schematic-designer
---

# Interface Protection Design

`hardware` · produces `protection-spec.md` · used by `pcb-schematic-designer`

Protect every connection to the outside world.

## Procedure
1. List every external interface and what a user can plug into it.
2. Protect against ESD, reverse polarity, overvoltage, and overcurrent per interface.
3. Check protection device ratings against the real fault, including hot-plug.
4. Ensure protection does not degrade signal integrity beyond the budget.
5. Verify with actual ESD and fault injection testing.

## Output contract
`protection-spec.md` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Every external interface protected
- Verified by real fault injection
- The output states its confidence grade and names the evidence behind every load-bearing claim.
