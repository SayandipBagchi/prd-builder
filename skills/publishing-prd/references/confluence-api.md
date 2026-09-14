# Wiki Publishing

Behaviour notes for Confluence-style wikis. Load this only when the tenant profile names a wiki as the target.

Nothing here overrides the destination rules in `../SKILL.md`. This is how to write once the destination is confirmed, not permission to find one.

## Draft pages version differently

A page in draft status stays at version 1 permanently. Draft versioning is not supported.

Always send `version.number` as `1` when updating a draft. Incrementing it to `2` returns a conflict, and the conflict looks like a permissions or payload problem until you know this. That one behaviour has cost more debugging time than everything else on this page.

Confirm draft status before assuming it. Fetch the page expanding version and status, and read the status back rather than inferring it from where the page sits.

## Published pages version normally

A published page increments. Read the current version, send current plus one, and expect a conflict if someone else saved in between. On conflict, re-read and show the difference rather than forcing.

## Payload shape

```json
{
  "id": "<pageId>",
  "type": "page",
  "title": "<title>",
  "status": "<draft | current>",
  "version": { "number": 1 },
  "body": {
    "storage": {
      "value": "<h2>Content</h2>",
      "representation": "storage"
    }
  }
}
```

The body is storage format, an XHTML-like markup, not Markdown and not the display HTML. Converting Markdown straight into the body produces a page that renders as escaped text or silently drops structure.

Tables, panels, status lozenges and expand blocks each have their own storage-format markup. A PRD is mostly tables, so this is where most of the conversion effort goes.

## Converting a PRD

- Headings map cleanly.
- Tables need full storage-format table markup. An empty cell still needs its cell element, or the row shifts.
- Code blocks become a structured macro, not a `pre` element.
- Internal links to other pages use the page reference form, not a bare URL, or they break when a page moves.
- Anchors from a table of contents need the heading IDs the wiki generates, which are not the ones a Markdown renderer would generate.

Check the rendered page after publishing. A payload that returns success can still render wrong, and a PRD that renders wrong is a PRD nobody reads.

## Titles

Titles are usually unique within a space. Publishing with a title that already exists fails, or attaches to the wrong page, depending on the endpoint.

Use the profile's naming convention. If a page with that title already exists and it is not the one you meant to update, stop and ask. Do not disambiguate by appending a number.

## What not to do

- Do not create a space.
- Do not create a parent page to hang a PRD under.
- Do not publish to a personal space as a fallback.
- Do not delete or archive an existing page to replace it. Update it.
- Do not strip page properties, labels or inline comments that exist on the page you are updating.
- Do not publish a second artefact in the same instruction.

## If publishing fails

Report the failure with what was attempted: the destination, the operation, and the response. Do not retry with a different destination, a different title, or a different status. Each of those is a new decision and it belongs to the user.
