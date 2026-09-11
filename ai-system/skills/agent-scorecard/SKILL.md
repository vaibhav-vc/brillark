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

**Category:** `orchestration` · **Output artifact:** `agent-scorecard.md`

## What this skill does
Report how well each agent actually performs, from evidence.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `agent-performance-analyst`, `evaluation-harness-agent`.

## Procedure
1. Score evaluation results, handoff acceptance rate, and rework attribution.
2. Separate capability problems from context problems — a starved agent is not a bad agent.
3. Show the trend across cycles.
4. Identify the single highest-value improvement per agent.
5. Feed findings into agent definition changes, not into blame.

## Output contract
Write `agent-scorecard.md` into `workspace/<venture-id>/orchestration/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** agent-scorecard
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
- Context problems distinguished from capability
- One actionable improvement per agent
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `orchestration` category
- Assigning a task to a group instead of one accountable agent.
- Reporting progress as a percentage instead of as artifacts that exist.
- Adding a review layer to fix a problem that a clearer definition of done would solve.
