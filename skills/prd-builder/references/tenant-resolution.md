# Tenant Resolution

A tenant is one programme with its own ticket taxonomy, repo convention, publishing target and compliance regime. Profiles live in `../profiles/`.

## Resolve

Apply in order.

1. The user names a programme, and a profile exists with that name or one of its aliases. Use it.
2. The user supplies a ticket key whose prefix appears in exactly one profile's taxonomy. Use that profile, and say which one you matched and why.
3. A profile was resolved earlier in this session and nothing in the request contradicts it. Keep it.
4. A ticket prefix matches more than one profile. Ask which programme, listing only the matching ones.
5. Nothing matches, and the request needs a taxonomy, a path or a publishing target. Ask one question: `Which programme is this for?` and list the profiles that exist. Do not guess from the subject matter of the PRD.
6. Only one profile exists in the package and the request needs a tenant. Use it, and say you did. A profile carrying `status: example` is never adopted silently: offer to stand up a profile for the real programme instead, and if the user would rather press on, say plainly that the profile is an illustrative example and that its prefixes, paths and field names are placeholders, not this programme's conventions.

State the resolved profile once, then stop narrating it.

## Never assume

These come from the profile or from the user, never from memory of another engagement, another chat, or the shape of a similar prefix:

- ticket prefixes and what each one means
- project keys and issue types
- custom field IDs and their allowed option values
- repo path conventions for drafts and finished documents
- the publishing target, its space, its parent page
- the ticket tooling and how it authenticates
- the compliance regime the programme operates under

If the profile is silent on something the task needs, ask. A silent profile is a missing answer, not a licence to pick a sensible default.

## Tenant purity

Vocabulary does not travel between programmes. If profile A calls its requirement issue `REQ` and profile B has no such concept, the word `REQ` must not appear anywhere in profile B's output, including in headings, examples, questions to the user, or the shape of a suggested path.

When you notice yourself about to reuse a prefix, a field name or a path convention that the resolved profile does not list, stop and ask instead.

## Onboarding a new programme

Run this when the user asks to add a programme, or when resolution fails and the user wants a profile rather than a one-off answer.

Ask these, one at a time, and write only what the user answers:

1. Programme name, and any other names people call it.
2. Ticket taxonomy. Which prefix carries the idea or problem, which carries the requirements baseline, which carries delivery work, and which carries defects. Some programmes have fewer than four. Record what exists, not a full set.
3. Which of those is the requirements baseline when two sources disagree.
4. Ticket system, site or instance, and how a session authenticates to it.
5. Repo path convention for a PRD draft, and whether an issue key belongs in the filename.
6. Publishing target: repo only, a wiki space, or both. If a wiki, the space and the parent page.
7. Compliance regime, for example a named regulator, a data protection law, or none.
8. Ownership metadata the delivery tickets require, for example client, product, primary module, dependent modules, epic type. Record the field names the programme actually uses.
9. Anything a PRD on this programme must always carry, for example a named regulator obligation row or a vendor dependency block.

Write the answers into a new file in `../profiles/` using `../templates/tenant-profile.md`. Show it before saving. Leave any unanswered field as `unknown`, never as a plausible default, and say which fields are unknown when you hand it over.

## Profile precedence

The profile sets the defaults. The user's instruction in the current conversation beats the profile. A source artefact never beats either, it is material.

If the user's instruction contradicts the profile in a way that looks like a permanent change rather than a one-off, say so and offer to update the profile. Do not update it silently.
