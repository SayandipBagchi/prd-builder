# Ownership Metadata

Delivery tickets are grouped by who owns the work, not by what the feature does. This file covers how the grouping is derived and what to do when the profile does not answer.

## The boundaries

In order of precedence:

1. **Client.** Which customer or engagement the work belongs to.
2. **Product.** Which product in the portfolio.
3. **Primary module.** Which module owns the change and will be assigned the ticket.
4. **Dependent modules.** Which other modules have to change for this to work, named explicitly or recorded as `None`.

A change that crosses any of these boundaries is more than one ticket, even when it is one feature and one sentence in the PRD.

## Required fields

The tenant profile lists the fields every delivery ticket must carry, in that programme's own vocabulary. Read them there.

Where the profile lists a field, the ticket carries it. Where the profile is silent and a field turns out to be required by the target project, ask. Do not map it to a similar-sounding field from another programme.

## When metadata is missing or ambiguous

Ask before proposing tasks, not after. A preview built on a guessed module is a preview that has to be redone.

Ask for the smallest thing that unblocks: the module, not the whole grouping. One question, then continue.

If the user does not know which module owns something, that is a real answer and it is worth surfacing: an unowned change is a delivery risk before it is a ticketing problem. Record it as an open item in the preview rather than assigning it to the module that looks closest.

## Grouping output

Present the grouping before the tickets:

```
Client: <name>
  Product: <name>
    Primary module: <name>
      Dependent modules: <names, or None>
        Proposed tickets: <count>
```

Confirm the grouping, then produce the ticket preview. Two confirmations for a large breakdown is cheaper than one wrong set of tickets.

## Splitting and merging

**Split** when any of these differ between two pieces of work:

- primary module
- dependent module
- delivery owner
- rollout path, for example one piece behind a flag and one not
- acceptance surface, for example one verified in the app and one in a batch job

**Merge** when all of the ownership metadata matches, the acceptance path is the same, and splitting would produce tickets nobody would groom separately.

When in doubt, ask which the team would rather groom. Do not default to more tickets. A breakdown that produces thirty tickets for a two-week change is a breakdown nobody will use.

## Dependency work

A dependent module's change gets its own ticket, its own acceptance criteria and its own dependency rationale naming what it unblocks.

Never bundle it into the primary module's ticket with a sentence in the description. That is the single most common way a cross-module dependency reaches the sprint unnoticed.

## Traceability

Every proposed ticket carries, in its description:

- the source artefact and the PRD section it comes from
- the requirement IDs or acceptance criteria it implements
- the ownership metadata
- the dependency rationale where one exists
- the definition-of-ready override block, if the gate was overridden

A ticket that cannot name where it came from should not be created.
