---
name: investor-reporting
category: finance
description: "Write an investor update that is accurate, consistent, and worth reading."
output: "investor-update.md"
used_by:
  - cfo-agent
  - investor-reporting-agent
---

# Investor Reporting

**Category:** `finance` · **Output artifact:** `investor-update.md`

## What this skill does
Write an investor update that is accurate, consistent, and worth reading.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `cfo-agent`, `investor-reporting-agent`.

## Procedure
1. Report the same metric set as last period, with the same definitions.
2. Lead with the numbers table, then the narrative.
3. State bad news plainly and early, with the action being taken.
4. Make asks specific: a name, an introduction, or a decision.
5. Reconcile every figure before sending.

## Output contract
Write `investor-update.md` into `workspace/<venture-id>/finance/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** investor-reporting
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
- Metric definitions unchanged from prior period
- Asks are specific and actionable
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `finance` category
- Presenting a single number where the honest answer is a range.
- Building a forecast from a growth percentage instead of from drivers.
- Reporting a metric whose definition changed since last period without saying so.
