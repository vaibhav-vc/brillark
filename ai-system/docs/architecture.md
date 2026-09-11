# How the system is put together

Five layers. Each depends only on the ones below it, which is why a change to a skill does not
require touching an agent, and a change to an agent does not require touching a schema.

```
  workflows/         what happens in what order            (17 definitions)
       |
  agents/            who is accountable                    (113 agents, 5 tiers, 8 domains)
       |
  skills/            how a thing is done                   (505 procedures)
       |
  runtime/           what may be loaded, and in what order (budgets, routing, loader spec)
       |
  knowledge-schema/  what may be stored, and in what shape (19 schemas)
       |
  prompts/           the rules every agent runs under      (7 system prompts, 6 templates)
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

## The loading layer

`runtime/` is the layer that makes the rest affordable. It is separate from `agents/` and `skills/`
on purpose: what an agent *is* and what gets *loaded* are different concerns, and conflating them is
how organisations like this become too expensive to run.

The indexes in `agents/index/` and `skills/index/` are generated from the registries and checked
against them by tests, so discovery can never silently drift from reality. That matters because a
stale index does not fail loudly — it just routes work to an agent that no longer exists.

## Why 113 agents rather than a handful

Because accountability does not compress. A single "finance agent" that owns pricing, runway,
fundraising, billing, and tax has no definition of done, no meaningful escalation condition, and no
way to be scored. Splitting it into twelve gives each one a charter narrow enough that "did this
succeed?" has an answer.

The cost is coordination, which is why the orchestration domain exists and why the reporting lines
are strict: every agent escalates to exactly one parent, and every path terminates at the Director.

The other cost would be context, except that it is not: because of tiering, a run loads one charter,
not 113. Adding agents makes the organisation more capable without making any single run more
expensive. That is the property that makes this shape viable at all — and it is measured, not assumed.

## Why 505 skills rather than 100

The skill count is a consequence, not a target. Each skill was derived from a capability some agent's
charter actually requires. Merging near-duplicates would produce fewer, vaguer procedures — and a
vague procedure is one an agent improvises around, which defeats the purpose.

The same tiering argument applies: an agent loads the five or six skills it declared, never the
library. The index shard it reads to choose them costs about 400 tokens.

## Why the improvement domain cannot rewrite everything

A system that can modify itself will optimise whatever it is measured on. The boundary is therefore
structural rather than a matter of good behaviour: prompts and skill steps may change automatically
with a passing trial; workflows and charters need the Director; guardrails, schemas, the org shape,
and the **evaluation criteria** need the human founder.

The evaluation criteria are the fixed point. Everything else in the loop turns around them, and a
loop permitted to move its own reference point is not an improvement loop.

## What this is not

- **Not a runtime.** These are definitions. An orchestrator reads them; nothing here executes itself.
- **Not a substitute for professional advice.** The legal, tax, and compliance agents spot issues and
  draft. Anything requiring a licensed attorney or accountant is escalated out of the system.
- **Not autonomous.** The Director reports to a human founder, and stage gates exist so a human can
  stop the thing.
