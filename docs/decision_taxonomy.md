# Reviewer Decision Taxonomy

| Label | Meaning | Typical action |
|---|---|---|
| `REPAIR` | Task is evaluable after correcting the rubric | Rewrite criteria; regrade |
| `REWORK_TASK` | Essential evidence, tools, or instructions are missing/ambiguous | Redesign fixtures or prompt |
| `MODEL_ERROR` | Model contradicted or ignored available evidence | Keep/strengthen evidence-backed fails |
| `NO_MODEL_ERROR` | Model met requirements supported by the evidence | Do not punish for rubric defects |

Labels may combine (e.g. `REPAIR` + `MODEL_ERROR`) when both the model and the evaluation setup are defective.
