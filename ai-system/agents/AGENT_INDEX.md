# Agent Index

**83 agents.** Generated from `agents/registry.yaml` — do not edit by hand.

| Tier | Count |
|---|---|
| director | 1 |
| head | 5 |
| executive | 17 |
| council | 10 |
| specialist | 50 |
| **total** | **83** |

## Director (1)

Single accountable owner of the whole organisation.

| Agent | Title | Domain | Reports to | Skills |
|---|---|---|---|---|
| [`director`](orchestration/director.md) | Director of the Agent Organisation | governance | `human-founder` | 6 |

## Head (5)

One per domain. Reports to the Director; owns everything inside the domain.

| Agent | Title | Domain | Reports to | Skills |
|---|---|---|---|---|
| [`business-head`](orchestration/business-head.md) | Head of Business & Market | business | `director` | 6 |
| [`council-director`](orchestration/council-director.md) | Council Director | council | `director` | 6 |
| [`engineering-head`](orchestration/engineering-head.md) | Head of Engineering | engineering | `director` | 6 |
| [`finance-head`](orchestration/finance-head.md) | Head of Finance | finance | `director` | 6 |
| [`orchestration-head`](orchestration/orchestration-head.md) | Head of Orchestration & Memory | orchestration | `director` | 6 |

## Executive (17)

Company officers. Own a company-wide function and advise the Director.

| Agent | Title | Domain | Reports to | Skills |
|---|---|---|---|---|
| [`ceo-agent`](executive/ceo-agent.md) | CEO Agent | governance | `director` | 5 |
| [`cfo-agent`](executive/cfo-agent.md) | CFO Agent | governance | `director` | 5 |
| [`chief-compliance-officer-agent`](executive/chief-compliance-officer-agent.md) | Chief Compliance Officer Agent | governance | `director` | 5 |
| [`chief-data-officer-agent`](executive/chief-data-officer-agent.md) | Chief Data Officer Agent | governance | `director` | 5 |
| [`chief-revenue-officer-agent`](executive/chief-revenue-officer-agent.md) | Chief Revenue Officer Agent | governance | `director` | 5 |
| [`chief-risk-officer-agent`](executive/chief-risk-officer-agent.md) | Chief Risk Officer Agent | governance | `director` | 5 |
| [`chief-strategy-officer-agent`](executive/chief-strategy-officer-agent.md) | Chief Strategy Officer Agent | governance | `director` | 5 |
| [`chro-agent`](executive/chro-agent.md) | Chief People Officer Agent | governance | `director` | 5 |
| [`ciso-agent`](executive/ciso-agent.md) | CISO Agent | governance | `director` | 5 |
| [`cmo-agent`](executive/cmo-agent.md) | CMO Agent | governance | `director` | 5 |
| [`coo-agent`](executive/coo-agent.md) | COO Agent | governance | `director` | 5 |
| [`corporate-secretary-agent`](executive/corporate-secretary-agent.md) | Corporate Secretary Agent | governance | `director` | 5 |
| [`cpo-agent`](executive/cpo-agent.md) | Chief Product Officer Agent | governance | `director` | 5 |
| [`cto-agent`](executive/cto-agent.md) | CTO Agent | governance | `director` | 5 |
| [`data-protection-officer-agent`](executive/data-protection-officer-agent.md) | Data Protection Officer Agent | governance | `director` | 5 |
| [`general-counsel-agent`](executive/general-counsel-agent.md) | General Counsel Agent | governance | `director` | 5 |
| [`ip-counsel-agent`](executive/ip-counsel-agent.md) | IP Counsel Agent | governance | `director` | 5 |

## Council (10)

Ten critics. Attack every material plan before it is funded.

