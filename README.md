# IP-Centrum

# Agentic AI Strategic Framework — Revised
## IP Centrum — European Patent Validation & Renewals
**Version 2.0 | Confidential Strategic Document**
---

## Executive Summary

IP Centrum's value proposition is structurally agentic: a single client instruction triggers an end-to-end process across up to 46 jurisdictions, multiple agents, translators, and regulatory frameworks — culminating in a completed validation and a single invoice.

This is not a business model awaiting AI augmentation. It is an orchestration model currently executed by humans. The strategic imperative is to deploy agentic AI to perform the monitoring, routing, escalation, communication, and completion tasks that the Control Centre team currently handles manually — at a scale and consistency that no human team can sustain as portfolio volume grows.

The constraint is absolute: patent formalities is a zero-error-tolerance domain. Statutory deadlines are non-negotiable. A missed deadline results in the permanent, irrevocable loss of patent rights. Every agentic deployment must therefore be architected around this constraint first, and capability second.

**Governing principle:** Agents act. Humans authorize at all statutory deadline junctures and all client-facing exception communications. This boundary is non-negotiable, auditable, and enforced by system design.

---

## Section 1: Business Context — Reading IP Centrum Through an AI Lens

### What IP Centrum Actually Sells

IP Centrum sells **cognitive relief and operational certainty** to IP formalities professionals. The service removes:

- The burden of coordinating multiple national agents across 46 states
- The complexity of managing multi-language translation requirements
- The risk of deadline management across a fragmented regulatory landscape
- The administrative overhead of POA generation, billing reconciliation, and status tracking

The promise is: *you make one decision; we handle every consequence of that decision.*

This is precisely the value proposition that agentic AI is architecturally suited to deliver — and to scale without proportional headcount growth.

### The Three Operational Layers Where AI Value Concentrates

**Layer 1: Intelligence** — extracting signal from structured data flows already in the system (EP numbers, patent documents, regulatory databases, deadline schedules, agent performance data, and UPC opt-out registers).

**Layer 2: Orchestration** — routing work, managing dependencies, monitoring progress, and escalating exceptions across a network of national agents, translators, and internal teams.

**Layer 3: Communication** — keeping clients informed with the precision and proactivity that builds the trust on which IP Centrum's white-label and partner relationships depend.

### The Constraint That Governs Everything

In no other professional services context is the error consequence more severe or more binary. A 30-day software bug delays a feature. A missed EP validation deadline permanently extinguishes a patent right that may represent years of R&D investment and millions in potential licensing revenue.

Every agentic AI deployment at IP Centrum must be designed with this constraint as the **primary architectural consideration** — not as a compliance footnote.

### The UPC / Unitary Patent Dimension

The entry into force of the Unified Patent Court (UPC) and the Unitary Patent (UP) system in June 2023 introduces a structural inflection point. The UP covers 17 EU member states with a single filing and renewal, reducing the number of classical EP validations for many clients. This is not a marginal change — it alters the validation calculus, translation volume, national agent routing, and renewal cost modeling across IP Centrum's entire portfolio.

Implications for the agentic framework:

- **DocIntel** must distinguish between UP-eligible and non-UP-eligible patents, flag UP coverage applicability, and identify which states require classical validation beyond UP coverage.
- **QuoteAdvisor** must present UP vs. classical validation as a structured decision, modeling cost differentials and territorial coverage trade-offs.
- **TransOrch** must route UP translations to certified UP providers where required, while maintaining classical validation translation flows for non-UP states.
- **RenewIntel** must model UP renewal cost trajectories separately from classical national renewal portfolios.
- **AgentNet** must track UP filing confirmations through the EPO's dedicated UP channels separately from national agent networks.
- **BizSignal** must monitor UP opt-out declarations as a signal of active classical validation intent.

Failure to integrate UP-aware logic into all relevant agents will result in systematic over-quoting, incorrect routing, and regulatory obsolescence.

---

## Section 2: The 10 Agents — IP Centrum's Agentic AI Portfolio

These are purpose-designed agents, each solving a specific operational problem within IP Centrum's workflow. They are sequenced by feasibility and risk, not aspiration. Each agent includes a **cascade risk** annotation indicating which downstream agents consume its output and the indirect consequence of error.

---

### Agent 1: DocIntel — Document Intelligence Agent

**Domain:** Quote generation & case setup  
**Risk tier:** Low (advisory output, no action taken)  
**Cascade risk:** Medium. Errors in claims count, technical domain, or drawing sheet count feed into QuoteAdvisor (quote accuracy) and TransOrch (translator routing). A misclassified technical domain propagates to the wrong translator network.

**What it does:**
When a client enters an EP number, DocIntel retrieves the full patent document from the EPO's public register and performs automated analysis:

- Claims count and claims complexity scoring (driving translation workload estimates)
- Technical domain classification (chemistry, pharma, mechanical, electronics, biotech, software) for translator routing
- Drawing sheet count and description length assessment
- Applicant and proprietor data cross-reference against EPO records
- Family member identification (other pending or granted patents in the same family)
- **UPC/UP flag**: Identifies whether the patent is UP-eligible, whether a UP opt-out has been registered, and recommends UP vs. classical validation pathway based on territorial coverage requirements

