# Scenario 01 — Reviewer analysis

**Verdict:** `REPAIR` / `NO_MODEL_ERROR`. Draft FAIL on Atlas 14 is unfair.

| Criterion | Finding | Fix |
|---|---|---|
| R1 | Prompt permits **$800 exactly**; draft uses **less than**. | Change to at most $800. |
| R2 | Correct. | Retain. |
| R3 | Prompt requires ≥512 GB; draft requires ≥1 TB. | Align to 512 GB. |
| R4 | Strict `<1.8 kg` is correct. | Retain. |
| R5 | Unsupported brand restriction. | Remove; replace with in-stock. |
| R6 | Bundles availability + budget. | Split into atomic checks. |

## Trace evidence
T3–T5 show Atlas 14 at $749 / 16 GB / 512 GB / 1.60 kg / in stock — all prompt constraints met.

## Counterfactuals
- **Valid boundary:** Exactly $800, 16 GB, 512 GB, 1.7 kg, in stock → should PASS; draft R1/R3 fail it.
- **Invalid:** Summit 15 fails weight despite passing price/RAM/SSD.

## Reviewer note
> REPAIR. Grader rejected a valid recommendation via invented SSD/brand rules and budget boundary drift. Atlas 14 should pass after revision.
