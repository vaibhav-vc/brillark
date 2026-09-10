---
name: disaster-recovery-testing
category: engineering
description: "Prove you can actually recover, not just that you have backups."
output: "dr-test-report.md"
used_by:
  - infra-devops-agent
---

# Disaster Recovery Testing

**Category:** `engineering` · **Output artifact:** `dr-test-report.md`

## What this skill does
Prove you can actually recover, not just that you have backups.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `infra-devops-agent`.

## Procedure
1. Define the recovery time and recovery point objectives.
2. Perform a real restore into a clean environment.
3. Verify data integrity and completeness after restore.
4. Measure the actual time taken against the objective.
5. Fix the gaps and schedule the next test.

## Output contract
Write `dr-test-report.md` into `workspace/<venture-id>/engineering/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** disaster-recovery-testing
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
- Real restore performed and verified
- Actual recovery time measured
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `engineering` category
- Designing for imagined scale instead of current load plus one order of magnitude.
- Skipping or quarantining a failing test to get a green build.
- Shipping without a verified way back.
