# Tenant Profile Template

Copy this into `../profiles/<programme-slug>.md` and fill it from what the user answers. Leave anything unanswered as `unknown`. Never fill a field with a plausible default.

---

```
# Profile: <Programme Name>

aliases: <other names people call this programme>
status: <active | in build | retired | example>

## Ticket taxonomy

| Role | Prefix | Issue type | Notes |
| --- | --- | --- | --- |
| Idea, problem, rationale |  |  |  |
| Requirements baseline |  |  |  |
| Delivery work |  |  |  |
| Defect |  |  |  |

Requirements baseline when sources disagree: <which prefix wins>
Ticket system and site: <instance>
Authentication note: <how a session authenticates, or unknown>

## Paths

PRD draft path: <convention, for example docs/prd/<issue-key>-<slug>.md>
Issue key in filename: <yes | no>
Finished document location: <repo path, wiki, or both>

## Publishing target

Target: <repo | wiki | both | none>
Wiki space: 
Parent page: 
Page naming convention: 

## Delivery ticket metadata

Fields every delivery ticket must carry, using this programme's own field names:

- 
- 
- 

Parent linkage: <which issue the delivery ticket parents to>

## Compliance

Regime: <named regulator, data protection law, or none>
Mandatory PRD content for this regime:
- 

## Programme constants

Anything a PRD here must always carry, for example a vendor dependency block, a named market, a currency, a customer segment:

- 

## Unknowns

Fields left unanswered, and who to ask:

- 
```

---

## Filling rules

- Record only what the user states. A programme with three ticket types gets three rows, not four with one invented.
- Field names go in the programme's own vocabulary. Do not normalise them to another programme's names.
- `unknown` is a real answer and belongs in the Unknowns list with a name beside it where possible.
- Show the filled profile before saving it.
- When you hand it over, say which fields are unknown and what they will block.
