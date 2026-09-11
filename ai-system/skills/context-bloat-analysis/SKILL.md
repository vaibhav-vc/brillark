---
name: context-bloat-analysis
category: efficiency
description: "Find context that is loaded and never used."
output: "bloat-report.md"
used_by:
  - token-efficiency-analyst
---

# Context Bloat Analysis

**Category:** `efficiency` · **Output artifact:** `bloat-report.md`

## What this skill does
Find context that is loaded and never used.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `token-efficiency-analyst`.

## Procedure
1. Capture what was placed in context for a sample of runs.
2. Identify what the output actually referenced or depended on.
3. Compute the loaded-but-unused ratio per agent.
4. Trace unused content to the packaging rule that included it.
5. Tighten the rule and re-measure rather than trimming by hand.

## Output contract
Write `bloat-report.md` into `workspace/<venture-id>/efficiency/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** context-bloat-analysis
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
- Unused content traced to its packaging rule
- Re-measured after the rule change
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `efficiency` category
- Measuring cost per call instead of cost per completed task.
- Demoting a model tier without checking the hardest cases.
- Trimming context by hand instead of fixing the rule that loaded it.
