---
name: pattern-detection
category: orchestration
description: "Find repeating structures in outcomes, failures, or requests."
output: "pattern-report.md"
used_by:
  - retrospective-agent
---

# Pattern Detection

**Category:** `orchestration` · **Output artifact:** `pattern-report.md`

## What this skill does
Find repeating structures in outcomes, failures, or requests.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `retrospective-agent`.

## Procedure
1. Collect events over at least three cycles; two points are not a pattern.
2. Group by cause and by structure rather than by label.
3. Test whether the pattern predicts anything, or is coincidence.
4. Quantify frequency and cost.
5. Recommend a systemic change proportional to the cost.

## Output contract
Write `pattern-report.md` into `workspace/<venture-id>/orchestration/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** pattern-detection
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
- At least three cycles of data
- Pattern shown to be predictive
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `orchestration` category
- Assigning a task to a group instead of one accountable agent.
- Reporting progress as a percentage instead of as artifacts that exist.
- Adding a review layer to fix a problem that a clearer definition of done would solve.
