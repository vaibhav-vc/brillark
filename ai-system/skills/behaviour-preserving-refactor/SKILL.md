---
name: behaviour-preserving-refactor
category: engineering
description: "Change structure without changing behaviour."
output: "refactor-record.md"
used_by:
  - tech-debt-refactor-agent
---

# Behaviour Preserving Refactor

**Category:** `engineering` · **Output artifact:** `refactor-record.md`

## What this skill does
Change structure without changing behaviour.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `tech-debt-refactor-agent`.

## Procedure
1. Establish characterisation tests for the current behaviour first.
2. Make one structural change at a time.
3. Never mix behaviour changes into a refactoring commit.
4. Run the full suite after each step.
5. If behaviour must change, do it as a separate, reviewed change.

## Output contract
Write `refactor-record.md` into `workspace/<venture-id>/engineering/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** behaviour-preserving-refactor
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
- Behaviour changes kept in separate commits
- Characterisation tests established first
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `engineering` category
- Designing for imagined scale instead of current load plus one order of magnitude.
- Skipping or quarantining a failing test to get a green build.
- Shipping without a verified way back.
