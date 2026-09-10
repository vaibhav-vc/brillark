---
name: partner-qualification
category: gtm
description: "Decide whether a candidate partner is worth the effort."
output: "partner-qualification.md"
used_by:
  - partnership-bd-agent
---

# Partner Qualification

**Category:** `gtm` · **Output artifact:** `partner-qualification.md`

## What this skill does
Decide whether a candidate partner is worth the effort.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `partnership-bd-agent`.

## Procedure
1. Verify they actually reach our ICP at meaningful volume.
2. Check the mutual incentive: what do they lose by not doing this?
3. Assess their capacity to execute, not just their willingness to sign.
4. Check for conflicts with their existing partners or roadmap.
5. Score and rank rather than pursuing everyone who responds.

## Output contract
Write `partner-qualification.md` into `workspace/<venture-id>/gtm/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** partner-qualification
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
- Mutual incentive verified
- Execution capacity assessed, not just intent
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `gtm` category
- Scaling a channel before its CAC is measured.
- Running a test with no kill criterion, so it never ends.
- Claiming differentiation that is not a reason anyone would switch.
