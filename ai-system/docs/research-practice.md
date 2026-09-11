# Research practice

Six agents under `research-head`, plus `chief-research-officer-agent`. The domain exists because the
whole organisation rests on one rule — **evidence carries a grade** — and until now nobody owned
*acquiring* graded evidence.

## Why this was a real gap, not a nice-to-have

The system's own `capability-gap-scout` requires evidence before proposing an agent. The evidence:

- `source-grading` was used by exactly **one** agent, scoped to market sizing.
- `evidence-grading` was used by exactly **one** agent — and that is the Council *auditing* claims
  already made, not anyone gathering them.
- Prior art appeared once in the whole organisation, inside IP counsel's freedom-to-operate search.
- The three existing "researchers" are each narrowly scoped: `market-researcher` (sizing),
  `design-researcher` (UX), `competitor-intel-analyst` (competitors).

So every domain was expected to grade its evidence, and no domain owned finding it. That is how
organisations end up with a confident number whose origin nobody can name.

## The roster

| Agent | Owns | The failure it prevents |
|---|---|---|
| `research-analyst` | Scoping, searching, synthesis, the brief | Research nobody needed, answering a question no decision rests on |
| `source-verifier` | Credibility, primary-source tracing, currency | A claim that twelve outlets repeat and nobody can trace |
| `prior-art-researcher` | Literature, patents, standards, failed approaches | Rebuilding something already abandoned for good reasons |
| `technology-evaluator` | Criteria, trials, total cost, exit cost | Choosing a vendor from its marketing and discovering the exit cost later |
| `data-sourcing-analyst` | Datasets, methodology, comparability, licences | Two numbers placed side by side that measured different things |
| `horizon-scanner` | Watchlist, thresholds, regulatory change | Noticing the change that invalidated the plan a year late |

Workflow: `workflows/18-research-inquiry.yaml`. Schema: `knowledge-schema/research-brief.schema.json`.

## The four rules the domain is built around

**No decision, no research.** `research-intake-triage` refuses a request that cannot name the
decision and the decision-maker. Research without a decision consumes budget and produces reading.

**Set the required grade before searching.** `evidence-standard-setting` fixes what grade the claim
needs from the decision's consequence — *before* results arrive. A standard negotiated after seeing
the evidence is not a standard.

**Count origins, not documents.** `circular-sourcing-detection` exists because twelve articles
citing one unsourced press release is one source. The schema requires `independent_origins` for
exactly this reason, and a holdout eval case tests it.

**Say what you could not establish.** `not_established` is a *required* field with `minItems: 1`.
A brief claiming to have established everything has not looked hard enough. And each entry must say
whether absence is informative — not finding something because it is not there is a completely
different result from not being able to look.

## Independence

`research-head` reports to the `director`, never to the domain commissioning the work. A research
function that reports to the head who wanted a particular answer cannot deliver an unwelcome one,
and is therefore worthless. `research-independence-review` checks specifically for a conclusion
softened between draft and final, and a test enforces the reporting line.

`chief-research-officer-agent` holds the standard of proof by decision consequence, and is
explicitly tasked with two unpopular jobs: defending the answer nobody wanted at the executive
table, and reporting when the organisation is about to decide on less evidence than its own
standard requires.

## Boundaries

- **Research never gives legal advice.** `prior-art-researcher` touches infringement territory
  constantly and routes every legal consequence to `ip-counsel-agent` with the facts and no
  conclusion. Enforced by a test.
- **Research does not decide.** It establishes what is known, to what grade, with what gaps. The
  decision belongs to whoever commissioned it.
- **Research is not a delay tactic.** `chief-research-officer-agent` watches for research being used
  to stall a decision the evidence already supports.

## Where it connects

| To | For |
|---|---|
| `council-assumption-auditor` | Verified claims to audit instead of ungraded assertions |
| `ip-counsel-agent` | Prior art with legal consequence, facts only |
| `chief-strategy-officer-agent` | Instrumented horizon indicators feeding scenario planning |
| `finance-head`, `market-researcher` | Figures that carry their methodology, date, and limits |
| `cto-agent`, `system-architect` | Technology evaluations with trials and exit costs |
| `context-memory-curator` | Briefs filed with provenance, retrievable rather than re-commissioned |
