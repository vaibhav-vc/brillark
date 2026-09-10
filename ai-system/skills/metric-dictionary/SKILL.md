---
name: metric-dictionary
category: data
description: "Define every metric once, with one owner."
output: "metric-dictionary.md"
used_by:
  - chief-data-officer-agent
---

# Metric Dictionary

**Category:** `data` · **Output artifact:** `metric-dictionary.md`

## What this skill does
Define every metric once, with one owner.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `chief-data-officer-agent`.

## Procedure
1. Write the precise definition, including the filters and the time basis.
2. Name the source system and the exact calculation.
3. Assign one owner responsible for the definition.
4. Record known caveats and where the metric is misleading.
5. Reject any duplicate definition of an existing metric.

## Output contract
Write `metric-dictionary.md` into `workspace/<venture-id>/data/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** metric-dictionary
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
- One definition and one owner per metric
- Caveats documented
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `data` category
- Two dashboards reporting the same metric with different definitions.
- Reporting an experiment result that never had the power to detect the effect.
- Collecting a field first and finding a purpose for it later.
