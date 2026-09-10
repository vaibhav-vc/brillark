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

**Category:** `orchestration` · **Output artifact:** `routing-decision.md`

## What this skill does
Send a request to exactly one accountable agent, chosen from capability rather than convenience.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `intake-router`, `orchestration-head`.

## Procedure
1. Classify the request by domain, urgency, and reversibility.
2. Match the classification against the agent registry's capability entries.
3. Check current load and budget before assigning; a blocked owner is not an owner.
4. Name one accountable agent — never two, never a group.
5. Record the routing decision and the reason, so misroutes can be traced.

## Output contract
Write `routing-decision.md` into `workspace/<venture-id>/orchestration/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** agent-routing
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
- Exactly one accountable owner named
- Routing reason recorded and traceable
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `orchestration` category
- Assigning a task to a group instead of one accountable agent.
- Reporting progress as a percentage instead of as artifacts that exist.
- Adding a review layer to fix a problem that a clearer definition of done would solve.
