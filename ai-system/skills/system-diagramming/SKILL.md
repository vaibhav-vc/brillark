---
name: system-diagramming
category: engineering
description: "Draw the system so a newcomer can understand it."
output: "architecture-diagram.md"
used_by:
  - system-architect
---

# System Diagramming

**Category:** `engineering` · **Output artifact:** `architecture-diagram.md`

## What this skill does
Draw the system so a newcomer can understand it.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `system-architect`.

## Procedure
1. Draw the context level first: who uses it and what it depends on.
2. Draw the container level: the deployable pieces and their protocols.
3. Draw component detail only where it is genuinely needed.
4. Label every arrow with what flows and in which direction.
5. Date the diagram and note what it deliberately omits.

## Output contract
Write `architecture-diagram.md` into `workspace/<venture-id>/engineering/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** system-diagramming
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
- Arrows labelled with what flows
- Omissions stated explicitly
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `engineering` category
- Designing for imagined scale instead of current load plus one order of magnitude.
- Skipping or quarantining a failing test to get a green build.
- Shipping without a verified way back.
