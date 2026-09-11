---
name: task-class-classification
category: efficiency
description: "Classify work so it can be routed to the right tier."
output: "task-classes.md"
used_by:
  - model-router-tuner
---

# Task Class Classification

**Category:** `efficiency` · **Output artifact:** `task-classes.md`

## What this skill does
Classify work so it can be routed to the right tier.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `model-router-tuner`.

## Procedure
1. Classify as mechanical, analytical, or judgement.
2. Mechanical: extraction, formatting, validation, tracking, lookup.
3. Analytical: synthesis, comparison, modelling, diagnosis.
4. Judgement: arbitration, strategy, ethics, irreversible decisions.
5. Record the classification with the agent's charter.

## Output contract
Write `task-classes.md` into `workspace/<venture-id>/efficiency/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** task-class-classification
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
- Classification recorded with the charter
- Irreversible decisions always classed as judgement
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `efficiency` category
- Measuring cost per call instead of cost per completed task.
- Demoting a model tier without checking the hardest cases.
- Trimming context by hand instead of fixing the rule that loaded it.
