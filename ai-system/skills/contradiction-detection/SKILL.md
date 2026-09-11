---
name: contradiction-detection
category: memory
description: "Catch conflicting claims across the knowledge graph as they arrive."
output: "contradiction-report.md"
used_by:
  - knowledge-graph-librarian
---

# Contradiction Detection

`memory` · produces `contradiction-report.md` · used by `knowledge-graph-librarian`

Catch conflicting claims across the knowledge graph as they arrive.

## Procedure
1. Define what constitutes a contradiction per claim type.
2. Check every incoming write against existing claims on the same entity.
3. Surface conflicts immediately rather than at consolidation time.
4. Include near-contradictions: same metric, different definition.
5. Route each detection to conflict resolution with both provenances attached.

## Output contract
`contradiction-report.md` → `workspace/<venture-id>/memory/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/memory.tsv`.

## Quality bar
- Detection at write time
- Metric-definition mismatches included
- The output states its confidence grade and names the evidence behind every load-bearing claim.
