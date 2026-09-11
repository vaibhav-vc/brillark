---
name: experience-quality-measurement
category: design
description: "Measure experience quality so it can be argued for with evidence."
output: "experience-metrics.md"
used_by:
  - chief-design-officer-agent
---

# Experience Quality Measurement

**Category:** `design` · **Output artifact:** `experience-metrics.md`

## What this skill does
Measure experience quality so it can be argued for with evidence.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `chief-design-officer-agent`.

## Procedure
1. Choose measures tied to user outcomes: task success, effort, and time to value.
2. Combine behavioural measures with attitudinal ones.
3. Track against the standard rather than against last quarter alone.
4. Connect the measures to a business outcome where the link is real.
5. Report honestly when the link cannot be demonstrated.

## Output contract
Write `experience-metrics.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** experience-quality-measurement
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
- Behavioural and attitudinal measures combined
- Unproven business links reported honestly
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
