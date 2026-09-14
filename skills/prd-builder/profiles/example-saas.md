# Profile: Example SaaS

aliases: Example, SaaS Jira, IDEA/REQ/DEL workflow
status: example

## Ticket taxonomy

| Role | Prefix | Issue type | Notes |
| --- | --- | --- | --- |
| Idea, problem, rationale | `IDEA` | Issue | Carries the problem, the rationale and the constraints. Supporting context, not the requirements baseline. |
| Requirements baseline | `REQ` | Issue | Primary requirements source when present. |
| Delivery work | `DEL` | Epic | Created under a parent `IDEA`. |
| Defect | unknown | unknown | Not recorded. Ask before assuming a defect flow exists. |

Requirements baseline when sources disagree: `REQ`
Ticket system and site: Jira, SaaS instance
Authentication note: unknown. Confirm how the ticket system authenticates before writing.

## Paths

PRD draft path: `docs/prd/<issue-key>-<slug>.md`
Issue key in filename: yes, when an `IDEA` or `REQ` key exists. Otherwise `docs/prd/<slug>.md`.
Finished document location: repo. Treat an existing file at the canonical path as the working baseline.

## Publishing target

Target: repo
Wiki space: unknown
Parent page: unknown
Page naming convention: unknown

## Delivery ticket metadata

Fields every delivery ticket must carry, using this programme's own field names:

- `Client`
- `Product`
- `Primary Module`
- `Dependent Module(s)`, or explicitly `None`
- `Work Type`

Parent linkage: the resolved parent `IDEA`.

Field IDs are not recorded here on purpose. Discover the current create metadata for project `DEL` and issue type `Epic` before every write, and treat any example issue as a shape rather than a source of defaults.

## Compliance

Regime: unknown at profile level. Varies by client engagement.
Mandatory PRD content for this regime:
- Ask per engagement. Do not assume a regime from the customer's market.

## Programme constants

- A feature is either a platform capability or a customer-specific customisation. The PRD says which.
- Work crossing more than one client, product, primary module or dependent module gets grouped by those boundaries before any split by feature.
- Rollout strategy is documented by engineering, not by the PM, but the PRD carries the section so the decisions surface before delivery starts.

## Unknowns

Fields left unanswered, and who to ask:

- Defect taxonomy. Ask the owning team before routing a defect through this profile.
- Wiki publishing target. Ask before any publish request on this profile.
- Per-engagement compliance regime. Ask at PRD start.
