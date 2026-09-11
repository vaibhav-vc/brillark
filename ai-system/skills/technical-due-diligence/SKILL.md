---
name: technical-due-diligence
category: strategy
description: "Keep the technical story ready for anyone who will examine it."
output: "tech-diligence-pack.md"
used_by:
  - cto-agent
---

# Technical Due Diligence

`strategy` · produces `tech-diligence-pack.md` · used by `cto-agent`

Keep the technical story ready for anyone who will examine it.

## Procedure
1. Assemble architecture, security posture, and dependency inventory.
2. Document known technical debt and the plan for it — hiding it fails diligence.
3. Verify IP ownership and licence compliance.
4. Prepare scaling evidence: what has been tested and to what level.
5. Keep it current so a raise or a deal never waits on engineering.

## Output contract
`tech-diligence-pack.md` → `workspace/<venture-id>/strategy/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/strategy.tsv`.

## Quality bar
- Known debt disclosed with a plan
- IP and licence position verified
- The output states its confidence grade and names the evidence behind every load-bearing claim.
