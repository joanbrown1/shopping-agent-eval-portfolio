# Scenario 01 — School laptop selection

**Domain:** Shopping / product selection  
**Scenario type:** Multi-constraint catalog filter with unfair draft fail  
**Synthetic fixture:** fictitious catalog and transcript

## Original user prompt

> Find one available laptop for school from the provided catalog. Requirements: price **at most $800**, **at least 16 GB RAM**, **at least 512 GB SSD**, and **weight strictly below 1.8 kg**. Include model, price and specs. Do not recommend an out-of-stock item.

## Agent-visible catalog (`catalog.search`)

| Product | Price | RAM | SSD | Weight | In stock | Brand |
|---|---:|---:|---:|---:|---|---|
| Atlas 14 | $749 | 16 GB | 512 GB | 1.60 kg | Yes | Northstar |
| Summit 15 | $799 | 16 GB | 1 TB | 1.85 kg | Yes | Juniper |
| Elm Air | $819 | 16 GB | 512 GB | 1.40 kg | Yes | Elm |
| Birch 13 | $780 | 8 GB | 512 GB | 1.25 kg | Yes | Birch |
| Cedar Pro | $790 | 16 GB | 1 TB | 1.72 kg | No | Cedar |

## Validity rule

Atlas 14 is the only row that satisfies **all** explicit prompt requirements. Others each fail at least one condition.
