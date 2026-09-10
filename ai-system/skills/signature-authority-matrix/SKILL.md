---
name: signature-authority-matrix
category: compliance
description: "Make it unambiguous who may bind the company."
output: "signature-authority.md"
used_by:
  - corporate-secretary-agent
---

# Signature Authority Matrix

**Category:** `compliance` · **Output artifact:** `signature-authority.md`

## What this skill does
Make it unambiguous who may bind the company.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `corporate-secretary-agent`.

## Procedure
1. Define the categories of commitment and their value thresholds.
2. Assign signing authority per category and threshold.
3. Require dual authorisation above defined limits.
4. Record delegations and their expiry.
5. Communicate the matrix so counterparties are not misled.

## Output contract
Write `signature-authority.md` into `workspace/<venture-id>/compliance/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** signature-authority-matrix
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
- Dual authorisation above defined limits
- Delegations recorded with expiry
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `compliance` category
- Writing a policy nobody can follow and treating publication as compliance.
- Collecting evidence at audit time rather than as the control operates.
- Building controls for a framework that was never shown to apply.
