---
name: product-requirements-doc
category: product
description: "Write requirements an engineer can build and a tester can verify."
output: "prd.md"
used_by:
  - cpo-agent
  - product-requirements-agent
---

# Product Requirements Doc

**Category:** `product` · **Output artifact:** `prd.md`

## What this skill does
Write requirements an engineer can build and a tester can verify.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `cpo-agent`, `product-requirements-agent`.

## Procedure
1. Open with the problem and the evidence for it, never with a solution.
2. Define the users and the specific situation the feature addresses.
3. State the success signal and how it will be measured.
4. Describe the required behaviour, including the unhappy paths.
5. List what is explicitly out of scope and why.

## Output contract
Write `prd.md` into `workspace/<venture-id>/product/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** product-requirements-doc
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
- Opens with an evidenced problem
- Out-of-scope list explicit
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `product` category
- Writing a requirement that starts with a solution instead of an evidenced problem.
- Shipping without defining, in advance, what would show it worked.
- Treating the roadmap as a promise rather than a current best sequence.
