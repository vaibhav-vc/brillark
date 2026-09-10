---
name: data-quality-scoring
category: data
description: "Measure whether the data can be trusted."
output: "data-quality-report.md"
used_by:
  - chief-data-officer-agent
---

# Data Quality Scoring

**Category:** `data` · **Output artifact:** `data-quality-report.md`

## What this skill does
Measure whether the data can be trusted.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `chief-data-officer-agent`.

## Procedure
1. Define quality dimensions: completeness, validity, timeliness, and consistency.
2. Set a check per dimension per critical dataset.
3. Score and publish, rather than assuming quality.
4. Alert on degradation, not just on absolute failure.
5. Fix the worst-scoring source each cycle.

## Output contract
Write `data-quality-report.md` into `workspace/<venture-id>/data/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** data-quality-scoring
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
- Checks defined per dimension
- Degradation alerts, not just failures
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `data` category
- Two dashboards reporting the same metric with different definitions.
- Reporting an experiment result that never had the power to detect the effect.
- Collecting a field first and finding a purpose for it later.
