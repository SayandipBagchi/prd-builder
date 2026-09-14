# Guided Clarification

Interaction flow only. `../templates/prd-template.md` defines the sections. `reviewing-prd` defines whether they are adequate.

## Rules

- Walk the template in order. Ask only about what is missing or unclear.
- Every section is required: fill it, mark it `N/A` with a reason, or carry it as an open question.
- Stay on one section or subsection until it is draftable, then move.
- If only small gaps remain in a section, draft it and ask a targeted follow-up rather than reopening the whole thing.
- Challenge current-state and constraint claims with evidence from the artefacts you fetched.
- Keep questions short and specific. Ask for numbers, owners, timeframes and explicit constraints rather than opinions.
- Never turn the adequacy bar into a batch questionnaire. One section at a time is the whole point.

## Modes

### Resume

- Map the existing draft onto the template.
- Classify each section as `complete`, `partial` or `missing`.
- Ask only about `partial` and `missing`.
- Say which section you are resuming from.

### First draft

- Map the fetched sources onto the template.
- Start at the first missing high-value section, which is usually Problem Statement or Goals, not Overview.
- Continue in template order.

## Section order

1. Overview and Feature Brief
2. Problem Statement
3. Current vs Desired Behaviour
4. Goals and Success Metrics
5. Dependencies and Impact
6. Solution Design and Requirements
7. Non-Functional Requirements
8. Assumptions and Out of Scope
9. Open Questions
10. Rollout Strategy
11. Decision Log

## Questions that work

Ask for the thing that would settle the section, not for the section.

| Weak | Better |
| --- | --- |
| What are the success metrics? | What does this number look like today, and what would tell you in ninety days that it worked? |
| Any dependencies? | Which team ships something before this can go live, and has anyone told them? |
| What is out of scope? | What will someone reasonably expect in the first release that will not be there? |
| Any compliance considerations? | Which obligation does this touch, and who signs off that it is met? |
| What is the current behaviour? | Walk me through what a customer sees today at the step where this breaks. |

## When the user does not know

That is an answer. Record it as an open question with an owner and a decision-needed-by date, and move on.

Do not fill it with a plausible value, do not leave it blank and silent, and do not ask the same question in different words later in the session.

## Stopping

Stop asking when every section is complete, `N/A`, or carried as an open question with an owner.

Then draft, say what is still open, and offer the review.