**Why this matters:**
Currently, quote accuracy depends on the client correctly characterizing their patent. DocIntel removes this dependency — generating accurate quotes from the EP number alone and pre-populating order forms with verified data.

**Output:** Enhanced quote precision, reduced data quality issues, faster case setup, UP-aware routing logic.

---

### Agent 2: CaseHealth — Real-Time Case Risk Monitor

**Domain:** Case management & escalation  
**Risk tier:** Medium (triggers human escalation; does not take autonomous deadline action)  
**Cascade risk:** High. CaseHealth triggers ClientComms (client notifications) and AgentNet (backup routing). A false negative means an at-risk case receives no human review.

**What it does:**
CaseHealth runs continuously across all active cases, calculating a dynamic risk score for each case based on:

- Days remaining to statutory deadline vs. current processing stage
- National agent acknowledgment latency (has the assigned agent confirmed receipt?)
- Translation status vs. expected delivery schedule
- POA return status (has the signed POA been received and uploaded?)
- Data anomalies flagged in case registration
- UP-specific milestones (opt-out deadline proximity, UP registration status)

When a case crosses a risk threshold, CaseHealth escalates to the Control Centre team with a **specific action recommendation** — not a generic alert — and routes to the correct human authority per the Authority Gate Protocol (Section 4).

**Example escalation:**  
*"Case EP22193847 — German validation. Translation agent has not confirmed acceptance in 72 hours. Filing deadline in 18 days. Recommend: contact backup translator and notify client of potential delay. [One-click action buttons: Contact Agent | Assign Backup | Notify Client]"*

**Output:** Proactive issue surfacing before they become deadline crises. Reduction in last-minute urgent handling costs.

---

### Agent 3: RegWatch — Regulatory Intelligence Agent

**Domain:** Law Engine maintenance & compliance monitoring  
**Risk tier:** Low (intelligence output for human review)  
**Cascade risk:** Medium. Stale regulatory data in the Law Engine affects QuoteAdvisor quotes and DataVerify validation rules. A missed fee change can result in under-charging or filing rejection.

**What it does:**
RegWatch maintains the Law Engine automatically by:

- Continuously monitoring official EPO, WIPO, EPO member states, and UPC publications for regulatory changes
- Detecting fee changes, deadline rule amendments, translation requirement updates, UP territorial expansion events
- Flagging changes with assessed impact: which active cases are affected, and how
- Generating proposed Law Engine updates for Control Centre review and approval
- Maintaining a **UP watch**: monitoring UP coverage state accession, UP fee adjustments, and UPC procedural rule amendments

**Output:** Faster Law Engine updates, reduced risk of quoting on stale regulatory data, proactive client alerts on regulatory changes affecting their portfolios.

---

### Agent 4: TransOrch — Translation Orchestration Agent

**Domain:** Translation management  
**Risk tier:** Medium (routing decisions; human review before handoff)  
**Cascade risk:** High. A routing error sends a patent to an unqualified translator, directly affecting filing quality and client rights.

**What it does:**
TransOrch manages the matching of translation tasks to translators across the active network, continuously optimizing for:

- Technical domain match (pharmaceutical chemistry claims should not go to a generalist translator)
- Current capacity vs. workload across translators
- Historical quality scores by translator, language pair, and technical domain
- Urgency tier (urgent cases route to translators with confirmed availability)
- UP-specific routing: certified UP translations vs. classical national translations
- Claims consistency checking for patents with multiple national filings (terminology consistency across states)

When a translation is delivered, TransOrch runs a pre-validation check:

- Word count against expected range for the EP document
- Claims count correspondence with source document
- Formatting compliance with target state requirements
- UP formatting compliance where applicable

Flagged issues go to a human reviewer. Clean translations proceed to the next workflow stage only if DataVerify has cleared the case.

**Output:** Higher translation quality consistency, faster routing, reduction in manual coordination overhead.

---

### Agent 5: AgentNet — National Agent Network Manager

**Domain:** National agent coordination  
**Risk tier:** High (manages the final filing step; requires human authorization for any action affecting statutory deadlines)  
**Cascade risk:** High. AgentNet manages the network that executes the statutory filing. An unacknowledged filing confirmation is a silent failure mode with rights-loss consequences.

**What it does:**
AgentNet manages IP Centrum's network of national agents across 46 states, functioning as an automated account manager:

- Monitors filing acknowledgments and confirmation receipts for all active cases
- Tracks certificate and proof document returns
- Flags agents with response latency anomalies (a normally responsive agent going quiet is an operational signal)
- Manages document distribution — delivering translations and POAs to the correct national agent for each state
- Maintains agent performance scorecards (on-time filing rate, quality, responsiveness)
- **UP coordination**: Tracks UP filing confirmations through the EPO's UP-specific channels; routes classical validations only to states outside UP coverage or where opt-out applies

