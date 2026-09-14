# Coverage Model

Every requirement gets swept for all seven case types. Most requirements will not need all seven, and saying "not applicable, because" for one is a finding worth having. Skipping it silently is not.

## The sweep

For each functional requirement and acceptance criterion:

1. **Happy path.** The stated behaviour, under the stated conditions, with valid input.
2. **Negative.** Each way the input or state can be invalid, and what the system does about each. Separate cases per failure reason, because they usually have separate handling.
3. **Boundary.** The edges of every range, limit, window, count or threshold the requirement names. At the limit, one below, one above. A window has a start edge and an end edge, and both need a case.
4. **State and sequence.** The same action from each state the entity can be in, and the same action twice. Out-of-order arrival where events are involved.
5. **Permission and role.** Each role that can reach the surface, including the role that should not, and the unauthenticated case.
6. **Idempotency and retry.** Duplicate submission, retried call, replayed event, resumed session. What the system does the second time.
7. **Failure of a dependency.** Each external system in the path: timeout, error response, partial response, slow response. Separate from negative input, because the handling usually differs.

## Cross-cutting suites

Run these once against the change as a whole, not per requirement.

**Data handling.** What personal data the change touches, whether it appears in logs, whether it crosses a boundary it did not before, and what deletion does.

**Regulatory evidence.** Where the PRD names an obligation, a case that verifies the evidence artefact exists and is correct. An obligation with no test is an obligation nobody can show was met.

**Observability.** The events, fields and identifiers the PRD says will exist, verified to exist with the right values. A success metric that cannot be measured after launch is a defect found cheapest here.

**Migration and rollback.** Where the change alters existing data or contracts: existing records behave, the flag off behaves as before, and rollback leaves nothing stranded.

**Concurrency.** Where two actors can touch the same entity: simultaneous action, and action during an in-flight change.

## Case shape

```
ID        TC-<area>-<n>
Traces    FR-x / AC-y
Type      happy | negative | boundary | state | permission | idempotency | dependency
Priority  P1 | P2 | P3, with the reason it is that
Pre       state and data the case starts from
Steps     numbered, each one observable
Expect    what is true afterwards, stated so someone can check it
Data      the specific values, or "undefined in source"
```

## Priority

Derive it, do not assign it by feel.

- **P1.** The requirement's failure is what the PRD's problem statement describes, or the case protects money, a regulatory obligation, or a customer's access to their account.
- **P2.** Real failure, contained blast radius, a workaround exists.
- **P3.** Cosmetic, rare, or recoverable without anyone noticing.

Where the PRD says nothing about severity or frequency, say the priority is unsourced rather than inventing a distribution.

## What not to produce

- Cases that test the implementation rather than the stated behaviour.
- Cases with "verify it works" as the expected result.
- A number picked to fill a threshold the source left undefined.
- Duplicated cases across requirements that share an acceptance surface. Trace one case to both.
- A P1 on everything. A design where everything is critical prioritises nothing.
