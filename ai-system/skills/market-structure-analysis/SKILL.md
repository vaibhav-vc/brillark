---
name: market-structure-analysis
category: strategy
description: "Understand who captures value in this market and why."
output: "market-structure.md"
used_by:
  - chief-strategy-officer-agent
---

# Market Structure Analysis

**Category:** `strategy` · **Output artifact:** `market-structure.md`

## What this skill does
Understand who captures value in this market and why.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `chief-strategy-officer-agent`.

## Procedure
1. Map the value chain from raw input to end customer.
2. Identify where margin actually accumulates and what protects it.
3. Assess the bargaining power at each link.
4. Determine where we sit and whether that position can hold.
5. Identify the structural shift that could change the answer.

## Output contract
Write `market-structure.md` into `workspace/<venture-id>/strategy/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** market-structure-analysis
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
- Margin capture located in the chain
- Positional durability assessed
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `strategy` category
- A strategy that states only what we will do, never what we will not.
- A moat described as a feature list rather than a compounding mechanism.
- Reviewing scenarios on a calendar instead of when an indicator trips.
