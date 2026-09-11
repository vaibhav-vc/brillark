# Conventions

## Naming

- Agents: `kebab-case`, role-descriptive, suffixed `-agent` only for company officers (`cfo-agent`)
  where the bare title would be ambiguous.
- Skills: `kebab-case` verb-or-noun phrases naming the *procedure* (`unit-economics-analysis`),
  never the tool.
- Artifacts: `kebab-case.md` named for content, not for the agent that produced it.
- Ids: prefixed by type — `mem_`, `ent_`, `dec_`, `ver_`, `art_`, `task_`, `ho_`.

## Evidence grades

`measured` > `sourced` > `benchmarked` > `estimated` > `guessed`. Every load-bearing claim carries one.
A `guessed` claim may not be load-bearing at a stage gate. Grades propagate: a figure derived from an
estimate is at best an estimate.

## Ownership

Exactly one owner per task, artifact, risk, and metric. Where two agents both have a claim, the one
accountable for the *outcome* owns it and the other is consulted. "Co-owned" is not a state this
system has.

## Escalation

Up the reporting line only, one level at a time. Cross-domain conflicts travel to the nearest common
parent — usually the Director. Every escalation carries a framed decision with options, a
recommendation, a deadline, and the default if no decision arrives.

## Handoffs

Nothing is transferred until the receiver accepts. A rejected handoff names one specific gap. Receivers
do not silently repair sender mistakes, because that hides the defect and it recurs.

## Writing style for artifacts

- Lead with the answer. The reasoning follows.
- Report disconfirming evidence before confirming evidence.
- Give a range where the honest answer is a range.
- Name the source of every number.
- State what would change your mind.

## Definitions of done

Written before work starts, checkable by someone other than the author, and free of subjective terms.
"High quality" is not a condition. "Passes the accessibility review at AA with findings recorded" is.

## Reversibility

Classify decisions as one-way or two-way doors. Two-way doors are decided fast and cheaply by the
owning agent. One-way doors go to the Council and then to the Director, regardless of how obvious
they seem.

## Budgets

Every task carries a ceiling on time, tokens, and spend, and an `on_exhaustion` behaviour. Unbounded
tasks consume whatever is available. Contingency is held centrally by the head, not distributed in advance.
