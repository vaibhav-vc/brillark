---
name: system-contribution-process
category: design
description: "Define how a component enters the system."
output: "contribution-record.md"
used_by:
  - design-system-architect
---

# System Contribution Process

`design` · produces `contribution-record.md` · used by `design-system-architect`

Define how a component enters the system.

## Procedure
1. Require evidence the need appeared at least three times.
2. Define the review: accessibility, tokens, states, documentation, and code parity.
3. Assign a maintainer before accepting the contribution.
4. Require a usage example and a migration note for anything it replaces.
5. Publish the addition so consumers discover it rather than rebuilding it.

## Output contract
`contribution-record.md` → `workspace/<venture-id>/design/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/design.tsv`.

## Quality bar
- Three-occurrence evidence required
- Maintainer assigned before acceptance
- The output states its confidence grade and names the evidence behind every load-bearing claim.
