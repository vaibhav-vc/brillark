---
name: risk-scoring
category: risk
description: "Score risks consistently so they can be ranked."
output: "risk-scores.md"
used_by:
  - chief-risk-officer-agent
---

# Risk Scoring

**Category:** `risk` · **Output artifact:** `risk-scores.md`

## What this skill does
Score risks consistently so they can be ranked.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `chief-risk-officer-agent`.

## Procedure
1. Define likelihood and impact bands with concrete anchors.
2. Score each risk against the same anchors.
3. Compute expected loss rather than using a colour.
4. Check scores for consistency across domains.
5. Re-score after every material change to the plan.

## Output contract
Write `risk-scores.md` into `workspace/<venture-id>/risk/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** risk-scoring
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
- Bands anchored concretely
- Ranked by expected loss
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `risk` category
- A risk register that ranks by how loudly a risk was raised.
- Accepting a terminal risk implicitly by never classifying it.
- A continuity plan that has never been tested.
