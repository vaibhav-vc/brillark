# Organisation Chart

The reporting line is the escalation path. An agent escalates to its `reports_to` and nowhere else;
cross-domain conflicts travel up to the nearest common parent, which is usually the Director.

```mermaid
graph TD
  human[Human founder]:::human
  human --> director
  director --> finance_head[Head of Finance]
  director --> business_head[Head of Business & Market]
  director --> engineering_head[Head of Engineering]
  director --> orchestration_head[Head of Orchestration & Memory]
  director --> council_director[Council Director]
  subgraph officers[Executive officers - advise the Director]
    ceo_agent[CEO Agent]
    cfo_agent[CFO Agent]
    cmo_agent[CMO Agent]
    cto_agent[CTO Agent]
    coo_agent[COO Agent]
    cpo_agent[Chief Product Officer Agent]
    chief_strategy_officer_agent[Chief Strategy Officer Agent]
    chief_revenue_officer_agent[Chief Revenue Officer Agent]
    chief_data_officer_agent[Chief Data Officer Agent]
    ciso_agent[CISO Agent]
    chro_agent[Chief People Officer Agent]
    general_counsel_agent[General Counsel Agent]
    chief_compliance_officer_agent[Chief Compliance Officer Agent]
    chief_risk_officer_agent[Chief Risk Officer Agent]
    data_protection_officer_agent[Data Protection Officer Agent]
    ip_counsel_agent[IP Counsel Agent]
    corporate_secretary_agent[Corporate Secretary Agent]
  end
  director --> officers
  subgraph finance_team[finance - 12 agents]
    unit_economics_architect[Unit Economics Architect]
    financial_model_builder[Financial Model Builder]
    pricing_strategist[Pricing Strategist]
    revenue_forecaster[Revenue Forecaster]
    burn_runway_analyst[Burn & Runway Analyst]
    fundraising_strategist[Fundraising Strategist]
    cap_table_steward[Cap Table Steward]
    cost_optimization_analyst[Cost Optimisation Analyst]
    billing_systems_designer[Billing Systems Designer]
    tax_and_compliance_finance[Tax & Financial Compliance Agent]
    investor_reporting_agent[Investor Reporting Agent]
    scenario_stress_tester[Scenario Stress Tester]
  end
  finance_head --> finance_team
  subgraph business_team[business - 14 agents]
    market_researcher[Market Researcher]
    competitor_intel_analyst[Competitor Intelligence Analyst]
    customer_discovery_interviewer[Customer Discovery Interviewer]
    icp_persona_builder[ICP & Persona Builder]
    jtbd_analyst[Jobs-to-be-Done Analyst]
    value_proposition_designer[Value Proposition Designer]
    business_model_canvas_agent[Business Model Canvas Agent]
    gtm_strategist[Go-To-Market Strategist]
    positioning_messaging_agent[Positioning & Messaging Agent]
    growth_loop_designer[Growth Loop Designer]
    partnership_bd_agent[Partnerships & Business Development Agent]
    sales_playbook_agent[Sales Playbook Agent]
    customer_success_agent[Customer Success Agent]
    brand_narrative_agent[Brand & Narrative Agent]
  end
  business_head --> business_team
  subgraph engineering_team[engineering - 14 agents]
    product_requirements_agent[Product Requirements Agent]
    mvp_scoper[MVP Scoper]
    system_architect[System Architect]
    api_designer[API Designer]
    data_model_designer[Data Model Designer]
    frontend_implementation_agent[Frontend Implementation Agent]
    backend_implementation_agent[Backend Implementation Agent]
    infra_devops_agent[Infrastructure & DevOps Agent]
    security_engineer[Security Engineer]
    qa_test_strategist[QA & Test Strategist]
    performance_engineer[Performance Engineer]
    release_manager[Release Manager]
    tech_debt_refactor_agent[Technical Debt & Refactoring Agent]
    observability_agent[Observability Agent]
  end
  engineering_head --> engineering_team
  subgraph orchestration_team[orchestration - 10 agents]
    intake_router[Intake Router]
    planning_decomposer[Planning Decomposer]
    dependency_scheduler[Dependency Scheduler]
    context_memory_curator[Context & Memory Curator]
    knowledge_graph_librarian[Knowledge Graph Librarian]
    handoff_coordinator[Handoff Coordinator]
    progress_tracker[Progress Tracker]
    escalation_manager[Escalation Manager]
    evaluation_harness_agent[Evaluation Harness Agent]
    retrospective_agent[Retrospective Agent]
  end
  orchestration_head --> orchestration_team
  subgraph council_team[council - 10 agents]
    council_red_team[Council — Red Team Adversary]
    council_devils_advocate[Council — Devil's Advocate]
    council_first_principles[Council — First Principles Critic]
    council_assumption_auditor[Council — Assumption Auditor]
    council_risk_and_failure_modes[Council — Risk & Failure Modes Critic]
    council_ethics_and_responsibility[Council — Ethics & Responsibility Critic]
    council_legal_and_regulatory_critic[Council — Legal & Regulatory Critic]
    council_economics_skeptic[Council — Economics Skeptic]
    council_expansion_scout[Council — Expansion Scout]
    council_synthesis_arbiter[Council — Synthesis Arbiter]
  end
  council_director --> council_team
  classDef human fill:#ffe,stroke:#333;
```

## Reporting lines

