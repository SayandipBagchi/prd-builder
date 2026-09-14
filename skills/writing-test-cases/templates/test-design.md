# Test Design Template

```
# Test Design: <feature>

Source: <PRD path or title>, version or date
Programme: <tenant profile>
Review verdict at time of writing: <ready | ready with conditions | not ready | not reviewed>
Requirements covered: <n>
Cases: <n>
Requirements in gaps: <n>
```

If the definition-of-ready gate was overridden, the override block goes here, above everything else.

## Coverage summary

| Requirement | Cases | Types covered | Notes |
| --- | --- | --- | --- |
| FR-1 |  |  |  |

A requirement with only a happy-path case needs a note saying why the other types do not apply.

## Cases

Group by area, then by requirement.

```
### <Area>

TC-<area>-1
Traces    FR-x / AC-y
Type      happy
Priority  P1, because <reason>
Pre       
Steps     1.
          2.
Expect    
Data      
```

Repeat per case. Keep the block shape identical so the set can be pasted into a test management tool without reshaping.

## Cross-cutting suites

### Data handling

| Case | What it verifies | Traces |
| --- | --- | --- |

### Regulatory evidence

| Obligation | Evidence artefact | Case | Traces |
| --- | --- | --- | --- |

### Observability

| Event or field | Expected value | Case | Traces |
| --- | --- | --- | --- |

### Migration and rollback

| Case | What it verifies | Traces |
| --- | --- | --- |

### Concurrency

| Case | What it verifies | Traces |
| --- | --- | --- |

Drop a suite that genuinely does not apply, and say in one line why.

## Gaps

### Untestable as written

| Requirement | What is missing | Owner |
| --- | --- | --- |

### Undefined threshold

| Requirement | What number is needed | Owner |
| --- | --- | --- |

### Out of reach

| Case | What it needs | Owner |
| --- | --- | --- |

## Not covered, deliberately

| Area | Why | Who agreed |
| --- | --- | --- |

An area excluded on purpose belongs here with a name against it. An area excluded by accident belongs in Gaps. The difference matters when someone reads this after an incident.
