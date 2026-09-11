---
name: instruction-placement
category: improvement
description: "Put the instruction where it will actually be read."
output: "placement-record.md"
used_by:
  - knowledge-distiller
---

# Instruction Placement

`improvement` · produces `placement-record.md` · used by `knowledge-distiller`

Put the instruction where it will actually be read.

## Procedure
1. Identify the exact moment the agent needs it.
2. Place it in the skill step or guardrail active at that moment.
3. Avoid distant documents that are never loaded at the point of decision.
4. Check the placement is inside the context the agent actually receives.
5. Verify by tracing a real run.

## Output contract
`placement-record.md` → `workspace/<venture-id>/improvement/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/improvement.tsv`.

## Quality bar
- Placed inside the context the agent actually receives
- Verified by tracing a real run
- The output states its confidence grade and names the evidence behind every load-bearing claim.
