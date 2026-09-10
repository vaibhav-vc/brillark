---
name: why-now-analysis
category: market
description: "Explain what changed that makes this opportunity possible or urgent today."
output: "why-now.md"
used_by:
  - market-researcher
---

# Why Now Analysis

**Category:** `market` · **Output artifact:** `why-now.md`

## What this skill does
Explain what changed that makes this opportunity possible or urgent today.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `market-researcher`.

## Procedure
1. Identify the enabling shift: technology, regulation, cost curve, or behaviour change.
2. Verify the shift with evidence rather than assertion.
3. Explain why this was not viable three years ago.
4. Explain why the window will not stay open indefinitely.
5. State what would prove the timing wrong.

## Output contract
Write `why-now.md` into `workspace/<venture-id>/market/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** why-now-analysis
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
- Shift evidenced, not asserted
- Window-closing mechanism explained
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `market` category
- Treating stated intent as evidence of demand.
- Sizing a market top-down and calling it bottom-up.
- Interviewing people who could never buy, then counting their enthusiasm.
