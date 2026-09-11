---
name: design-capability-planning
category: design
description: "Plan the design capability the roadmap actually needs."
output: "capability-plan.md"
used_by:
  - chief-design-officer-agent
---

# Design Capability Planning

**Category:** `design` · **Output artifact:** `capability-plan.md`

## What this skill does
Plan the design capability the roadmap actually needs.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `chief-design-officer-agent`.

## Procedure
1. Identify the design work the roadmap requires, by type.
2. Compare against current capability and capacity.
3. Decide what to build, hire, or systematise.
4. Invest in the system where it removes repeated work.
5. Sequence against the roadmap rather than hiring generically.

## Output contract
Write `capability-plan.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** design-capability-planning
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
- Capability need derived from the roadmap
- System investment weighed against repeated work
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
