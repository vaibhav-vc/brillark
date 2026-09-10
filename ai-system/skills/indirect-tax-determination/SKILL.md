---
name: indirect-tax-determination
category: finance
description: "Decide the VAT, GST, or sales tax treatment per product and market."
output: "indirect-tax-logic.md"
used_by:
  - tax-and-compliance-finance
---

# Indirect Tax Determination

**Category:** `finance` · **Output artifact:** `indirect-tax-logic.md`

## What this skill does
Decide the VAT, GST, or sales tax treatment per product and market.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `tax-and-compliance-finance`.

## Procedure
1. Classify the product for tax purposes in each market.
2. Determine the place of supply rules that apply.
3. Establish whether the customer's status changes the treatment.
4. Define the evidence needed to support the treatment.
5. Document the logic so the billing system can implement it deterministically.

## Output contract
Write `indirect-tax-logic.md` into `workspace/<venture-id>/finance/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** indirect-tax-determination
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
- Place of supply determined per market
- Evidence requirements documented
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `finance` category
- Presenting a single number where the honest answer is a range.
- Building a forecast from a growth percentage instead of from drivers.
- Reporting a metric whose definition changed since last period without saying so.
