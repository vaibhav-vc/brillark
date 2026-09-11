---
name: identity-stress-testing
category: design
description: "Test the identity where it is most likely to fail."
output: "identity-stress.md"
used_by:
  - brand-identity-designer
---

# Identity Stress Testing

**Category:** `design` · **Output artifact:** `identity-stress.md`

## What this skill does
Test the identity where it is most likely to fail.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `brand-identity-designer`.

## Procedure
1. Render at favicon size and check it still reads.
2. Convert to monochrome and to single-colour print.
3. Test on light, dark, and photographic backgrounds.
4. Test at low resolution and under heavy compression.
5. Fix the system rather than making one-off exceptions.

## Output contract
Write `identity-stress.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** identity-stress-testing
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
- Tested at smallest size and in monochrome
- Fixes applied to the system, not as exceptions
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
