---
name: test-data-management
category: engineering
description: "Make test data predictable and safe."
output: "test-data-standard.md"
used_by:
  - qa-test-strategist
---

# Test Data Management

`engineering` · produces `test-data-standard.md` · used by `qa-test-strategist`

Make test data predictable and safe.

## Procedure
1. Define how test data is created, per test rather than shared where possible.
2. Never copy production personal data into test environments.
3. Make data setup explicit in the test, so failures are readable.
4. Clean up deterministically so ordering does not matter.
5. Keep fixtures small enough to understand at a glance.

## Output contract
`test-data-standard.md` → `workspace/<venture-id>/engineering/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/engineering.tsv`.

## Quality bar
- No production personal data in test environments
- Tests independent of execution order
- The output states its confidence grade and names the evidence behind every load-bearing claim.
