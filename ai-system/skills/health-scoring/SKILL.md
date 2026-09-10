---
name: health-scoring
category: gtm
description: "Predict which customers are at risk before they leave."
output: "health-score-model.md"
used_by:
  - customer-success-agent
---

# Health Scoring

**Category:** `gtm` · **Output artifact:** `health-score-model.md`

## What this skill does
Predict which customers are at risk before they leave.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `customer-success-agent`.

## Procedure
1. Build the score from behaviour: usage depth, breadth, and frequency.
2. Weight by what actually predicted past churn, not by intuition.
3. Validate the score against historical outcomes.
4. Define the intervention triggered at each score band.
5. Recalibrate as the product and the customer base change.

## Output contract
Write `health-score-model.md` into `workspace/<venture-id>/gtm/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** health-scoring
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
- Weights validated against past churn
- Intervention defined per band
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `gtm` category
- Scaling a channel before its CAC is measured.
- Running a test with no kill criterion, so it never ends.
- Claiming differentiation that is not a reason anyone would switch.
