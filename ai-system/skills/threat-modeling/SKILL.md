---
name: threat-modeling
category: engineering
description: "Work out how a system could be attacked, before building it."
output: "threat-model.md"
used_by:
  - ciso-agent
  - engineering-head
  - security-engineer
---

# Threat Modeling

**Category:** `engineering` · **Output artifact:** `threat-model.md`

## What this skill does
Work out how a system could be attacked, before building it.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `ciso-agent`, `engineering-head`, `security-engineer`.

## Procedure
1. Draw the data flow and mark every trust boundary.
2. Enumerate threats per element using a structured method such as STRIDE.
3. Rate each by impact and likelihood in our actual context.
4. Define the control for each threat above the threshold.
5. Record accepted risks with an owner and an expiry date.

## Output contract
Write `threat-model.md` into `workspace/<venture-id>/engineering/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** threat-modeling
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
- Trust boundaries explicitly marked
- Accepted risks have owners and expiry
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `engineering` category
- Designing for imagined scale instead of current load plus one order of magnitude.
- Skipping or quarantining a failing test to get a green build.
- Shipping without a verified way back.
