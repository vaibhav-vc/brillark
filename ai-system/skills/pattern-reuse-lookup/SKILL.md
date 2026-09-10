---
name: pattern-reuse-lookup
category: memory
description: "Find the prior decomposition, plan, or solution that matches this shape."
output: "pattern-match.md"
used_by:
  - planning-decomposer
---

# Pattern Reuse Lookup

**Category:** `memory` · **Output artifact:** `pattern-match.md`

## What this skill does
Find the prior decomposition, plan, or solution that matches this shape.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `planning-decomposer`.

## Procedure
1. Describe the current problem by its structure, not its surface topic.
2. Search procedural memory for matching structures.
3. Assess fit honestly — a forced match costs more than starting fresh.
4. Adapt the pattern and record what had to change.
5. Update the pattern's success record with this application's outcome.

## Output contract
Write `pattern-match.md` into `workspace/<venture-id>/memory/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** pattern-reuse-lookup
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
- Match assessed on structure
- Adaptation and outcome recorded
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `memory` category
- Storing a claim without provenance, so nobody can later tell whether to trust it.
- Keeping two contradicting facts because resolving them is inconvenient.
- Treating a stale memory as current because it is well written.
