---
name: icp-definition
category: market
description: "Define the customer precisely enough to build a target list."
output: "icp.md"
used_by:
  - icp-persona-builder
---

# Icp Definition

**Category:** `market` · **Output artifact:** `icp.md`

## What this skill does
Define the customer precisely enough to build a target list.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `icp-persona-builder`.

## Procedure
1. Specify firmographic and behavioural attributes you can actually filter on.
2. Add the trigger condition that makes them start looking.
3. Write the disqualification criteria explicitly.
4. Verify you can name a list, community, or channel where they exist.
5. Test the definition against known good and bad customers.

## Output contract
Write `icp.md` into `workspace/<venture-id>/market/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** icp-definition
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
- Filterable against a real list
- Disqualification criteria explicit
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `market` category
- Treating stated intent as evidence of demand.
- Sizing a market top-down and calling it bottom-up.
- Interviewing people who could never buy, then counting their enthusiasm.
