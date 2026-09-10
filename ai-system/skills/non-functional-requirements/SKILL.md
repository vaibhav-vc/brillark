---
name: non-functional-requirements
category: product
description: "State the qualities the system must have, not just its behaviour."
output: "nfr.md"
used_by:
  - product-requirements-agent
---

# Non Functional Requirements

**Category:** `product` · **Output artifact:** `nfr.md`

## What this skill does
State the qualities the system must have, not just its behaviour.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `product-requirements-agent`.

## Procedure
1. Specify latency and throughput targets for the critical journeys.
2. Specify availability and the acceptable failure behaviour.
3. Specify security, privacy, and data retention requirements.
4. Specify accessibility and browser or device support.
5. Make each testable; an untestable requirement is a wish.

## Output contract
Write `nfr.md` into `workspace/<venture-id>/product/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** non-functional-requirements
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
- Every requirement testable
- Failure behaviour specified, not just uptime
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `product` category
- Writing a requirement that starts with a solution instead of an evidenced problem.
- Shipping without defining, in advance, what would show it worked.
- Treating the roadmap as a promise rather than a current best sequence.