**Critical constraint:** AgentNet does not instruct national agents to file. That instruction goes through the established, human-reviewed process. AgentNet manages everything before and after the instruction.

**Output:** Improved agent accountability, earlier detection of filing confirmation delays, better agent performance data for network quality management.

---

### Agent 6: ClientComms — Client Communication Agent

**Domain:** Client-facing communication  
**Risk tier:** Low (draft generation; human review for non-routine communications)  
**Cascade risk:** Medium. A poorly calibrated communication erodes the trust that underpins white-label relationships. A missed exception notification damages client confidence.

**What it does:**
ClientComms generates proactive, personalized case status communications:

- Automatic status update drafts triggered by case milestone events (instruction received, translations complete, filed in state X, certificate received, UP registered)
- Intelligent calibration to client communication preferences (some clients want updates at every stage; others want exceptions only)
- Exception notifications generated and drafted for Control Centre team review before sending — **human authorization required per Authority Gate Protocol**
- Periodic portfolio summary reports for in-house IP departments with large portfolios
- UP-specific communications: UP coverage confirmation, opt-out status, cost differential summaries

For white-label and partner firm clients, ClientComms generates communications in the partner firm's name and tone — supporting the "invisible" positioning that is a core IP Centrum value proposition.

**Output:** Fewer inbound status inquiries, higher client satisfaction through proactivity, reduced Control Centre team communication overhead.

---

### Agent 7: QuoteAdvisor — Intelligent Quote Optimization Agent

**Domain:** Sales & client advisory  
**Risk tier:** Low (advisory recommendations; client retains decision authority)  
**Cascade risk:** Low-to-medium. Poor recommendations may reduce average instruction value or suggest non-optimal validation scope. However, the client retains final authority.

**What it does:**
QuoteAdvisor moves beyond quote generation to quote intelligence:

- Advises on optimal validation strategy based on patent technology area and commercially relevant markets
- Presents **UP vs. classical validation pathways**: models cost, territorial coverage, and renewal trajectory for each route
- Analyzes applicant type (individual inventor vs. large corporation signals different risk tolerance)
- Uses historical validation patterns in IP Centrum's portfolio (where does the technology actually get validated? where are validations rarely maintained through renewal?)
- Cost-benefit analysis for borderline states — presenting incremental cost vs. commercial case
- For the renewals platform, analyzes currency trends and price-break timing to recommend the optimal payment window

**Output:** Higher validation scope per instruction (commercial upside for IP Centrum), better client outcomes, differentiated advisory positioning versus pure execution competitors.

---

### Agent 8: RenewIntel — Renewals Intelligence Agent

**Domain:** Patent renewals portfolio management  
**Risk tier:** Medium (recommendations only; client retains instruction authority)  
**Cascade risk:** Medium. A poorly timed AutoRenew recommendation may cost the client marginally more; it does not risk rights loss because the client must still authorize renewal.

**What it does:**
RenewIntel is the intelligence layer for IP Centrum's Renewals platform:

- Portfolio health analysis: which patents are approaching renewal decision points
- Technology lifecycle analysis: flagging patents in technology areas with declining market relevance
- Renewal cost trajectory modeling: projecting the cumulative cost of maintaining a portfolio to term
- Competitive landscape signals: identifying patents in areas with high competitor filing activity
- **UP renewal modeling**: UP renewals follow a distinct fee trajectory and single-payment mechanism vs. classical national renewals. RenewIntel models both pathways.
- AutoRenew optimization: recommending the most cost-effective instruction timing based on price-break calendars and currency trend analysis

For in-house IP department clients managing large multi-country portfolios, RenewIntel provides analytics that previously required expensive dedicated IP management software.

**Output:** Deeper client relationships, higher retention through demonstrable strategic value, new revenue opportunity through premium advisory tier.

---

### Agent 9: DataVerify — Case Data Quality Agent

**Domain:** Case registration & data integrity  
**Risk tier:** Medium (blocks or flags cases with data issues before they enter the processing pipeline)  
**Cascade risk:** High. DataVerify is a **gateway agent**. All downstream agents (TransOrch, AgentNet, CaseHealth, ClientComms) consume its output. A missed discrepancy propagates to translation, filing, and client communication.

**What it does:**
DataVerify makes systematic and comprehensive the "unique, state-of-the-art verification processes" IP Centrum already employs:

- Cross-references every new case against EPO public register data (applicant name, address, EP number validity, grant date, filing date)
- Flags discrepancies **before** they enter the processing pipeline — not after a national agent has received incorrect documents
- Detects address format issues that would fail national filing requirements in specific states
- Identifies cases where the Druckexemplar has changed since quote generation (triggering a quote revision alert)
- Validates translation instructions against the actual text to be translated
- **UP verification**: Confirms UP eligibility, checks for existing UP registrations or opt-outs, and validates that state selections are consistent with UP coverage choices

**Gate rule:** No case may proceed to TransOrch or AgentNet until DataVerify clears it or a Control Centre manager explicitly overrides with documented justification.

