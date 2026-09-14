# PRD Template

Use this structure for definition-of-ready PRDs.

Be specific and data-driven. Keep it concise but complete. Every section appears: filled, marked `N/A` with a reason, or carried as an open question.

## Overview

| Field | Details |
| --- | --- |
| Feature |  |
| Programme / Tenant |  |
| Customer / Segment |  |
| Market(s) |  |
| Author (PM) |  |
| Status | Draft / Review / Approved / Shipped |
| Review verdict | Not reviewed / Ready / Ready with conditions / Not ready |
| Feature Type | Platform capability / Customer-specific customisation |
| Priority / Driver | Strategic roadmap / Regulatory / Revenue impact / Pre-sales |
| Reviewers |  |
| Source artefacts |  |

## Feature Brief

| Field | Details |
| --- | --- |
| Problem (1-2 lines) |  |
| Proposed Solution (1-2 lines) |  |
| Customer / Business Impact |  |
| Why Now |  |

## Problem Statement

### Problem Definition

- Exact customer problem:
- Workflow location:

### Impacted Users / Systems

| Field | Details |
| --- | --- |
| Personas |  |
| Systems / Modules |  |

### Problem Severity

| Field | Details |
| --- | --- |
| Frequency |  |
| Impact |  |

### Evidence

| Field | Details |
| --- | --- |
| Qualitative evidence |  |
| Quantitative evidence |  |
| Source and date of each |  |

### Behaviour Summary

- Current state:
- Desired state:

## Current vs Desired Behaviour

| Workflow Step / Scenario | Current Behaviour | Desired Behaviour | Notes |
| --- | --- | --- | --- |
|  |  |  |  |

## Goals and Success Metrics

### Product / Business Metrics

| Metric | Baseline | Target | Timeframe | Instrumented? |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

### Guardrail Metrics

| Metric | Acceptable Range | Risk if Breached |
| --- | --- | --- |
|  |  |  |

A metric with no baseline is not a metric. A target with no timeframe is not a target. Mark anything not yet instrumented, because that is delivery work.

## Dependencies and Impact

| Field | Details |
| --- | --- |
| Affected teams / downstream consumers |  |
| Internal modules |  |
| Capability type | Reusable capability / Customer-specific customisation |
| Can this be generalised later? |  |
| Duplication risk |  |

### Vendor and Third Party

| Vendor / Partner | What it provides | Contract or capability gap | Lead time | Owner |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

### Regulatory and Compliance

| Field | Details |
| --- | --- |
| Regime(s) in scope |  |
| Specific obligation touched |  |
| Evidence or audit artefact required |  |
| Approver |  |
| Consent or permission change |  |

## Solution Design and Requirements

### Lifecycle

Describe the end-to-end flow in numbered steps.

1.
2.
3.

### Proposed Solution

- What it is:
- Existing system fitment / constraints:
- API / synchronous integration changes:
- Event-driven integration changes:
- Data / batch / data lake changes:
- Dependent module changes:
- UI / UX changes:

Keep this at outcome and contract level. For APIs capture consumers, inputs, outputs, errors, compatibility and SLAs. For events capture producers, consumers, triggers, payload expectations, delivery guarantees, ordering, retries, idempotency and failure handling. For data and batch capture source systems, data contracts, freshness, backfills, reconciliation and downstream consumers. For UI reference the mocks rather than pixel detail, unless the detail is a real requirement.

### Functional Requirements

| ID | Requirement | Source | Priority |
| --- | --- | --- | --- |
| FR-1 |  |  |  |

Write each one as observable behaviour with inputs, conditions and expected results.

### Acceptance Criteria

One block per scenario, each traceable to a functional requirement.

```
AC-1  (FR-x)
Scenario:
Given:
When:
Then:
```

Cover the unhappy paths as well as the happy one.

## Non-Functional Requirements

| Requirement Area | Details | Threshold |
| --- | --- | --- |
| Availability |  |  |
| Scalability |  |  |
| Performance |  |  |
| Logging / Observability |  |  |
| Security / Audit |  |  |
| PII handling |  |  |
| Data retention and deletion |  |  |
| Accessibility |  |  |
| Localisation / Multi-tenant behaviour |  |  |

## Assumptions and Out of Scope

| Field | Details |
| --- | --- |
| Assumptions |  |
| Out of scope for this release |  |
| Deferred, with expected release |  |

## Open Questions

| Question | Owner | Decision Needed By | Blocks |
| --- | --- | --- | --- |
|  |  |  |  |

## Rollout Strategy (documented by engineering)

| Field | Details |
| --- | --- |
| Migration plan |  |
| Breaking changes |  |
| Forward / backward compatibility |  |
| Versioning strategy |  |
| Deprecation plan |  |
| Rollback plan |  |
| Feature flags |  |
| Other rollout constraints |  |

## Decision Log

| Date | Decision | Rationale | Alternatives Considered | Departs from source? |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

Any omission, narrowing, expansion or contradiction of a source artefact belongs in this table, in Assumptions and Out of Scope, or in Open Questions. Unrecorded, it is drift.
