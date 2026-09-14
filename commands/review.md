---
description: Score a PRD against its sources and return a readiness verdict
argument-hint: "[PRD path, or paste the draft]"
---

Use the `reviewing-prd` skill. Do not rewrite anything.

Score all eleven checks as pass, fail or not run, each with evidence cited by PRD section and source field. A check you could not run is not a check that passed.

Lead with the verdict, then the scorecard, then Source Alignment, then the gaps. Use only the three buckets: Definition-of-Ready Gaps, Needs Clarification, Optional Tightening. No code-review severity language.

Any failure among source drift, absent success metrics, unobservable behaviour or untestable requirements makes the verdict not ready, however good the rest is.

Do not supply a missing number, owner or date, even as an illustration. The gap is the finding.

PRD:

$ARGUMENTS
