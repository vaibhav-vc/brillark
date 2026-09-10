---
name: knowledge-graph-modeling
category: memory
description: "Design the entities and typed relationships that make cross-domain questions answerable."
output: "graph-model.md"
used_by:
  - knowledge-graph-librarian
---

# Knowledge Graph Modeling

**Category:** `memory` · **Output artifact:** `graph-model.md`

## What this skill does
Design the entities and typed relationships that make cross-domain questions answerable.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `knowledge-graph-librarian`.

## Procedure
1. List the entity types the organisation actually reasons about.
2. Define typed relationships — 'competes with', 'depends on', 'evidences' — never 'related to'.
3. Attach each relationship to the artifact that justifies it.
4. Model time where it matters: relationships change and history is useful.
5. Validate by writing the five questions the graph must answer and testing them.

## Output contract
Write `graph-model.md` into `workspace/<venture-id>/memory/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** knowledge-graph-modeling
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
- All relationships typed
- Model validated against real questions
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `memory` category
- Storing a claim without provenance, so nobody can later tell whether to trust it.
- Keeping two contradicting facts because resolving them is inconvenient.
- Treating a stale memory as current because it is well written.
