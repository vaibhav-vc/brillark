---
name: memory-conflict-resolution
category: memory
description: "Resolve two stored facts that cannot both be true."
output: "conflict-resolution.md"
used_by:
  - orchestration-head
---

# Memory Conflict Resolution

`memory` · produces `conflict-resolution.md` · used by `orchestration-head`

Resolve two stored facts that cannot both be true.

## Procedure
1. Detect the conflict at write time by comparing against existing claims.
2. Compare provenance: evidence grade, recency, and author authority.
3. Prefer measured over sourced over estimated, and recent over old for volatile facts.
4. Supersede the loser explicitly with a pointer to the winner — never keep both silently.
5. Escalate to the domain head when both claims are equally well evidenced.

## Output contract
`conflict-resolution.md` → `workspace/<venture-id>/memory/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/memory.tsv`.

## Quality bar
- Loser superseded, not deleted or duplicated
- Equal-evidence conflicts escalated
- The output states its confidence grade and names the evidence behind every load-bearing claim.
