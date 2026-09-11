---
name: typography-system
category: design
description: "Set type so the product can be read comfortably."
output: "type-system.md"
used_by:
  - visual-designer
---

# Typography System

**Category:** `design` · **Output artifact:** `type-system.md`

## What this skill does
Set type so the product can be read comfortably.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `visual-designer`.

## Procedure
1. Define a scale with enough steps to build hierarchy and few enough to stay consistent.
2. Set line length and line height for reading, not for fitting.
3. Check the smallest text against contrast and size requirements.
4. Define styles semantically — body, caption, heading — not by pixel value.
5. Test with the longest realistic string in every supported language.

## Output contract
Write `type-system.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** typography-system
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
- Scale defined semantically
- Tested with longest realistic strings
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
