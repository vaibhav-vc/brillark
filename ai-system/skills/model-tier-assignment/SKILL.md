---
name: model-tier-assignment
category: efficiency
description: "Put each agent on the cheapest tier that holds quality."
output: "tier-assignment.md"
used_by:
  - model-router-tuner
  - token-efficiency-analyst
---

# Model Tier Assignment

**Category:** `efficiency` · **Output artifact:** `tier-assignment.md`

## What this skill does
Put each agent on the cheapest tier that holds quality.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `model-router-tuner`, `token-efficiency-analyst`.

## Procedure
1. Classify the agent's work: mechanical, analytical, or judgement.
2. Run the golden cases at the candidate tier.
3. Compare quality against the rubric floor, not against the stronger tier's ceiling.
4. Assign the cheapest tier that clears the floor.
5. Keep judgement, arbitration, and Council work on the strongest tier.

## Output contract
Write `tier-assignment.md` into `workspace/<venture-id>/efficiency/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** model-tier-assignment
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
- Quality verified against a rubric floor
- Judgement work never demoted
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `efficiency` category
- Measuring cost per call instead of cost per completed task.
- Demoting a model tier without checking the hardest cases.
- Trimming context by hand instead of fixing the rule that loaded it.
