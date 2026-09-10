---
name: secrets-management
category: engineering
description: "Keep credentials out of reach and rotatable."
output: "secrets-policy.md"
used_by:
  - security-engineer
---

# Secrets Management

**Category:** `engineering` · **Output artifact:** `secrets-policy.md`

## What this skill does
Keep credentials out of reach and rotatable.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `security-engineer`.

## Procedure
1. Inventory every secret and where it is used.
2. Move all secrets into a managed store with access control.
3. Scan the repository history, not just the current state.
4. Define and actually run a rotation schedule.
5. Ensure secrets never appear in logs, errors, or client bundles.

## Output contract
Write `secrets-policy.md` into `workspace/<venture-id>/engineering/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** secrets-management
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
- Repository history scanned
- Rotation schedule actually executed
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `engineering` category
- Designing for imagined scale instead of current load plus one order of magnitude.
- Skipping or quarantining a failing test to get a green build.
- Shipping without a verified way back.
