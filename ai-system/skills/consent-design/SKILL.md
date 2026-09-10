---
name: consent-design
category: compliance
description: "Design consent that is genuine rather than assumed."
output: "consent-design.md"
used_by:
  - data-protection-officer-agent
---

# Consent Design

**Category:** `compliance` · **Output artifact:** `consent-design.md`

## What this skill does
Design consent that is genuine rather than assumed.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `data-protection-officer-agent`.

## Procedure
1. Make consent specific to each purpose, not bundled.
2. Ensure it is freely given — service must not be conditional on unnecessary consent.
3. Make withdrawal as easy as giving it.
4. Record what was consented to, when, and in what wording.
5. Re-obtain consent when the purpose changes.

## Output contract
Write `consent-design.md` into `workspace/<venture-id>/compliance/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** consent-design
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
- Consent unbundled per purpose
- Withdrawal as easy as granting
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `compliance` category
- Writing a policy nobody can follow and treating publication as compliance.
- Collecting evidence at audit time rather than as the control operates.
- Building controls for a framework that was never shown to apply.
