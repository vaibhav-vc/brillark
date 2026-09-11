---
name: memory-write-standard
category: memory
description: "Enforce the structure that makes a memory retrievable months later."
output: "memory-record.json"
used_by:
  - context-memory-curator
---

# Memory Write Standard

`memory` · produces `memory-record.json` · used by `context-memory-curator`

Enforce the structure that makes a memory retrievable months later.

## Procedure
1. Classify the memory: episodic, semantic, procedural, or decision.
2. Write the claim as a standalone statement that needs no surrounding context.
3. Attach provenance: author agent, evidence, date, and confidence grade.
4. Add retrieval keys — entities, venture stage, and domain.
5. Validate against the schema and reject the write if it fails.

## Output contract
`memory-record.json` → `workspace/<venture-id>/memory/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/memory.tsv`.

## Quality bar
- Claim is standalone and context-free
- Provenance and confidence attached
- The output states its confidence grade and names the evidence behind every load-bearing claim.
