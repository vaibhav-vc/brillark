---
name: sensitivity-analysis
category: finance
description: "Find which inputs actually move the outcome."
output: "sensitivity-table.md"
used_by:
  - council-economics-skeptic
  - scenario-stress-tester
  - unit-economics-architect
---

# Sensitivity Analysis

**Category:** `finance` · **Output artifact:** `sensitivity-table.md`

## What this skill does
Find which inputs actually move the outcome.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `council-economics-skeptic`, `scenario-stress-tester`, `unit-economics-architect`.

## Procedure
1. Flex one input at a time across a realistic range.
2. Record the outcome change per input and rank by impact.
3. Identify the inputs where a small error produces a large outcome swing.
4. Cross-check that the high-impact inputs are the best-evidenced ones; if not, that is the finding.
5. Present as a ranked table, not a wall of scenarios.

## Output contract
Write `sensitivity-table.md` into `workspace/<venture-id>/finance/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** sensitivity-analysis
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
- Ranges realistic, not symmetric by default
- High-impact inputs cross-checked against evidence grade
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `finance` category
- Presenting a single number where the honest answer is a range.
- Building a forecast from a growth percentage instead of from drivers.
- Reporting a metric whose definition changed since last period without saying so.
