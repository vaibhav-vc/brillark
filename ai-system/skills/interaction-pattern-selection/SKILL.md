---
name: interaction-pattern-selection
category: design
description: "Reuse an established pattern before inventing one."
output: "pattern-decision.md"
used_by:
  - interaction-designer
---

# Interaction Pattern Selection

**Category:** `design` · **Output artifact:** `pattern-decision.md`

## What this skill does
Reuse an established pattern before inventing one.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `interaction-designer`.

## Procedure
1. Identify the interaction problem in general terms before reaching for a solution.
2. Check the design system and platform conventions for an existing pattern.
3. Judge a novel pattern against the learning cost it imposes on every user.
4. If inventing, define the pattern properly so it can be reused and documented.
5. Record the decision so the next designer does not re-litigate it.

## Output contract
Write `pattern-decision.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** interaction-pattern-selection
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
- Existing pattern checked before invention
- Novel patterns justified against learning cost
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
