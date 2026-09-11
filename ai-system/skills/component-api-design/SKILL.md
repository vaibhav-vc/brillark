---
name: component-api-design
category: design
description: "Design a component's interface so it is hard to misuse."
output: "component-spec.md"
used_by:
  - design-system-architect
---

# Component API Design

**Category:** `design` · **Output artifact:** `component-spec.md`

## What this skill does
Design a component's interface so it is hard to misuse.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `design-system-architect`.

## Procedure
1. Define the component's single responsibility and what it deliberately does not do.
2. Specify every state and variant, including disabled, loading, and error.
3. Design props so invalid combinations cannot be expressed.
4. Document the intended use and the cases it is wrong for.
5. Review the API with a consumer before publishing it.

## Output contract
Write `component-spec.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** component-api-design
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
- Invalid combinations unrepresentable
- Wrong-use cases documented
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
