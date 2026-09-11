---
name: instruction-pruning
category: improvement
description: "Remove instructions that no longer earn their tokens."
output: "pruning-record.md"
used_by:
  - knowledge-distiller
---

# Instruction Pruning

`improvement` · produces `pruning-record.md` · used by `knowledge-distiller`

Remove instructions that no longer earn their tokens.

## Procedure
1. Identify instructions that no failure in recent cycles relates to.
2. Identify instructions duplicated across layers.
3. Identify instructions superseded by a newer one.
4. Remove and record, rather than leaving them to dilute the rest.
5. Watch the next cycle for the failure returning, and restore if it does.

## Output contract
`pruning-record.md` → `workspace/<venture-id>/improvement/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/improvement.tsv`.

## Quality bar
- Removals watched for the failure returning
- Duplicated instructions consolidated
- The output states its confidence grade and names the evidence behind every load-bearing claim.
