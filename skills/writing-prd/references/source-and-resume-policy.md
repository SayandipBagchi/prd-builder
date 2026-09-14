# Source And Resume Policy

## Source priority

1. Explicit user corrections or pasted replacement text in the active conversation
2. An existing PRD draft at the tenant's canonical path
3. The tenant's requirements baseline issue
4. Linked artefacts: wiki pages, markdown files, attached documents
5. The tenant's idea issue

When two sources conflict, keep the higher-priority one and ask about the disputed field only. Do not reopen the whole section, and do not silently merge.

## Source use

- The requirements baseline issue is the primary requirements source when it exists. The idea issue is supporting problem and rationale context.
- Linked markdown, wiki pages and attached documents are supporting or fallback requirements input when the higher-priority sources are missing.
- If an idea issue exists and a requirements issue does not, name the gap and guide the user to create or link one. If they decline, continue from the idea issue and the other artefacts rather than blocking the session.
- If neither exists, run a net-new PRD flow from whatever the user supplies.

## Fetch first

Before asking a single clarification question:

- pull the available idea and requirements issues
- follow links out to wiki pages, markdown and attached documents
- look for an existing draft at the tenant's canonical path
- run one lightweight analysis pass over all of it
- name the missing requirements baseline if there is one

If a fetch is blocked, report it once and continue from what is available. Do not retry in a loop, and do not stall the session waiting on it.

A question whose answer was sitting in a source you did not fetch is the most expensive mistake this skill can make.

## Canonical path

The tenant profile owns the path convention. Read it there.

Treat an existing file at that path as the working baseline, not as a draft to replace. If the user wants a fresh start, they will say so.

## Resume strategy

- Classify every section and subsection as `complete`, `partial` or `missing`.
- Continue from the first `partial` or `missing` item in template order.
- Do not restart from the top unless the user asks for a reset, or the existing draft is incompatible with what they now want.
- Say where you are resuming from, once.

## Loop control

- Never repeat a clarification the user already answered in this run.
- Skip `complete` sections unless the user asks for a rewrite.
- Advance in deterministic template order, so a repeated turn moves forward rather than circling.
- If the same section comes up a third time, stop asking and record what remains as an open question with an owner.

## Departures from source

Any omission, narrowing, expansion or contradiction of a source gets recorded in the PRD, in Assumptions and Out of Scope, Open Questions, or the Decision Log, with the rationale.

Recording it is what makes it a decision. Not recording it is what makes it drift.
