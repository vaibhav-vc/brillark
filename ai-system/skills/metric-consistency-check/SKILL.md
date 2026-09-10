---
name: metric-consistency-check
category: compliance
description: "Verify a reported metric means the same thing it did last period."
output: "consistency-check.md"
used_by:
  - investor-reporting-agent
---

# Metric Consistency Check

**Category:** `compliance` · **Output artifact:** `consistency-check.md`

## What this skill does
Verify a reported metric means the same thing it did last period.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `investor-reporting-agent`.

## Procedure
1. Compare the current definition to the one used previously.
2. Check the source data and the filters have not changed.
3. Identify any restatement and disclose it explicitly.
4. Verify the same number appears identically across documents.
5. Block publication until inconsistencies are resolved.

## Output contract
Write `consistency-check.md` into `workspace/<venture-id>/compliance/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** metric-consistency-check
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
- Restatements disclosed explicitly
- Cross-document consistency verified
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `compliance` category
- Writing a policy nobody can follow and treating publication as compliance.
- Collecting evidence at audit time rather than as the control operates.
- Building controls for a framework that was never shown to apply.
