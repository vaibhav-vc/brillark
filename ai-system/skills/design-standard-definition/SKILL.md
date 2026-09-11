---
name: design-standard-definition
category: design
description: "Define the experience standard the business strategy requires."
output: "design-standard.md"
used_by:
  - chief-design-officer-agent
---

# Design Standard Definition

**Category:** `design` · **Output artifact:** `design-standard.md`

## What this skill does
Define the experience standard the business strategy requires.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `chief-design-officer-agent`.

## Procedure
1. State what the experience must achieve for the strategy to work.
2. Define the standard concretely enough to judge a surface against it.
3. State what the standard rules out.
4. Tie the standard to a measurable business outcome.
5. Publish it so trade-offs are argued against a written bar.

## Output contract
Write `design-standard.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** design-standard-definition
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
- Standard concrete enough to judge against
- Tied to a measurable business outcome
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
