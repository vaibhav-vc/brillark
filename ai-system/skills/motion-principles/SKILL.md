---
name: motion-principles
category: design
description: "Define what motion is for in this product, and what it is not for."
output: "motion-principles.md"
used_by:
  - motion-designer
---

# Motion Principles

**Category:** `design` · **Output artifact:** `motion-principles.md`

## What this skill does
Define what motion is for in this product, and what it is not for.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `motion-designer`.

## Procedure
1. State the purposes motion serves here: continuity, causality, feedback, and status.
2. Define the duration and easing scale as tokens.
3. Rule out decorative motion that delays the user.
4. Define how motion behaves when many elements change at once.
5. Document the reduced-motion contract for the whole product.

## Output contract
Write `motion-principles.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** motion-principles
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
- Purposes stated and decoration ruled out
- Reduced-motion contract documented
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
