---
name: dependency-failure-analysis
category: engineering
description: "Decide what happens when each external dependency fails."
output: "dependency-failure-plan.md"
used_by:
  - system-architect
---

# Dependency Failure Analysis

`engineering` · produces `dependency-failure-plan.md` · used by `system-architect`

Decide what happens when each external dependency fails.

## Procedure
1. List every external dependency and what it provides.
2. For each, define the behaviour when it is slow, wrong, or absent.
3. Choose a strategy: fail fast, degrade, cache, or queue.
4. Set timeouts and retry policy deliberately, with backoff.
5. Test the failure behaviour rather than assuming it.

## Output contract
`dependency-failure-plan.md` → `workspace/<venture-id>/engineering/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/engineering.tsv`.

## Quality bar
- Behaviour defined for slow as well as absent
- Failure behaviour actually tested
- The output states its confidence grade and names the evidence behind every load-bearing claim.
