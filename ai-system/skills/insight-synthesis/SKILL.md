---
name: insight-synthesis
category: design
description: "Turn raw observation into insights that survive challenge."
output: "insights.md"
used_by:
  - design-researcher
---

# Insight Synthesis

**Category:** `design` · **Output artifact:** `insights.md`

## What this skill does
Turn raw observation into insights that survive challenge.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `design-researcher`.

## Procedure
1. Cluster observations by what the participant was trying to achieve.
2. Write each insight as an observation plus its implication for design.
3. Attach the supporting evidence and the number of participants behind it.
4. Mark insights that contradict the team's prior belief and lead with those.
5. State the confidence and what would overturn each insight.

## Output contract
Write `insights.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** insight-synthesis
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
- Insights carry evidence and participant counts
- Contradicting insights led with
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