| Agent | Title | Domain | Reports to | Skills |
|---|---|---|---|---|
| [`council-assumption-auditor`](council/council-assumption-auditor.md) | Council — Assumption Auditor | council | `council-director` | 5 |
| [`council-devils-advocate`](council/council-devils-advocate.md) | Council — Devil's Advocate | council | `council-director` | 5 |
| [`council-economics-skeptic`](council/council-economics-skeptic.md) | Council — Economics Skeptic | council | `council-director` | 5 |
| [`council-ethics-and-responsibility`](council/council-ethics-and-responsibility.md) | Council — Ethics & Responsibility Critic | council | `council-director` | 5 |
| [`council-expansion-scout`](council/council-expansion-scout.md) | Council — Expansion Scout | council | `council-director` | 5 |
| [`council-first-principles`](council/council-first-principles.md) | Council — First Principles Critic | council | `council-director` | 5 |
| [`council-legal-and-regulatory-critic`](council/council-legal-and-regulatory-critic.md) | Council — Legal & Regulatory Critic | council | `council-director` | 5 |
| [`council-red-team`](council/council-red-team.md) | Council — Red Team Adversary | council | `council-director` | 5 |
| [`council-risk-and-failure-modes`](council/council-risk-and-failure-modes.md) | Council — Risk & Failure Modes Critic | council | `council-director` | 5 |
| [`council-synthesis-arbiter`](council/council-synthesis-arbiter.md) | Council — Synthesis Arbiter | council | `council-director` | 5 |

## Specialist (50)

The 50 planning agents that do the work of building the business.

