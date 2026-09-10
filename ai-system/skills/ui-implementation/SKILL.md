---
name: ui-implementation
category: engineering
description: "Build the interface to the acceptance criteria, including the hard states."
output: "ui-code"
used_by:
  - frontend-implementation-agent
---

# Ui Implementation

**Category:** `engineering` · **Output artifact:** `ui-code`

## What this skill does
Build the interface to the acceptance criteria, including the hard states.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `frontend-implementation-agent`.

## Procedure
1. Implement against acceptance criteria, not against the mock alone.
2. Reuse existing components before creating new ones.
3. Handle loading, empty, and error states as first-class work.
4. Meet accessibility requirements while building, not afterwards.
5. Measure the bundle impact and justify any new dependency.

## Output contract
Write `ui-code` into `workspace/<venture-id>/engineering/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** ui-implementation
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
- Reuse checked before creation
- Accessibility built in, not retrofitted
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `engineering` category
- Designing for imagined scale instead of current load plus one order of magnitude.
- Skipping or quarantining a failing test to get a green build.
- Shipping without a verified way back.
