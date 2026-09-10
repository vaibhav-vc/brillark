---
name: budget-approval
category: finance
description: "Approve or refuse spend with a stated reason either way."
output: "budget-decision.md"
used_by:
  - cfo-agent
---

# Budget Approval

**Category:** `finance` · **Output artifact:** `budget-decision.md`

## What this skill does
Approve or refuse spend with a stated reason either way.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `cfo-agent`.

## Procedure
1. Require a written case: amount, purpose, expected outcome, and alternative.
2. Check the request against the budget envelope and the runway impact.
3. Compare against the next-best use of the same money.
4. Approve, refuse, or approve with conditions — always in writing.
5. When refusing, state the condition that would turn it into a yes.

## Output contract
Write `budget-decision.md` into `workspace/<venture-id>/finance/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** budget-approval
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
- Compared against next-best use
- Refusals state their reversal condition
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `finance` category
- Presenting a single number where the honest answer is a range.
- Building a forecast from a growth percentage instead of from drivers.
- Reporting a metric whose definition changed since last period without saying so.
