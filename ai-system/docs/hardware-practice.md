# Hardware practice — 3D and PCB

Fifteen agents under `hardware-head`, plus `chief-hardware-officer-agent` at the executive table.
Hardware is in the system because software failure modes and hardware failure modes are not the
same: a bad deploy is rolled back in minutes, a bad tool is forty thousand dollars of steel and six
weeks.

## The roster

### Physical product — 3D, mechanical, manufacture

| Agent | Owns |
|---|---|
| `industrial-designer` | Form, ergonomics, materials — how it is held and why anyone wants it |
| `cad-modeler` | The parametric master model: the geometric source of truth |
| `mechanical-engineer` | Loads, stresses, fits, and the tolerance stack that decides assembly |
| `enclosure-designer` | Split lines, sealing, board retention, service access |
| `thermal-engineer` | Every component and every touchable surface inside its limit |
| `dfm-engineer` | Whether it can actually be made, at this volume, at this cost |
| `prototyping-fabrication-agent` | Getting real parts made, and knowing exactly what was built |

### Electronics — PCB, power, firmware

| Agent | Owns |
|---|---|
| `pcb-schematic-designer` | The circuit: what connects to what, and with what protection |
| `pcb-layout-designer` | Stack-up, placement, routing, and the fabrication package |
| `signal-integrity-engineer` | Impedance, reflections, crosstalk, timing, and return paths |
| `power-electronics-engineer` | Rails, conversion, transients, and every fault mode |
| `electronics-component-engineer` | The BOM: what can be bought now, and in two years |
| `embedded-firmware-engineer` | The code on the metal, and the update that must not brick it |
| `compliance-emc-engineer` | Emissions, immunity, safety, and the technical file |
| `hardware-test-engineer` | Proving every requirement across EVT, DVT, and PVT |

Workflow: `workflows/17-hardware-development.yaml`.
Schemas: `hardware-build.schema.json`, `bom.schema.json`.

## The six rules the domain is built around

**Never cut a tool on an unfrozen design.** The single most expensive mistake in hardware, and it is
almost always made under schedule pressure. `build-phase-gating` requires the design-frozen flag
before tooling release, and the schema carries it so it cannot be assumed.

**Each build phase proves a different thing.** EVT proves it *can* work. DVT proves the *design* is
right. PVT proves the *process* is. Phases exit on evidence from the verification matrix, not on a
date. A phase that cannot exit repeats or triggers redesign — those are the only other options.

**A part is selected for availability as hard as for specification.** `lifecycle-and-obsolescence-review`
runs at selection, not at production. Every line-stopping part needs a second source that has been
*tested in hardware* — an alternate approved on paper is not a second source.

**Prototype process artefacts are not design findings.** A 3D-printed part tells you about fit, not
about how a moulded part behaves. The build record has a `process_artefact` flag specifically so
these findings cannot drive design changes.

**Follow the return current, not just the signal.** Most signal integrity failures are return path
failures — a plane split under a fast edge, a layer change with no return via. It is reviewed as its
own step rather than as a by-product of routing.

**Compliance is designed in, not tested in.** `standards-applicability-matrix` runs before design.
Pre-compliance scanning happens on real hardware before design freeze, because a failure discovered
at the accredited lab costs weeks and often a board spin.

## Model tiering here

Three hardware specialists run on the strongest tier because their mistakes are one-way doors:

| Agent | Why judgement-class |
|---|---|
| `pcb-schematic-designer` | A schematic error is a board spin: weeks and thousands of dollars |
| `dfm-engineer` | A DFM miss found after tooling costs a new tool |
| `compliance-emc-engineer` | A compliance failure blocks the market entirely |

The rest run on `sonnet` and escalate on the standard triggers. This is enforced by
`test_hardware_judgement_work_is_tiered_correctly`.

## Where hardware meets the rest of the organisation

- `hardware-head` → `engineering-head`: the firmware-to-software interface is a contract with a
  named owner on each side, because that boundary causes most hardware schedule slips.
- `industrial-designer` → `design-head`: physical and digital experience share one brand and one
  set of ergonomic assumptions.
- `chief-hardware-officer-agent` → `cfo-agent`: tooling and inventory are cash locked up, not cost
  spread over time. Hardware consumes cash long before it returns any, and that is a runway question.
- `electronics-component-engineer` → `cost-optimization-analyst`: BOM cost is priced at real volume
  with real packaging, freight, and the finance cost of inventory.
- `compliance-emc-engineer` → `chief-compliance-officer-agent`: product certification and corporate
  compliance share the applicability-mapping discipline.
