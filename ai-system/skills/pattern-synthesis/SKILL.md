---
name: pattern-synthesis
category: market
description: "Find the signal across many conversations without inventing it."
output: "synthesis.md"
used_by:
  - customer-discovery-interviewer
---

# Pattern Synthesis

**Category:** `market` · **Output artifact:** `synthesis.md`

## What this skill does
Find the signal across many conversations without inventing it.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `customer-discovery-interviewer`.

## Procedure
1. Count how many participants independently raised each theme.
2. Weight by segment — a theme from three of four target buyers matters more than from ten non-buyers.
3. Look for the absence of expected themes; silence is data.
4. Distinguish patterns from single vivid anecdotes.
5. State the confidence and the sample behind each conclusion.

## Output contract
Write `synthesis.md` into `workspace/<venture-id>/market/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** pattern-synthesis
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
- Themes counted across participants
- Sample size stated with each conclusion
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `market` category
- Treating stated intent as evidence of demand.
- Sizing a market top-down and calling it bottom-up.
- Interviewing people who could never buy, then counting their enthusiasm.
