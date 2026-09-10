---
name: message-hierarchy
category: gtm
description: "Structure the message from headline claim to supporting proof."
output: "message-hierarchy.md"
used_by:
  - positioning-messaging-agent
---

# Message Hierarchy

**Category:** `gtm` · **Output artifact:** `message-hierarchy.md`

## What this skill does
Structure the message from headline claim to supporting proof.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `positioning-messaging-agent`.

## Procedure
1. State one headline claim; more than one means none will land.
2. Support it with at most three pillars.
3. Attach specific proof under each pillar.
4. Write the version for each audience without changing the spine.
5. Cut anything that does not support the headline.

## Output contract
Write `message-hierarchy.md` into `workspace/<venture-id>/gtm/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** message-hierarchy
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
- Exactly one headline claim
- Proof attached to every pillar
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `gtm` category
- Scaling a channel before its CAC is measured.
- Running a test with no kill criterion, so it never ends.
- Claiming differentiation that is not a reason anyone would switch.
