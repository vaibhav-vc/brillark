---
name: pipeline-model
category: gtm
description: "Model the pipeline so forecasts mean something."
output: "pipeline-model.md"
used_by:
  - chief-revenue-officer-agent
---

# Pipeline Model

**Category:** `gtm` · **Output artifact:** `pipeline-model.md`

## What this skill does
Model the pipeline so forecasts mean something.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `chief-revenue-officer-agent`.

## Procedure
1. Define each stage by an observable buyer action.
2. Measure historical conversion and duration per stage.
3. Compute the pipeline coverage needed to hit the target.
4. Identify the stage where deals actually die.
5. Refresh the rates quarterly; stale conversion rates produce confident wrong forecasts.

## Output contract
Write `pipeline-model.md` into `workspace/<venture-id>/gtm/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** pipeline-model
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
- Stages defined by buyer actions
- Conversion rates refreshed from actuals
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `gtm` category
- Scaling a channel before its CAC is measured.
- Running a test with no kill criterion, so it never ends.
- Claiming differentiation that is not a reason anyone would switch.
