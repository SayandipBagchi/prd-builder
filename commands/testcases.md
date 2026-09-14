---
description: Derive a test design from a PRD, and name what cannot be tested
argument-hint: "[PRD path, ticket key, or paste the acceptance criteria]"
---

Use the `writing-test-cases` skill.

Check the definition-of-ready verdict first. On a not-ready verdict, say which checks fail and offer the review, because a PRD with untestable requirements can only produce a plausible-looking test design.

Sweep every requirement for all seven case types: happy, negative, boundary, state and sequence, permission, idempotency, and dependency failure. Then run the cross-cutting suites: data handling, regulatory evidence, observability, migration and rollback, concurrency.

Every case traces to a requirement ID or acceptance criterion. Expected results are observable. Where the source leaves a threshold undefined, write the case and mark the value undefined in source rather than picking a number.

End with the gaps section: untestable as written, undefined threshold, out of reach. That section is the point.

Source:

$ARGUMENTS
