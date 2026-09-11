---
name: tree-testing
category: design
description: "Test whether people can find things in a structure before anything is designed on top of it."
output: "tree-test-results.md"
used_by:
  - information-architect
---

# Tree Testing

**Category:** `design` · **Output artifact:** `tree-test-results.md`

## What this skill does
Test whether people can find things in a structure before anything is designed on top of it.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `information-architect`.

## Procedure
1. Build the tree from labels alone, with no visual design to compensate.
2. Write find-tasks as goals rather than naming the destination.
3. Measure success, directness, and where people went wrong.
4. Identify the nodes that attract wrong turns; those labels are failing.
5. Retest after restructuring rather than assuming the fix worked.

## Output contract
Write `tree-test-results.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** tree-testing
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
- Tested on labels alone
- Wrong-turn nodes identified for relabelling
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
