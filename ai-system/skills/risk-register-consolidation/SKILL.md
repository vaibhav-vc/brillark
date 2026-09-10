---
name: risk-register-consolidation
category: risk
description: "Merge domain risk registers into one ranked list."
output: "risk-register.md"
used_by:
  - chief-risk-officer-agent
---

# Risk Register Consolidation

**Category:** `risk` · **Output artifact:** `risk-register.md`

## What this skill does
Merge domain risk registers into one ranked list.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `chief-risk-officer-agent`.

## Procedure
1. Collect registers from every domain.
2. Deduplicate risks described differently by different teams.
3. Normalise scoring across sources.
4. Rank by expected loss and assign a single owner to each.
5. Publish the top risks and the mitigation status of each.

## Output contract
Write `risk-register.md` into `workspace/<venture-id>/risk/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** risk-register-consolidation
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
- Cross-domain duplicates merged
- One owner per consolidated risk
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `risk` category
- A risk register that ranks by how loudly a risk was raised.
- Accepting a terminal risk implicitly by never classifying it.
- A continuity plan that has never been tested.
