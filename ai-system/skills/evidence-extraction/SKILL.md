---
name: evidence-extraction
category: market
description: "Turn raw conversation into structured, countable evidence."
output: "evidence-extract.md"
used_by:
  - customer-discovery-interviewer
---

# Evidence Extraction

**Category:** `market` · **Output artifact:** `evidence-extract.md`

## What this skill does
Turn raw conversation into structured, countable evidence.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `customer-discovery-interviewer`.

## Procedure
1. Extract statements about pains, workarounds, spend, and triggers.
2. Tag each with the participant, their segment, and the strength of the signal.
3. Separate what they did from what they said they would do.
4. Keep the original quote alongside the extraction.
5. Load into the evidence store so patterns can be counted.

## Output contract
Write `evidence-extract.md` into `workspace/<venture-id>/market/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** evidence-extraction
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
- Behaviour separated from stated intent
- Original quotes retained
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `market` category
- Treating stated intent as evidence of demand.
- Sizing a market top-down and calling it bottom-up.
- Interviewing people who could never buy, then counting their enthusiasm.
