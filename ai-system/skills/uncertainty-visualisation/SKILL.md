---
name: uncertainty-visualisation
category: design
description: "Show how confident the numbers are."
output: "uncertainty-spec.md"
used_by:
  - data-visualization-designer
---

# Uncertainty Visualisation

**Category:** `design` · **Output artifact:** `uncertainty-spec.md`

## What this skill does
Show how confident the numbers are.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `data-visualization-designer`.

## Procedure
1. Identify where uncertainty exists: sampling, estimation, or incomplete data.
2. Show intervals or ranges rather than a single confident line.
3. Mark incomplete periods so partial data is not read as a decline.
4. Distinguish measured from forecast values visually.
5. State the sample size where it affects interpretation.

## Output contract
Write `uncertainty-spec.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** uncertainty-visualisation
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
- Incomplete periods marked
- Forecast visually distinguished from measured
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
