---
name: differentiation-analysis
category: market
description: "State the reason a customer would switch, or admit there is none."
output: "differentiation.md"
used_by:
  - competitor-intel-analyst
---

# Differentiation Analysis

**Category:** `market` · **Output artifact:** `differentiation.md`

## What this skill does
State the reason a customer would switch, or admit there is none.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `competitor-intel-analyst`.

## Procedure
1. List what we do that alternatives do not, from the customer's perspective.
2. Test each difference against 'would this alone justify switching?'
3. Assess how easily each difference could be copied and how fast.
4. Identify the difference that compounds rather than the one that is merely present.
5. State the differentiation in one sentence a customer would recognise.

## Output contract
Write `differentiation.md` into `workspace/<venture-id>/market/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** differentiation-analysis
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
- Stated as a switching reason
- Copyability of each difference assessed
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `market` category
- Treating stated intent as evidence of demand.
- Sizing a market top-down and calling it bottom-up.
- Interviewing people who could never buy, then counting their enthusiasm.
