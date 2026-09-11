---
name: design-decision-record
category: design
description: "Record a design decision so it is not re-argued every week."
output: "design-decision.md"
used_by:
  - design-critic
---

# Design Decision Record

**Category:** `design` · **Output artifact:** `design-decision.md`

## What this skill does
Record a design decision so it is not re-argued every week.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `design-critic`.

## Procedure
1. State the decision and the goal it serves.
2. Record the alternatives considered and why each was rejected.
3. Record the evidence: research, testing, or constraint.
4. Record what would reopen the decision.
5. Store it with the surface so the next designer finds it.

## Output contract
Write `design-decision.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** design-decision-record
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
- Rejected alternatives recorded with reasons
- Reopening condition stated
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
