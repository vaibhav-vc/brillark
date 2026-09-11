---
name: inclusive-design-review
category: design
description: "Review the design for who it excludes before it is built."
output: "inclusive-review.md"
used_by:
  - accessibility-designer
---

# Inclusive Design Review

**Category:** `design` · **Output artifact:** `inclusive-review.md`

## What this skill does
Review the design for who it excludes before it is built.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `accessibility-designer`.

## Procedure
1. List the ways people might differ: ability, device, connection, language, literacy, context.
2. Walk the flow as each, and note where it fails.
3. Check assumptions about steady hands, full attention, and fast connections.
4. Prioritise findings by how many are excluded and how completely.
5. Propose the change that removes the exclusion, not a parallel path.

## Output contract
Write `inclusive-review.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** inclusive-design-review
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
- Exclusions identified before build
- Fixes remove exclusion rather than adding a side path
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
