# GitHub

**Source of truth for:** Code, pull requests, review history, CI results, and the technical decision trail.

**Primary agents:** `engineering-head`, `release-manager`, `qa-test-strategist`, `security-engineer`, `tech-debt-refactor-agent`

## Rules

- Architecture decision records live in the repository, not only in memory — the code and its reasoning should travel together.
- CI status is authoritative for whether something passes. Memory records the conclusion drawn, not a copy of the run.
- `release-manager` reads check status before a go/no-go; a red pipeline is a no-go regardless of schedule pressure.
- Never push to a branch outside the agreed one, and never merge on an agent's own authority.

## Contract

Read access is default. Writes are outward-facing actions requiring the owning agent's authority.
Everything entering memory from here carries provenance (system, query, timestamp) and an evidence
grade. If this system is unreachable, escalate — do not fall back to stale memory.
