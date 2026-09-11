---
name: design-system-governance
category: design
description: "Keep the system coherent as more people contribute to it."
output: "governance-policy.md"
used_by:
  - design-head
---

# Design System Governance

**Category:** `design` · **Output artifact:** `governance-policy.md`

## What this skill does
Keep the system coherent as more people contribute to it.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `design-head`.

## Procedure
1. Define who decides what, and what may be decided locally.
2. Set the criteria a contribution must meet before acceptance.
3. Review one-off exceptions regularly; each is future inconsistency.
4. Track adoption and act on the surfaces that are drifting.
5. Publish the system's roadmap so teams stop building around it.

## Output contract
Write `governance-policy.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** design-system-governance
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
- Decision rights explicit
- Exceptions reviewed rather than accumulated
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
