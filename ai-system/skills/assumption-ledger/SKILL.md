---
name: assumption-ledger
category: finance
description: "Collect every assumption that touches money into one auditable list."
output: "assumption-ledger.md"
used_by:
  - council-assumption-auditor
  - finance-head
  - financial-model-builder
---

# Assumption Ledger

**Category:** `finance` · **Output artifact:** `assumption-ledger.md`

## What this skill does
Collect every assumption that touches money into one auditable list.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `council-assumption-auditor`, `finance-head`, `financial-model-builder`.

## Procedure
1. Extract assumptions from the model, including defaults buried inside formulas.
2. Record the value, the source, the evidence grade, and the owner for each.
3. Score how much of the plan depends on each assumption.
4. Flag high-dependency, low-evidence assumptions as priority tests.
5. Re-review the ledger whenever the model changes materially.

## Output contract
Write `assumption-ledger.md` into `workspace/<venture-id>/finance/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** assumption-ledger
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
- Assumptions inside formulas surfaced
- Dependency scored per assumption
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `finance` category
- Presenting a single number where the honest answer is a range.
- Building a forecast from a growth percentage instead of from drivers.
- Reporting a metric whose definition changed since last period without saying so.
