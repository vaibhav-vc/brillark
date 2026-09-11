---
name: design-research-planning
category: design
description: "Plan research that answers a specific decision rather than producing general interest."
output: "research-plan.md"
used_by:
  - design-researcher
---

# Design Research Planning

**Category:** `design` · **Output artifact:** `research-plan.md`

## What this skill does
Plan research that answers a specific decision rather than producing general interest.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `design-researcher`.

## Procedure
1. Name the decision the research must inform and who will make it.
2. Write the question as something an observation could answer.
3. Choose the method from the question: observation for behaviour, interview for motivation, analytics for scale.
4. Define the participant criteria and how many, before recruiting.
5. State in advance what result would change the decision.

## Output contract
Write `research-plan.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** design-research-planning
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
- Research tied to a named decision and decision-maker
- Method chosen from the question, not from habit
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
