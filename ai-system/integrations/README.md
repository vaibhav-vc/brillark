# Integrations

The organisation reads and writes external systems. Each contract below states what the system is the
source of truth for, which agents touch it, and what must never happen.

The rule that applies to all of them: **external systems are the source of truth for their own data,
and memory records what we concluded from it, never a copy of it.** A stale copy in memory that
disagrees with the live system is exactly the contradiction the memory model exists to prevent.

| Integration | Source of truth for | Primary agents |
|---|---|---|
| `github.md` | Code, reviews, CI status, technical history | engineering domain |
| `supabase.md` | Application data, auth, usage events | engineering, data |
| `vercel.md` | Deployments, runtime logs, web analytics | infra, release, performance |
| `analytics.md` | Product behaviour and funnel data | data, business, gtm |
| `accounting.md` | Financial actuals | finance domain |
| `crm.md` | Pipeline and customer relationships | revenue, business |
| `canva.md` | Brand and marketing assets | marketing |

## Common contract

Every integration adapter must:

1. **Declare its source-of-truth boundary.** What it is authoritative for, and what it is not.
2. **Attach provenance.** Anything entering memory from an external system records the system, the
   query, and the timestamp.
3. **Grade its evidence.** Data pulled from a live system is `measured`. Data a human typed into that
   system is at best `sourced`.
4. **Be read-mostly.** Writing to an external system is an outward-facing action and needs the owning
   agent's explicit authority, not a side effect of a research task.
5. **Fail visibly.** An integration that cannot be reached produces an escalation, never a silent
   fallback to stale memory.
6. **Never carry secrets into artifacts.** Credentials live in the runtime's secret store. No artifact,
   memory record, or log may contain one.