**Output:** Fewer case amendments after instruction, reduced rework cost, stronger quality assurance that supports IP Centrum's premium positioning.

---

### Agent 10: BizSignal — Business Development Intelligence Agent

**Domain:** Commercial growth  
**Risk tier:** Low (intelligence output for commercial team review)  
**Cascade risk:** Low. BizSignal does not touch active case processing.

**What it does:**
BizSignal monitors the EPO's public grants database continuously to identify commercial opportunities:

- Detects EP grants to organizations that are not currently IP Centrum clients
- Prioritizes leads by grant volume, technology area, and applicant type
- Identifies patent attorney firms managing high-volume validation portfolios who do not currently use IP Centrum
- Tracks **UPC opt-out activity** — a strong signal of active EP validation decision-making
- Tracks UP registration data to identify applicants choosing broad territorial coverage (high-value renewals targets)

Additionally, BizSignal monitors UK and EU regulatory developments affecting IP formalities requirements — providing early warning of service expansion opportunities (new EPO member states, new translation requirement changes, UPC evolution, UP territorial expansion).

**Output:** Structured, intelligence-led business development pipeline rather than reactive outreach.

---

### Agent Interaction Matrix

The following matrix defines event publication and consumption relationships between agents. **Rule: DataVerify must complete with no unresolved discrepancies before TransOrch or AgentNet may act on a case.**

| Agent | Publishes Events To | Consumes Events From | Independent |
|---|---|---|---|
| DocIntel | QuoteAdvisor, TransOrch, DataVerify | — | No |
| DataVerify | All downstream agents | DocIntel, EPO register | No |
| CaseHealth | ClientComms, AgentNet | All processing agents | No |
| RegWatch | QuoteAdvisor, DataVerify | Regulatory sources | Yes |
| TransOrch | CaseHealth, ClientComms | DocIntel, DataVerify | No |
| AgentNet | CaseHealth, ClientComms | TransOrch, DataVerify | No |
| ClientComms | — | CaseHealth, AgentNet, TransOrch | No |
| QuoteAdvisor | — | DocIntel, RegWatch, RenewIntel | No |
| RenewIntel | QuoteAdvisor | EPO, portfolio DB | Yes |
| BizSignal | Commercial CRM | EPO grants DB | Yes |

---

## Section 3: The Phased Deployment Roadmap

Given IP Centrum's zero-error-tolerance constraint, the deployment sequence prioritizes low-risk intelligence agents before high-consequence orchestration agents. Each phase builds the data foundation and organizational trust required for the next.

---

### Phase 1: Intelligence Foundation (Months 1–4)

**Agents deployed:** DocIntel, CaseHealth, RegWatch, DataVerify

**Rationale:** These four agents are advisory in nature — they generate intelligence and surface issues to human decision-makers. They do not take autonomous actions that affect statutory deadlines. This makes them the correct starting point for an organization where error tolerance is zero.

**Key deliverables:**
- EPO public register API integration for real-time patent data retrieval
- CaseHealth risk scoring model built on historical case data
- Regulatory change monitoring pipeline across EPO, WIPO, UPC, and national office publications
- Data quality validation ruleset built on known filing requirement specifics for each of the 46 states, plus UP-specific validation rules
- **Baseline metrics captured** (see Section 6) before any production deployment

**Success metrics:**
- Quote data accuracy improvement (% of cases requiring no post-instruction data correction)
- Percentage of escalations surfaced by CaseHealth before vs. after reaching critical urgency threshold
- Time from regulatory change publication to Law Engine update (target: under 48 hours)
- **DataVerify gate efficacy**: % of cases flagged with discrepancies pre-pipeline vs. post-pipeline error rate

**Organizational change:** Control Centre team works with AI-generated alerts and recommendations. Training focus: calibrating trust in CaseHealth risk scores. Creating feedback loop where Control Centre corrections improve the model.

---

### Phase 2: Workflow Automation (Months 5–9)

**Agents deployed:** TransOrch, ClientComms, QuoteAdvisor

**Rationale:** With the intelligence foundation established and Control Centre trust in Phase 1 outputs demonstrated, Phase 2 automates the coordination and communication workflows — the highest-volume manual tasks that do not touch statutory deadline actions.

**Key deliverables:**
- Translator performance database built on historical quality and delivery data
- ClientComms template library covering all case milestone events, exception scenarios, and UP-specific communications
- QuoteAdvisor recommendation engine trained on IP Centrum's historical validation data, with UP vs. classical pathway modeling
- Integration between TransOrch and existing case management system
- **Cascade risk monitoring**: Log and review all cases where DocIntel → TransOrch routing produced translator mismatch or quality flag

**Success metrics:**
- Translation routing time (time from document receipt to translator assignment)
- Inbound client status inquiry volume (target: measurable reduction through proactive ClientComms)
- Average quote value per instruction (QuoteAdvisor commercial contribution)
- Translation quality error rate (pre-filing issues identified vs. post-filing corrections)
- **UP quote accuracy**: % of UP-eligible patents where UP option is correctly presented and modeled

