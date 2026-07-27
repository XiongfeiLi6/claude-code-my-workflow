# R1 Concern Matrix — JEEM-D-26-00040R1 (Referee 2 audit)

**Date:** 2026-07-24. Page references: "ms p." = printed manuscript page; response = pp. 13–22 of the R1 PDF; revised manuscript = pdf pp. 43–87 (ms pp. 1–45); appendix = pdf pp. 23–42.

## Major comments (round 1 §3.1–3.6)

### R2.1 — Core interpretation: monitoring vs. broader post-2013 shifts → PARTIALLY RESOLVED
**What they did (verified):**
- Event study added (Fig 3, ms p. 25): pre-adoption coefficients imprecise (range −1.0 to +0.55), no systematic trend, all insignificant; post-adoption gradient strengthens gradually, significant after ~3 event years. Presentation is honest ("economically large... estimated imprecisely").
- Reframing carried through: title changed; Results text now interprets "the baseline coefficient as the change in the reduced-form effect of realized air-pollution shocks... following the shift" (ms p. 23); conclusion explicitly states they "do not directly test" weight-change channels (ms p. ~38, verified verbatim).
- NEW information-gains test (Table 3, ms p. 27): city-level correlation between official API and satellite-reconstructed API pre-2014 (mean 0.56, SD 0.10, 115 cities); triple interaction log(PM2.5)×Post×APIcorr = +0.139** (0.059) — larger info gains → larger gradient change; 44% of the post-shift increment.
- Effort event study (App Fig 3): flat pre-trends, response significant at event years +3 to +5.

**Residual issues:**
1. Table 3 reports no lower-order interactions (log(PM2.5)×APIcorr, Post×APIcorr). If omitted, the triple interaction conflates the information-gain effect with time-invariant gradient differences and level shifts across high/low-correlation cities. Ask to include/report them (or state they are included).
2. Low pre-period API correlation ≈ manipulation intensity, which plausibly correlates with broader post-2013 crackdown exposure (bigger revelation → bigger targets/scrutiny) — so the test narrows but does not cleanly isolate "information" from bundled accountability. Text hedges appropriately; the ABSTRACT does not ("We show that at least part of this change occurred through an observability-and-incentives mechanism" — should be "provide evidence consistent with").
3. Rollout compressed into 2012–2014 → event time nearly collinear with calendar time; worth one explicit sentence acknowledging this limit (the reframing already concedes it implicitly).

### R2.2 — Model–empirics mapping (multitask) → RESOLVED
Model fully rewritten (ms pp. 8–13, verified): W_t = π̄_t − γ_tS + δ_tG with G = ḡ − κe + ν; CARA utility over realized payoff (Eq. 5); certainty equivalent with risk premium (ρ/2)[γ²(σ_ε²+σ_t²)+δ²σ_g²] (Eq. 6); center's objective Y = ω(−P) + χG separates policy weights from career-reward slopes; binding participation makes risk premium costly to the center; FOC ce = γ_t(θ_t+βa) − δ_tκ is exactly the requested net-promotion-return condition; Prop 1 closed form + comparative statics in four primitives. Target-vs-realized-pollution ambiguity addressed institutionally (Section 2.1, ms p. 6). Also fixes Referee 1's signal-variance critique.
*Optional note:* δ_t (growth career slope) is exogenous while γ_t is optimized — a one-sentence justification would help.

### R2.3 — Promotion coding and sample restrictions → RESOLVED
Verified: explicit coding rule (ms p. 17 + fn 6: sub-provincial/provincial-capital lateral moves = promotion; other same-rank moves = 0); demoted/disciplined now IN baseline (ms p. 14 fn 5; Table 1 row; Table 2 notes); Table 7 col (5) exclusion robustness: −0.337*** vs baseline −0.313***; col (3) excludes sub-provincial cities: −0.317***. Documentation expanded.
*Minor residual:* alternative promotion definitions (strict-upward-only; multinomial splits) not shown — the main bias concern is addressed, so not blocking.

### R2.4 — IV exclusion and diagnostics → PARTIALLY RESOLVED
**What they did (verified):** expanded exclusion discussion (ms p. 17); App Table 2 tests inversions → weather channels; Table 7 col (4) adds visibility/dew point/min temp + ×Post interactions: interaction stays negative/significant (−0.569**).
**Residual issues:**
1. App Table 2 actually shows visibility 2.852* and dew point 1.349* significant at 10% (2 of 3 outcomes) — the text's "limited evidence" / "no strong relationship" soft-pedals this. Characterization should be accurate.
2. Table 7 col (4): the interaction magnitude nearly doubles (−0.313 → −0.569) when weather controls enter. Sign/significance robust, but an 80% magnitude swing from controls that "shouldn't matter" deserves discussion — it suggests the weather channel is not innocuous, and the baseline may understate (or col 4 overstate) the effect.
3. The round-1 ask for a falsification on promotion-relevant non-pollution outcomes was not done (weather controls are a partial substitute). Could be requested as a cheap addition or dropped at referee's discretion.

