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

**Category:** `memory` · **Output artifact:** `consolidation-report.md`

## What this skill does
Promote scattered episodic events into durable semantic and procedural memory.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `context-memory-curator`, `orchestration-head`.

## Procedure
1. Gather episodic records for the period or stage.
2. Identify facts confirmed by three or more independent episodes and promote them to semantic memory.
3. Identify sequences that repeatedly produced good outcomes and promote them to procedural memory.
4. Rewrite promoted memories as generalisations with their supporting episode links.
5. Expire or archive the episodic detail that is no longer load-bearing.

## Output contract
Write `consolidation-report.md` into `workspace/<venture-id>/memory/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** memory-consolidation
- **Author agent:** <agent-id>
- **Date:** <ISO-8601>
- **Confidence:** measured | sourced | benchmarked | estimated | guessed

## Summary
<the answer in three sentences or fewer>

## Body
<the substance produced by the procedure above>

## Evidence
| Claim | Source | Grade |
|---|---|---|

## Open questions
<what remains unknown, and who could answer it>

## Next action
<the single next step and its owner>
```

## Quality bar
- Promotions backed by repeated evidence
- Superseded episodic detail archived
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `memory` category
- Storing a claim without provenance, so nobody can later tell whether to trust it.
- Keeping two contradicting facts because resolving them is inconvenient.
- Treating a stale memory as current because it is well written.
