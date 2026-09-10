---
name: source-grading
category: market
description: "Rate how much a source can be trusted before using it in an argument."
output: "source-grades.md"
used_by:
  - market-researcher
---

# Source Grading

**Category:** `market` · **Output artifact:** `source-grades.md`

## What this skill does
Rate how much a source can be trusted before using it in an argument.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `market-researcher`.

## Procedure
1. Identify who produced the source and what they gain from its conclusion.
2. Check the methodology and the sample; no methodology means no grade above 'estimated'.
3. Check the date and whether the underlying conditions still hold.
4. Look for a primary source behind a secondary claim.
5. Assign a grade — measured, sourced, benchmarked, estimated, or guessed — and carry it forward.

## Output contract
Write `source-grades.md` into `workspace/<venture-id>/market/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** source-grading
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
- Producer incentive assessed
- Grade carried into every downstream use
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `market` category
- Treating stated intent as evidence of demand.
- Sizing a market top-down and calling it bottom-up.
- Interviewing people who could never buy, then counting their enthusiasm.
