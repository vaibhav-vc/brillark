---
name: agent-routing
category: orchestration
description: "Send a request to exactly one accountable agent, chosen from capability rather than convenience."
output: "routing-decision.md"
used_by:
  - intake-router
  - orchestration-head
---

# Agent Routing

`orchestration` · produces `routing-decision.md` · used by `intake-router`, `orchestration-head`

Send a request to exactly one accountable agent, chosen from capability rather than convenience.

## Procedure
1. Classify the request by domain, urgency, and reversibility.
2. Match the classification against the agent registry's capability entries.
3. Check current load and budget before assigning; a blocked owner is not an owner.
4. Name one accountable agent — never two, never a group.
5. Record the routing decision and the reason, so misroutes can be traced.

## Output contract
`routing-decision.md` → `workspace/<venture-id>/orchestration/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/orchestration.tsv`.

## Quality bar
- Exactly one accountable owner named
- Routing reason recorded and traceable
- The output states its confidence grade and names the evidence behind every load-bearing claim.
