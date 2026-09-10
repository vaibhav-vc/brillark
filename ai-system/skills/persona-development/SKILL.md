---
name: persona-development
category: market
description: "Describe the people involved in the purchase and what each one needs."
output: "personas.md"
used_by:
  - icp-persona-builder
---

# Persona Development

**Category:** `market` · **Output artifact:** `personas.md`

## What this skill does
Describe the people involved in the purchase and what each one needs.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `icp-persona-builder`.

## Procedure
1. Separate the buyer, the user, the influencer, and the blocker.
2. For each, capture their goal, their risk, and what makes them say no.
3. Ground every attribute in interview evidence, not imagination.
4. Record their vocabulary for the problem.
5. Note where each persona goes for information.

## Output contract
Write `personas.md` into `workspace/<venture-id>/market/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** persona-development
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
- Every attribute traced to evidence
- Blocker persona included
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `market` category
- Treating stated intent as evidence of demand.
- Sizing a market top-down and calling it bottom-up.
- Interviewing people who could never buy, then counting their enthusiasm.
