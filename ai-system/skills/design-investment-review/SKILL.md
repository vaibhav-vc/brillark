---
name: design-investment-review
category: design
description: "Judge whether design effort is going where it pays."
output: "investment-review.md"
used_by:
  - chief-design-officer-agent
---

# Design Investment Review

**Category:** `design` · **Output artifact:** `investment-review.md`

## What this skill does
Judge whether design effort is going where it pays.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `chief-design-officer-agent`.

## Procedure
1. List where design effort actually went last cycle.
2. Compare against the surfaces that most affect customer outcomes.
3. Identify effort spent on internal preference rather than customer outcome.
4. Identify high-impact surfaces receiving no attention.
5. Reallocate explicitly and state what is being deprioritised.

## Output contract
Write `investment-review.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** design-investment-review
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
- Effort compared against outcome impact
- Deprioritised work stated explicitly
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
