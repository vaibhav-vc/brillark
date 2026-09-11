---
name: ingress-protection-design
category: hardware
description: "Keep water and dust out, to the rating the product claims."
output: "ip-design.md"
used_by:
  - enclosure-designer
---

# Ingress Protection Design

`hardware` · produces `ip-design.md` · used by `enclosure-designer`

Keep water and dust out, to the rating the product claims.

## Procedure
1. Determine the required rating from real use, not from marketing.
2. Design a continuous compressed sealing path with no interruptions.
3. Specify gasket material, compression range, and groove geometry.
4. Seal every opening: connectors, buttons, vents, and fasteners.
5. Test to the rating on production-process parts, not on prototypes.

## Output contract
`ip-design.md` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Sealing path continuous with specified compression
- Tested on production-process parts
- The output states its confidence grade and names the evidence behind every load-bearing claim.
