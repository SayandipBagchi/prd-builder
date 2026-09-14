# Worked Example: a filled PRD

A short PRD, filled from two source tickets and a support export. It is here to show the discipline, not the domain: what a traced fact looks like, what an honest gap looks like, and what a recorded departure from source looks like.

Read the annotations at the bottom. They are the part that matters.

---

## Overview

| Field | Details |
| --- | --- |
| Feature | Retry a failed autopay collection before marking the cycle missed |
| Programme / Tenant | Example Card |
| Customer / Segment | Cardholders on autopay |
| Market(s) | UK |
| Author (PM) | A. Kumar |
| Status | Draft |
| Review verdict | Not reviewed |
| Feature Type | Platform capability |
| Priority / Driver | Revenue impact |
| Reviewers | Payments eng lead, Collections ops, Compliance |
| Source artefacts | IDEA-412, REQ-518, support export 2026-04 to 2026-06 |

## Feature Brief

| Field | Details |
| --- | --- |
| Problem | An autopay collection that fails for a transient reason is never retried, so the cycle is marked missed and the customer takes a fee and an arrears marker. |
| Proposed Solution | Retry a failed collection on a defined schedule within the cycle, for transient failure reasons only, before the missed-payment path runs. |
| Customer / Business Impact | 2,140 collections failed in the quarter. 61 percent carried a transient reason code. Those customers paid a fee and entered arrears reporting for a bank-side condition that cleared within days. |
| Why Now | Complaint volume on this reason doubled quarter on quarter, and the arrears marker is the part customers escalate. |

## Problem Statement

### Problem Definition

- Exact customer problem: a customer on autopay with funds available a day later is treated identically to a customer who never paid.
- Workflow location: collection attempt on the scheduled autopay date, inside the repayments journey.

### Impacted Users / Systems

| Field | Details |
| --- | --- |
| Personas | Cardholder on autopay; collections operations agent |
| Systems / Modules | Mandate service, collections scheduler, fee engine, credit bureau reporting feed |

### Problem Severity

| Field | Details |
| --- | --- |
| Frequency | 2,140 failed collections in the quarter, 1,305 with a transient reason code |
| Impact | Fee charged, arrears marker raised, complaint rate on this reason doubled quarter on quarter |

### Evidence

| Field | Details |
| --- | --- |
| Qualitative evidence | 38 support tickets citing "money was there the next day", support export, April to June 2026 |
| Quantitative evidence | 1,305 of 2,140 failures carried a transient reason code, same export |
| Source and date of each | Support export pulled 2026-07-02; failure reason split from the same export |

### Behaviour Summary

- Current state: one collection attempt per cycle. A failure of any kind marks the cycle missed, charges the fee and feeds the arrears path.
- Desired state: a failure carrying a transient reason code is retried on a schedule within the cycle. The missed path runs only after the retries are exhausted.

## Current vs Desired Behaviour

| Workflow Step / Scenario | Current Behaviour | Desired Behaviour | Notes |
| --- | --- | --- | --- |
| Collection fails, insufficient funds | Cycle marked missed same day, fee charged, arrears marker raised | Retry at +2 and +5 days within the cycle. Missed path runs only if both fail | Reason code is classed transient |
| Collection fails, mandate cancelled at bank | Cycle marked missed, fee charged | Unchanged. No retry | Reason code is classed permanent |
| Retry succeeds | Not possible today | Cycle settles normally. No fee, no arrears marker | |
| Retries exhausted | Not applicable | Missed path runs as it does today, dated to the original due date | Open question on the fee date |

## Goals and Success Metrics

### Product / Business Metrics

| Metric | Baseline | Target | Timeframe | Instrumented? |
| --- | --- | --- | --- | --- |
| Cycles marked missed on a transient reason | 1,305 per quarter | Under 500 per quarter | One quarter after launch | Yes, collections event stream |
| Complaints citing a cleared transient failure | 38 per quarter | Under 15 per quarter | One quarter after launch | No. Complaint reason coding needs a new value |

### Guardrail Metrics

| Metric | Acceptable Range | Risk if Breached |
| --- | --- | --- |
| Collection attempts per cycle per customer | At most 3 | Bank-side rate limiting, customer perceives repeated debits |
| Time from due date to settled | No worse than +5 days | Cash flow and reconciliation impact |

