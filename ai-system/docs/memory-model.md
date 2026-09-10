# Memory model

The point of the memory system is that the tenth venture is cheaper to plan than the first. That only
happens if memory is structured, graded, consolidated, and expired. An unstructured pile of notes is
worse than nothing, because agents trust it.

## Four types

| Type | Question it answers | Example |
|---|---|---|
| **Episodic** | What happened? | "On 12 March, three of five interviewees said they already pay for a workaround." |
| **Semantic** | What is true? | "Mid-market operations leads control a tooling budget of roughly $2k per month." |
| **Procedural** | How do we do this? | "Channel tests need a kill criterion set before spend, or they never end." |
| **Decision** | What did we choose, and why? | "We priced per workspace, not per seat, because seats punish the exact expansion we want." |

Episodic memory accumulates fast and decays fast. Semantic and procedural memory are earned:
`context-memory-curator` promotes an episodic fact into semantic memory only when at least three
independent episodes support it, and a sequence into procedural memory only when it repeatedly
produced good outcomes.

## Provenance is mandatory

Every record carries the author agent, the skill used, the date, an evidence grade, and links to the
source artifacts. This is enforced by `memory-record.schema.json`, not by convention. A claim you
cannot trace is a claim you cannot safely act on in six months.

Grades, weakest to strongest: `guessed`, `estimated`, `benchmarked`, `sourced`, `measured`.
A guessed claim may never be load-bearing at a stage gate.

## Contradictions are resolved, never stored

When a new write conflicts with an existing claim, `knowledge-graph-librarian` catches it at write time
and `memory-conflict-resolution` decides. The loser is *superseded* with a pointer to the winner — not
deleted, so the history stays auditable, and not kept in parallel, so agents cannot pick whichever
version suits them. Equal-evidence conflicts escalate to the domain head.

## Decay is deliberate

Stale context is worse than missing context, because it is trusted. Every record has a shelf life by
type: market data expires quickly, decision records rarely. Past shelf life a record is marked `stale`
and must be re-verified before it can support a decision. Nothing is silently deleted.

## The knowledge graph

Entities are canonical: one real thing, one node. Relationships are typed from a fixed list —
`competes_with`, `depends_on`, `evidences`, `contradicts`, and so on. `related_to` is deliberately not
available, because it carries no information. Every edge names the artifact that justifies it.

This is what makes cross-domain questions answerable: "which decisions rest on the assumption that
churn stays under 3%?" is a graph traversal, not a search through prose.

## Retrieval is measured

If an agent rediscovers a fact the organisation already knew, that is logged as a retrieval defect,
not as an agent error. `memory-retrieval-tuning` samples real tasks, checks which known facts failed
to surface, and fixes the keys and entity links rather than adding more text.

## Consolidation runs at every stage gate

`09-memory-consolidation` gathers the period's writes, resolves entities and contradictions, promotes
what has earned promotion, expires what is stale, and measures retrieval quality. A stage gate that
skips consolidation leaves the next stage starting cold.

## Scopes

Memory is namespaced: `org.finance`, `org.decisions`, `venture.<id>.engineering`, `council.verdicts`,
and so on. Each agent declares the scopes it reads in its frontmatter, which keeps context packages
small and keeps one venture's assumptions from leaking into another's.
