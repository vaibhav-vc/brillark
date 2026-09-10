---
name: refactoring-planning
category: engineering
description: "Plan a refactor that pays off soon."
output: "refactor-plan.md"
used_by:
  - tech-debt-refactor-agent
---

# Refactoring Planning

**Category:** `engineering` · **Output artifact:** `refactor-plan.md`

## What this skill does
Plan a refactor that pays off soon.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `tech-debt-refactor-agent`.

## Procedure
1. Justify from delivery pain or defect clustering, not from taste.
2. Refactor along the path of imminent work.
3. Ensure test coverage exists before changing structure.
4. Split into steps that each leave the system working.
5. Define the measurable improvement expected.

## Output contract
Write `refactor-plan.md` into `workspace/<venture-id>/engineering/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** refactoring-planning
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
- Justified by delivery pain
- Each step leaves the system working
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `engineering` category
- Designing for imagined scale instead of current load plus one order of magnitude.
- Skipping or quarantining a failing test to get a green build.
- Shipping without a verified way back.
