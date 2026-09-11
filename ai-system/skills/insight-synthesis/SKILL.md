---
name: insight-synthesis
category: design
description: "Turn raw observation into insights that survive challenge."
output: "insights.md"
used_by:
  - design-researcher
---

# Insight Synthesis

`design` · produces `insights.md` · used by `design-researcher`

Turn raw observation into insights that survive challenge.

## Procedure
1. Cluster observations by what the participant was trying to achieve.
2. Write each insight as an observation plus its implication for design.
3. Attach the supporting evidence and the number of participants behind it.
4. Mark insights that contradict the team's prior belief and lead with those.
5. State the confidence and what would overturn each insight.

## Output contract
`insights.md` → `workspace/<venture-id>/design/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/design.tsv`.

## Quality bar
- Insights carry evidence and participant counts
- Contradicting insights led with
- The output states its confidence grade and names the evidence behind every load-bearing claim.
