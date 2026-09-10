---
name: customer-discovery-interview
category: market
description: "Learn what customers actually do, without leading them or selling."
output: "interview-notes.md"
used_by:
  - business-head
  - customer-discovery-interviewer
---

# Customer Discovery Interview

**Category:** `market` · **Output artifact:** `interview-notes.md`

## What this skill does
Learn what customers actually do, without leading them or selling.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `business-head`, `customer-discovery-interviewer`.

## Procedure
1. Screen the participant against the ICP before booking.
2. Ask about specific past events: the last time the problem occurred.
3. Follow the workaround — what they built, bought, or endured.
4. Never pitch; the moment you sell, the data stops.
5. Record verbatim and extract evidence immediately after, while context is fresh.

## Output contract
Write `interview-notes.md` into `workspace/<venture-id>/market/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** customer-discovery-interview
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
- Questions about past behaviour, not future intent
- No pitching during the session
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `market` category
- Treating stated intent as evidence of demand.
- Sizing a market top-down and calling it bottom-up.
- Interviewing people who could never buy, then counting their enthusiasm.
