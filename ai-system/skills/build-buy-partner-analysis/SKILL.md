---
name: build-buy-partner-analysis
category: strategy
description: "Decide whether to build a capability, buy it, or partner for it."
output: "build-buy-partner.md"
used_by:
  - cto-agent
---

# Build Buy Partner Analysis

**Category:** `strategy` · **Output artifact:** `build-buy-partner.md`

## What this skill does
Decide whether to build a capability, buy it, or partner for it.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `cto-agent`.

## Procedure
1. Assess whether the capability is differentiating — customers pay for it — or merely necessary.
2. Estimate the true cost to build, including maintenance for three years.
3. Evaluate the buy option's fit, lock-in, and exit path.
4. Evaluate the partner option's incentive alignment and dependency risk.
5. Decide, and record the condition that would reverse the decision.

## Output contract
Write `build-buy-partner.md` into `workspace/<venture-id>/strategy/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** build-buy-partner-analysis
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
- Differentiation assessed first
- Three-year maintenance cost included
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `strategy` category
- A strategy that states only what we will do, never what we will not.
- A moat described as a feature list rather than a compounding mechanism.
- Reviewing scenarios on a calendar instead of when an indicator trips.
