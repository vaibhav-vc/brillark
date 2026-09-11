---
name: hardware-architecture
category: hardware
description: "Settle how mechanical, electrical, and firmware fit together before detail work starts."
output: "hw-architecture.md"
used_by:
  - hardware-head
---

# Hardware Architecture

`hardware` · produces `hw-architecture.md` · used by `hardware-head`

Settle how mechanical, electrical, and firmware fit together before detail work starts.

## Procedure
1. Define the block architecture across all three disciplines.
2. Define the interface contracts: volume, connectors, pin assignment, and protocols.
3. Identify the decisions that are expensive to reverse and make them deliberately.
4. Agree the build phase plan and what each phase proves.
5. Record the architecture so every discipline works from the same picture.

## Output contract
`hw-architecture.md` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Interface contracts defined across all three disciplines
- Expensive-to-reverse decisions made deliberately
- The output states its confidence grade and names the evidence behind every load-bearing claim.
