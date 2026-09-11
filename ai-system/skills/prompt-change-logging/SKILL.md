---
name: prompt-change-logging
category: improvement
description: "Keep the history of what changed and what it bought."
output: "prompt-change-log.md"
used_by:
  - prompt-optimizer
---

# Prompt Change Logging

`improvement` · produces `prompt-change-log.md` · used by `prompt-optimizer`

Keep the history of what changed and what it bought.

## Procedure
1. Record the before and after text of the change.
2. Record the diagnosed failure that motivated it.
3. Record the measured delta and the sample.
4. Record the date and who adopted it.
5. Keep reverted changes in the log with the reason.

## Output contract
`prompt-change-log.md` → `workspace/<venture-id>/improvement/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/improvement.tsv`.

## Quality bar
- Measured delta recorded with each change
- Reverted changes retained with reasons
- The output states its confidence grade and names the evidence behind every load-bearing claim.
