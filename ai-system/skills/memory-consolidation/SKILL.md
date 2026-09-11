---
name: memory-consolidation
category: memory
description: "Promote scattered episodic events into durable semantic and procedural memory."
output: "consolidation-report.md"
used_by:
  - context-memory-curator
  - orchestration-head
---

# Memory Consolidation

`memory` · produces `consolidation-report.md` · used by `context-memory-curator`, `orchestration-head`

Promote scattered episodic events into durable semantic and procedural memory.

## Procedure
1. Gather episodic records for the period or stage.
2. Identify facts confirmed by three or more independent episodes and promote them to semantic memory.
3. Identify sequences that repeatedly produced good outcomes and promote them to procedural memory.
4. Rewrite promoted memories as generalisations with their supporting episode links.
5. Expire or archive the episodic detail that is no longer load-bearing.

## Output contract
`consolidation-report.md` → `workspace/<venture-id>/memory/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/memory.tsv`.

## Quality bar
- Promotions backed by repeated evidence
- Superseded episodic detail archived
- The output states its confidence grade and names the evidence behind every load-bearing claim.
