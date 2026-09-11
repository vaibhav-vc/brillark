# Stage gates

Seven stages. The `director` is the only agent that may declare one complete, and only in writing.

| Stage | Question it answers | Exit requires |
|---|---|---|
| **Idea** | Is there something here worth spending on? | Intent restated and confirmed; charter written; kill criteria set |
| **Business model** | Could this make money if it worked? | Evidence-tagged canvas; pricing defended from floor and ceiling; unit economics positive or a named path to positive; Council verdict |
| **Validation** | Do real customers behave the way we assumed? | Five or more qualified conversations; disconfirming evidence reported first; canvas updated from evidence |
| **MVP** | What is the smallest thing that tests our riskiest belief? | Scope line justified against the riskiest assumption; every deferral has a revisit trigger; ADR recorded; threat model complete |
| **Launch** | Will real users do the thing? | Rollback verified; claims substantiated; privacy and security signed off; success signal instrumented |
| **Upgrade** | What did we learn, and what is next? | Features judged against pre-set signals; expansion sequenced behind prerequisites; scaling limits known and costed |
| **Scale** | Does this hold at ten times the size? | Breaking point per critical path; survival requirement stated; moat forming with evidence |

## What a gate actually requires

Three things, every time:

1. **The domain evidence pack** — the artifacts the stage was supposed to produce, each with its
   evidence grade.
2. **A Council verdict** — schema-valid, with every blocker either cleared or explicitly overruled in
   writing.
3. **A written decision** — go, no-go, pivot, or kill, naming the evidence that moved it and the
   evidence that would reverse it.

Then `09-memory-consolidation` runs. A gate that skips consolidation leaves the next stage starting cold.

## The four outcomes

- **Go** — the belief held. Fund the next stage with an explicit budget.
- **No-go** — not yet. Name what specifically must be true, and the test that would establish it.
- **Pivot** — the belief failed but something adjacent is worth pursuing. Requires a new charter,
  not an amendment to the old one.
- **Kill** — the kill criterion was met. Stop. Consolidate what was learned into memory so the next
  venture starts from it.

## Kill criteria are written first

`kill-criteria-definition` runs when a bet starts, not when it is struggling. A criterion written
after the evidence arrives is a rationalisation. Each one needs a numeric threshold, a deadline, and
a named agent who declares it.

## The rule that matters most

**No stage advances on effort.** Time spent, code written, and interviews conducted are inputs. A gate
is passed on evidence about the world, not on evidence of activity.
