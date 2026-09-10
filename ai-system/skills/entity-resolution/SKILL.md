---
name: entity-resolution
category: memory
description: "Make sure one real-world thing is one node in the knowledge graph."
output: "entity-resolution-report.md"
used_by:
  - knowledge-graph-librarian
---

# Entity Resolution

**Category:** `memory` · **Output artifact:** `entity-resolution-report.md`

## What this skill does
Make sure one real-world thing is one node in the knowledge graph.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `knowledge-graph-librarian`.

## Procedure
1. Normalise names, aliases, and identifiers before comparison.
2. Compare candidate matches on stable attributes, not on name similarity alone.
3. Merge duplicates and redirect all references to the canonical node.
4. Record the merge so it can be reversed if wrong.
5. Flag ambiguous cases for human or head review instead of guessing.

## Output contract
Write `entity-resolution-report.md` into `workspace/<venture-id>/memory/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** entity-resolution
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
- Merges are reversible
- Ambiguous matches escalated, not guessed
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `memory` category
- Storing a claim without provenance, so nobody can later tell whether to trust it.
- Keeping two contradicting facts because resolving them is inconvenient.
- Treating a stale memory as current because it is well written.