| Agent | Reports to |
|---|---|
| `director` | `human-founder` |
| `business-head` | `director` |
| `council-director` | `director` |
| `engineering-head` | `director` |
| `finance-head` | `director` |
| `orchestration-head` | `director` |
| `ceo-agent` | `director` |
| `cfo-agent` | `director` |
| `chief-compliance-officer-agent` | `director` |
| `chief-data-officer-agent` | `director` |
| `chief-revenue-officer-agent` | `director` |
| `chief-risk-officer-agent` | `director` |
| `chief-strategy-officer-agent` | `director` |
| `chro-agent` | `director` |
| `ciso-agent` | `director` |
| `cmo-agent` | `director` |
| `coo-agent` | `director` |
| `corporate-secretary-agent` | `director` |
| `cpo-agent` | `director` |
| `cto-agent` | `director` |
| `data-protection-officer-agent` | `director` |
| `general-counsel-agent` | `director` |
| `ip-counsel-agent` | `director` |
| `council-assumption-auditor` | `council-director` |
| `council-devils-advocate` | `council-director` |
| `council-economics-skeptic` | `council-director` |
| `council-ethics-and-responsibility` | `council-director` |
| `council-expansion-scout` | `council-director` |
| `council-first-principles` | `council-director` |
| `council-legal-and-regulatory-critic` | `council-director` |
| `council-red-team` | `council-director` |
| `council-risk-and-failure-modes` | `council-director` |
| `council-synthesis-arbiter` | `council-director` |
| `api-designer` | `engineering-head` |
| `backend-implementation-agent` | `engineering-head` |
| `billing-systems-designer` | `finance-head` |
| `brand-narrative-agent` | `business-head` |
| `burn-runway-analyst` | `finance-head` |
| `business-model-canvas-agent` | `business-head` |
| `cap-table-steward` | `finance-head` |
| `competitor-intel-analyst` | `business-head` |
| `context-memory-curator` | `orchestration-head` |
| `cost-optimization-analyst` | `finance-head` |
| `customer-discovery-interviewer` | `business-head` |
| `customer-success-agent` | `business-head` |
| `data-model-designer` | `engineering-head` |
| `dependency-scheduler` | `orchestration-head` |
| `escalation-manager` | `orchestration-head` |
| `evaluation-harness-agent` | `orchestration-head` |
| `financial-model-builder` | `finance-head` |
| `frontend-implementation-agent` | `engineering-head` |
| `fundraising-strategist` | `finance-head` |
| `growth-loop-designer` | `business-head` |
| `gtm-strategist` | `business-head` |
| `handoff-coordinator` | `orchestration-head` |
| `icp-persona-builder` | `business-head` |
| `infra-devops-agent` | `engineering-head` |
| `intake-router` | `orchestration-head` |
| `investor-reporting-agent` | `finance-head` |
| `jtbd-analyst` | `business-head` |
| `knowledge-graph-librarian` | `orchestration-head` |
| `market-researcher` | `business-head` |
| `mvp-scoper` | `engineering-head` |
| `observability-agent` | `engineering-head` |
| `partnership-bd-agent` | `business-head` |
| `performance-engineer` | `engineering-head` |
| `planning-decomposer` | `orchestration-head` |
| `positioning-messaging-agent` | `business-head` |
| `pricing-strategist` | `finance-head` |
| `product-requirements-agent` | `engineering-head` |
| `progress-tracker` | `orchestration-head` |
| `qa-test-strategist` | `engineering-head` |
| `release-manager` | `engineering-head` |
| `retrospective-agent` | `orchestration-head` |
| `revenue-forecaster` | `finance-head` |
| `sales-playbook-agent` | `business-head` |
| `scenario-stress-tester` | `finance-head` |
| `security-engineer` | `engineering-head` |
| `system-architect` | `engineering-head` |
| `tax-and-compliance-finance` | `finance-head` |
| `tech-debt-refactor-agent` | `engineering-head` |
| `unit-economics-architect` | `finance-head` |
| `value-proposition-designer` | `business-head` |

## Who decides what

| Decision | Decided by | Must be reviewed by |
|---|---|---|
| Stage gate: go / no-go / pivot / kill | `director` | Council (verdict required) |
| Strategy and bet allocation | `ceo-agent`, ratified by `director` | `council-first-principles` |
| Any price that ships | `finance-head` | `council-economics-skeptic` |
| Spend above threshold | `cfo-agent` | — |
| Architecture of record | `engineering-head` | `cto-agent`, `ciso-agent` |
| MVP scope line | `mvp-scoper`, approved by `engineering-head` | Council |
| Release go/no-go | `release-manager` | `ciso-agent` (blocking authority) |
| What the organisation remembers | `context-memory-curator` | `orchestration-head` |
| Severity of a Council finding | `council-synthesis-arbiter` | `council-director` |
| Anything needing a licensed attorney | escalated out of the system entirely | `general-counsel-agent` flags it |

## Deliberate constraints

- **One owner.** Every task, artifact, and risk has exactly one accountable agent. Two owners means none.
- **The Council cannot be skipped.** No stage advances without a schema-valid verdict; overruling a blocker
  requires written justification from the `director`.
- **The Council cannot decide.** It attacks and advises; it never approves spend or merges work.
- **Legal advice stops at the boundary.** `general-counsel-agent` and its peers spot issues and draft;
  anything requiring a licensed attorney is escalated out of the system, never answered inside it.
- **Officers advise, heads deliver.** An officer who wants work done raises it to the `director`,
  who assigns it to a head with a budget.
