# Canva

**Source of truth for:** Brand assets, marketing collateral, and design templates.

**Primary agents:** `brand-narrative-agent`, `positioning-messaging-agent`, `cmo-agent`

## Rules

- Assets must conform to the voice and visual guidelines; `brand-consistency-audit` checks for drift.
- Every external claim in a published asset must appear in the substantiation file first.
- Terminology follows the glossary: one concept, one name, across every surface.
- Publishing is an outward-facing action and needs the owning agent's explicit authority.

## Contract

Read access is default. Writes are outward-facing actions requiring the owning agent's authority.
Everything entering memory from here carries provenance (system, query, timestamp) and an evidence
grade. If this system is unreachable, escalate — do not fall back to stale memory.
