---
name: experiment-design
category: data
description: "Design a test that can actually answer the question."
output: "experiment-design.md"
used_by:
  - chief-data-officer-agent
---

# Experiment Design

**Category:** `data` · **Output artifact:** `experiment-design.md`

## What this skill does
Design a test that can actually answer the question.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `chief-data-officer-agent`.

## Procedure
1. State the hypothesis and the single primary metric in advance.
2. Compute the sample size required for the effect worth detecting.
3. Define the randomisation unit and check for interference.
4. Set the duration to cover a full behavioural cycle.
5. Pre-register the analysis; decide the threshold before seeing results.

## Output contract
Write `experiment-design.md` into `workspace/<venture-id>/data/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** experiment-design
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
- Sample size computed before launch
- Analysis pre-registered
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `data` category
- Two dashboards reporting the same metric with different definitions.
- Reporting an experiment result that never had the power to detect the effect.
- Collecting a field first and finding a purpose for it later.
