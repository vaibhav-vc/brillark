---
name: component-api-design
category: design
description: "Design a component's interface so it is hard to misuse."
output: "component-spec.md"
used_by:
  - design-system-architect
---

# Component API Design

`design` · produces `component-spec.md` · used by `design-system-architect`

Design a component's interface so it is hard to misuse.

## Procedure
1. Define the component's single responsibility and what it deliberately does not do.
2. Specify every state and variant, including disabled, loading, and error.
3. Design props so invalid combinations cannot be expressed.
4. Document the intended use and the cases it is wrong for.
5. Review the API with a consumer before publishing it.

## Output contract
`component-spec.md` → `workspace/<venture-id>/design/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/design.tsv`.

## Quality bar
- Invalid combinations unrepresentable
- Wrong-use cases documented
- The output states its confidence grade and names the evidence behind every load-bearing claim.
