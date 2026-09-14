---
description: Stand up a tenant profile for a new programme
argument-hint: "[programme name]"
---

Use the `prd-builder` skill and run the onboarding flow in its tenant-resolution reference.

Ask the nine questions one at a time: programme name and aliases, ticket taxonomy, which artefact is the requirements baseline, ticket system and authentication, repo path convention, publishing target, compliance regime, the ownership metadata delivery tickets require, and anything a PRD on this programme must always carry.

Record only what the user answers, in the programme's own vocabulary. Do not normalise a field name to another programme's naming, do not fill a taxonomy row the programme does not have, and do not carry any prefix, path or field from an existing profile.

Leave anything unanswered as unknown and list it under Unknowns with a name beside it where possible.

Show the filled profile before saving, and when you hand it over, say which fields are unknown and what they will block.

Programme:

$ARGUMENTS
