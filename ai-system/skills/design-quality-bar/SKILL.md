---
name: design-quality-bar
category: design
description: "Define what finished means for a design."
output: "quality-bar.md"
used_by:
  - design-head
---

# Design Quality Bar

**Category:** `design` · **Output artifact:** `quality-bar.md`

## What this skill does
Define what finished means for a design.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `design-head`.

## Procedure
1. Require a stated user problem with evidence.
2. Require the full flow, all view states, and the unhappy paths.
3. Require accessibility annotation and contrast verification.
4. Require design system compliance or a recorded exception.
5. Require validation with real users before build.

## Output contract
Write `quality-bar.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** design-quality-bar
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
- All states and unhappy paths required
- Accessibility required before build, not after
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
