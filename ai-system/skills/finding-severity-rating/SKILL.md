---
name: finding-severity-rating
category: design
description: "Rate usability findings so the team fixes the right ones first."
output: "severity-ratings.md"
used_by:
  - usability-tester
---

# Finding Severity Rating

`design` · produces `severity-ratings.md` · used by `usability-tester`

Rate usability findings so the team fixes the right ones first.

## Procedure
1. Rate by consequence: does it block the task, cost time, or merely annoy?
2. Factor in frequency — how many users hit it, how often.
3. Distinguish comprehension failures from discoverability failures.
4. Rate consistently against prior rounds so trends mean something.
5. Attach the observed evidence to each rating.

## Output contract
`severity-ratings.md` → `workspace/<venture-id>/design/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/design.tsv`.

## Quality bar
- Consequence and frequency both factored
- Comprehension separated from discoverability
- The output states its confidence grade and names the evidence behind every load-bearing claim.
