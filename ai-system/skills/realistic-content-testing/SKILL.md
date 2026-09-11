---
name: realistic-content-testing
category: design
description: "Test the design with the content it will actually hold."
output: "content-stress-results.md"
used_by:
  - prototyper
  - visual-designer
---

# Realistic Content Testing

**Category:** `design` · **Output artifact:** `content-stress-results.md`

## What this skill does
Test the design with the content it will actually hold.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `prototyper`, `visual-designer`.

## Procedure
1. Use real data, including the longest, shortest, and missing cases.
2. Test with the volume real users have, not with three tidy items.
3. Check every supported language, including the ones that expand text.
4. Check names, numbers, and dates in their real formats.
5. Fix what breaks before the design is called complete.

## Output contract
Write `content-stress-results.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** realistic-content-testing
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
- Longest, shortest, and missing cases tested
- Real data volumes used
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
