---
name: layout-composition
category: design
description: "Arrange the screen so the structure is obvious without explanation."
output: "layout-spec.md"
used_by:
  - visual-designer
---

# Layout Composition

**Category:** `design` · **Output artifact:** `layout-spec.md`

## What this skill does
Arrange the screen so the structure is obvious without explanation.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `visual-designer`.

## Procedure
1. Establish the grid and the spacing scale, and use them consistently.
2. Group related elements by proximity before adding borders or boxes.
3. Give the primary content the space its importance deserves.
4. Design the dense case with real data volumes, not the showcase case.
5. Check every breakpoint, especially the narrowest supported width.

## Output contract
Write `layout-spec.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** layout-composition
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
- Proximity used before decoration
- Dense realistic case designed
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
