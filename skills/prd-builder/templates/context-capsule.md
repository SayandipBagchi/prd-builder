# Context Capsule

Hand this to the user at the end of a working session so a later session, or a colleague, can pick the thread up without rereading the conversation.

Keep it short enough to paste into a new chat. Everything in it is something that was decided or produced, never a plan you are proposing.

---

```
## PRD context capsule

Programme: <profile name>
Artefact: <PRD path or title>
Source tickets: <keys, with which one is the requirements baseline>

### State
Sections complete: <list, or "all">
Sections partial: <list>
Sections missing: <list>

### Review
Verdict: <ready | ready with conditions | not ready | not reviewed>
Date and version reviewed: 
Failing checks: <one line each, or none>
Conditions to close: <one line each, or none>

### Decisions taken
- <decision, rationale, date>

### Open questions
- <question, owner, decision needed by>

### Downstream
Tickets created: <keys, or none>
Test design: <done | not started>
Published: <where, or not published>
Gate overridden: <yes, with what unresolved | no>

### Next step
<one line>
```

---

## Rules

- Only record what happened. A capsule is not a plan.
- Carry the review verdict verbatim, including a `not reviewed`. A capsule that omits the verdict lets the next session guess.
- If the gate was overridden, the capsule says so. That fact outlives the conversation.
- Name owners for open questions where an owner exists, and leave them blank rather than guessing where one does not.
- Offer the capsule. Do not append it to every response.
