---
name: dissent-recording
category: council
description: "Preserve minority positions on the record."
output: "dissent-log.md"
used_by:
  - council-director
  - council-synthesis-arbiter
---

# Dissent Recording

**Category:** `council` · **Output artifact:** `dissent-log.md`

## What this skill does
Preserve minority positions on the record.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `council-director`, `council-synthesis-arbiter`.

## Procedure
1. Record the dissenting position in the dissenter's own words.
2. Record what evidence would vindicate it.
3. Note who overruled it and on what basis.
4. Keep it attached to the decision permanently.
5. Review dissent when the decision's outcome becomes known.

## Output contract
Write `dissent-log.md` into `workspace/<venture-id>/council/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** dissent-recording
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
- Dissent recorded verbatim
- Vindicating evidence stated
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `council` category
- An objection stated as an adjective rather than a concrete failure sequence.
- Criticism offered with no remedy at any cost level.
- Averaging two positions instead of testing which survives the evidence.