**Organizational change:** Control Centre team transitions from manual translation coordination to exception management. Human review remains mandatory for all client-facing communications before dispatch for non-routine scenarios.

---

### Phase 3: Orchestration Layer (Months 10–18)

**Agents deployed:** AgentNet, RenewIntel

**Rationale:** By Month 10, IP Centrum has operational AI infrastructure, trained models on its own production data, and a Control Centre team that has developed calibrated trust in AI outputs. Phase 3 deploys the higher-consequence orchestration agents — with explicit human authority gates at all deadline-critical decision points.

**Key deliverables:**
- AgentNet integration with national agent communication channels and document delivery systems
- Agent performance scoring system built on Phases 1–2 data
- RenewIntel portfolio analytics module for the Renewals platform, with UP renewal modeling
- **Clear human authority gate protocol**: written specification of every action that requires human authorization before AgentNet can proceed
- **Resilience & fallback protocols**: documented circuit breakers and graceful degradation paths (see Section 4)

**Success metrics:**
- National agent acknowledgment latency (time from document dispatch to agent confirmation)
- Filing confirmation receipt time
- Renewals platform client retention (RenewIntel advisory contribution)
- AutoRenew instruction optimization savings delivered to clients (calculable as currency/timing benefit)
- **UP filing confirmation tracking**: latency and accuracy of UP registration confirmation vs. classical national confirmations

**Organizational change:** Control Centre team role evolves from process executor to exception handler and quality governor. This is a significant organizational change that requires explicit workforce development investment — retraining around exception judgment rather than routine coordination.

---

### Phase 4: Autonomous Operations & Market Intelligence (Months 19–30)

**Agents deployed:** BizSignal + multi-agent orchestration optimization across all Phase 1–3 agents

**Rationale:** With a mature multi-agent infrastructure operating in production, Phase 4 focuses on two things: commercial growth through BizSignal, and continuous improvement of the agent network through inter-agent feedback loops.

**Key deliverables:**
- BizSignal integration with EPO grants database and CRM system
- Multi-agent performance optimization: agents share learning across case types and state-specific patterns
- **White-label AI capability package**: optional offering for large IP firm clients to access RenewIntel and QuoteAdvisor analytics within their own systems via API
- **UP market tracking**: Monitor UP adoption rates, territorial expansion, and competitor service offerings to adjust IP Centrum's advisory positioning

**Strategic upside:** The white-label AI capability offering creates a new revenue stream and deepens the switching cost for large partner clients — transforming IP Centrum from a service provider into an embedded technology partner.

---

## Section 4: The Governance Model — Non-Negotiable Controls

Given the UK regulatory environment (UK GDPR, professional indemnity standards) and the IP domain's error consequences, the governance framework is foundational — not optional.

---

### The Human Authority Gate Principle

Define explicitly, in writing, before any agent goes into production: which actions require human authorization, and which can the agent execute autonomously.

For IP Centrum, the mandatory human authority gates are:

| Action | Human Authorization Required | Default if Unacknowledged |
|---|---|---|
| Instructing a national agent to file | Yes — always | Case held; escalate to Control Centre Manager |
| Sending a client an exception or deadline-risk notification | Yes — for non-templated communications | Templated alerts may auto-send per approved library; non-templated held for review |
| Updating the Law Engine fee or deadline data | Yes — for all updates affecting active cases | Proposed update held in staging; current data remains active |
| Abandoning or not renewing a patent | Yes — always | Renewal reminder continues; no negative action taken |
| Issuing a revised quote | Yes — where material difference from original | Quote held; client receives "under review" status |
| Routing a translation to a new translator | Advisory recommendation; human confirmation | Default to highest-confidence match; log for review |
| Marking a case as complete | Yes — until confidence threshold is validated | Case remains "pending confirmation" |
| Filing a Unitary Patent request | Yes — always | UP pathway held; classical validation prepared as fallback |
| Updating client portfolio data in CRM | Yes — if derived from AI inference | Verified data may auto-update; inferred data requires review |

---

### Human Authority Gate Protocol — Escalation Routing & SLA

In a multi-agent system where CaseHealth, AgentNet, and TransOrch may escalate simultaneously, explicit routing logic prevents alert fatigue and missed signals.

| Alert Type | Route To | Acknowledgment SLA | Default if Unacknowledged |
|---|---|---|---|
| CaseHealth: Translator non-acceptance | Control Centre Team Lead | 4 hours | Escalate to Manager + draft client delay notification |
| CaseHealth: Deadline < 14 days with open task | Control Centre Manager | 2 hours | Emergency protocol: assign backup agent + notify client |
| AgentNet: Filing confirmation overdue | Agent Relations Manager | 8 hours | Flag agent for network review + client alert drafted |
| DataVerify: Material discrepancy | Control Centre Team Lead | 1 hour | Case held in quarantine; do not proceed to TransOrch |
| ClientComms: Exception draft ready | Control Centre Team Lead | 4 hours | Auto-send if templated; hold if non-routine |
| RegWatch: Regulatory change affecting active cases | Law Engine Manager | 24 hours | Proposed update staged; no active case data changed |
| RenewIntel: AutoRenew recommendation ready | Client Account Manager | 48 hours | Client receives advisory summary; no action taken without consent |
| TransOrch: Translation quality flag | Translation QA Lead | 4 hours | Translation held; case status updated to "QA review" |
| DocIntel: EP register data conflict with client input | Control Centre Team Lead | 2 hours | Case held; client notified of data mismatch |

