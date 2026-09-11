---
name: accessibility-conformance-review
category: design
description: "Decide whether a surface meets the bar to ship."
output: "conformance-decision.md"
used_by:
  - design-head
---

# Accessibility Conformance Review

**Category:** `design` · **Output artifact:** `conformance-decision.md`

## What this skill does
Decide whether a surface meets the bar to ship.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `design-head`.

## Procedure
1. Confirm the target level and which criteria apply to this surface.
2. Check the audit is current for the code actually shipping.
3. Treat unresolved failures as defects, not as enhancements.
4. Block release on failures that prevent task completion.
5. Record any accepted risk with an owner, a date, and a remediation plan.

## Output contract
Write `conformance-decision.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** accessibility-conformance-review
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
- Task-blocking failures block release
- Accepted risks carry owner and date
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
