---
name: moat-thesis
category: strategy
description: "State the defensibility as a mechanism, not as a feature list."
output: "moat-thesis.md"
used_by:
  - chief-strategy-officer-agent
---

# Moat Thesis

**Category:** `strategy` · **Output artifact:** `moat-thesis.md`

## What this skill does
State the defensibility as a mechanism, not as a feature list.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `chief-strategy-officer-agent`.

## Procedure
1. Identify the candidate mechanism: network effect, switching cost, scale economy, brand, or proprietary data.
2. Explain how it strengthens as we grow, specifically.
3. Estimate how long a well-funded competitor would need to replicate it.
4. Identify what would erode it.
5. State the evidence that it is actually forming, not just intended.

## Output contract
Write `moat-thesis.md` into `workspace/<venture-id>/strategy/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** moat-thesis
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
- Mechanism compounds with scale
- Formation evidence, not intention
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `strategy` category
- A strategy that states only what we will do, never what we will not.
- A moat described as a feature list rather than a compounding mechanism.
- Reviewing scenarios on a calendar instead of when an indicator trips.
