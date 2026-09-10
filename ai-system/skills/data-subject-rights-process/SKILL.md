---
name: data-subject-rights-process
category: compliance
description: "Build a rights request process that actually works."
output: "rights-process.md"
used_by:
  - data-protection-officer-agent
---

# Data Subject Rights Process

**Category:** `compliance` · **Output artifact:** `rights-process.md`

## What this skill does
Build a rights request process that actually works.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `data-protection-officer-agent`.

## Procedure
1. Define the intake channel and how requests are identified.
2. Define identity verification proportionate to the request.
3. Map where personal data lives so a request can be fulfilled completely.
4. Set the internal deadline ahead of the statutory one.
5. Test the process end to end with a real request.

## Output contract
Write `rights-process.md` into `workspace/<venture-id>/compliance/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** data-subject-rights-process
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
- Complete data map enables full fulfilment
- Process tested end to end
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `compliance` category
- Writing a policy nobody can follow and treating publication as compliance.
- Collecting evidence at audit time rather than as the control operates.
- Building controls for a framework that was never shown to apply.
