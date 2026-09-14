---
name: publishing-prd
description: Writes a finished PRD or review to the target the tenant profile names, a repo path or a wiki space, without inventing a location. Explicit-only, because it writes outside the conversation. Use when the user names this skill, or asks to publish, push, upload or save a PRD to Confluence, a wiki, or a repo path, or to update a page that already exists. It checks the definition-of-ready verdict first, shows what will be written and where, and waits for an instruction rather than agreement. Do not use it to author or review the PRD (use writing-prd and reviewing-prd), to create delivery tickets (use planning-task-breakdown), or to publish anything that is not a PRD or its review.
disable-model-invocation: true
metadata:
  author: Sayandip Bagchi
---

# Publishing PRD: put it where the profile says, and nowhere else

Write the finished artefact to its destination. Get the destination from the tenant profile, confirm before writing, and never guess a space, a parent or a path.

## Check the gate

- `ready`: publish.
- `ready with conditions`: publish, with the conditions carried into the document, near the top, where a reader will see them.
- `not ready`, or no review: stop. Name the failing checks, or say no review exists, and offer the review.

Override needs an instruction. When overridden, the override block goes into the published document itself, above the content. Publishing is exactly the point at which the conversation stops travelling with the artefact, so the block has to be inside it.

## Resolve the destination

From the tenant profile: the target, the space, the parent page, the page naming convention, the repo path convention.

If the profile says `unknown` for anything the publish needs, ask. One question, then continue. Do not:

- pick a space because its name resembles the programme
- attach a page to a parent because it holds similar documents
- create a new parent, a new space or a new folder
- publish to a personal space because the target one is not resolvable
- fall back to a repo path when the profile names a wiki, or the reverse

A missing destination is a question, never a choice.

## Before writing

Show:

- the exact destination: path, or space and parent and title
- whether this creates something new or updates something that exists
- for an update, what changes, at section level
- the verdict, and the override block if there is one

Then wait for an instruction to publish. "That's the right place" is not an instruction.

## Writing

If the target is a repo path, read `references/repo-publish.md`.

If the target is a wiki, read `references/confluence-api.md`. It carries behaviour that is not obvious and has cost time before, including how draft pages version.

Either way: one destination per instruction. Publishing to a second place needs a second instruction.

## Updating something that exists

Never overwrite a document you have not read in this session. Read it, show what changes, then write.

If the document changed since the version you were working from, say so and show the difference before writing. Do not merge silently, and do not force past it because the change looks small.

Preserve anything the destination adds that the source does not have: page properties, labels, inline comments, reviewer annotations. Publishing a PRD should not strip a reviewer's comment thread.

## After

Report the destination and, where the target gives one, the link. Say what was created versus updated.

Do not also publish the review, the test design or anything else unless asked. One artefact per instruction.
