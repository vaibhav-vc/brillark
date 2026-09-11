---
name: brand-guideline-authoring
category: design
description: "Write guidelines people can actually follow."
output: "brand-guidelines.md"
used_by:
  - brand-identity-designer
---

# Brand Guideline Authoring

**Category:** `design` · **Output artifact:** `brand-guidelines.md`

## What this skill does
Write guidelines people can actually follow.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `brand-identity-designer`.

## Procedure
1. Show correct and incorrect examples side by side.
2. Give exact values: colours, spacing, sizes, and clear space.
3. Cover the awkward cases people actually hit.
4. Keep it short enough to be read, with detail available behind it.
5. Provide the assets alongside the rules so nobody recreates them.

## Output contract
Write `brand-guidelines.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** brand-guideline-authoring
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
- Correct and incorrect shown side by side
- Awkward real cases covered
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
