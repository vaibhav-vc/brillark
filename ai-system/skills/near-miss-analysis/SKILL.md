---
name: near-miss-analysis
category: risk
description: "Learn from the failures that almost happened."
output: "near-miss-log.md"
used_by:
  - chief-risk-officer-agent
---

# Near Miss Analysis

**Category:** `risk` · **Output artifact:** `near-miss-log.md`

## What this skill does
Learn from the failures that almost happened.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `chief-risk-officer-agent`.

## Procedure
1. Capture near misses deliberately; they are rarely reported unprompted.
2. Analyse what stopped the failure — design or luck.
3. Treat luck-stopped near misses as failures for analysis purposes.
4. Identify the control that would make the outcome reliable.
5. Track near-miss frequency as a leading indicator.

## Output contract
Write `near-miss-log.md` into `workspace/<venture-id>/risk/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** near-miss-analysis
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
- Luck distinguished from design
- Frequency tracked as a leading indicator
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `risk` category
- A risk register that ranks by how loudly a risk was raised.
- Accepting a terminal risk implicitly by never classifying it.
- A continuity plan that has never been tested.
