---
name: component-deprecation
category: design
description: "Remove a component without stranding the people using it."
output: "deprecation-plan.md"
used_by:
  - design-system-architect
---

# Component Deprecation

**Category:** `design` · **Output artifact:** `deprecation-plan.md`

## What this skill does
Remove a component without stranding the people using it.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `design-system-architect`.

## Procedure
1. Announce the deprecation with the replacement and a migration example.
2. Instrument usage so remaining consumers are known, not guessed.
3. Set a removal date with enough time for consumers to migrate.
4. Help migrate the largest consumers rather than waiting for them.
5. Remove it only when usage reaches zero, and confirm afterwards.

## Output contract
Write `deprecation-plan.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** component-deprecation
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
- Usage instrumented, not guessed
- Removal only at zero usage
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
