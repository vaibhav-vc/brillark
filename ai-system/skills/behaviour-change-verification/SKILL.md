---
name: behaviour-change-verification
category: improvement
description: "Check the instruction actually changed what agents do."
output: "verification-record.md"
used_by:
  - knowledge-distiller
---

# Behaviour Change Verification

`improvement` · produces `verification-record.md` · used by `knowledge-distiller`

Check the instruction actually changed what agents do.

## Procedure
1. Record the behaviour before the instruction was added.
2. Sample runs after the change and check for the behaviour.
3. Distinguish the instruction being followed from the outcome improving.
4. If nothing changed, the instruction is in the wrong place or too vague.
5. Record the verification and act on a null result.

## Output contract
`verification-record.md` → `workspace/<venture-id>/improvement/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/improvement.tsv`.

## Quality bar
- Following distinguished from outcome improvement
- Null results acted on, not filed
- The output states its confidence grade and names the evidence behind every load-bearing claim.
