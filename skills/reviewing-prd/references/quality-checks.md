# Definition-of-Ready Checks

Eleven checks. Four are fatal: any one of them failing makes the verdict `not ready`, however good the rest of the document is.

Score each as `pass`, `fail` or `not run`. A check you could not run because something was missing is `not run`, never `pass`.

## Baseline

- The requirements baseline artefact carries the requirements. The tenant profile names which one it is.
- The idea artefact carries the problem, the rationale and the constraints.
- Review the PRD against both.
- Any omission, narrowing, expansion or contradiction has to be recorded in the PRD as a decision, assumption, out-of-scope choice, or open question with rationale. Recorded, it passes. Unrecorded, it fails.

## Fatal checks

### Check 1: Source alignment (FATAL)

- **Fails when:** the PRD omits, narrows, expands or contradicts the problem, user need, rationale, constraints or requirements direction of its sources, without recording it.
- **Consequence:** a reviewer cannot tell whether scope changed on purpose or context was dropped.
- **Sections:** Feature Brief, Problem Statement, Goals and Success Metrics, Dependencies and Impact, Solution Design and Requirements, Assumptions and Out of Scope, Open Questions, Decision Log
- **Passes when:** the core problem and user need survive from the idea artefact, the relevant rationale and constraints survive, the requirements direction matches the baseline artefact, and every deliberate deviation is written down with its reason.
- **Not run when:** no source artefacts were supplied.

### Check 5: Success metrics (FATAL)

- **Fails when:** there is no primary success metric, or a metric has no baseline, no target, or no timeframe.
- **Consequence:** nobody can say afterwards whether the feature worked or whether the trade-offs were worth it.
- **Sections:** Feature Brief, Goals and Success Metrics
- **Passes when:** at least one primary metric carries a baseline, a target and a timeframe, and guardrails exist wherever regression is a real risk. A metric that is not instrumented yet passes only if the PRD says so, because that is delivery work rather than a measurement gap.

### Check 7: Behaviour is observable (FATAL)

- **Fails when:** current or desired behaviour is described in abstractions such as "improve the experience", "make it seamless", "streamline the flow", with no workflow step that visibly changes.
- **Consequence:** design, engineering and QA leave with three different pictures of what ships.
- **Sections:** Problem Statement, Behaviour Summary; Current vs Desired Behaviour; Acceptance Criteria
- **Passes when:** current behaviour is concrete enough to go and look at, the desired flow is described step by step, and the desired state is observable enough to test.

### Check 9: Requirements are testable (FATAL)

- **Fails when:** functional requirements or acceptance criteria use verbs such as "support", "optimise", "handle better", "improve", without conditions or expected results.
- **Consequence:** engineering, QA and stakeholders each decide separately what done means.
- **Sections:** Functional Requirements, Acceptance Criteria, Non-Functional Requirements
- **Passes when:** each requirement states inputs, conditions and expected output, non-functional expectations carry measurable thresholds where a threshold is possible, and acceptance criteria cover the unhappy paths rather than only the happy one.

## Non-fatal checks

### Check 2: Written with people, not at them

- **Fails when:** the PRD was shared only once it already looked finished, no reviewers are named, and no unresolved trade-off appears anywhere.
- **Consequence:** low buy-in, and rationale gets relitigated late.
- **Sections:** Overview, Dependencies and Impact, Solution Design and Requirements, Open Questions, Decision Log
- **Passes when:** reviewers are named, design and engineering were involved while drafting, and unresolved trade-offs sit in Open Questions or the Decision Log rather than in someone's memory.

### Check 3: Evidence behind the problem

- **Fails when:** the problem is asserted as belief or intuition, or the document jumps to solution framing before showing the pain, with no customer signal, support signal or usage data.
- **Consequence:** the team argues about whether the problem is real instead of how to solve it.
- **Sections:** Feature Brief, Problem Statement, Problem Severity, Evidence
- **Passes when:** qualitative evidence such as customer asks, sales input or support feedback, and quantitative evidence such as usage, failure rate, latency, ticket volume or operational cost, are present where available and dated, and the current pain is stated separately from the proposed solution.

### Check 4: Solution is not over-prescriptive

- **Fails when:** the PRD locks UI detail, API shapes or implementation choices before they are requirements.
- **Consequence:** the PRD becomes a rigid handoff spec and the cheaper options never get raised.
- **Sections:** Proposed Solution and its integration subsections, Functional Requirements, Acceptance Criteria
- **Passes when:** the PRD stays at outcome and contract level. APIs described by consumers, inputs, outputs, errors, compatibility and SLAs. Events by producers, consumers, triggers, payload expectations, delivery guarantees, ordering, retries, idempotency and failure handling. Data and batch by source systems, data contracts, freshness, backfills, reconciliation and downstream consumers. UI by reference to mocks, unless a pixel is genuinely a requirement.

### Check 6: Out of scope is written down

- **Fails when:** the PRD says what will be built and not what will not.
- **Consequence:** scope creep, and stakeholders expecting things nobody planned.
- **Sections:** Assumptions and Out of Scope, Open Questions
- **Passes when:** the assumptions the draft depends on, what is not being built now, what is deferred, and what is still undecided are all stated, so the release boundary is legible.

### Check 8: Fits the system that exists

- **Fails when:** the PRD proposes a clean solution without checking current behaviour, affected dependencies or existing constraints.
- **Consequence:** the solution turns out infeasible, or the estimate misses hidden rework.
- **Sections:** Behaviour Summary, Dependencies and Impact, Vendor and Third Party, Regulatory and Compliance, Solution Design and Requirements, Rollout Strategy
- **Passes when:** relevant current behaviour, upstream and downstream dependencies, architectural limits, data model constraints, integration limits, vendor capability and lead time, operational and compliance impact, and compatibility expectations are captured from real artefacts rather than assumed.

### Check 10: Rollout is thought about now

- **Fails when:** migration, compatibility, rollback or feature-flag decisions are blank because they are assumed to be engineering's problem for later.
- **Consequence:** launch risk, and delivery work that only appears once implementation is underway.
- **Sections:** Rollout Strategy, Dependencies and Impact
- **Passes when:** migration, feature flags, breaking changes, versioning, compatibility and rollback are captured early enough to expose the work. Sections present and marked not yet documented pass if the PRD names who documents them. Deleted sections fail.

### Check 11: Decisions and questions live in the document

- **Fails when:** material trade-offs were settled in meetings or chat and the PRD records neither the decisions nor the open items.
- **Consequence:** the same debates repeat, and teams work from different stale assumptions.
- **Sections:** Open Questions, Decision Log
- **Passes when:** unresolved questions carry owners and decision dates, and material decisions carry rationale and the alternatives that were considered.

## Scoring

| Outcome | Condition |
| --- | --- |
| `not ready` | Any of checks 1, 5, 7, 9 fails |
| `ready with conditions` | No fatal failure, and one or more of checks 2, 3, 4, 6, 8, 10, 11 fails |
| `ready` | All eleven pass, or the only failures are already recorded in the PRD as open questions with owners and dates |

A `not run` on check 1 does not by itself force `not ready`, but the verdict has to say the alignment check could not run and why. Treat that PRD as unverified against its sources when anything downstream reads the verdict.
