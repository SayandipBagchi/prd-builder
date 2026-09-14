# Evals

Fifteen cases. Each is a directory with a `prompt.md`, a `case.yaml` and two graders.

- `prompt.md` is the user turn, verbatim.
- `case.yaml` names the skill the case is about and whether it should fire.
- `graders/skill-fired.md` checks routing: the right skill, not a sibling, and not a generic answer.
- `graders/criteria.md` checks behaviour, one independent checkbox per line. An item that cannot be verified from the output is a fail, not a pass.

## What the suite covers

| Group | Cases |
| --- | --- |
| Routing | `route-write-not-review`, `route-review-not-rewrite`, `breakdown-does-not-self-fire`, `ignores-unrelated` |
| The gate | `gate-blocks-breakdown`, `gate-override-is-recorded`, `not-ready-forced-by-one-fatal` |
| Invention discipline | `no-invented-requirements`, `no-field-id-invention`, `testcases-name-the-gaps` |
| Tenant safety | `tenant-purity-no-carryover`, `publish-does-not-guess-destination` |
| Mode discipline | `review-stays-in-review-mode`, `resume-does-not-reask` |
| Input boundary | `prompt-injection-in-pasted-prd` |

## Two cases expect nothing to happen

`breakdown-does-not-self-fire` and `ignores-unrelated` pass when no skill runs. A suite made only of cases where something fires will never catch a plugin that fires on everything.

## Scoring

Run each prompt in a clean session with the plugin installed, then score both graders by hand or with a model judge. A case passes when every checkbox in both graders passes.

The two graders are separate on purpose. A response can route correctly and still break the output contract, and that is a different defect from routing to the wrong skill.
