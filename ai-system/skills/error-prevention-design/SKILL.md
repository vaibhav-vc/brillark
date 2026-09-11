---
name: error-prevention-design
category: design
description: "Stop the error happening rather than reporting it afterwards."
output: "error-prevention-spec.md"
used_by:
  - interaction-designer
---

# Error Prevention Design

**Category:** `design` · **Output artifact:** `error-prevention-spec.md`

## What this skill does
Stop the error happening rather than reporting it afterwards.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `interaction-designer`.

## Procedure
1. Identify the errors users actually make, from testing and support data.
2. Constrain the input so the invalid value cannot be entered.
3. Use good defaults so the common case needs no decision.
4. Confirm only destructive and irreversible actions; confirmation fatigue defeats itself.
5. Make every non-destructive action undoable rather than confirmed.

## Output contract
Write `error-prevention-spec.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** error-prevention-design
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
- Constraints preferred over post-hoc validation
- Confirmation reserved for irreversible actions
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
