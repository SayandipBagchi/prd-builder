# Worked Example: a review output

The PRD under review is a two-page draft called "Smarter Onboarding", written from one idea ticket. Its sources are IDEA-902 and REQ-961.

This is what the review looks like when the answer is no. Read the notes at the bottom.

---

## Verdict

**Not ready.** Three of eleven checks fail, two of them fatal.

## Scorecard

| # | Check | Verdict | Reason |
| --- | --- | --- | --- |
| 1 | Source alignment | fail | REQ-961 scopes this to returning applicants. The PRD covers all applicants and does not say why. |
| 2 | Written with people | pass | Design and onboarding engineering named as reviewers, two trade-offs in the Decision Log. |
| 3 | Evidence behind the problem | pass | Drop-off rate cited with a dated dashboard pull, plus six research quotes. |
| 4 | Solution not over-prescriptive | pass | Screens referenced by mock, no API shapes fixed. |
| 5 | Success metrics | fail | Target with no baseline and no timeframe. |
| 6 | Out of scope written down | pass | Two exclusions and one deferral stated. |
| 7 | Behaviour observable | pass | Current and desired flows given step by step against the live screens. |
| 8 | Fits the system that exists | pass | KYC vendor limits and the existing session timeout both captured from real artefacts. |
| 9 | Requirements testable | pass | Nine requirements, each with conditions and expected results. |
| 10 | Rollout thought about now | fail | Section deleted from the template. |
| 11 | Decisions and questions in the document | pass | Four open questions with owners and dates. |

## Source Alignment

**Expansion, unrecorded.** REQ-961, Scope field, limits this work to applicants who have previously started and abandoned an application. The PRD, Feature Brief and Functional Requirements, applies the new flow to every applicant. The Decision Log records two decisions, neither about this. That is check 1, and it is fatal.

Either narrow the PRD back to returning applicants, or record the expansion as a decision with its rationale and get it reflected in REQ-961.

**Narrowing, recorded, acceptable.** IDEA-902 asks for document re-upload as part of the same change. The PRD defers it under Assumptions and Out of Scope with a reason and an expected release. That is how a departure is supposed to look.

**Contradiction, unrecorded.** IDEA-902 states the driver as regulatory remediation. The PRD, Overview, lists the driver as Strategic roadmap. One of the two is wrong, and whichever it is, the mismatch changes how this gets prioritised.

## Definition-of-Ready Gaps

**Check 1, fatal. Scope expanded beyond the requirements baseline.** Feature Brief and FR-1 through FR-9 apply to all applicants; REQ-961 scopes to returning applicants only. Closes when the PRD either narrows to match, or records the expansion in the Decision Log with rationale and a note that REQ-961 needs updating.

**Check 5, fatal. Success metrics are not evaluable.** Goals and Success Metrics gives one metric, "onboarding completion rate", with a target of 70 percent, no baseline and no timeframe. Nobody can tell whether 70 is a stretch or a regression. Closes when the metric carries a current baseline with its source and date, and a timeframe for the target. The guardrails table is empty, and given the flow change touches KYC, a guardrail on verification pass rate is worth one row.

**Check 10. Rollout Strategy is absent.** The section is not in the document. The PRD changes a live onboarding flow with a KYC vendor in the path, so migration, feature flags and rollback are in scope before build, not after. Closes when the section exists, even marked not yet documented, with a named owner.

## Needs Clarification

**Which applicants see the new flow first?** FR-4 mentions a phased exposure. Nothing says by what: market, cohort, or percentage. This may be intentional, and it changes what Rollout has to cover.

**"Session resumes where the applicant left off", FR-6.** Unclear whether that includes a session abandoned before KYC submission, which is the case the evidence section spends most of its space on.

**The driver mismatch above.** Recorded under Source Alignment rather than as a gap, because it may be a typo in Overview rather than a real disagreement.

## Optional Tightening

Evidence is strong but the six research quotes are undated. If they predate the last onboarding change, the drop-off they describe may already be partly fixed.

---

## What to notice

**The verdict is the first line.** The reader is deciding whether to send this out. They get that answer before anything else, and again at the end.

**Eight passes are one line each.** A passing check does not earn a paragraph. The detail goes where something is wrong.

**Every finding cites a section and a source field.** "REQ-961, Scope field" and "Feature Brief and FR-1 through FR-9" can be acted on. "The scope feels off" cannot.

**Each gap says what closes it.** The reader leaves with three tasks, not three complaints.

**Nothing is rewritten.** The review names the missing baseline. It does not supply a number to illustrate, because an illustrative baseline has a way of becoming the baseline.

**A recorded narrowing is called out as correct.** Showing what good looks like, in the same document, costs two lines and teaches more than the rules do.

**Check 10 fails on a deleted section.** Present and marked not yet documented would have passed. Deleting it is what turns a known gap into an invisible one.
