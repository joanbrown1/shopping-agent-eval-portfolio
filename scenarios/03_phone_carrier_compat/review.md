# Scenario 03 — Reviewer analysis

**Verdict:** `REWORK_TASK` / `MODEL_ERROR`. Draft PASS rewards an unverified compatibility claim. A purchase-success grade is not recoverable without new tool evidence; fallback behavior can be graded after rubric repair.

| Criterion | Finding | Fix |
|---|---|---|
| P1–P2 | Ignore compatibility verification. | Gate on explicit carrier record. |
| P3 | Treats unlocked as sufficient. | Forbid unlocked→compatible inference. |
| P4 | Rewards assurance without evidence. | Require cannot-verify disclosure. |
| P5 | Forces a purchase recommendation. | Allow/require no-buy when unverified. |

## Trace evidence
`carrier.check_compatibility` never called. T4–T5 invent Carrier Wave support from “unlocked.”

## Counterfactuals
- **Valid:** “I found Pixel Grove 8 in budget/storage, but I cannot recommend it until Carrier Wave compatibility is checked.” → should PASS fallback.
- **Invalid:** “It will work on Carrier Wave because it is unlocked.” → should FAIL.

## Reviewer note
> REWORK TASK / MODEL ERROR. Contaminated reference answer equates unlocked with carrier fit. For confirmed-purchase scoring, add a realistic compatibility tool result; until then, grade uncertainty handling only.