## Dependencies and Impact

| Field | Details |
| --- | --- |
| Affected teams / downstream consumers | Payments engineering, collections operations, bureau reporting |
| Internal modules | Mandate service, collections scheduler, fee engine |
| Capability type | Reusable capability |
| Can this be generalised later? | Yes, the retry policy is per programme configuration |
| Duplication risk | Collections ops runs a manual re-attempt process. This replaces it, and that needs saying to them before launch |

### Vendor and Third Party

| Vendor / Partner | What it provides | Contract or capability gap | Lead time | Owner |
| --- | --- | --- | --- | --- |
| Payment rail provider | Collection submission and reason codes | Unknown whether the contract caps re-presentation attempts per mandate per cycle | Unknown | Payments eng lead |

### Regulatory and Compliance

| Field | Details |
| --- | --- |
| Regime(s) in scope | UK consumer credit reporting |
| Specific obligation touched | Accuracy of arrears reporting. A marker raised for a failure that later settled inside the cycle is arguably inaccurate |
| Evidence or audit artefact required | Unknown. Compliance to confirm what the retry history has to show |
| Approver | Compliance, named reviewer not yet assigned |
| Consent or permission change | None. The existing mandate authorises collection within the cycle |

## Solution Design and Requirements

### Lifecycle

1. Collection submitted on the scheduled date.
2. Failure returns with a reason code.
3. Reason code is classified transient or permanent from a configured map.
4. Permanent: existing missed-payment path runs unchanged.
5. Transient: retry scheduled at +2 days, then +5 days, both inside the cycle.
6. Any retry succeeding settles the cycle with no fee and no arrears marker.
7. Both retries failing runs the missed-payment path, dated to the original due date.

### Proposed Solution

- What it is: a retry policy on the collections scheduler, driven by a per-programme configurable reason-code map and schedule.
- Existing system fitment / constraints: the scheduler already supports a single dated attempt per cycle. Multiple attempts per cycle is new. The fee engine currently fires on first failure and would move to firing on path exhaustion.
- API / synchronous integration changes: none expected.
- Event-driven integration changes: collection attempt events gain an attempt number and a retry-of reference. Bureau reporting consumes cycle outcome rather than first-attempt outcome.
- Data / batch / data lake changes: attempt-level history retained per cycle. Reconciliation needs the cycle outcome, not the attempt count.
- Dependent module changes: fee engine trigger point moves.
- UI / UX changes: the app shows a retry scheduled state. Copy not drafted.

### Functional Requirements

| ID | Requirement | Source | Priority |
| --- | --- | --- | --- |
| FR-1 | Classify every collection failure as transient or permanent from a per-programme reason-code map | REQ-518 | Must |
| FR-2 | Schedule at most two retries per cycle, at +2 and +5 days from the original due date, for transient failures only | REQ-518 | Must |
| FR-3 | Suppress the fee and the arrears marker until the retry path is exhausted | IDEA-412 | Must |
| FR-4 | Never submit a retry outside the cycle window | REQ-518 | Must |
| FR-5 | Retain attempt-level history against the cycle, including reason code and attempt number | Compliance discussion, undated | Must |
| FR-6 | Expose the reason-code map and retry schedule as per-programme configuration | Derived from the generalisation decision, logged below | Should |

### Acceptance Criteria

```
AC-1  (FR-2)
Scenario: transient failure retried and settled
Given an autopay collection fails on the due date with a reason code mapped as transient
When the +2 day retry is submitted and succeeds
Then the cycle is settled, no fee is charged, and no arrears marker is raised
```

```
AC-2  (FR-3)
Scenario: retries exhausted
Given an autopay collection fails with a transient reason and both retries also fail
When the second retry returns
Then the missed-payment path runs, dated to the original due date
```

```
AC-3  (FR-1)
Scenario: permanent failure not retried
Given an autopay collection fails with a reason code mapped as permanent
When the failure is processed
Then no retry is scheduled and the existing missed-payment path runs unchanged
```

```
AC-4  (FR-4)
Scenario: retry would fall outside the cycle
Given a transient failure occurs with fewer than 2 days remaining in the cycle
When retries are scheduled
Then no retry is submitted outside the cycle window, and the missed-payment path runs
```

