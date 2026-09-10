---
name: claim-substantiation-planning
category: market
description: "Decide what proof each marketing claim needs before it is made."
output: "claim-proof-plan.md"
used_by:
  - value-proposition-designer
---

# Claim Substantiation Planning

**Category:** `market` · **Output artifact:** `claim-proof-plan.md`

## What this skill does
Decide what proof each marketing claim needs before it is made.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `value-proposition-designer`.

## Procedure
1. List every claim the messaging makes, including implied ones.
2. Classify each as measurable, comparative, or subjective.
3. Define the proof required per claim: data, case study, benchmark, or guarantee.
4. Identify claims that cannot be proven and cut them.
5. Assign an owner and a deadline to gather each proof.

## Output contract
Write `claim-proof-plan.md` into `workspace/<venture-id>/market/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** claim-substantiation-planning
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
- Implied claims included
- Unprovable claims cut, not softened
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `market` category
- Treating stated intent as evidence of demand.
- Sizing a market top-down and calling it bottom-up.
- Interviewing people who could never buy, then counting their enthusiasm.
