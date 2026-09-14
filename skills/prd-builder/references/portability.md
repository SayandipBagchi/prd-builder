# Portability

The skills are plain Markdown with relative references inside each skill directory. Nothing in the prose calls a tool, runs a shell command, imports a package, opens a network connection or reads a vendor-specific variable.

That makes the same folders runnable on any host that supports Agent Skills. What changes between hosts is how a skill gets invoked and what tooling is available to the session, not what the skill says.

## Claude

Installed as a plugin. Skills fire from their descriptions; the six commands in `commands/` give every skill a named entry point.

`planning-task-breakdown` and `publishing-prd` carry `disable-model-invocation: true`, so they run only when named or invoked by command. That is deliberate: both write outside the conversation.

Subagents would live in `agents/`. This package has none, and `agents/` stays absent so it is never mistaken for host metadata.

## OpenAI hosts

`hosts/openai.yaml` at package root carries display names, short descriptions and default prompts. It is optional metadata and affects nothing about behaviour.

Note the location. In Claude plugin format `agents/` means subagents, so host metadata in `agents/openai.yaml` is a naming collision. It lives in `hosts/`.

Implicit invocation is allowed for the router, authoring, review and test-case skills, and refused for breakdown and publishing, matching the Claude behaviour.

## Codex, Cursor, Copilot and other hosts

Point the host at the `skills/` directory. Each skill is self-contained: its references, templates and examples sit under its own folder, and no file reaches across a skill boundary with a relative path.

Where a host has no notion of explicit-only invocation, the guardrail still holds through prose. Both writing skills state that they preview and wait for an instruction before any external write.

## Tooling assumptions

The skills name what they need in business terms: fetch the source ticket, discover the create metadata, publish to the target. They do not name a CLI.

The tenant profile is where a specific tool gets named. That keeps the prose portable and puts the brittle part in one file per programme, which is also the file that gets edited when a team changes tooling.

If a session has no ticket or wiki tooling at all, the skills still work on pasted artefacts and produce Markdown. Only the write steps become unavailable, and they say so rather than pretending.

## Style constraint

The skill prose carries no dashes: no em dash, no en dash, no spaced hyphen standing in for one, no double hyphen. Hyphenated compounds such as definition-of-ready are fine.

The validator enforces this. It exists because the output these skills produce gets pasted into documents other people read, and a house style that holds across a package is worth more than any single sentence it costs.
