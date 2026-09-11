---
name: coverage-mapping
category: improvement
description: "Know what the evaluation does and does not cover."
output: "coverage-map.md"
used_by:
  - benchmark-curator
---

# Coverage Mapping

**Category:** `improvement` · **Output artifact:** `coverage-map.md`

## What this skill does
Know what the evaluation does and does not cover.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `benchmark-curator`.

## Procedure
1. Map cases to agents, skills, and failure modes.
2. Identify agent classes with no coverage.
3. Identify failure modes no case would catch.
4. Report thin coverage honestly rather than implying completeness.
5. Prioritise new cases by risk, not by ease of construction.

## Output contract
Write `coverage-map.md` into `workspace/<venture-id>/improvement/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** coverage-mapping
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
- Uncovered agent classes named
- Thin coverage reported honestly
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `improvement` category
- Starting an improvement cycle with an idea instead of a measurement.
- Adopting a change that beat the cases it was tuned on.
- Adding an instruction without removing one, until none of them are read.
