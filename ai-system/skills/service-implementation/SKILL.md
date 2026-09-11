---
name: service-implementation
category: engineering
description: "Build the server-side behaviour to match the contract exactly."
output: "service-code"
used_by:
  - backend-implementation-agent
---

# Service Implementation

`engineering` · produces `service-code` · used by `backend-implementation-agent`

Build the server-side behaviour to match the contract exactly.

## Procedure
1. Implement against the specification, not against an assumption of intent.
2. Validate every input at the boundary and reject clearly.
3. Make write paths idempotent where retries are possible.
4. Fail loudly and specifically rather than swallowing errors.
5. Instrument the decision points, not just the entry and exit.

## Output contract
`service-code` → `workspace/<venture-id>/engineering/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/engineering.tsv`.

## Quality bar
- Behaviour matches the specification exactly
- Decision points instrumented
- The output states its confidence grade and names the evidence behind every load-bearing claim.
