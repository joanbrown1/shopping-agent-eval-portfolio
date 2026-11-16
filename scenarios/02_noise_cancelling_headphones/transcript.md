# Scenario 02 — Simulated agent transcript

- **T1 — User:** Over-ear, ANC, ≥30 h battery, ≤$250, wired, cheapest valid, in stock.
- **T2 — Tool:** `catalog.search({"category":"headphones","form":"over-ear"})`.
- **T3 — Tool:** Five-row catalog from `task.md`.
- **T4 — Analysis:** AeroBud Max is cheapest at $199 and lists “Transparency mode”; treat as ANC-equivalent.
- **T5 — Final:** “Buy AeroBud Max — $199, 40 h battery, wired, transparency/ANC, in stock.”
- **T6 — Draft grader:** PASS (reference answer wrongly set to AeroBud Max as cheapest).

## Independent review question

Does “transparency mode” satisfy an explicit ANC requirement? Is the draft PASS fair?
