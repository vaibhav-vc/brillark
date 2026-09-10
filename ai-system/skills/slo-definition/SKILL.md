---
name: slo-definition
category: engineering
description: "Define reliability targets from what users actually notice."
output: "slo.md"
used_by:
  - observability-agent
---

# Slo Definition

**Category:** `engineering` · **Output artifact:** `slo.md`

## What this skill does
Define reliability targets from what users actually notice.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `observability-agent`.

## Procedure
1. Identify the critical user journeys.
2. Define the indicator that reflects user experience for each.
3. Set the objective from user expectation and business need, not from what is easy.
4. Derive the error budget and agree what happens when it is spent.
5. Review quarterly against actual performance and user complaints.

## Output contract
Write `slo.md` into `workspace/<venture-id>/engineering/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** slo-definition
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
- Indicators reflect user experience
- Error budget consequence agreed in advance
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `engineering` category
- Designing for imagined scale instead of current load plus one order of magnitude.
- Skipping or quarantining a failing test to get a green build.
- Shipping without a verified way back.
