---
name: routing-telemetry-review
category: efficiency
description: "Check the routing is working in practice."
output: "routing-review.md"
used_by:
  - model-router-tuner
---

# Routing Telemetry Review

**Category:** `efficiency` · **Output artifact:** `routing-review.md`

## What this skill does
Check the routing is working in practice.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `model-router-tuner`.

## Procedure
1. Review escalation frequency per agent against expectation.
2. Identify agents escalating constantly — they were demoted too far.
3. Identify expensive-tier agents whose work never needed it.
4. Check routing decisions against outcome quality.
5. Propose reassignments with the evidence.

## Output contract
Write `routing-review.md` into `workspace/<venture-id>/efficiency/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** routing-telemetry-review
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
- Over-escalating agents identified
- Over-provisioned agents identified
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `efficiency` category
- Measuring cost per call instead of cost per completed task.
- Demoting a model tier without checking the hardest cases.
- Trimming context by hand instead of fixing the rule that loaded it.
