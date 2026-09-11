---
name: filing-calendar
category: finance
description: "Make sure no statutory deadline is missed."
output: "filing-calendar.md"
used_by:
  - corporate-secretary-agent
  - tax-and-compliance-finance
---

# Filing Calendar

`finance` · produces `filing-calendar.md` · used by `corporate-secretary-agent`, `tax-and-compliance-finance`

Make sure no statutory deadline is missed.

## Procedure
1. List every filing obligation with its jurisdiction and frequency.
2. Record the statutory deadline and the internal deadline that precedes it.
3. Assign an owner and a preparer to each.
4. Set reminders with enough lead time to actually prepare.
5. Record completion with the confirmation reference.

## Output contract
`filing-calendar.md` → `workspace/<venture-id>/finance/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/finance.tsv`.

## Quality bar
- Internal deadlines precede statutory ones
- Completion recorded with a reference
- The output states its confidence grade and names the evidence behind every load-bearing claim.
