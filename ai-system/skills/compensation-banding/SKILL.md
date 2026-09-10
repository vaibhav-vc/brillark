---
name: compensation-banding
category: people
description: "Set pay bands and apply them consistently."
output: "compensation-bands.md"
used_by:
  - chro-agent
---

# Compensation Banding

**Category:** `people` · **Output artifact:** `compensation-bands.md`

## What this skill does
Set pay bands and apply them consistently.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `chro-agent`.

## Procedure
1. Gather benchmarks for the role, level, and market.
2. Define levels by scope and impact, not by tenure.
3. Set bands with a stated position against the market.
4. Define the equity component and its philosophy.
5. Document every exception and review them for pattern bias.

## Output contract
Write `compensation-bands.md` into `workspace/<venture-id>/people/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** compensation-banding
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
- Levels defined by scope, not tenure
- Exceptions documented and reviewed
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `people` category
- Writing a job advertisement before writing the outcomes the role must produce.
- Assessing candidates on different evidence and calling it judgement.
- Hiring to relieve a bottleneck that process or tooling would fix faster.
