---
name: ground-and-return-path-design
category: hardware
description: "Design where the current comes back, not just where it goes."
output: "return-path-review.md"
used_by:
  - pcb-layout-designer
---

# Ground And Return Path Design

`hardware` · produces `return-path-review.md` · used by `pcb-layout-designer`

Design where the current comes back, not just where it goes.

## Procedure
1. Trace the return path for every critical signal.
2. Keep return paths continuous; a plane split under a fast edge is a fault.
3. Place return vias adjacent to every signal layer change.
4. Keep switching loops tight and away from sensitive circuits.
5. Review plane integrity as a distinct step, not as a by-product of routing.

## Output contract
`return-path-review.md` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Return path traced for every critical signal
- Plane integrity reviewed as its own step
- The output states its confidence grade and names the evidence behind every load-bearing claim.
