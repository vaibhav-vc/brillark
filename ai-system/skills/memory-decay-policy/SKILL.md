---
name: memory-decay-policy
category: memory
description: "Expire stale context deliberately, because trusted-but-wrong is worse than missing."
output: "decay-policy.md"
used_by:
  - context-memory-curator
---

# Memory Decay Policy

`memory` · produces `decay-policy.md` · used by `context-memory-curator`

Expire stale context deliberately, because trusted-but-wrong is worse than missing.

## Procedure
1. Assign a shelf life per memory type — market data decays faster than a decision record.
2. Mark memories past shelf life as stale rather than deleting them silently.
3. Require re-verification before a stale memory is used in a decision.
4. Archive rather than destroy, so history remains auditable.
5. Review decay settings when a stale memory causes an error.

## Output contract
`decay-policy.md` → `workspace/<venture-id>/memory/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/memory.tsv`.

## Quality bar
- Shelf life set per memory type
- Stale memories quarantined, not silently used
- The output states its confidence grade and names the evidence behind every load-bearing claim.
