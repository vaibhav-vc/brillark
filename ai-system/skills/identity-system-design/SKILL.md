---
name: identity-system-design
category: design
description: "Design the identity as a system, not as a logo."
output: "identity-system.md"
used_by:
  - brand-identity-designer
---

# Identity System Design

**Category:** `design` · **Output artifact:** `identity-system.md`

## What this skill does
Design the identity as a system, not as a logo.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `brand-identity-designer`.

## Procedure
1. Define the mark, palette, type, imagery, and layout principles together.
2. Specify how they combine across surfaces and sizes.
3. Design for the constrained cases: monochrome, tiny, and single-colour print.
4. Check every colour pairing against contrast requirements.
5. Document the system so others can apply it without you.

## Output contract
Write `identity-system.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** identity-system-design
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
- System covers all elements and their combination
- Contrast verified across pairings
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
