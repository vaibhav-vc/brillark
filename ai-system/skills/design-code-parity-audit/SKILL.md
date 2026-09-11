---
name: design-code-parity-audit
category: design
description: "Check that the design source and the shipped code still agree."
output: "parity-report.md"
used_by:
  - design-system-architect
---

# Design Code Parity Audit

**Category:** `design` · **Output artifact:** `parity-report.md`

## What this skill does
Check that the design source and the shipped code still agree.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `design-system-architect`.

## Procedure
1. Compare tokens in the design source against the values in code.
2. Compare component states and variants in both.
3. Sample real screens and diff them against their designs.
4. Record every divergence with which side is correct.
5. Fix at the source of truth, not by patching the other side.

## Output contract
Write `parity-report.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** design-code-parity-audit
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
- Divergences recorded with the correct side named
- Fixes applied at the source of truth
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