---

### Override Classification & Feedback Loop Requirement

Every human correction of an AI recommendation must be captured and fed back into the model. Override data is training data. Without this loop, models decay as operational conditions change.

When a Control Centre staff member overrides an agent recommendation, they must classify the override into one of three categories:

1. **Model Error** — The agent's data or reasoning was factually incorrect.  
   *Action:* Triggers a model improvement ticket. Automatically logged for batch retraining review.

2. **Policy Override** — The agent's recommendation was valid, but a human decision (client relationship, special arrangement, precedent, or exceptional circumstance) dictated a different action.  
   *Action:* Logged for audit trail. Does not trigger model retraining. Used to calibrate "human preference" boundaries.

3. **Incomplete Information** — The agent lacked data the human possessed at decision time.  
   *Action:* Triggers data integration improvement. Surfaces missing data source or field for pipeline enhancement.

**AI Quality Owner:** Designate a named AI Quality Owner within the Control Centre team whose responsibilities include: reviewing override patterns weekly, identifying systematic AI errors, commissioning model updates, and reporting monthly override taxonomy distributions to the governance board.

---

### Data & Privacy Controls

IP Centrum handles highly sensitive commercial data: patent applications, applicant identities, prosecution histories, and strategic IP portfolios of some of the world's largest corporations.

- Agent access to client data must be strictly scoped to the minimum required for the task (principle of least privilege)
- No client portfolio data may be used to train shared models without explicit contractual consent
- All agentic decision logs must be retained for a minimum of 7 years (professional indemnity standard)
- UK GDPR data subject rights must be implementable across all AI-processed client records
- Any AI system processing personal data of EU clients requires GDPR Article 22 compliance for automated decision-making
- **UP data handling**: UP registration data may include personal data of inventors and applicants; process under same GDPR constraints as classical validation data

---

### Resilience & Fallback Protocols

Agents must not fail closed in ways that silently halt case progress.

**Graceful Degradation**
- If DocIntel cannot reach EPO OPS, the system falls back to client-provided data with a clear "unverified" flag and triggers a manual verification task.
- If RegWatch cannot access a national patent office publication, it flags the source as stale and alerts the Law Engine Manager — it does not suppress the alert.
- If DataVerify detects an API mismatch between EPO data and internal records, the case enters quarantine; it does not proceed on the assumption that the internal record is correct.

**Circuit Breakers**
- If TransOrch's quality assessment model fails or returns confidence below threshold, translations route to human review rather than failing closed.
- If CaseHealth risk scoring produces an anomalous result (e.g., a case jumps from low-risk to critical in minutes without an identifiable event), the alert is tagged "anomaly — manual verification required" and routed to the AI Quality Owner.
- If AgentNet cannot retrieve an acknowledgment from a national agent after repeated attempts, the case is escalated to the Agent Relations Manager and a backup agent is suggested — the case does not wait indefinitely.

**Agent Interlocks**
- AgentNet cannot route filing instructions if DataVerify has flagged unresolved data discrepancies in the same case.
- TransOrch cannot mark a translation as complete if DataVerify has not cleared the source document.
- ClientComms cannot send a "case complete" notification if CaseHealth has an unresolved high-risk flag on the same case.
- **UP interlock**: AgentNet cannot file a UP request and classical validations for the same patent simultaneously without human authorization, to prevent double-filing and double-billing.

---

## Section 5: Technology Stack Recommendations

IP Centrum is a UK-based SME with existing proprietary technology infrastructure. The stack recommendations reflect this reality — AI is additive, not replacement.

---

### Core Architecture Principles

**Principle 1: API-first integration**
Agents connect to existing systems via IP Centrum's existing API infrastructure. Build the agent layer on top of existing data, not alongside it.

**Principle 2: RAG over fine-tuning for most cases**
IP Centrum's operational knowledge — regulatory rules, agent performance data, client history, UPC procedural rules — is better delivered to AI systems through retrieval-augmented generation than through fine-tuning. RAG keeps knowledge current; fine-tuned models are static.

**Principle 3: Domain-specific models where it matters**
For patent document analysis and translation quality assessment, domain-specific models (fine-tuned on patent corpus data) will significantly outperform general-purpose models. Prioritize this investment for DocIntel and TransOrch.

**Principle 4: Human-readable audit trails**
Every agent decision must produce a human-readable log entry explaining the action taken, the data it was based on, and the confidence level. This is a legal requirement in UK professional services context, not a technical nicety.

**Principle 5: Event-driven, stateful orchestration**
Agents must operate as a coordinated network, not as isolated scripts. An event bus ensures that the right agent activates at the right time, with the correct dependency sequencing.

