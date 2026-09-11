---
name: red-team-attack
category: council
description: "Attack a plan the way a competitor or bad actor would."
output: "red-team-report.md"
used_by:
  - council-red-team
---

# Red Team Attack

`council` · produces `red-team-report.md` · used by `council-red-team`

Attack a plan the way a competitor or bad actor would.

## Procedure
1. Attack the plan's strongest claim first; weak points are already known.
2. Model three attackers: a funded competitor, an abusive user, and an indifferent market.
3. Write each attack as a concrete sequence of events, not an adjective.
4. Rank by damage multiplied by plausibility and drop what cannot be made concrete.
5. Propose the cheapest defence for each surviving attack.

## Output contract
`red-team-report.md` → `workspace/<venture-id>/council/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/council.tsv`.

## Quality bar
- Attacks written as concrete sequences
- A defence proposed for each surviving attack
- The output states its confidence grade and names the evidence behind every load-bearing claim.
