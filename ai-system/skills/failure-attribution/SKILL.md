---
name: failure-attribution
category: improvement
description: "Determine whether a failure was capability, context, or task definition — because the fixes are different."
output: "attribution-report.md"
used_by:
  - agent-performance-analyst
---

# Failure Attribution

`improvement` · produces `attribution-report.md` · used by `agent-performance-analyst`

Determine whether a failure was capability, context, or task definition — because the fixes are different.

## Procedure
1. Reconstruct what the agent was given and what it produced.
2. Check whether the required information was in the context package at all.
3. Check whether the task and its definition of done were unambiguous.
4. Only when both hold, attribute the failure to the agent's capability.
5. Record the attribution and route the fix to whoever owns that cause.

## Output contract
`attribution-report.md` → `workspace/<venture-id>/improvement/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/improvement.tsv`.

## Quality bar
- Context and task definition ruled out before blaming capability
- Fix routed to the owner of the actual cause
- The output states its confidence grade and names the evidence behind every load-bearing claim.
