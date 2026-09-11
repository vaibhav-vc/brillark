---
name: context-packaging
category: orchestration
description: "Assemble everything an agent needs so it never has to rediscover known facts."
output: "context-package.json"
used_by:
  - handoff-coordinator
  - intake-router
  - orchestration-head
---

# Context Packaging

`orchestration` · produces `context-package.json` · used by `handoff-coordinator`, `intake-router`, `orchestration-head`

Assemble everything an agent needs so it never has to rediscover known facts.

## Procedure
1. Pull the task brief, its DoD, and its inputs.
2. Retrieve relevant semantic memory, decisions, and prior attempts.
3. Include the constraints in force and the assumptions already accepted.
4. List the open questions being carried forward.
5. Trim anything not needed — an oversized package is as bad as an empty one.

## Output contract
`context-package.json` → `workspace/<venture-id>/orchestration/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/orchestration.tsv`.

## Quality bar
- Prior attempts included
- Package trimmed to what is needed
- The output states its confidence grade and names the evidence behind every load-bearing claim.
