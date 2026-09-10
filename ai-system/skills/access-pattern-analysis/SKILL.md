---
name: access-pattern-analysis
category: engineering
description: "Establish how data will actually be read and written."
output: "access-patterns.md"
used_by:
  - data-model-designer
---

# Access Pattern Analysis

**Category:** `engineering` · **Output artifact:** `access-patterns.md`

## What this skill does
Establish how data will actually be read and written.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `data-model-designer`.

## Procedure
1. List every query the application makes, with its frequency and latency need.
2. List every write pattern and its consistency requirement.
3. Identify the patterns that will dominate at scale.
4. Check the model serves them without full scans or fan-out.
5. Re-check when a new feature adds an access pattern.

## Output contract
Write `access-patterns.md` into `workspace/<venture-id>/engineering/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** access-pattern-analysis
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
- Frequency and latency captured per query
- Dominant patterns identified
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `engineering` category
- Designing for imagined scale instead of current load plus one order of magnitude.
- Skipping or quarantining a failing test to get a green build.
- Shipping without a verified way back.
