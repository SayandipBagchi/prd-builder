# Review Rules

How findings get worded, bucketed and evidenced. `quality-checks.md` decides what is checked.

## Method

- Lead with findings. Praise only where it changes what the reader does next.
- Cite evidence from the PRD and the source artefacts. A finding with no citation is an opinion.
- Reference PRD headings and source fields, not vague prose. "The metrics table" beats "the goals bit".
- For each finding say three things: what is wrong, why it blocks definition-of-ready, and what the source expected where a source is involved.
- Prefer omission over weak suspicion.
- Name context gaps explicitly instead of guessing around them.
- End with a readiness verdict, and put the same verdict at the top.

## Buckets

Three, and only three:

- **Definition-of-Ready Gaps.** A failing check. Blocks, or carries a condition.
- **Needs Clarification.** The PRD may be right but cannot be read one way. Ambiguity, not error.
- **Optional Tightening.** Improves the document, blocks nothing. Keep this section short, and drop it entirely rather than padding it.

Do not invent a fourth. Do not use code-review severity words: no blocker, critical, major, minor, nit, P0.

## Source alignment

- Compare against every source before judging prose quality.
- Call out four things: omission, narrowing, expansion, contradiction.
- Non-alignment is acceptable when the PRD records it as a justified decision, assumption, out-of-scope choice, or open question with rationale. Recorded, it is a decision. Unrecorded, it is drift and it fails the check.
- Say which source, which field, and which PRD section, for each one.

## Wording

| Weak | Better |
| --- | --- |
| Metrics could be stronger | Goals and Success Metrics: no baseline on either metric, so neither target can be evaluated. Check 5 fails. |
| Some requirements are vague | FR-3 says "handle partial failures". No inputs, conditions or expected result, so it cannot be tested. Check 9 fails. |
| Consider adding rollout detail | Rollout Strategy is empty. The PRD changes an event contract, so compatibility and rollback are in scope before build. Check 10 fails. |
| Looks good overall | Ten of eleven checks pass. |

## What not to do

- Do not rewrite a sentence to show what you meant. Describe what is missing.
- Do not start asking clarification questions section by section. That is the authoring skill.
- Do not score the writing. Tone, length and polish are not checks.
- Do not add a finding because a section is short. Short and complete passes.
- Do not pass a check you could not run. Mark it `not run` and say what was missing.
- Do not fill in a number, owner or date the PRD lacks, even as an illustration. The gap is the finding.
