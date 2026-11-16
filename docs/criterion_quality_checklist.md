# Criterion Quality Checklist

| Check | Pass condition | Common failure mode |
|---|---|---|
| **Prompt-traceable** | Every required criterion maps to an explicit user requirement or documented baseline policy | Silent adds (brand, nicer thresholds, “confidence”) |
| **Atomic** | One measurable claim per criterion | Bundled checks (“in stock and under budget”) |
| **Objective** | Two reviewers would score the same response the same way from the same evidence | Subjective language (“convenient”, “helpful”) |
| **Evidence-grounded** | Pass/fail depends on transcript or tool records | Contaminated reference answers |
| **Threshold-faithful** | Inequality and units match the prompt exactly | Boundary drift (`<` vs `≤`) |
| **Non-duplicative** | No two criteria score the same underlying requirement | Overlapping wording |
| **Uncertainty-safe** | Honest “cannot confirm / no option qualifies” can pass when evidence is missing | Criteria that reward fabricated certainty |
| **Schema-clean** | Stable IDs, non-empty text, boolean `required`, optional `source` | Duplicate IDs |

## Mini tests
1. **False-negative probe:** valid response must pass every criterion.
2. **False-positive probe:** invalid / invented response must fail at least one.
3. **Missing-evidence probe:** unused confirmation tools must not allow a “success” grade.
