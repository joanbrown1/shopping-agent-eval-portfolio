# Scenario 04 — School supply cart under a hard budget

**Domain:** Shopping / multi-item cart assembly  
**Scenario type:** Bundle constraints + tax/shipping; model ignores shipping in total  
**Synthetic fixture**

## Original user prompt

> Build a cart with **all** of the following in-stock items if possible: 1 pack of college-ruled notebooks (5-count), 1 pack of black pens (12-count), 1 calculator labeled **scientific**, and 1 backpack. Total **checkout price including shipping** must be **at most $60**. If the full set cannot fit the budget, say which item to drop first to stay ≤$60 and show the resulting total. Use only catalog prices and the shipping quote tool. Do not ignore shipping.

## Agent-visible evidence

**`catalog.search`:**

| SKU | Item | Price | In stock |
|---|---|---:|---|
| NB-5 | Notebooks 5-count | $12.00 | Yes |
| PN-12 | Black pens 12-count | $8.50 | Yes |
| CALC-SCI | Scientific calculator | $18.00 | Yes |
| CALC-BASIC | Basic calculator | $9.00 | Yes |
| BP-DAY | Daypack backpack | $22.00 | Yes |
| BP-PRO | Pro backpack | $35.00 | Yes |

**`cart.shipping_quote` for a 4-item cart (NB-5 + PN-12 + CALC-SCI + BP-DAY):**  
Returns shipping **$9.99**.

**Subtotal of that 4-item cart:** $12 + $8.50 + $18 + $22 = **$60.50** + shipping **$9.99** = **$70.49** (over budget).

**Valid reduced cart example:** drop backpack → notebooks + pens + scientific calc = $38.50 + shipping for 3 items **$5.99** = **$44.49** ≤ $60.

## Validity rule

A full 4-item recommendation at “about $60” without shipping is invalid. Correct paths: disclose over-budget full set and propose a drop, or assemble an in-budget subset with shipping included.
