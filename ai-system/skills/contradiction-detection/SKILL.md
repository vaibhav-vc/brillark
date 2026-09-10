---
name: contradiction-detection
category: memory
description: "Catch conflicting claims across the knowledge graph as they arrive."
output: "contradiction-report.md"
used_by:
  - knowledge-graph-librarian
---

# Contradiction Detection

**Category:** `memory` · **Output artifact:** `contradiction-report.md`

## What this skill does
Catch conflicting claims across the knowledge graph as they arrive.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `knowledge-graph-librarian`.

## Procedure
1. Define what constitutes a contradiction per claim type.
2. Check every incoming write against existing claims on the same entity.
3. Surface conflicts immediately rather than at consolidation time.
4. Include near-contradictions: same metric, different definition.
5. Route each detection to conflict resolution with both provenances attached.

## Output contract
Write `contradiction-report.md` into `workspace/<venture-id>/memory/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** contradiction-detection
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
- Detection at write time
- Metric-definition mismatches included
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `memory` category
- Storing a claim without provenance, so nobody can later tell whether to trust it.
- Keeping two contradicting facts because resolving them is inconvenient.
- Treating a stale memory as current because it is well written.
