---
name: data-model-design
category: engineering
description: "Design the data structure around how it will actually be used."
output: "data-model.md"
used_by:
  - data-model-designer
---

# Data Model Design

**Category:** `engineering` · **Output artifact:** `data-model.md`

## What this skill does
Design the data structure around how it will actually be used.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `data-model-designer`.

## Procedure
1. Model the entities and relationships in the domain first.
2. Enumerate the queries and write patterns the system must support.
3. Choose the storage technology from those patterns, not from preference.
4. Define integrity constraints and enforce them at the storage layer.
5. Classify every field for privacy and retention at creation.

## Output contract
Write `data-model.md` into `workspace/<venture-id>/engineering/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** data-model-design
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
- Access patterns enumerated before design
- Constraints enforced at the storage layer
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `engineering` category
- Designing for imagined scale instead of current load plus one order of magnitude.
- Skipping or quarantining a failing test to get a green build.
- Shipping without a verified way back.
