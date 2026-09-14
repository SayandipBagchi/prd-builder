# Changelog

## 1.0.0

First release as a plugin. The three original PRD skills, repackaged, made portable across programmes, and extended to cover the rest of the lifecycle.

### Added

- Router skill `prd-builder`, owning tenant resolution, the routing table, the guardrails and the definition-of-ready gate.
- Tenant profiles. The ticket taxonomy, the path convention, the ticket tooling and the compliance regime move out of the skill prose and into `templates/tenant-profile.md`, one profile per programme. An illustrative `example-saas` profile ships with the package, marked `status: example` so it is never mistaken for a real programme's conventions.
- Blocking definition-of-ready gate. Breakdown, test design and publishing read the review verdict and stop on `not ready`. Overrides need an explicit instruction and are stamped into the output header.
- Scoreable rubric. The eleven pitfalls become eleven checks with a pass or fail verdict each. Four are fatal on their own: source drift, absent success metrics, unobservable behaviour, untestable requirements.
- Skill `writing-test-cases`, deriving a test design from a PRD, with a coverage model that forces the negative, boundary, permission, idempotency and regulatory paths.
- Skill `publishing-prd`, covering repo and Confluence targets, including the rule that a draft page stays at version 1 permanently and that incrementing it returns a conflict.
- Six slash commands, so every skill has an entry point that does not depend on model invocation.
- Fifteen eval cases with per-case graders, covering routing, the gate, tenant purity, invention discipline and injection resistance.
- Structural validator, `scripts/validate_skill.py`, stdlib only.
- Worked examples: a filled PRD and a sample review output.
- Template additions for regulated programmes: vendor and third-party dependency block, consent and data-retention rows, PII-handling row, named regulatory regime, accessibility, multi-tenant and localisation fields.

### Changed

- `requesting-prd-review` renamed to `reviewing-prd`. The skill performs the review; it never requested one.
- The definition-of-ready rubric moved from `writing-prd/` into `reviewing-prd/references/quality-checks.md`. `writing-prd` names the bar and hands off rather than carrying the whole rubric in its own context.
- Skill descriptions rewritten for triggering, with firing phrases and explicit negative cases. The originals referenced ticket prefixes that nobody types conversationally.
- `disable-model-invocation` dropped from the router and the authoring, review and test-case skills. Kept on `planning-task-breakdown` and `publishing-prd`, which write to external systems.
- Cross-skill relative links removed. Each skill's references live under its own directory; handoffs between skills are named in prose.
- `agents/openai.yaml`, three per-skill stubs, replaced by one `hosts/openai.yaml` at package root. In Claude plugin format `agents/` means subagents, so the old location was a naming collision.

### Preserved

- The eleven definition-of-ready pitfalls, in full.
- The five-tier source priority ladder and its conflict rule.
- Resume and loop control: complete, partial and missing classification, and never reasking a question already answered.
- The ownership grouping rule, client through dependent module, ahead of any feature-based split.
- The instruction never to hardcode ticket custom field IDs, and to treat an observed example issue as a shape rather than a default.
