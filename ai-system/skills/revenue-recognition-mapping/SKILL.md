---
name: revenue-recognition-mapping
category: finance
description: "Determine when revenue may actually be recognised, not when cash arrives."
output: "rev-rec-policy.md"
used_by:
  - billing-systems-designer
---

# Revenue Recognition Mapping

**Category:** `finance` · **Output artifact:** `rev-rec-policy.md`

## What this skill does
Determine when revenue may actually be recognised, not when cash arrives.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `billing-systems-designer`.

## Procedure
1. Identify each distinct performance obligation in the contract.
2. Determine when control transfers for each obligation.
3. Allocate the transaction price across obligations.
4. Define the recognition schedule and how it is automated.
5. Document the treatment and flag anything requiring professional advice.

## Output contract
Write `rev-rec-policy.md` into `workspace/<venture-id>/finance/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** revenue-recognition-mapping
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
- Obligations identified separately
- Advice-grade items flagged
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `finance` category
- Presenting a single number where the honest answer is a range.
- Building a forecast from a growth percentage instead of from drivers.
- Reporting a metric whose definition changed since last period without saying so.
