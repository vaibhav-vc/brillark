---
name: entity-resolution
category: memory
description: "Make sure one real-world thing is one node in the knowledge graph."
output: "entity-resolution-report.md"
used_by:
  - knowledge-graph-librarian
---

# Entity Resolution

`memory` · produces `entity-resolution-report.md` · used by `knowledge-graph-librarian`

Make sure one real-world thing is one node in the knowledge graph.

## Procedure
1. Normalise names, aliases, and identifiers before comparison.
2. Compare candidate matches on stable attributes, not on name similarity alone.
3. Merge duplicates and redirect all references to the canonical node.
4. Record the merge so it can be reversed if wrong.
5. Flag ambiguous cases for human or head review instead of guessing.

## Output contract
`entity-resolution-report.md` → `workspace/<venture-id>/memory/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/memory.tsv`.

## Quality bar
- Merges are reversible
- Ambiguous matches escalated, not guessed
- The output states its confidence grade and names the evidence behind every load-bearing claim.