### R2.5 — Effort measure validation beyond work-report text → PARTIALLY RESOLVED
**What they did (verified):** App Fig 2 category-level adoption trends; replication package now includes the AI text-classification code; new coarse realized-effort proxy (provincial per-capita waste-gas treatment investment): App Table 4 (response of investment to lagged pollution ×Post = 36.715*, 10% only, ONE specification, province-clustered), App Table 6 (investment weakens inversion–PM2.5 link post-shift: triple −0.002**), Table 1 shows investment nearly doubled post-shift.
**Residual issues:**
1. The core round-1 ask — human-audit validation of the AI classification (audit sample, intercoder agreement, precision/recall by category) — was NOT done. This remains the cheapest, most direct fix and is still missing.
2. App Fig 2 partially undercuts "relatively stable adoption": 3–4 categories (clean heating, heavy-pollution emergency response, dust control, traffic) break exactly at 2013–14; emergency-response plans were *mandated* by the Action Plan, so template-driven reporting remains plausible for those categories. Authors should either exclude Action-Plan-mandated categories in a robustness check or temper the claim.
3. Investment validation is a single 10%-significant specification — fine as "suggestive," and the text says so, but it cannot carry more weight than that.

### R2.6 — Fog/smog speculation → RESOLVED
Verified: reworded to "One possible interpretation..." (hedged, plausible, no over-claim).

## Secondary comments (round 1 §4.1–4.6)

| # | Ask | Status | Verification notes |
|---|-----|--------|--------------------|
| S1 (4.1) | Avoid overstating zero-to-negative break | RESOLVED (minor) | IV pre-period −0.275 (0.298), max |t|≈1.01 across Table 7 (p≈0.312 col 5, verified); Results text careful ("imprecisely estimated zero"). Minor: abstract's "no more likely to be promoted before" still reads like a precise zero — suggest "no detectably more likely." |
| S2 (4.2) | Drop log(1+y); add PPML | RESOLVED (doc fix) | Unlogged specs; App Table 3 notes state Poisson QML; **App Table 5's notes are silent on estimator** (response letter claims PPML) — ask authors to state the estimator in the notes. Substantively both measure types now significant (admin −0.550***, tech −0.256**). |
| S3 (4.3) | Local projections | RESOLVED | App Fig 4, h=0..3, IV. Effort outcomes robust at all horizons; Promote negative throughout but h=3 CI includes zero, h=1 borderline — "robust to alternative horizons" is slightly generous for promotion. |
| S4 (4.4) | Hierarchy beyond mayors | RESOLVED (minor) | New Section 9 + App Table 7: provincial leaders 2003–20, IV interaction −0.785 (0.683), null; honest power discussion (768 obs, 22 clusters); three-reason interpretation present. Minor: **col (2) OLS interaction is +0.282** (positive, significant)** — unmentioned sign flip; ask for a sentence reconciling OLS vs IV here. |
| S5 (4.5) | Heterogeneity | RESOLVED | Table 4 verified: waves null; ×After-2015 −0.519***; key regions 9% smaller (+0.027***); tenure 19% smaller/yr (+0.047***); age/edu/gender null. Learning interpretation reasonable. |
| S6 (4.6) | Documentation | RESOLVED | Coding rules + sample restrictions expanded; Python pipeline in replication package; App Fig 2 + discussion. (Human-validation stats folded into R2.5.) |

## New issues introduced by the revision (Phase 3 sweep)

1. **[N1 — moderate]** Table 3: lower-order interactions not reported (see R2.1 residual 1).
2. **[N2 — moderate]** Table 7 col (4) magnitude sensitivity to weather controls unexplained (see R2.4 residual 2).
3. **[N3 — minor]** App Table 5 estimator undocumented; response letter says PPML (see S2).
4. **[N4 — minor]** App Table 7 col (2) OLS positive-significant interaction unreconciled (see S4).
5. **[N5 — moderate]** Abstract overclaims relative to the paper's own hedging: "We show that at least part of this change occurred through an observability-and-incentives mechanism" vs Section 7.1's "supporting the existence of" + the 115-city representativeness caveat. Suggest "We provide evidence consistent with..."

## Bottom-line assessment (for discussion)

The revision is serious and largely successful: the model is now correct and delivers exactly the requested mapping; the framing was genuinely tempered; every requested analysis exists in some form; the response letter's claims verify against the manuscript with no misrepresentations found (a few generous characterizations noted above). Remaining items are bounded: mechanism-language calibration (abstract), Table 3 lower-order interactions, weather-control magnitude discussion, the still-missing human-validation audit of the text classifier, and three documentation fixes. None requires a new identification strategy or new data collection beyond a small coding audit.

**Suggested recommendation: Minor Revision.**
