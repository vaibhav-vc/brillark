---
name: agent-scorecard
category: orchestration
description: "Report how well each agent actually performs, from evidence."
output: "agent-scorecard.md"
used_by:
  - agent-performance-analyst
  - evaluation-harness-agent
---

# Agent Scorecard

`orchestration` · produces `agent-scorecard.md` · used by `agent-performance-analyst`, `evaluation-harness-agent`

Report how well each agent actually performs, from evidence.

## Procedure
1. Score evaluation results, handoff acceptance rate, and rework attribution.
2. Separate capability problems from context problems — a starved agent is not a bad agent.
3. Show the trend across cycles.
4. Identify the single highest-value improvement per agent.
5. Feed findings into agent definition changes, not into blame.

## Output contract
`agent-scorecard.md` → `workspace/<venture-id>/orchestration/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/orchestration.tsv`.

## Quality bar
- Context problems distinguished from capability
- One actionable improvement per agent
- The output states its confidence grade and names the evidence behind every load-bearing claim.
