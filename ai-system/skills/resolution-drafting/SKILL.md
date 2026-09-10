---
name: resolution-drafting
category: compliance
description: "Draft a resolution that is unambiguous and effective."
output: "resolution.md"
used_by:
  - corporate-secretary-agent
---

# Resolution Drafting

**Category:** `compliance` · **Output artifact:** `resolution.md`

## What this skill does
Draft a resolution that is unambiguous and effective.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `corporate-secretary-agent`.

## Procedure
1. State the action being authorised precisely.
2. State the authority under which it is made.
3. Name who is authorised to execute it and within what limits.
4. Include the effective date and any conditions.
5. Check consistency with the governing documents before adoption.

## Output contract
Write `resolution.md` into `workspace/<venture-id>/compliance/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** resolution-drafting
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
- Execution authority named with limits
- Consistency with governing documents checked
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `compliance` category
- Writing a policy nobody can follow and treating publication as compliance.
- Collecting evidence at audit time rather than as the control operates.
- Building controls for a framework that was never shown to apply.