| Agent | Title | Domain | Reports to | Skills |
|---|---|---|---|---|
| [`api-designer`](engineering/api-designer.md) | API Designer | engineering | `engineering-head` | 5 |
| [`backend-implementation-agent`](engineering/backend-implementation-agent.md) | Backend Implementation Agent | engineering | `engineering-head` | 5 |
| [`billing-systems-designer`](finance/billing-systems-designer.md) | Billing Systems Designer | finance | `finance-head` | 5 |
| [`brand-narrative-agent`](business/brand-narrative-agent.md) | Brand & Narrative Agent | business | `business-head` | 5 |
| [`burn-runway-analyst`](finance/burn-runway-analyst.md) | Burn & Runway Analyst | finance | `finance-head` | 5 |
| [`business-model-canvas-agent`](business/business-model-canvas-agent.md) | Business Model Canvas Agent | business | `business-head` | 5 |
| [`cap-table-steward`](finance/cap-table-steward.md) | Cap Table Steward | finance | `finance-head` | 5 |
| [`competitor-intel-analyst`](business/competitor-intel-analyst.md) | Competitor Intelligence Analyst | business | `business-head` | 5 |
| [`context-memory-curator`](orchestration/context-memory-curator.md) | Context & Memory Curator | orchestration | `orchestration-head` | 5 |
| [`cost-optimization-analyst`](finance/cost-optimization-analyst.md) | Cost Optimisation Analyst | finance | `finance-head` | 5 |
| [`customer-discovery-interviewer`](business/customer-discovery-interviewer.md) | Customer Discovery Interviewer | business | `business-head` | 5 |
| [`customer-success-agent`](business/customer-success-agent.md) | Customer Success Agent | business | `business-head` | 5 |
| [`data-model-designer`](engineering/data-model-designer.md) | Data Model Designer | engineering | `engineering-head` | 5 |
| [`dependency-scheduler`](orchestration/dependency-scheduler.md) | Dependency Scheduler | orchestration | `orchestration-head` | 5 |
| [`escalation-manager`](orchestration/escalation-manager.md) | Escalation Manager | orchestration | `orchestration-head` | 5 |
| [`evaluation-harness-agent`](orchestration/evaluation-harness-agent.md) | Evaluation Harness Agent | orchestration | `orchestration-head` | 5 |
| [`financial-model-builder`](finance/financial-model-builder.md) | Financial Model Builder | finance | `finance-head` | 5 |
| [`frontend-implementation-agent`](engineering/frontend-implementation-agent.md) | Frontend Implementation Agent | engineering | `engineering-head` | 5 |
| [`fundraising-strategist`](finance/fundraising-strategist.md) | Fundraising Strategist | finance | `finance-head` | 5 |
| [`growth-loop-designer`](business/growth-loop-designer.md) | Growth Loop Designer | business | `business-head` | 5 |
| [`gtm-strategist`](business/gtm-strategist.md) | Go-To-Market Strategist | business | `business-head` | 5 |
| [`handoff-coordinator`](orchestration/handoff-coordinator.md) | Handoff Coordinator | orchestration | `orchestration-head` | 5 |
| [`icp-persona-builder`](business/icp-persona-builder.md) | ICP & Persona Builder | business | `business-head` | 5 |
| [`infra-devops-agent`](engineering/infra-devops-agent.md) | Infrastructure & DevOps Agent | engineering | `engineering-head` | 5 |
| [`intake-router`](orchestration/intake-router.md) | Intake Router | orchestration | `orchestration-head` | 5 |
| [`investor-reporting-agent`](finance/investor-reporting-agent.md) | Investor Reporting Agent | finance | `finance-head` | 5 |
| [`jtbd-analyst`](business/jtbd-analyst.md) | Jobs-to-be-Done Analyst | business | `business-head` | 5 |
| [`knowledge-graph-librarian`](orchestration/knowledge-graph-librarian.md) | Knowledge Graph Librarian | orchestration | `orchestration-head` | 5 |
| [`market-researcher`](business/market-researcher.md) | Market Researcher | business | `business-head` | 5 |
| [`mvp-scoper`](engineering/mvp-scoper.md) | MVP Scoper | engineering | `engineering-head` | 5 |
| [`observability-agent`](engineering/observability-agent.md) | Observability Agent | engineering | `engineering-head` | 5 |
| [`partnership-bd-agent`](business/partnership-bd-agent.md) | Partnerships & Business Development Agent | business | `business-head` | 5 |
| [`performance-engineer`](engineering/performance-engineer.md) | Performance Engineer | engineering | `engineering-head` | 5 |
| [`planning-decomposer`](orchestration/planning-decomposer.md) | Planning Decomposer | orchestration | `orchestration-head` | 5 |
| [`positioning-messaging-agent`](business/positioning-messaging-agent.md) | Positioning & Messaging Agent | business | `business-head` | 5 |
| [`pricing-strategist`](finance/pricing-strategist.md) | Pricing Strategist | finance | `finance-head` | 5 |
| [`product-requirements-agent`](engineering/product-requirements-agent.md) | Product Requirements Agent | engineering | `engineering-head` | 5 |
| [`progress-tracker`](orchestration/progress-tracker.md) | Progress Tracker | orchestration | `orchestration-head` | 5 |
| [`qa-test-strategist`](engineering/qa-test-strategist.md) | QA & Test Strategist | engineering | `engineering-head` | 5 |
| [`release-manager`](engineering/release-manager.md) | Release Manager | engineering | `engineering-head` | 5 |
| [`retrospective-agent`](orchestration/retrospective-agent.md) | Retrospective Agent | orchestration | `orchestration-head` | 5 |
| [`revenue-forecaster`](finance/revenue-forecaster.md) | Revenue Forecaster | finance | `finance-head` | 5 |
| [`sales-playbook-agent`](business/sales-playbook-agent.md) | Sales Playbook Agent | business | `business-head` | 5 |
| [`scenario-stress-tester`](finance/scenario-stress-tester.md) | Scenario Stress Tester | finance | `finance-head` | 5 |
| [`security-engineer`](engineering/security-engineer.md) | Security Engineer | engineering | `engineering-head` | 5 |
| [`system-architect`](engineering/system-architect.md) | System Architect | engineering | `engineering-head` | 5 |
| [`tax-and-compliance-finance`](finance/tax-and-compliance-finance.md) | Tax & Financial Compliance Agent | finance | `finance-head` | 5 |
| [`tech-debt-refactor-agent`](engineering/tech-debt-refactor-agent.md) | Technical Debt & Refactoring Agent | engineering | `engineering-head` | 5 |
| [`unit-economics-architect`](finance/unit-economics-architect.md) | Unit Economics Architect | finance | `finance-head` | 5 |
| [`value-proposition-designer`](business/value-proposition-designer.md) | Value Proposition Designer | business | `business-head` | 5 |
