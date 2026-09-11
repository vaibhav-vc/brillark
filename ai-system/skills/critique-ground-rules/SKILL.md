---
name: critique-ground-rules
category: design
description: "Set the rules that make critique safe and useful."
output: "ground-rules.md"
used_by:
  - design-critic
---

# Critique Ground Rules

**Category:** `design` · **Output artifact:** `ground-rules.md`

## What this skill does
Set the rules that make critique safe and useful.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `design-critic`.

## Procedure
1. State that the work is being critiqued, not the designer.
2. Require the goal before the feedback.
3. Ban solutioning over the designer and rank-based override.
4. Give quieter participants a structured turn.
5. Time-box and close with recorded decisions.

## Output contract
Write `ground-rules.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** critique-ground-rules
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
- Rank-based override explicitly banned
- Structured turn for quieter participants
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
