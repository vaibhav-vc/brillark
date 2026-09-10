---
name: evidence-tagging
category: market
description: "Mark how much each claim in an artifact is actually supported."
output: "evidence-tags.md"
used_by:
  - business-model-canvas-agent
---

# Evidence Tagging

**Category:** `market` · **Output artifact:** `evidence-tags.md`

## What this skill does
Mark how much each claim in an artifact is actually supported.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `business-model-canvas-agent`.

## Procedure
1. Tag each claim as measured, sourced, benchmarked, estimated, or guessed.
2. Attach the source reference to every non-guessed tag.
3. Compute the proportion of the artifact resting on guesses.
4. Highlight guessed claims that carry significant weight.
5. Refuse to advance a stage gate on guessed load-bearing claims.

## Output contract
Write `evidence-tags.md` into `workspace/<venture-id>/market/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** evidence-tagging
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
- Every claim carries a grade
- Load-bearing guesses highlighted
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `market` category
- Treating stated intent as evidence of demand.
- Sizing a market top-down and calling it bottom-up.
- Interviewing people who could never buy, then counting their enthusiasm.
