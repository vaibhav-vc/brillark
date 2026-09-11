---
name: taste-versus-principle-separation
category: design
description: "Tell apart a real problem and a personal preference."
output: "objection-triage.md"
used_by:
  - design-critic
---

# Taste Versus Principle Separation

**Category:** `design` · **Output artifact:** `objection-triage.md`

## What this skill does
Tell apart a real problem and a personal preference.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `design-critic`.

## Procedure
1. Ask what evidence or principle supports the objection.
2. Check whether it would fail for a user or only differ from your choice.
3. Test the objection against the design system and research findings.
4. Drop preferences that do not affect the goal.
5. Record genuine principles so they become shared rather than repeated.

## Output contract
Write `objection-triage.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** taste-versus-principle-separation
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
- Preferences dropped when they do not affect the goal
- Principles recorded to become shared
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
