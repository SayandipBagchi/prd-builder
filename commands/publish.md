---
description: Write the finished PRD to its configured destination
argument-hint: "[PRD path, and the destination if it differs from the profile]"
---

Use the `publishing-prd` skill.

Check the definition-of-ready verdict first. On a not-ready verdict, or no review, stop and offer the review. When overridden, the override block goes inside the published document, above the content, because the conversation does not travel with the artefact.

Take the destination from the tenant profile. If the profile says unknown for anything the publish needs, ask. Never pick a space because its name resembles the programme, never create a parent to hang the page under, and never fall back to a personal space or a different target.

Show the exact destination, whether this creates or updates, and what changes, then wait for an instruction to publish.

For a wiki target, remember that draft pages stay at version 1 permanently and that incrementing returns a conflict. Check the rendered page afterwards, because a successful write can still render wrong.

One artefact per instruction.

Artefact:

$ARGUMENTS
