---
name: control-framework-design
category: compliance
description: "Build the controls that make compliance demonstrable."
output: "control-framework.md"
used_by:
  - chief-compliance-officer-agent
---

# Control Framework Design

**Category:** `compliance` · **Output artifact:** `control-framework.md`

## What this skill does
Build the controls that make compliance demonstrable.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `chief-compliance-officer-agent`.

## Procedure
1. Map each applicable requirement to exactly one control.
2. Design the control to be evidenced automatically where possible.
3. Assign an owner and an operating frequency to each control.
4. Define what evidence proves the control operated.
5. Avoid duplicate controls serving the same requirement.

## Output contract
Write `control-framework.md` into `workspace/<venture-id>/compliance/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** control-framework-design
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
- One control per requirement
- Evidence definition per control
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `compliance` category
- Writing a policy nobody can follow and treating publication as compliance.
- Collecting evidence at audit time rather than as the control operates.
- Building controls for a framework that was never shown to apply.
