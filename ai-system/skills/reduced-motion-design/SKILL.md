---
name: reduced-motion-design
category: design
description: "Give an equivalent experience to people who have turned motion off."
output: "reduced-motion-spec.md"
used_by:
  - motion-designer
---

# Reduced Motion Design

**Category:** `design` · **Output artifact:** `reduced-motion-spec.md`

## What this skill does
Give an equivalent experience to people who have turned motion off.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `motion-designer`.

## Procedure
1. Honour the system reduced-motion preference everywhere.
2. Replace movement with an instant change or a simple fade, never nothing at all.
3. Ensure state changes remain perceivable without motion.
4. Never make reduced motion a degraded or slower experience.
5. Test the entire flow with the preference enabled.

## Output contract
Write `reduced-motion-spec.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** reduced-motion-design
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
- Preference honoured across the whole product
- State changes perceivable without motion
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
