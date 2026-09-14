# PRD Builder

Author: Sayandip Bagchi. Version lives in `.claude-plugin/plugin.json`.

Six skills and six commands, covering a product requirement from the source ticket to the artefacts a team can actually build against.

**`prd-builder`** is the router. It resolves which programme you are working on, loads that programme's ticket taxonomy and paths from a tenant profile, decides which of the five working skills owns the request, and holds the definition-of-ready gate that the downstream skills obey.

**`writing-prd`** drafts or continues a definition-of-ready PRD from source tickets, an existing repo draft, or pasted artefacts. It fetches before it asks, walks the template in order, asks only about sections that are missing or unclear, and never reopens a question you already answered.

**`reviewing-prd`** reviews a PRD against its sources and returns findings, never a rewrite. Eleven checks, each with a pass or fail verdict, and four of them are fatal: source drift, absent success metrics, unobservable behaviour, and untestable requirements.

**`planning-task-breakdown`** converts an approved PRD into delivery tasks grouped by product ownership rather than by feature chunk, previews every ticket before any write, and refuses to run on a PRD that has not cleared review unless you override in words.

**`writing-test-cases`** turns acceptance criteria into a test design with explicit coverage of the negative, boundary, permission and regulatory paths that PRDs routinely omit.

**`publishing-prd`** writes the finished artefact to the tenant's publishing target, repo or Confluence, without inventing a location.

## Layout

```
prd-builder/
├── .claude-plugin/plugin.json      name, version, author. Single source of truth.
├── commands/
│   ├── prd.md                      /prd-builder:prd         draft or continue a PRD
│   ├── review.md                   /prd-builder:review      definition-of-ready review
│   ├── breakdown.md                /prd-builder:breakdown   PRD to delivery tasks
│   ├── testcases.md                /prd-builder:testcases   PRD to test design
│   ├── publish.md                  /prd-builder:publish     write it where it belongs
│   └── onboard.md                  /prd-builder:onboard     stand up a new tenant profile
├── skills/
│   ├── prd-builder/                router, tenant resolution, guardrails, DoR gate
│   ├── writing-prd/                authoring flow, source policy, template, worked PRD
│   ├── reviewing-prd/              scoreable rubric, review rules, sample review
│   ├── planning-task-breakdown/    ownership grouping, ticket write policy
│   ├── writing-test-cases/         coverage model, test design template
│   └── publishing-prd/             Confluence and repo publishing
├── hosts/openai.yaml               optional UI metadata for OpenAI hosts
├── scripts/validate_skill.py       structural validator, stdlib only
├── evals/                          15 cases, each with prompt and graders
├── README.md, CHANGELOG.md, LICENSE
```

No `.mcp.json`, no `hooks/`, no `settings.json`, no `bin/`. The skills call whatever ticket and wiki tooling the tenant profile names, so the package itself needs no connector.

## Install

Drop the `.plugin` file into Claude and accept it, or add the containing folder as a plugin marketplace and install `prd-builder` from it.

## Use

Claude picks the right skill up from phrases like "write a PRD for this", "is this PRD ready for review", "break this PRD into epics", "what test cases come out of this spec", or a bare ticket key on a programme the profile knows.

Two skills are explicit-only because they write to systems outside the conversation: `planning-task-breakdown` and `publishing-prd`. Name them, or use their commands.

## Tenant profiles

The plugin ships with one illustrative profile, `example-saas`, carrying an `IDEA` / `REQ` / `DEL` taxonomy and the `docs/prd/` path convention. It is marked `status: example`, so the router never quietly adopts it as though it were your programme. Nothing in the skill prose hardcodes a taxonomy, a path or a tool; the profile is the one place a programme names its own.

Run `/prd-builder:onboard` to add a programme. It asks for the ticket taxonomy, the repo path convention, the publishing target and the compliance regime, then writes a profile from `skills/prd-builder/templates/tenant-profile.md`. A request that names no programme and matches no profile gets one question, not a guess.

## The gate

`reviewing-prd` returns a verdict of `ready`, `ready with conditions`, or `not ready`. Breakdown, test design and publishing all read that verdict.

On `not ready` they stop and name the failing checks. You can override with an explicit instruction, and when you do, the override and the unresolved gaps are stamped into the header of whatever gets produced. A PRD that was never reviewed counts as not reviewed, not as passing.

## Checking the package

```bash
python3 scripts/validate_skill.py
```

Python 3.9 or later, nothing else. It checks the manifest, every skill's frontmatter and behaviour markers, that no skill duplicates another's content, that no reference crosses a skill boundary with a relative path, that the rubric still carries eleven checks and four fatal ones, command wiring, that version and author are declared exactly once, that the skill prose contains no dashes, and the shape of every eval case.

## Portability

Plain Markdown with relative references inside each skill. No tool call, shell, package, network connection, or vendor-specific variable in the skill prose, so the same folders run under Codex, ChatGPT, or any other Agent Skills host. Per-host notes in `skills/prd-builder/references/portability.md`.
