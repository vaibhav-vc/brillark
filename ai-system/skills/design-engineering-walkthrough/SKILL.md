---
name: design-engineering-walkthrough
category: design
description: "Walk the spec with engineering before handoff, not after."
output: "walkthrough-notes.md"
used_by:
  - interaction-designer
---

# Design Engineering Walkthrough

**Category:** `design` · **Output artifact:** `walkthrough-notes.md`

## What this skill does
Walk the spec with engineering before handoff, not after.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `interaction-designer`.

## Procedure
1. Walk the flow state by state with the engineer who will build it.
2. Ask what is expensive, what is impossible, and what is ambiguous.
3. Resolve the ambiguities in the spec during the session rather than in tickets later.
4. Agree which states are in scope for the first implementation.
5. Record the agreed simplifications and why they are acceptable.

## Output contract
Write `walkthrough-notes.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** design-engineering-walkthrough
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
- Ambiguities resolved in the session
- Agreed simplifications recorded with reasons
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
