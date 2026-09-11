---
name: model-revision-control
category: hardware
description: "Keep geometry versions unambiguous."
output: "revision-log.md"
used_by:
  - cad-modeler
---

# Model Revision Control

`hardware` · produces `revision-log.md` · used by `cad-modeler`

Keep geometry versions unambiguous.

## Procedure
1. Version every released model and drawing with an immutable revision.
2. Record what changed and why on each revision.
3. Keep released revisions read-only; work in progress is separate.
4. Propagate a revision change to every consumer: drawings, BOM, and suppliers.
5. Never let two people hold different geometry for the same part number.

## Output contract
`revision-log.md` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Released revisions immutable
- Changes propagated to every consumer
- The output states its confidence grade and names the evidence behind every load-bearing claim.
