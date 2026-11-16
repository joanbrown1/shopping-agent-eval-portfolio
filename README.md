# Shopping Agent Evaluation Portfolio

**Standalone portfolio project** for AI evaluation / rubric review on **shopping and product-selection agents**.

Multiple scenarios under one domain — not a single prompt/answer demo. Each scenario includes prompt, catalog/tool fixtures, simulated transcript, defective draft rubric, full reviewer audit, and repaired rubric.

> **Honesty note:** All catalogs, tool outputs, and transcripts are **synthetic fixtures** for portfolio practice. Not confidential employer work or live production grading.

## Scenarios

| ID | Scenario | Draft grader issue | Reviewer call |
|---|---|---|---|
| [`01_school_laptop`](scenarios/01_school_laptop/) | Multi-constraint laptop pick | Unfair FAIL (invented SSD/brand rules) | `REPAIR` + `NO_MODEL_ERROR` |
| [`02_noise_cancelling_headphones`](scenarios/02_noise_cancelling_headphones/) | ANC + battery + wired + budget | PASS on transparency≠ANC | `REPAIR` + `MODEL_ERROR` |
| [`03_phone_carrier_compat`](scenarios/03_phone_carrier_compat/) | Carrier compatibility gate | PASS on unlocked≠compatible | `REWORK_TASK` + `MODEL_ERROR` |
| [`04_school_supply_budget_cart`](scenarios/04_school_supply_budget_cart/) | Multi-SKU cart + shipping cap | PASS ignoring shipping | `REPAIR` + `MODEL_ERROR` |

## What’s in each scenario

```text
task.md              # user prompt + agent-visible catalog/tools + validity rules
transcript.md        # tool-use trace + draft automatic grade
rubric_before.json   # defective draft criteria / contaminated answer key
review.md            # criterion audit, counterfactuals, reviewer note
rubric_after.json    # repaired criteria with source provenance
```

## Quick start

```bash
python3 validate.py
# Then work any scenario blind: task → transcript → rubric_before → your verdict → compare review.md
```

## Docs

- [`SKILLS.md`](SKILLS.md) — skill → evidence map for applications
- [`METHODOLOGY.md`](METHODOLOGY.md) — review workflow
- [`docs/criterion_quality_checklist.md`](docs/criterion_quality_checklist.md)
- [`docs/decision_taxonomy.md`](docs/decision_taxonomy.md)

## Job-application blurb

> Shopping-agent evaluation portfolio: four synthetic multi-constraint product scenarios covering unfair fails, feature-label drift, unverified compatibility claims, and shipping-inclusive cart budgets. Includes before/after rubrics, counterfactual grading, and a validation script.

## License

MIT — see [`LICENSE`](LICENSE).
