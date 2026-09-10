---
name: cap-table-reconciliation
category: finance
description: "Make the cap table match the signed documents exactly."
output: "cap-table-reconciliation.md"
used_by:
  - cap-table-steward
  - corporate-secretary-agent
---

# Cap Table Reconciliation

**Category:** `finance` · **Output artifact:** `cap-table-reconciliation.md`

## What this skill does
Make the cap table match the signed documents exactly.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `cap-table-steward`, `corporate-secretary-agent`.

## Procedure
1. List every equity instrument and locate its signed document.
2. Verify share counts, dates, prices, and vesting terms against the document.
3. Reconcile option grants against board approvals.
4. Resolve every discrepancy before the table is used for any decision.
5. Record the reconciliation date and the version certified.

## Output contract
Write `cap-table-reconciliation.md` into `workspace/<venture-id>/finance/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** cap-table-reconciliation
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
- Every line matched to a signed document
- Discrepancies resolved before use
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `finance` category
- Presenting a single number where the honest answer is a range.
- Building a forecast from a growth percentage instead of from drivers.
- Reporting a metric whose definition changed since last period without saying so.
