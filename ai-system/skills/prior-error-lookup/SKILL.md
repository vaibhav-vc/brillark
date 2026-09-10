---
name: prior-error-lookup
category: memory
description: "Check whether this organisation has already been wrong about this."
output: "prior-error-report.md"
used_by:
  - council-assumption-auditor
---

# Prior Error Lookup

**Category:** `memory` · **Output artifact:** `prior-error-report.md`

## What this skill does
Check whether this organisation has already been wrong about this.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `council-assumption-auditor`.

## Procedure
1. Extract the assumptions in the current plan.
2. Search memory for previously disproven assumptions on the same subject.
3. Report matches with the evidence that disproved them.
4. Check whether the conditions that made it wrong still hold.
5. Block the plan from repeating an error without an explicit reason why this time differs.

## Output contract
Write `prior-error-report.md` into `workspace/<venture-id>/memory/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** prior-error-lookup
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
- Matches carry the disproving evidence
- Repeat requires an explicit difference
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `memory` category
- Storing a claim without provenance, so nobody can later tell whether to trust it.
- Keeping two contradicting facts because resolving them is inconvenient.
- Treating a stale memory as current because it is well written.
