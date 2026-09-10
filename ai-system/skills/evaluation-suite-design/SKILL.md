---
name: evaluation-suite-design
category: orchestration
description: "Build a repeatable test set that shows whether agents and skills work."
output: "evaluation-suite.yaml"
used_by:
  - evaluation-harness-agent
---

# Evaluation Suite Design

**Category:** `orchestration` · **Output artifact:** `evaluation-suite.yaml`

## What this skill does
Build a repeatable test set that shows whether agents and skills work.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `evaluation-harness-agent`.

## Procedure
1. Select real past tasks, including known failures, as cases.
2. Define the expected output properties per case before running anything.
3. Separate outcome quality from process compliance in the scoring.
4. Automate what can be automated; keep judgement cases explicit.
5. Version the suite alongside the agent and skill definitions.

## Output contract
Write `evaluation-suite.yaml` into `workspace/<venture-id>/orchestration/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** evaluation-suite-design
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
- Cases drawn from real work
- Expected properties defined in advance
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `orchestration` category
- Assigning a task to a group instead of one accountable agent.
- Reporting progress as a percentage instead of as artifacts that exist.
- Adding a review layer to fix a problem that a clearer definition of done would solve.
