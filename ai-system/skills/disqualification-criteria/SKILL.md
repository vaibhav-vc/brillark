---
name: disqualification-criteria
category: market
description: "Define who we will not sell to, and stick to it."
output: "disqualification.md"
used_by:
  - icp-persona-builder
---

# Disqualification Criteria

**Category:** `market` · **Output artifact:** `disqualification.md`

## What this skill does
Define who we will not sell to, and stick to it.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `icp-persona-builder`.

## Procedure
1. Identify the attributes that predicted past failures or churn.
2. Write each as an observable, checkable condition.
3. Distinguish 'not now' from 'never'.
4. Give sellers permission to disqualify and a script for doing it well.
5. Measure how often the criteria are overridden and what happened.

## Output contract
Write `disqualification.md` into `workspace/<venture-id>/market/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** disqualification-criteria
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
- Criteria observable and checkable
- Override rate measured
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `market` category
- Treating stated intent as evidence of demand.
- Sizing a market top-down and calling it bottom-up.
- Interviewing people who could never buy, then counting their enthusiasm.
