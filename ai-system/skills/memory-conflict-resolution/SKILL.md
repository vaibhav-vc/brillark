---
name: memory-conflict-resolution
category: memory
description: "Resolve two stored facts that cannot both be true."
output: "conflict-resolution.md"
used_by:
  - orchestration-head
---

# Memory Conflict Resolution

**Category:** `memory` · **Output artifact:** `conflict-resolution.md`

## What this skill does
Resolve two stored facts that cannot both be true.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `orchestration-head`.

## Procedure
1. Detect the conflict at write time by comparing against existing claims.
2. Compare provenance: evidence grade, recency, and author authority.
3. Prefer measured over sourced over estimated, and recent over old for volatile facts.
4. Supersede the loser explicitly with a pointer to the winner — never keep both silently.
5. Escalate to the domain head when both claims are equally well evidenced.

## Output contract
Write `conflict-resolution.md` into `workspace/<venture-id>/memory/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** memory-conflict-resolution
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
- Loser superseded, not deleted or duplicated
- Equal-evidence conflicts escalated
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `memory` category
- Storing a claim without provenance, so nobody can later tell whether to trust it.
- Keeping two contradicting facts because resolving them is inconvenient.
- Treating a stale memory as current because it is well written.
