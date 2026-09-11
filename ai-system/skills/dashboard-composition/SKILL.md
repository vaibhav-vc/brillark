---
name: dashboard-composition
category: design
description: "Compose a dashboard that answers questions rather than displaying numbers."
output: "dashboard-spec.md"
used_by:
  - data-visualization-designer
---

# Dashboard Composition

**Category:** `design` · **Output artifact:** `dashboard-spec.md`

## What this skill does
Compose a dashboard that answers questions rather than displaying numbers.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `data-visualization-designer`.

## Procedure
1. Name the question each panel answers, and delete panels with no question.
2. Order panels by the sequence someone would actually investigate.
3. Give the most important comparison the most space.
4. Keep density high enough to compare without scrolling between related panels.
5. Test with a real user doing a real investigation.

## Output contract
Write `dashboard-spec.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** dashboard-composition
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
- Every panel answers a named question
- Ordering follows real investigation sequence
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
