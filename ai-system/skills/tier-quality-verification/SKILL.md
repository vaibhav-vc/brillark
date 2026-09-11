---
name: tier-quality-verification
category: efficiency
description: "Prove a demotion did not cost quality."
output: "tier-verification.md"
used_by:
  - model-router-tuner
---

# Tier Quality Verification

**Category:** `efficiency` · **Output artifact:** `tier-verification.md`

## What this skill does
Prove a demotion did not cost quality.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `model-router-tuner`.

## Procedure
1. Run the full golden case set at both tiers.
2. Compare per case, not in aggregate.
3. Check the hardest cases specifically; averages hide their failure.
4. Check escalation frequency stayed within the expected range.
5. Revert the demotion if either check fails.

## Output contract
Write `tier-verification.md` into `workspace/<venture-id>/efficiency/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** tier-quality-verification
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
- Hardest cases checked specifically
- Demotion reverted on any failed check
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `efficiency` category
- Measuring cost per call instead of cost per completed task.
- Demoting a model tier without checking the hardest cases.
- Trimming context by hand instead of fixing the rule that loaded it.
