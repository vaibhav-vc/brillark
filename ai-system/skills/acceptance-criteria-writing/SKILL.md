---
name: acceptance-criteria-writing
category: product
description: "Write conditions that decide unambiguously whether the work is done."
output: "acceptance-criteria.md"
used_by:
  - cpo-agent
  - product-requirements-agent
---

# Acceptance Criteria Writing

**Category:** `product` · **Output artifact:** `acceptance-criteria.md`

## What this skill does
Write conditions that decide unambiguously whether the work is done.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `cpo-agent`, `product-requirements-agent`.

## Procedure
1. Express each criterion as given, when, then.
2. Cover the unhappy paths, the empty states, and the error states.
3. Make each criterion independently testable.
4. Remove anything subjective or unmeasurable.
5. Agree them with engineering and QA before build starts.

## Output contract
Write `acceptance-criteria.md` into `workspace/<venture-id>/product/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** acceptance-criteria-writing
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
- Unhappy paths covered
- Agreed before build begins
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `product` category
- Writing a requirement that starts with a solution instead of an evidenced problem.
- Shipping without defining, in advance, what would show it worked.
- Treating the roadmap as a promise rather than a current best sequence.
