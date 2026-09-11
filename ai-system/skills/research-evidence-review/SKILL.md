---
name: research-evidence-review
category: design
description: "Check that a design decision rests on evidence rather than assertion."
output: "evidence-review.md"
used_by:
  - design-head
---

# Research Evidence Review

**Category:** `design` · **Output artifact:** `evidence-review.md`

## What this skill does
Check that a design decision rests on evidence rather than assertion.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `design-head`.

## Procedure
1. Ask what evidence supports the central choice.
2. Check the evidence actually addresses this decision.
3. Check the sample and the method support the weight placed on it.
4. Identify the choices resting on assumption and flag the riskiest.
5. Require a cheap test for the riskiest unsupported choice.

## Output contract
Write `evidence-review.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** research-evidence-review
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
- Evidence checked for being on point
- Riskiest unsupported choice gets a test
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
