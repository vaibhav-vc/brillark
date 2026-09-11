---
name: prototype-scoping
category: design
description: "Be explicit about what the prototype proves and what it fakes."
output: "prototype-scope.md"
used_by:
  - prototyper
---

# Prototype Scoping

**Category:** `design` · **Output artifact:** `prototype-scope.md`

## What this skill does
Be explicit about what the prototype proves and what it fakes.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `prototyper`.

## Procedure
1. List what is real and what is simulated.
2. State the questions the prototype cannot answer.
3. Warn testers and stakeholders before they see it.
4. Set the boundary for feedback so critique stays on the question.
5. Record the scope alongside the results.

## Output contract
Write `prototype-scope.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** prototype-scoping
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
- Faked elements listed explicitly
- Unanswerable questions stated up front
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
