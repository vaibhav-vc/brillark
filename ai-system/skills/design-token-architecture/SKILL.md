---
name: design-token-architecture
category: design
description: "Structure tokens so themes, modes, and brands work without rework."
output: "token-architecture.md"
used_by:
  - design-system-architect
---

# Design Token Architecture

**Category:** `design` · **Output artifact:** `token-architecture.md`

## What this skill does
Structure tokens so themes, modes, and brands work without rework.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `design-system-architect`.

## Procedure
1. Separate primitive values from semantic tokens that name an intent.
2. Name semantic tokens by role — surface, border, text-danger — never by colour.
3. Define the full set for each theme and mode rather than patching one.
4. Define the token for state variations: hover, focus, disabled, selected.
5. Version tokens and define how a change propagates to consumers.

## Output contract
Write `token-architecture.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** design-token-architecture
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
- Semantic layer named by role, not colour
- Every theme defined in full
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
