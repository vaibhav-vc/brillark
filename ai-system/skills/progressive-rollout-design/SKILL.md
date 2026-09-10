---
name: progressive-rollout-design
category: engineering
description: "Expose a change gradually so problems are found by few, not by all."
output: "rollout-plan.md"
used_by:
  - release-manager
---

# Progressive Rollout Design

**Category:** `engineering` · **Output artifact:** `rollout-plan.md`

## What this skill does
Expose a change gradually so problems are found by few, not by all.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `release-manager`.

## Procedure
1. Define the exposure stages and the population at each.
2. Define the signals watched at each stage and their thresholds.
3. Set the minimum soak time per stage.
4. Define the automatic rollback condition.
5. Decouple deployment from exposure using flags.

## Output contract
Write `rollout-plan.md` into `workspace/<venture-id>/engineering/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** progressive-rollout-design
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
- Automatic rollback condition defined
- Soak time set per stage
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `engineering` category
- Designing for imagined scale instead of current load plus one order of magnitude.
- Skipping or quarantining a failing test to get a green build.
- Shipping without a verified way back.
