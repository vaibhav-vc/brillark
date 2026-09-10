---
name: infrastructure-rightsizing
category: engineering
description: "Match provisioned capacity to actual demand."
output: "rightsizing-report.md"
used_by:
  - cost-optimization-analyst
  - infra-devops-agent
---

# Infrastructure Rightsizing

**Category:** `engineering` · **Output artifact:** `rightsizing-report.md`

## What this skill does
Match provisioned capacity to actual demand.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `cost-optimization-analyst`, `infra-devops-agent`.

## Procedure
1. Measure actual utilisation over a representative period, including peaks.
2. Identify idle, over-provisioned, and orphaned resources.
3. Distinguish waste from headroom deliberately held for spikes.
4. Resize incrementally and verify performance after each change.
5. Set alerts so drift is caught before it accumulates.

## Output contract
Write `rightsizing-report.md` into `workspace/<venture-id>/engineering/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** infrastructure-rightsizing
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
- Headroom distinguished from waste
- Performance verified after each change
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `engineering` category
- Designing for imagined scale instead of current load plus one order of magnitude.
- Skipping or quarantining a failing test to get a green build.
- Shipping without a verified way back.
