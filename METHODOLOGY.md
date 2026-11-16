# Review Methodology — Shopping Agent Evaluation

A repeatable process for auditing agent tasks, transcripts, and grading rubrics in this portfolio.

## Workflow (per scenario)

1. **Parse the user prompt** into explicit requirements. Do not add preferred brands, tighter thresholds, or policies the user never stated.
2. **Establish the evidence boundary.** List tool outputs visible to the model. Distinguish *absent data* from *ignored data*.
3. **Inspect the transcript chronologically.** Mark tool results, decision points, unsupported inferences, and the final answer.
4. **Audit every rubric criterion** against `docs/criterion_quality_checklist.md`.
5. **Counterfactual grade.** Apply the draft rubric to one clearly valid and one clearly invalid alternative response.
6. **Decide the action** using `docs/decision_taxonomy.md` (`REPAIR`, `REWORK_TASK`, `MODEL_ERROR`, `NO_MODEL_ERROR`).
7. **Write a concise note:** verdict, criterion IDs, exact evidence, grading consequence, remediation.

## Artifact contract

Each folder under `scenarios/` must contain:

| File | Purpose |
|---|---|
| `task.md` | Original prompt + agent-visible fixtures + validity notes |
| `transcript.md` | Simulated tool-use trace and draft grader outcome |
| `rubric_before.json` | Defective or contaminated draft criteria |
| `review.md` | Criterion-by-criterion audit + counterfactuals |
| `rubric_after.json` | Revised criteria with `source` provenance and `decision` |

```bash
python3 validate.py
```
