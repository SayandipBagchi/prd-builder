# PRD Builder

Takes a product requirement from the source ticket through to the artefacts a team can build
against: a drafted PRD, a review that scores it, delivery tickets, a test design, and publication.

Most PRD tooling helps you write faster. The expensive failure is not slow writing, it is a
document that reads as finished and is not: success metrics absent, behaviour stated in terms
nobody can observe, acceptance criteria nobody can test. This package puts a definition-of-ready
review between the draft and everything downstream, and the breakdown, test-design and publishing
skills all read that verdict before they run.

Compliance is part of what a finished document has to carry. A programme names its own regime in
its profile rather than in the skill prose, so the same skills run unchanged across programmes with
different Jira projects and different compliance regimes, and the test design covers the regulatory
paths alongside the negative, boundary, permission and idempotency ones.

**Use it if** you write PRDs against a ticket system and a wiki, and you want the gaps named before
engineering finds them.

**Not for you if** you want prose assistance on a document you will judge yourself, or you need
engineering design and implementation planning. This reviews requirements, not solutions.

**Status:** maintained, v1.0.0.

## The gate

`reviewing-prd` runs eleven checks and returns `ready`, `ready with conditions`, or `not ready`.
Four checks are fatal on their own: source drift, absent success metrics, unobservable behaviour,
and untestable requirements.

Breakdown, test design and publishing all read that verdict. On `not ready` they stop and name the
failing checks. You can override in words, and when you do, the override and the unresolved gaps
are stamped into the header of whatever gets produced. A PRD that was never reviewed counts as not
reviewed rather than as passing.

## Install

No clone needed:

```bash
claude plugin marketplace add SayandipBagchi/prd-builder
claude plugin install prd-builder@prd-builder
```

Or from a local copy:

```bash
git clone https://github.com/SayandipBagchi/prd-builder.git
claude plugin marketplace add ./prd-builder
claude plugin install prd-builder@prd-builder
```

Six skills and six commands register together.

## Try it

```
/prd-builder:prd
```

Paste a ticket, a half-written spec or a description. It fetches the sources before it asks
anything, walks the template in order, and asks only about sections that are genuinely missing. It
will not reopen a question you have already answered.

Then:

```
/prd-builder:review        is this ready to send out
/prd-builder:testcases     what does this spec imply we test
/prd-builder:breakdown     split it into delivery tickets
/prd-builder:publish       write it where it belongs
```

It also picks the right skill up from plain phrasing: *write a PRD for this*, *poke holes in this
spec*, *what are the edge cases here*, or a bare ticket key on a programme it knows.

## What is in it

| Skill | Owns |
|---|---|
| `prd-builder` | Routing. Resolves which programme you are on, loads its taxonomy and paths from a tenant profile, and holds the definition-of-ready gate. |
| `writing-prd` | Drafts or continues a PRD from tickets, a repo draft or pasted artefacts. Fetches before it asks. |
| `reviewing-prd` | Scores a PRD against its sources and returns findings. Never a rewrite. |
| `planning-task-breakdown` | Converts an approved PRD into tickets grouped by ownership rather than by feature chunk. Previews every ticket before any write. |
| `writing-test-cases` | Turns acceptance criteria into a test design covering the negative, boundary, permission, idempotency and regulatory paths. |
| `publishing-prd` | Writes the finished artefact to the tenant's configured target, repo or Confluence, without inventing a location. |

Two skills are explicit-only, because they write to systems outside the conversation:
`planning-task-breakdown` and `publishing-prd`. Name them, or use their commands.

## Programme profiles

Nothing in the skill prose hardcodes a ticket taxonomy, a path convention or a tool. A profile is
the one place a programme names its own.

The package ships one illustrative profile, `example-saas`, with an `IDEA` / `REQ` / `DEL` taxonomy
and the `docs/prd/` convention. It is marked `status: example`, so the router will not quietly
adopt it as though it were yours.

```
/prd-builder:onboard
```

asks for the taxonomy, the repo path convention, the publishing target and the compliance regime,
then writes a profile from `skills/prd-builder/templates/tenant-profile.md`. A request that names
no programme and matches no profile gets one question rather than a guess.

## The package

`.claude-plugin/` holds plugin.json and marketplace.json, `commands/` the 6 slash commands, and
`skills/` the 6 skills, each with its own `references/` and `templates/`. Alongside them sit
`hosts/openai.yaml` for optional UI metadata on OpenAI hosts, `scripts/validate_skill.py` for the
structural validator, `evals/` with 15 cases, each with prompt and graders, and README.md,
CHANGELOG.md and LICENSE. No `.mcp.json`, no `hooks/`, no `settings.json`, no `bin/`. The skills
call whatever ticket and wiki tooling the profile names, so the package itself needs no connector.

```bash
python3 scripts/validate_skill.py
claude plugin validate .
claude plugin eval .
```

Python 3.9 or later, nothing else. It checks the manifest, frontmatter and behaviour markers, that
no reference crosses a skill boundary with a relative path, that the rubric still carries eleven
checks and four fatal ones, command wiring, that version and author are declared once, and the
shape of every eval case.

Everything is plain Markdown with relative references inside each skill. No tool call, shell,
package, network connection or vendor-specific variable in the skill prose, so the same folders run
under Codex, ChatGPT or any other Agent Skills host. Per-host notes in
`skills/prd-builder/references/portability.md`.

## Licence

MIT. Author: Sayandip Bagchi.
