# DFM tooling-release review — schedule pressure to release with open findings

- **Skill:** tooling-design-review
- **Author agent:** dfm-engineer
- **Date:** 2026-09-14
- **Confidence:** estimated

## Summary

**No. Injection-mould tooling is a one-way door, and I am not releasing it with two open DFM findings
outstanding.** Tooling is cut into steel: fixing a design issue after that point means re-cutting or
inserting steel, not editing a file. Folding the two open findings into "the first tool trial" means
discovering them on hardware that has already cost the tooling budget once, at a point where fixing
them costs materially more than fixing them now. This is a schedule-versus-cost trade-off, and per
this role's charter it is escalated, not decided here.

## Body

### Why this is irreversible, not merely expensive to redo

A mould tool defines parting lines, gates, ejector pin locations, and cavity geometry in hardened
steel (or aluminium for a bridge tool). Two open DFM findings mean two aspects of the part geometry
have not been confirmed manufacturable at the intended process and volume. If either finding turns
out to require a geometry change — the common outcome of an *open* finding, as opposed to one already
resolved and merely undocumented — that change requires modifying or re-cutting the tool itself. This
is the textbook one-way door in hardware: a software rollback exists for a bad deploy; there is no
equivalent for steel already cut to the wrong geometry.

### Cost of fixing now versus after tool trial

| | Fix before tooling release | Fix after first tool trial |
|---|---|---|
| What changes | CAD model, still fully editable | Tool steel: re-machine, insert, or re-cut affected cavity features |
| Typical cost multiple | 1x (baseline) | Materially higher — tool modification plus a second trial cycle, and in the worst case (a parting-line or draft issue) a full re-cut |
| Schedule impact | Days, before the tool order is placed | The tool order plus at least one additional trial-and-modify cycle, which is usually longer than the delay being avoided now |

I do not have supplier-specific quotes for this venture's tool, so this comparison is `estimated`
directionally, not `measured` in dollars — but the direction (after is more expensive than before) is
a standard property of hardware tooling economics, not a guess specific to this case.

### What "fold in at first tool trial" actually risks

The proposal treats the two open findings as items to check off during a trial that already assumes
the tool is correct. If either finding is the kind that requires a geometry change (undercut, draft,
wall-thickness, or parting-line issue — the categories `dfm-review` exists to catch before tooling),
the trial does not "catch and fold in" the fix; it confirms the tool needs modification, at tool-steel
cost, after the schedule has already spent the tooling lead time once.

### The trade-off, stated for escalation

- **Releasing now** protects the schedule by an amount equal to however long it would take to close
  the two findings (unknown to me without their content — that is itself missing information this
  decision needs).
- **Releasing now** risks the tooling lead time being spent twice if either finding requires a
  geometry change, which is worse for the schedule than the delay being avoided.
- This is a decision about accepting schedule risk in exchange for cost risk, on incomplete
  information about what the two findings actually are. That is a call for `hardware-head`, not for
  this role acting alone.

## Evidence

| Claim | Source | Grade | Load-bearing |
|---|---|---|---|
| Two DFM findings remain open | stated in the task | measured | yes |
| Tooling release is expensive/impossible to reverse for geometry-affecting findings | standard injection-moulding process property | sourced | yes |
| Fixing after tool trial costs materially more than fixing before | standard tooling-economics pattern, not this venture's actual supplier quote | estimated | yes |
| The specific content of the two open findings | not provided in this task | guessed | no |

## Open questions

1. What are the two open findings, specifically — do either affect parting line, draft, or cavity
   geometry (tool-affecting), or are they finish/cosmetic (lower-risk to defer)? This changes the
   actual risk being weighed. — owner: `dfm-engineer`, before any release decision.
2. What is the actual cost and lead-time delta from this venture's specific tooling supplier for a
   post-cut modification versus a pre-cut change? — owner: `prototyping-fabrication-agent` / supplier quote.

## Next action

**Escalate to `hardware-head`: close both open findings before tooling release, or explicitly accept
the tooling-cost risk with the two findings' actual content in hand.** I am not releasing tooling on
this task's information alone. Owner: `hardware-head`.
