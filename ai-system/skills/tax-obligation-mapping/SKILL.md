---
name: tax-obligation-mapping
category: finance
description: "Determine what the venture owes, where, and when."
output: "tax-obligations.md"
used_by:
  - tax-and-compliance-finance
---

# Tax Obligation Mapping

**Category:** `finance` · **Output artifact:** `tax-obligations.md`

## What this skill does
Determine what the venture owes, where, and when.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `tax-and-compliance-finance`.

## Procedure
1. Identify every jurisdiction where a nexus exists, including digital-service rules.
2. Map obligation types: income, indirect, payroll, and filing-only.
3. Record registration requirements and thresholds.
4. Build the deadline calendar with the lead time each filing needs.
5. Flag every item requiring a qualified tax adviser.

## Output contract
Write `tax-obligations.md` into `workspace/<venture-id>/finance/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** tax-obligation-mapping
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
- Nexus assessed per jurisdiction
- Adviser-grade items flagged
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `finance` category
- Presenting a single number where the honest answer is a range.
- Building a forecast from a growth percentage instead of from drivers.
- Reporting a metric whose definition changed since last period without saying so.