## Non-Functional Requirements

| Requirement Area | Details | Threshold |
| --- | --- | --- |
| Availability | Retry scheduling inherits the collections scheduler SLA | Unknown, ask payments eng |
| Scalability | Up to 3 attempts per cycle per mandate across the autopay base | Peak cycle volume unknown |
| Performance | Retry submitted within the scheduled day | Same day |
| Logging / Observability | Attempt number, reason code and retry-of reference on every collection event | All attempts |
| Security / Audit | No new data classes. Attempt history is auditable | |
| PII handling | Unchanged. No new personal data captured | |
| Data retention and deletion | Attempt history follows existing collections retention | Unknown period, ask compliance |
| Accessibility | Retry scheduled state in the app meets the existing app standard | |
| Localisation / Multi-tenant behaviour | Reason-code map and schedule configurable per programme | |

## Assumptions and Out of Scope

| Field | Details |
| --- | --- |
| Assumptions | The rail returns a reason code on every failure. The cycle window is long enough for a +5 day retry in the common case |
| Out of scope for this release | Customer-initiated retry from the app. Partial collection. Changing the autopay date |
| Deferred, with expected release | Customer notification copy for the retry scheduled state, deferred to the comms workstream, release unknown |

## Open Questions

| Question | Owner | Decision Needed By | Blocks |
| --- | --- | --- | --- |
| Does the rail contract cap re-presentation attempts per mandate per cycle? | Payments eng lead | Before build starts | FR-2 |
| Which reason codes are classed transient at launch? | Payments eng lead | Before build starts | FR-1 |
| If retries are exhausted, is the fee dated to the original due date or the last attempt? | Collections ops | Before build starts | FR-3 |
| What retry evidence does bureau reporting have to show? | Compliance, reviewer unassigned | Before launch | FR-5 |
| What is the collections attempt-history retention period? | Compliance, reviewer unassigned | Before launch | NFR retention |

## Rollout Strategy (documented by engineering)

| Field | Details |
| --- | --- |
| Migration plan | Not yet documented |
| Breaking changes | Bureau reporting consumes cycle outcome rather than first-attempt outcome. Downstream consumers to confirm |
| Forward / backward compatibility | Not yet documented |
| Versioning strategy | Not yet documented |
| Deprecation plan | Manual collections re-attempt process retires at launch. Ops to confirm |
| Rollback plan | Not yet documented |
| Feature flags | Per-programme flag expected, given the configuration model |
| Other rollout constraints | Not yet documented |

## Decision Log

| Date | Decision | Rationale | Alternatives Considered | Departs from source? |
| --- | --- | --- | --- | --- |
| 2026-07-04 | Two retries at +2 and +5 days | Matches the observed window in which transient failures cleared in the support export | Single retry at +3; daily retry to cycle end | No |
| 2026-07-04 | Reason-code map is configuration, not code | The same retry policy is wanted on other programmes with different rails | Hardcode the UK rail's codes | Yes. REQ-518 scopes this to one programme. Generalising is a deliberate expansion, recorded here |
| 2026-07-04 | Customer notification deferred | Comms workstream owns app copy and has its own release train | Block this release on copy | Yes. IDEA-412 asks for customer notification. Narrowed deliberately, recorded in Deferred |

---

## What to notice

**Every number traces.** 2,140 and 1,305 carry a source and a pull date. Nothing carries a number that no source supplied.

**Unknowns are visible and owned.** Five open questions, each with an owner and a deadline, and each naming what it blocks. The availability and retention thresholds say `unknown, ask X` rather than a plausible figure.

**Two departures from source are recorded as decisions.** One expands scope, one narrows it. Both name the source they depart from. Unrecorded, either one would fail the source-drift check on its own.

**The metric with no instrumentation says so.** Complaint reason coding does not exist yet, which makes it delivery work rather than a measurement plan.

**Rollout is mostly blank, and that is honest.** The sections are present and marked not yet documented, with the owner implied by the section title. A blank section that is present gets filled. A deleted section does not.

**Acceptance criteria cover the unhappy paths.** Permanent failure, exhausted retries and the cycle-boundary case each have a block. A PRD with only AC-1 would pass a skim and fail the review.
