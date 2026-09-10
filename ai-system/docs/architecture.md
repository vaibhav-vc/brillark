# How the system is put together

Five layers. Each depends only on the ones below it, which is why a change to a skill does not
require touching an agent, and a change to an agent does not require touching a schema.

```
  workflows/         what happens in what order        (14 definitions)
       |
  agents/            who is accountable                (83 agents, 5 tiers)
       |
  skills/            how a thing is done               (363 procedures)
       |
  knowledge-schema/  what may be stored, and in what shape  (14 schemas)
       |
  prompts/           the rules every agent runs under  (5 system prompts, 6 templates)
```

## Separation of concerns

**Agents own accountability. Skills own method.** An agent's definition says what it is answerable
for, who it escalates to, and what finished looks like. It does not contain procedures — it references
skills. This means the same procedure is applied identically whether `finance-head` or
`unit-economics-architect` runs it, and improving a procedure improves every agent that uses it.

**Workflows own sequence.** They do not contain logic; they name agents and skills in order, with a
completion condition per step. They are data, which is why the tests can verify every reference.

**Schemas own truth.** Several organisational rules are enforced structurally rather than by
convention — a memory record cannot exist without provenance, a decision cannot omit its accepted
costs, a Council finding cannot be an adjective. Rules enforced by documents erode; rules enforced by
schemas do not.

## The three loops

**The delivery loop** — intake, decompose, schedule, execute, hand off, track. Owned by orchestration.
Its job is that no agent ever waits on ambiguity about who owns what.

**The critique loop** — every material plan goes to the Council, gets attacked from ten angles,
receives a verdict with owners on each blocker, and the recurring flaws feed back into the guardrails
of the agents that produced them. Its job is that the organisation's mistakes get cheaper over time.

**The memory loop** — write with provenance, resolve contradictions at write time, consolidate at each
stage gate, expire what is stale, measure retrieval. Its job is that the tenth venture costs less to
plan than the first.

## Why 83 agents rather than a handful

Because accountability does not compress. A single "finance agent" that owns pricing, runway,
fundraising, billing, and tax has no definition of done, no meaningful escalation condition, and no
way to be scored. Splitting it into twelve gives each one a charter narrow enough that "did this
succeed?" has an answer.

The cost is coordination, which is why the orchestration domain exists and why the reporting lines
are strict: every agent escalates to exactly one parent, and every path terminates at the Director.

## Why 363 skills rather than 100

The skill count is a consequence, not a target. Each skill was derived from a capability some agent's
charter actually requires. Merging near-duplicates would produce fewer, vaguer procedures — and a
vague procedure is one an agent improvises around, which defeats the purpose.

## What this is not

- **Not a runtime.** These are definitions. An orchestrator reads them; nothing here executes itself.
- **Not a substitute for professional advice.** The legal, tax, and compliance agents spot issues and
  draft. Anything requiring a licensed attorney or accountant is escalated out of the system.
- **Not autonomous.** The Director reports to a human founder, and stage gates exist so a human can
  stop the thing.
