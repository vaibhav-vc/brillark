---
name: visual-hierarchy-design
category: design
description: "Make the order things are read match the order they matter."
output: "hierarchy-spec.md"
used_by:
  - visual-designer
---

# Visual Hierarchy Design

**Category:** `design` · **Output artifact:** `hierarchy-spec.md`

## What this skill does
Make the order things are read match the order they matter.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `visual-designer`.

## Procedure
1. Decide what must be read first, second, and not at all.
2. Create the hierarchy with size, weight, and space before reaching for colour.
3. Check the hierarchy by squinting or blurring — the structure should survive.
4. Ensure the primary action is unambiguous on every screen.
5. Verify with real content, where competing elements actually compete.

## Output contract
Write `hierarchy-spec.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** visual-hierarchy-design
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
- Hierarchy holds when blurred
- Primary action unambiguous per screen
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
