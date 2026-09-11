---
name: contrast-and-colour-audit
category: design
description: "Check colour works for everyone who has to read it."
output: "contrast-audit.md"
used_by:
  - accessibility-designer
---

# Contrast And Colour Audit

**Category:** `design` · **Output artifact:** `contrast-audit.md`

## What this skill does
Check colour works for everyone who has to read it.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `accessibility-designer`.

## Procedure
1. Measure contrast for every text and meaningful non-text element.
2. Check against the required ratio for the actual size and weight.
3. Verify no meaning is carried by colour alone.
4. Simulate the common colour vision deficiencies.
5. Check the same in every theme and mode.

## Output contract
Write `contrast-audit.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** contrast-and-colour-audit
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
- Every meaningful element measured
- No meaning carried by colour alone
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
