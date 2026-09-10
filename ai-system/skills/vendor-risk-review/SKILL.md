---
name: vendor-risk-review
category: strategy
description: "Assess what a vendor dependency actually exposes us to."
output: "vendor-risk.md"
used_by:
  - cto-agent
---

# Vendor Risk Review

**Category:** `strategy` · **Output artifact:** `vendor-risk.md`

## What this skill does
Assess what a vendor dependency actually exposes us to.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `cto-agent`.

## Procedure
1. Identify what breaks for customers if the vendor fails or changes terms.
2. Assess concentration: how much depends on this one supplier.
3. Check contractual protections, data portability, and notice periods.
4. Define the exit path and estimate the time and cost to execute it.
5. Set the monitoring signal for vendor deterioration.

## Output contract
Write `vendor-risk.md` into `workspace/<venture-id>/strategy/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** vendor-risk-review
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
- Exit path costed, not just identified
- Customer impact of failure assessed
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `strategy` category
- A strategy that states only what we will do, never what we will not.
- A moat described as a feature list rather than a compounding mechanism.
- Reviewing scenarios on a calendar instead of when an indicator trips.
