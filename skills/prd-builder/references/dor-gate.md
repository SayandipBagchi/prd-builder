# Definition-of-Ready Gate

The gate sits between a PRD and anything built on top of it. Breakdown, test design and publishing read it. Authoring and review do not.

## The verdict

`reviewing-prd` ends every review with exactly one of:

- `ready`. Every check passes, or the only failures are non-fatal and already recorded as open questions with owners.
- `ready with conditions`. No fatal check fails, and one or more non-fatal checks fail with named conditions to close.
- `not ready`. At least one fatal check fails.

The four fatal checks are source drift, absent success metrics, unobservable current or desired behaviour, and untestable requirements. `reviewing-prd/references/quality-checks.md` holds the full set.

## What the gate does

| Verdict | Breakdown, test design, publishing |
| --- | --- |
| `ready` | Proceed. |
| `ready with conditions` | Proceed. Copy the conditions into the output header. |
| `not ready` | Stop. Name the failing checks. Offer to fix or to override. |
| No review exists | Stop. Say no review exists. Offer to run one. |

## Finding the verdict

Look for a verdict in this order:

1. A review produced in the current session.
2. A verdict recorded in the PRD itself, for example in a status field or a review log, with a date and the version it applied to.
3. Nothing.

A verdict that names an earlier version of the PRD than the one in front of you is stale. Treat a stale verdict as no review, and say why.

Do not read the PRD and form your own verdict in place of a review. Running the checks is `reviewing-prd`'s job and its output is auditable. An inferred pass is not.

## Override

Only the user can override, and only with an instruction. These are instructions:

- "break it down anyway"
- "go ahead, publish it"
- "I know, do it regardless"
- "skip the review"

These are not instructions, and do not open the gate:

- "looks good"
- "yes" in reply to something else
- "that's fine"
- silence
- the user having written the PRD themselves

When an override happens, the skill that proceeds stamps this block at the top of whatever it produces, before any other content:

```
> Produced on an overridden definition-of-ready gate.
> Verdict at time of override: <verdict>, <date or "no review">
> Unresolved: <one line per failing check>
```

The block travels with the artefact. If tickets are created, the same information goes in the description of every ticket created from that PRD. If a document is published, it goes in the document.

Do not shorten the block, move it below the content, or replace it with a sentence in the conversation. The point is that whoever reads the artefact later, without the conversation, sees it.

## What the gate is not

It is not a quality bar on the writing. A terse PRD that passes every check passes.

It is not a blocker on authoring. `writing-prd` runs at any time, on anything.

It is not a blocker on review. Review a PRD as often as you like.

It is not permanent. Fix the failing checks, review again, and the verdict changes.