---

### Integration Architecture

**Event-Driven Agent Activation**
All agents subscribe to a lightweight event bus (or case management system webhooks) rather than polling:

- `case.created` → triggers DataVerify, DocIntel
- `data.verified` → triggers QuoteAdvisor, TransOrch
- `translation.delivered` → triggers TransOrch validation, CaseHealth recalculation
- `agent.filed` → triggers AgentNet confirmation monitoring, ClientComms milestone
- `regulatory.change.detected` → triggers RegWatch staging, Control Centre alert
- `up.optout.registered` → triggers re-evaluation of classical validation necessity

**Source-of-Truth Hierarchy**
1. **EPO public register** is the authoritative source for patent document metadata.
2. **UPC Registry** is the authoritative source for Unitary Patent status, opt-outs, and territorial coverage.
3. **IP Centrum case management system** is the authoritative source for case status, agent assignments, and client instructions.
4. **Agent-derived data** is authoritative *only within its own reasoning chain* and must be stamped with provenance before writing to the case management system.
5. **Human override** supersedes all automated sources and is logged as the final authority.

**Conflict Resolution**
If DataVerify flags a discrepancy between client-provided data and EPO register data, the protocol is: flag to Control Centre, hold case in quarantine, do not auto-correct the source system. The human authority gate resolves the conflict.

---

### Recommended Infrastructure

**Agent orchestration framework:** LangGraph or similar stateful agent framework — supports the multi-agent coordination, event-driven activation, and dependency sequencing required by Phase 3 deployments.

**Foundation model:** Anthropic Claude API (claude-sonnet-4 for production; claude-opus-4 for complex reasoning tasks like QuoteAdvisor and RenewIntel analysis). The context window capability is particularly valuable for processing full patent documents and multi-jurisdictional regulatory texts.

**Vector database:** Pinecone or Weaviate for the regulatory knowledge base powering RegWatch, DocIntel retrieval, and UPC procedural rules.

**Patent document retrieval:** EPO's OPS (Open Patent Services) API for EP grants and publications; UPC Registry API (or automated monitoring) for UP status and opt-out data.

**Monitoring & observability:** LangSmith or equivalent — full trace logging of agent reasoning chains is non-negotiable in IP Centrum's error-sensitive context. Every agent decision must be traceable to its data inputs, reasoning steps, and confidence score.

---

## Section 6: The ROI Framework

Present this to the IP Centrum board in four value pools — not just cost reduction. **All metrics require pre-deployment baselines captured in the First 90 Days data audit.**

---

### Value Pool 1: Operational Efficiency (Quantifiable)

- Control Centre team hours redirected from routine coordination to exception handling
- Reduction in post-instruction data correction (rework cost)
- Reduction in urgent/rush handling premiums through earlier issue detection
- Translation routing time compression (each hour saved is margin improvement)
- **UP efficiency gain**: Reduction in manual UP eligibility checks and dual-pathway quote preparation

**Baseline required:** Current Control Centre hours per case type; current post-instruction amendment rate; current rush handling frequency and premium cost; current translation assignment time.

---

### Value Pool 2: Revenue Growth (Semi-quantifiable)

- QuoteAdvisor contribution to average instruction value (measure: average states per validation before vs. after deployment)
- UP advisory contribution: % of UP-eligible clients selecting UP pathway through QuoteAdvisor modeling
- BizSignal-attributed new client revenue
- White-label AI capability tier: new premium pricing for large partner firms

**Baseline required:** Average states per validation (trailing 12 months); current UP uptake rate among eligible clients; current partner firm pricing tiers.

---

### Value Pool 3: Risk Reduction (Risk-adjusted value)

- Reduction in near-miss deadline events (each near-miss has a cost; each actual miss has a potentially catastrophic liability cost)
- Regulatory change response time improvement (reduced risk of quoting on stale Law Engine data)
- Data quality improvement (fewer cases requiring amendment after instruction)
- **UP compliance risk reduction**: Accurate UP vs. classical routing prevents double-filing, unnecessary translation costs, and territorial coverage gaps

**Baseline required:** Near-miss event frequency (trailing 24 months); regulatory update lag time (current average days from publication to Law Engine update); current data amendment rate.

---

### Value Pool 4: Competitive Moat (Strategic)

- IP Centrum's technology advantage becomes significantly stronger with an AI orchestration layer competitors cannot replicate quickly
- Switching cost deepening for large partner clients through embedded AI advisory tools
- Capacity to scale volume without proportional headcount growth — a structural unit economics improvement
- **UP-first advisory positioning**: Early mover advantage in AI-assisted UP vs. classical validation advisory

---

## Section 7: The First 90 Days — Where to Start

---

### Days 1–30: Data Audit and Infrastructure Baseline

Before building any agent, complete a structured audit. **Do not skip this step.** Agents built on poor data infrastructure fail in production.

**Data Audit Checklist:**

