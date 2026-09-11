---
name: design-token-application
category: design
description: "Use the system's tokens rather than introducing one-off values."
output: "token-usage-report.md"
used_by:
  - visual-designer
---

# Design Token Application

**Category:** `design` · **Output artifact:** `token-usage-report.md`

## What this skill does
Use the system's tokens rather than introducing one-off values.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `visual-designer`.

## Procedure
1. Look up the semantic token for the intent, not the literal value you want.
2. Propose a token addition when none fits, rather than hard-coding.
3. Check the token works in every theme and mode the product supports.
4. Flag any one-off value remaining, with a reason and a plan to remove it.
5. Verify the applied tokens survive a theme switch.

## Output contract
Write `token-usage-report.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** design-token-application
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
- No hard-coded values without a recorded reason
- Verified across themes and modes
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
