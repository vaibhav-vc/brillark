---
name: knowledge-graph-modeling
category: memory
description: "Design the entities and typed relationships that make cross-domain questions answerable."
output: "graph-model.md"
used_by:
  - knowledge-graph-librarian
---

# Knowledge Graph Modeling

`memory` · produces `graph-model.md` · used by `knowledge-graph-librarian`

Design the entities and typed relationships that make cross-domain questions answerable.

## Procedure
1. List the entity types the organisation actually reasons about.
2. Define typed relationships — 'competes with', 'depends on', 'evidences' — never 'related to'.
3. Attach each relationship to the artifact that justifies it.
4. Model time where it matters: relationships change and history is useful.
5. Validate by writing the five questions the graph must answer and testing them.

## Output contract
`graph-model.md` → `workspace/<venture-id>/memory/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/memory.tsv`.

## Quality bar
- All relationships typed
- Model validated against real questions
- The output states its confidence grade and names the evidence behind every load-bearing claim.
