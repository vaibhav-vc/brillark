---
name: risk-scoring
category: risk
description: "Score risks consistently so they can be ranked."
output: "risk-scores.md"
used_by:
  - chief-risk-officer-agent
---

# Risk Scoring

`risk` · produces `risk-scores.md` · used by `chief-risk-officer-agent`

Score risks consistently so they can be ranked.

## Procedure
1. Define likelihood and impact bands with concrete anchors.
2. Score each risk against the same anchors.
3. Compute expected loss rather than using a colour.
4. Check scores for consistency across domains.
5. Re-score after every material change to the plan.

## Output contract
`risk-scores.md` → `workspace/<venture-id>/risk/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/risk.tsv`.

## Quality bar
- Bands anchored concretely
- Ranked by expected loss
- The output states its confidence grade and names the evidence behind every load-bearing claim.
