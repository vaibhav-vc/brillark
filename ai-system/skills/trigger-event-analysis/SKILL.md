---
name: trigger-event-analysis
category: market
description: "Find the moment that makes a buyer start looking."
output: "trigger-events.md"
used_by:
  - icp-persona-builder
---

# Trigger Event Analysis

**Category:** `market` · **Output artifact:** `trigger-events.md`

## What this skill does
Find the moment that makes a buyer start looking.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `icp-persona-builder`.

## Procedure
1. Ask every interviewee what changed just before they went looking.
2. Group triggers into types: growth, failure, regulation, personnel change.
3. Assess which triggers are detectable from outside.
4. Design the outreach to arrive shortly after the detectable ones.
5. Measure conversion by trigger type.

## Output contract
Write `trigger-events.md` into `workspace/<venture-id>/market/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** trigger-event-analysis
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
- Triggers grounded in interview evidence
- Detectability assessed per trigger
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `market` category
- Treating stated intent as evidence of demand.
- Sizing a market top-down and calling it bottom-up.
- Interviewing people who could never buy, then counting their enthusiasm.
