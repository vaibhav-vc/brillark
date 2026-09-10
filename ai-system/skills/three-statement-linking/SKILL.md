---
name: three-statement-linking
category: finance
description: "Connect profit and loss, balance sheet, and cash flow so the model cannot lie."
output: "three-statement-model.md"
used_by:
  - financial-model-builder
---

# Three Statement Linking

**Category:** `finance` · **Output artifact:** `three-statement-model.md`

## What this skill does
Connect profit and loss, balance sheet, and cash flow so the model cannot lie.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `financial-model-builder`.

## Procedure
1. Build the P&L from the revenue and cost drivers.
2. Flow net income into retained earnings on the balance sheet.
3. Derive cash flow from net income plus non-cash adjustments and working capital movements.
4. Check that the balance sheet balances in every period; an imbalance is a bug, not a rounding issue.
5. Verify the closing cash in the cash flow matches the balance sheet cash exactly.

## Output contract
Write `three-statement-model.md` into `workspace/<venture-id>/finance/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** three-statement-linking
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
- Balance sheet balances every period
- Closing cash reconciles across statements
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `finance` category
- Presenting a single number where the honest answer is a range.
- Building a forecast from a growth percentage instead of from drivers.
- Reporting a metric whose definition changed since last period without saying so.
