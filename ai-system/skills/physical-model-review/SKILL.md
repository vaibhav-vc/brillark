---
name: physical-model-review
category: hardware
description: "Judge form with a physical object, because screens flatter shapes that fail in the hand."
output: "model-review.md"
used_by:
  - industrial-designer
---

# Physical Model Review

`hardware` · produces `model-review.md` · used by `industrial-designer`

Judge form with a physical object, because screens flatter shapes that fail in the hand.

## Procedure
1. Build at full scale in a material with representative weight where possible.
2. Hold, carry, and operate it in the real context.
3. Check the details screens hide: edge sharpness, parting lines, and grip transitions.
4. Get reactions from people outside the design team.
5. Record what changed as a result, so the model earned its cost.

## Output contract
`model-review.md` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Reviewed at full scale in real context
- Changes recorded against the model
- The output states its confidence grade and names the evidence behind every load-bearing claim.
