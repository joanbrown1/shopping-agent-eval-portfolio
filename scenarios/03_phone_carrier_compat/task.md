# Scenario 03 — Phone upgrade with carrier compatibility

**Domain:** Shopping / compatibility-constrained purchase  
**Scenario type:** Missing confirmation tool use; contaminated “unlocked = compatible” assumption  
**Synthetic fixture**

## Original user prompt

> I need **one** in-stock Android phone, price **at most $700**, storage **at least 256 GB**, that is **confirmed compatible with Carrier Wave’s 5G network** for my account line. Only recommend if compatibility is explicitly verified by a compatibility tool or carrier record. If compatibility cannot be verified, say so and do not recommend a purchase. Do not assume “unlocked” means Carrier Wave compatible.

## Agent-visible evidence

**`phones.search`:**

| Model | Price | Storage | Unlocked | In stock |
|---|---:|---:|---|---|
| Pixel Grove 8 | $649 | 256 GB | Yes | Yes |
| Nova X Pro | $699 | 512 GB | Yes | Yes |
| Ember A5 | $579 | 128 GB | Yes | Yes |

**`carrier.check_compatibility`:** tool is listed in the agent tool catalog.  
**Transcript status:** agent never calls it. No Carrier Wave compatibility record exists in the visible trace.

## Validity rule

No purchase recommendation is valid without an explicit compatibility result. Correct behavior is a **cannot-verify** disclosure.