- [ ] **EPO OPS API**: Verify rate limits, coverage of historical grants (not just recent), and reliability (uptime %). Test retrieval for a representative sample of EP numbers spanning all technology domains.
- [ ] **UPC Registry / UP data sources**: Identify available APIs or data feeds for UP registration status, opt-out records, and territorial coverage. Assess completeness and latency.
- [ ] **Case Management System**: Document all tables/collections accessed by agents; identify fields that are human-editable vs. system-generated; assess API event capabilities (webhooks vs. polling).
- [ ] **Translator Database**: Assess completeness of historical quality scores, domain expertise tags, and delivery time data. If <80% completeness, DataVerify and TransOrch accuracy will be materially degraded — flag as Phase 1 dependency.
- [ ] **National Agent Database**: Confirm agent contact protocols (API? Email? Portal?) and response format consistency. Document acknowledgment receipt patterns.
- [ ] **Deadline/Fee Tables**: Identify last manual update date; measure drift between published national office fees and IP Centrum's Law Engine. If >5% divergence, RegWatch priority increases.
- [ ] **Client Communication Archive**: Assess availability of structured client preference data (frequency, tone, white-label parameters). ClientComms accuracy depends on this.
- [ ] **Historical Case Outcome Data**: Extract trailing 24 months of case outcomes, exception events, near-misses, and resolution times to train CaseHealth risk models.

**Baseline Metrics Capture (record before any AI deployment):**

| Metric | Current Value | Measurement Method |
|---|---|---|
| % of quotes revised post-instruction | | Trailing 12 months case review |
| Average translation assignment time | | Trailing 12 months dispatcher logs |
| Post-instruction data amendment rate | | Trailing 12 months amendment tickets |
| Near-miss deadline event frequency | | Trailing 24 months incident log |
| Average regulatory update lag | | Trailing 12 months Law Engine update log |
| Inbound client status inquiry volume | | Trailing 3 months support ticket classification |
| Average states per validation instruction | | Trailing 12 months order data |
| UP uptake rate among eligible clients | | Trailing 12 months UP vs. classical orders |

---

### Days 31–60: Build and Deploy DocIntel

DocIntel is the correct first agent because:

- It uses a publicly available API (EPO OPS) — minimal internal data integration required
- Its output is advisory — it improves quotes, it does not affect filings
- It generates immediate, measurable commercial value (better quotes) that demonstrates AI ROI to stakeholders
- It begins accumulating the patent document processing capability that underpins TransOrch and DataVerify in later phases
- UP eligibility flagging builds organizational competence in UP data handling before high-consequence agents touch UP pathways

**Deliverables:**
- DocIntel prototype retrieving and analyzing 100 representative EP patents
- Comparison against human-generated quotes: accuracy of claims count, drawing sheets, technical domain classification
- UP eligibility detection accuracy vs. manual UPC register checks
- Integration with quote generation UI: pre-populated fields, confidence scores, human override capture

---

### Days 61–90: Deploy CaseHealth in Monitoring Mode

Run CaseHealth alongside human monitoring — not replacing it. For the first 30 days, compare CaseHealth's risk flags with issues identified by the Control Centre team.

**Calibration Phase Protocol:**
- CaseHealth generates risk scores and alerts for all active cases.
- Control Centre team continues normal monitoring.
- At the end of each week, compare: Which cases did CaseHealth flag that humans missed? Which cases did humans flag that CaseHealth missed? What was the override classification (Model Error, Policy Override, Incomplete Information)?
- AI Quality Owner reviews weekly comparison and adjusts thresholds.

**At Day 90, you will have:**
- One production agent (DocIntel) delivering measurable commercial value
- A second agent (CaseHealth) in validated monitoring mode, with initial trust calibration data
- A completed data audit with identified integration gaps and a remediation plan
- A documented governance framework (Authority Gate Protocol, override taxonomy, escalation SLAs) tested against real case scenarios
- A Control Centre team that has begun the cultural shift from process executors to AI-augmented decision-makers
- Baseline metrics recorded for all Phase 1 and Phase 2 ROI measures

---

## Conclusion: The Strategic Alignment

IP Centrum's business is built on a promise: one instruction, everything handled.

Agentic AI does not change that promise. It makes it more reliable, more scalable, more valuable, and more defensible — across both the classical EP validation network of 46 states and the evolving Unitary Patent landscape.

The organizations that use IP Centrum — the IP firms, the in-house departments, the portfolio managers — chose IP Centrum because they trust it to handle complexity they do not want to manage. That trust is IP Centrum's most valuable asset.

Every agentic AI deployment described in this framework is designed to deepen that trust: by catching issues earlier, communicating more proactively, advising more intelligently, and handling more consistently — while keeping the human authority gates in place that the zero-error-tolerance nature of this domain demands.

Done right, the agentic AI program does not change what IP Centrum is. It makes IP Centrum better at being exactly what it already is — and ready for the UP-era market that is already here.

---

*Framework prepared for internal strategic use. All agent concepts, phasing, governance recommendations, and UPC integration assumptions are subject to technical feasibility assessment and legal review prior to implementation.*
