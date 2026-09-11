---
name: security-test-design
category: engineering
description: "Test that the security controls actually work."
output: "security-tests.md"
used_by:
  - security-engineer
---

# Security Test Design

`engineering` · produces `security-tests.md` · used by `security-engineer`

Test that the security controls actually work.

## Procedure
1. Derive test cases from the threat model, not from a generic checklist.
2. Test authorisation on every protected path, including the negative cases.
3. Test input handling with hostile payloads.
4. Test that rate limits and lockouts function under real conditions.
5. Automate what can be automated and schedule the rest.

## Output contract
`security-tests.md` → `workspace/<venture-id>/engineering/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/engineering.tsv`.

## Quality bar
- Cases derived from the threat model
- Negative authorisation cases tested
- The output states its confidence grade and names the evidence behind every load-bearing claim.
