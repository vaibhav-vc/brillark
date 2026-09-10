---
name: minute-taking
category: compliance
description: "Record decisions so the corporate record is accurate."
output: "minutes.md"
used_by:
  - corporate-secretary-agent
---

# Minute Taking

**Category:** `compliance` · **Output artifact:** `minutes.md`

## What this skill does
Record decisions so the corporate record is accurate.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `corporate-secretary-agent`.

## Procedure
1. Record attendance, quorum, and the time.
2. Record the decision made, not the discussion around it.
3. Record any conflict of interest declared and how it was handled.
4. Record dissent and abstention where they occurred.
5. Circulate promptly for approval while memories are accurate.

## Output contract
Write `minutes.md` into `workspace/<venture-id>/compliance/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** minute-taking
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
- Decisions recorded, not discussion narrative
- Conflicts and dissent recorded
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `compliance` category
- Writing a policy nobody can follow and treating publication as compliance.
- Collecting evidence at audit time rather than as the control operates.
- Building controls for a framework that was never shown to apply.
