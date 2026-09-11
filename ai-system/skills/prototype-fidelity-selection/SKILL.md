---
name: prototype-fidelity-selection
category: design
description: "Choose the cheapest fidelity that answers the question."
output: "fidelity-decision.md"
used_by:
  - prototyper
---

# Prototype Fidelity Selection

**Category:** `design` · **Output artifact:** `fidelity-decision.md`

## What this skill does
Choose the cheapest fidelity that answers the question.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `prototyper`.

## Procedure
1. State the question the prototype must answer.
2. Match fidelity: sketch for structure, clickable for flow, coded for feel and performance.
3. Reject higher fidelity than the question requires.
4. Estimate build time and cap it before starting.
5. Confirm the chosen fidelity can actually produce the answer.

## Output contract
Write `fidelity-decision.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** prototype-fidelity-selection
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
- Fidelity justified by the question
- Build time capped in advance
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
