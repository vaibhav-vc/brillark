---
name: evaluation-revalidation
category: improvement
description: "Re-check the evaluation when the job changes."
output: "revalidation-record.md"
used_by:
  - eval-designer
---

# Evaluation Revalidation

**Category:** `improvement` · **Output artifact:** `revalidation-record.md`

## What this skill does
Re-check the evaluation when the job changes.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `eval-designer`.

## Procedure
1. Check whether the agent's charter or skills changed since the rubric was written.
2. Check whether the case set still reflects the real task mix.
3. Re-run discrimination analysis.
4. Retire criteria that no longer apply and add ones that now do.
5. Record the revalidation date.

## Output contract
Write `revalidation-record.md` into `workspace/<venture-id>/improvement/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** evaluation-revalidation
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
- Case set re-checked against the real task mix
- Revalidation date recorded
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `improvement` category
- Starting an improvement cycle with an idea instead of a measurement.
- Adopting a change that beat the cases it was tuned on.
- Adding an instruction without removing one, until none of them are read.
