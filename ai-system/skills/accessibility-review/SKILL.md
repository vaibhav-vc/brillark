---
name: accessibility-review
category: engineering
description: "Check the interface works for people who do not use it the default way."
output: "accessibility-report.md"
used_by:
  - council-ethics-and-responsibility
  - frontend-implementation-agent
---

# Accessibility Review

**Category:** `engineering` · **Output artifact:** `accessibility-report.md`

## What this skill does
Check the interface works for people who do not use it the default way.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `council-ethics-and-responsibility`, `frontend-implementation-agent`.

## Procedure
1. Test keyboard-only navigation through every flow.
2. Check semantic structure, labels, and roles with a screen reader.
3. Verify colour contrast and that colour is never the only signal.
4. Check focus order, focus visibility, and error announcement.
5. Record findings against the conformance level being targeted.

## Output contract
Write `accessibility-report.md` into `workspace/<venture-id>/engineering/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** accessibility-review
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
- Keyboard-only path tested end to end
- Colour never the sole signal
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `engineering` category
- Designing for imagined scale instead of current load plus one order of magnitude.
- Skipping or quarantining a failing test to get a green build.
- Shipping without a verified way back.
