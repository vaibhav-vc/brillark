---
name: scenario-analysis
category: finance
description: "Model distinct futures defined by driver values rather than adjectives."
output: "scenarios.md"
used_by:
  - finance-head
  - financial-model-builder
  - revenue-forecaster
  - scenario-stress-tester
---

# Scenario Analysis

**Category:** `finance` · **Output artifact:** `scenarios.md`

## What this skill does
Model distinct futures defined by driver values rather than adjectives.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `finance-head`, `financial-model-builder`, `revenue-forecaster`, `scenario-stress-tester`.

## Procedure
1. Define each scenario by explicit values for the key drivers.
2. Build base, downside, and upside — and a severe case that tests survival.
3. Include correlated effects: shocks rarely arrive alone.
4. Report the outcome and the decision each scenario would trigger.
5. Name the indicator that would tell you which scenario is unfolding.

## Output contract
Write `scenarios.md` into `workspace/<venture-id>/finance/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** scenario-analysis
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
- Scenarios defined by driver values
- Each scenario has a leading indicator
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `finance` category
- Presenting a single number where the honest answer is a range.
- Building a forecast from a growth percentage instead of from drivers.
- Reporting a metric whose definition changed since last period without saying so.
