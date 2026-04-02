# Stablecoin Depeg Detector

### What if UST had an early warning system?

$40 billion evaporated when UST depegged. USDC briefly lost its peg during the SVB crisis. These events devastated portfolios and cascaded through DeFi.

This Intelligent Contract monitors stablecoin prices in real-time using AI-powered analysis on GenLayer. When a stablecoin starts drifting from its peg, you'll know — trustlessly, on-chain, before the crowd panics.

---

**How it works:**

The contract fetches live stablecoin price data → AI evaluates deviation severity → multiple validators reach consensus → result stored on-chain.

**Severity levels:**

| Status | What it means | What you should do |
|--------|--------------|-------------------|
| `ALL_STABLE` | Every major stablecoin within 0.1% of peg | Nothing, relax |
| `MINOR_DEVIATION` | Small drift detected (0.1-0.5%) | Monitor closely |
| `WARNING` | Significant deviation (0.5-2%) | Consider reducing exposure |
| `CRITICAL_DEPEG` | Major depeg event (>2%) | Emergency exit positions |

**Example output:**

```json
{
  "depeg_status": "MINOR_DEVIATION",
  "most_at_risk": "USDD",
  "deviation_pct": "0.3",
  "summary": "Minor USDD deviation, all major stablecoins safe."
}
```

---

**Deploy:**

GenLayer Studio → paste `05_stablecoin_depeg.py` → constructor `scan_url` = `https://www.coingecko.com/en/categories/stablecoins` → Deploy → call `check_depeg`

**Why GenLayer:** No other chain can natively fetch web price data + run AI risk assessment + achieve decentralized consensus in a single contract.

**Future plans:** Real-time monitoring loop, multi-stablecoin simultaneous tracking, DeFi circuit breaker integration.

*MIT License*
