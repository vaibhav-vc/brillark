---
name: escalation-rule-design
category: efficiency
description: "Define when a cheaper tier must hand up."
output: "escalation-rules.md"
used_by:
  - model-router-tuner
---

# Escalation Rule Design

**Category:** `efficiency` · **Output artifact:** `escalation-rules.md`

## What this skill does
Define when a cheaper tier must hand up.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `model-router-tuner`.

## Procedure
1. Identify the conditions the cheaper tier handles badly.
2. Write each as an observable trigger, not a judgement call.
3. Define what the escalating agent passes up.
4. Set the expected escalation frequency and what an excess means.
5. Test the rule fires when it should before relying on it.

## Output contract
Write `escalation-rules.md` into `workspace/<venture-id>/efficiency/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** escalation-rule-design
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
- Triggers observable, not judgement calls
- Expected frequency stated
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `efficiency` category
- Measuring cost per call instead of cost per completed task.
- Demoting a model tier without checking the hardest cases.
- Trimming context by hand instead of fixing the rule that loaded it.
