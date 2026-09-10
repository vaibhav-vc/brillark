---
name: graph-query-design
category: memory
description: "Build the specific queries agents need rather than a generic search box."
output: "query-catalogue.md"
used_by:
  - knowledge-graph-librarian
---

# Graph Query Design

**Category:** `memory` · **Output artifact:** `query-catalogue.md`

## What this skill does
Build the specific queries agents need rather than a generic search box.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `knowledge-graph-librarian`.

## Procedure
1. Collect the questions agents actually ask, in their own words.
2. Turn each into a parameterised graph traversal.
3. Return provenance alongside every answer.
4. Cap result size and rank by evidence grade.
5. Retire queries nobody uses and add ones the retrospectives reveal.

## Output contract
Write `query-catalogue.md` into `workspace/<venture-id>/memory/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** graph-query-design
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
- Answers carry provenance
- Queries derived from real agent questions
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `memory` category
- Storing a claim without provenance, so nobody can later tell whether to trust it.
- Keeping two contradicting facts because resolving them is inconvenient.
- Treating a stale memory as current because it is well written.
