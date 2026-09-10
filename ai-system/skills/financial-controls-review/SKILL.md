---
name: financial-controls-review
category: finance
description: "Check that money cannot leave the company without the right approvals."
output: "controls-review.md"
used_by:
  - cfo-agent
---

# Financial Controls Review

**Category:** `finance` · **Output artifact:** `controls-review.md`

## What this skill does
Check that money cannot leave the company without the right approvals.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `cfo-agent`.

## Procedure
1. Map every path by which funds can be disbursed.
2. Check each path for approval thresholds and segregation of duties.
3. Test a sample of transactions for control compliance.
4. Identify paths with a single point of authorisation.
5. Report gaps with the specific control that would close each.

## Output contract
Write `controls-review.md` into `workspace/<venture-id>/finance/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** financial-controls-review
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
- All disbursement paths mapped
- Sample testing performed, not just policy review
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `finance` category
- Presenting a single number where the honest answer is a range.
- Building a forecast from a growth percentage instead of from drivers.
- Reporting a metric whose definition changed since last period without saying so.
