---
name: recurring-flaw-analysis
category: council
description: "Find the mistakes this organisation keeps making."
output: "recurring-flaws.md"
used_by:
  - council-director
---

# Recurring Flaw Analysis

`council` · produces `recurring-flaws.md` · used by `council-director`

Find the mistakes this organisation keeps making.

## Procedure
1. Group findings across reviews by underlying flaw type.
2. Identify flaws appearing in three or more reviews.
3. Trace each to the agent, skill, or process that permits it.
4. Convert into a guardrail or checklist change at the source.
5. Track whether the flaw rate falls in subsequent reviews.

## Output contract
`recurring-flaws.md` → `workspace/<venture-id>/council/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/council.tsv`.

## Quality bar
- Traced to a specific artifact that permits it
- Recurrence rate tracked afterwards
- The output states its confidence grade and names the evidence behind every load-bearing claim.
