---
name: journey-mapping
category: design
description: "Map the customer's whole path, including the parts the product never sees."
output: "journey-map.md"
used_by:
  - design-researcher
---

# Journey Mapping

**Category:** `design` · **Output artifact:** `journey-map.md`

## What this skill does
Map the customer's whole path, including the parts the product never sees.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `design-researcher`.

## Procedure
1. Define the journey's start and end from the customer's perspective, not the product's.
2. Lay out the stages with the actions, thoughts, and emotions at each.
3. Mark the pain points and their evidence from research.
4. Include the offline, human, and waiting steps.
5. Identify the two moments that most determine whether the journey succeeds.

## Output contract
Write `journey-map.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** journey-mapping
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
- Journey bounded by the customer's goal
- Offline and waiting steps included
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
