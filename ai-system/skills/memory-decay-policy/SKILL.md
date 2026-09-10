---
name: memory-decay-policy
category: memory
description: "Expire stale context deliberately, because trusted-but-wrong is worse than missing."
output: "decay-policy.md"
used_by:
  - context-memory-curator
---

# Memory Decay Policy

**Category:** `memory` · **Output artifact:** `decay-policy.md`

## What this skill does
Expire stale context deliberately, because trusted-but-wrong is worse than missing.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `context-memory-curator`.

## Procedure
1. Assign a shelf life per memory type — market data decays faster than a decision record.
2. Mark memories past shelf life as stale rather than deleting them silently.
3. Require re-verification before a stale memory is used in a decision.
4. Archive rather than destroy, so history remains auditable.
5. Review decay settings when a stale memory causes an error.

## Output contract
Write `decay-policy.md` into `workspace/<venture-id>/memory/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** memory-decay-policy
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
- Shelf life set per memory type
- Stale memories quarantined, not silently used
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `memory` category
- Storing a claim without provenance, so nobody can later tell whether to trust it.
- Keeping two contradicting facts because resolving them is inconvenient.
- Treating a stale memory as current because it is well written.
