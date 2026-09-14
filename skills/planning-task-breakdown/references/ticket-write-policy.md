# Ticket Write Policy

Everything between an approved preview and a created ticket.

## Order of operations

1. Preview shown, including every required field.
2. Explicit instruction to create received.
3. Current create metadata discovered for the target project and issue type.
4. Business fields mapped to current field IDs and allowed option values.
5. Any unmappable field asked about, not filled.
6. Tickets created.
7. Keys reported back, with anything that failed and why.

Skipping step 3 is how a breakdown silently writes into the wrong field or fails halfway through a set.

## Field discovery

Discover the create or edit metadata for the target project and issue type before every write session. Do not cache it from a previous session or a previous programme.

An example issue tells you which business fields a programme expects to see populated: client, product, module grouping, epic type, and so on. It does not tell you the field IDs on the current instance, and its option values are examples rather than defaults.

Treat every observed value as an example. A module name that exists on one example issue is not the module for this work.

## What never gets inferred

- Field IDs
- Allowed option values
- Project keys
- Issue types
- Parent linkage
- Assignees
- Dates, priorities, story points, sprints, labels and components

If a required field has no value supported by the source artefact or by the user, stop and ask for that one field. Do not select the closest option, do not leave a plausible default, and do not create the ticket without it and plan to fix it after.

## Writing several tickets

Prefer a single structured create carrying all the fields over a create followed by a sequence of edits. A half-populated ticket sitting in a board while the edits run is a ticket someone can pick up.

If a batch partially fails, report exactly which tickets were created and which were not, and stop. Do not retry the whole batch, which duplicates the ones that worked.

## The override block

If the definition-of-ready gate was overridden, every ticket created from that PRD carries this in its description, at the top:

```
Produced on an overridden definition-of-ready gate.
Verdict at time of override: <verdict>, <date or "no review">
Unresolved: <one line per failing check>
```

It goes in the ticket, not only in the conversation. Whoever grooms this next will not have the conversation.

## After the write

Report the created keys, the parent they were created under, and anything that did not get created with the reason.

Do not transition tickets, assign them, add them to a sprint or link them beyond the parent unless the user asked. Creation was the instruction.

## What this skill never does

- Create tickets that are not a breakdown of a supplied artefact
- Create a ticket for work the PRD does not contain
- Edit or transition an existing ticket that was not created in this run
- Write to a system the tenant profile does not name
