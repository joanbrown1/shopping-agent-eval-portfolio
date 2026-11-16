# Scenario 02 — Noise-cancelling headphones

**Domain:** Shopping / accessory selection  
**Scenario type:** Feature + budget filter; model over-weights a marketing label  
**Synthetic fixture**

## Original user prompt

> Recommend **one** pair of over-ear headphones. Requirements: **active noise cancelling (ANC)**, battery life **at least 30 hours**, price **at most $250**, and must support **wired use** (3.5 mm or USB-C analog). Prefer the cheapest option that meets all hard requirements. Do not recommend out-of-stock items.

## Agent-visible catalog (`catalog.search`)

| Product | Price | ANC | Battery | Wired | In stock | Notes |
|---|---:|---|---:|---|---|---|
| Pulse Quiet 2 | $229 | Yes | 35 h | Yes (3.5 mm) | Yes | — |
| AeroBud Max | $199 | “Transparency mode” only | 40 h | Yes | Yes | No ANC field = false |
| Harbor ANC Lite | $249 | Yes | 28 h | Yes | Yes | Battery below requirement |
| Studio Shield | $239 | Yes | 32 h | No (BT only) | Yes | No wired |
| Nightowl Pro | $245 | Yes | 36 h | Yes (USB-C) | No | Out of stock |

## Validity rule

**Pulse Quiet 2** is the only in-stock row meeting ANC + ≥30 h + ≤$250 + wired.
