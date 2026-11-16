# Shopping Agent Eval Practice

I put this together to practice reviewing AI shopping agents — the kind that search a catalog and recommend a product.

The idea is simple: an agent gets a user request, looks at product data, and answers. A draft rubric grades that answer. Sometimes the rubric is wrong, sometimes the model is wrong, and sometimes both are. I walk through each case, decide what actually went wrong, and fix the rubric where I can.

Everything here is made up for practice (fake catalogs, fake transcripts). It’s not real company work.

## What’s inside

There are four shopping scenarios:

1. **[School laptop](scenarios/01_school_laptop/)** — User wants a laptop under clear limits (price, RAM, SSD, weight, in stock). The agent picks a valid one, but the grader fails it for rules the user never asked for (like “must be Apple” and a higher SSD minimum).
2. **[Noise-cancelling headphones](scenarios/02_noise_cancelling_headphones/)** — User asks for real ANC, battery life, wired support, and a budget. The agent treats “transparency mode” as ANC and the draft grader lets it slide.
3. **[Phone + carrier compatibility](scenarios/03_phone_carrier_compat/)** — User only wants a phone if Carrier Wave compatibility is actually checked. The agent assumes “unlocked” is enough and never runs the compatibility tool.
4. **[School supply cart](scenarios/04_school_supply_budget_cart/)** — User needs a few items with a hard total that includes shipping. The agent gets a shipping quote, then ignores it and says the cart is within budget.

## How each scenario is set up

Every folder has the same files:

- `task.md` — what the user asked for, and what product/tool data the agent could see
- `transcript.md` — step-by-step what the agent did and what the draft grader said
- `rubric_before.json` — the original grading criteria (with problems on purpose)
- `review.md` — my notes on each criterion, plus what I’d change
- `rubric_after.json` — the cleaned-up rubric

If you want to try one yourself, read `task.md`, `transcript.md`, and `rubric_before.json` first. Write your own call, then compare with `review.md`.

## Run the checker

```bash
python3 validate.py
```

That just checks the folders and rubric files are set up correctly.

## Other notes

- [SKILLS.md](SKILLS.md) — what this project is meant to show
- [METHODOLOGY.md](METHODOLOGY.md) — how I review a case
- [docs/criterion_quality_checklist.md](docs/criterion_quality_checklist.md) — quick checklist for rubric quality
- [docs/decision_taxonomy.md](docs/decision_taxonomy.md) — what labels like REPAIR / MODEL_ERROR mean

## License

MIT. See [LICENSE](LICENSE).
