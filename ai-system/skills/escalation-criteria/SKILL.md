---
name: escalation-criteria
category: orchestration
description: "Define what must go up, to whom, and how fast."
output: "escalation-policy.md"
used_by:
  - escalation-manager
---

# Escalation Criteria

`orchestration` · produces `escalation-policy.md` · used by `escalation-manager`

Define what must go up, to whom, and how fast.

## Procedure
1. Define severity levels by consequence, not by emotion.
2. Map each severity to a decision-maker and a response deadline.
3. Specify what must accompany an escalation at each level.
4. Define what explicitly does not escalate, to protect the signal.
5. Review the criteria when escalation volume rises or falls sharply.

## Output contract
`escalation-policy.md` → `workspace/<venture-id>/orchestration/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/orchestration.tsv`.

## Quality bar
- Severity defined by consequence
- Non-escalating cases defined too
- The output states its confidence grade and names the evidence behind every load-bearing claim.
