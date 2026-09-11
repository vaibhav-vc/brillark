---
name: state-specification
category: design
description: "Specify every state a view can be in, so none is discovered in production."
output: "state-spec.md"
used_by:
  - interaction-designer
---

# State Specification

**Category:** `design` · **Output artifact:** `state-spec.md`

## What this skill does
Specify every state a view can be in, so none is discovered in production.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `interaction-designer`.

## Procedure
1. Specify empty, loading, partial, error, and success for every view.
2. Design the first-use empty state as an onboarding opportunity, not a blank box.
3. Specify what the error state says and what action it offers.
4. Define the loading behaviour by expected duration, not one spinner for everything.
5. Specify the partial state where some data arrived and some did not.

## Output contract
Write `state-spec.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** state-specification
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
- All five states specified per view
- Error states offer a recovery action
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
