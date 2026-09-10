---
name: evidence-collection
category: compliance
description: "Gather proof that controls actually operated."
output: "evidence-register.md"
used_by:
  - chief-compliance-officer-agent
---

# Evidence Collection

**Category:** `compliance` · **Output artifact:** `evidence-register.md`

## What this skill does
Gather proof that controls actually operated.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `chief-compliance-officer-agent`.

## Procedure
1. Define the evidence artifact for each control in advance.
2. Automate collection where the control is technical.
3. Timestamp and store evidence immutably.
4. Check completeness periodically rather than at audit time.
5. Flag controls with no evidence as failed controls.

## Output contract
Write `evidence-register.md` into `workspace/<venture-id>/compliance/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** evidence-collection
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
- Evidence defined before the period begins
- Missing evidence treated as control failure
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `compliance` category
- Writing a policy nobody can follow and treating publication as compliance.
- Collecting evidence at audit time rather than as the control operates.
- Building controls for a framework that was never shown to apply.
