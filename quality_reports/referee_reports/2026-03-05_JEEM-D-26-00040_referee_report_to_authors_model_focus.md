# Referee Report to Authors (Model-Focused)

**Manuscript ID:** JEEM-D-26-00040  
**Title:** Monitoring the Monitors: How Environmental Information Shapes Bureaucratic Incentives in China  
**Reviewer:** Anonymous Referee  
**Date:** 2026-03-05

## Overall assessment

This paper studies an important question and has strong empirical potential. My main recommendation is to substantially revise the model section so that it matches the institutional mechanism you are testing.

At present, the model does not explicitly put economic performance into promotion probability. Because your argument is about changes in incentive weighting under monitoring reform, this omission weakens the theoretical part and limits interpretation of the empirical coefficients.

## Recommendation

**Major Revision**

## Major comments

### 1) Add economic performance directly to the promotion rule

The current Section 3 effectively models promotion as a function of environmental signal and effort cost. This is too narrow for a cadre-evaluation context where growth and environmental targets are jointly relevant.

Please consider a multi-task promotion index, for example:

- `R = omega_y * Y - omega_p * S_p`
- `Pr(promote) = Lambda(R)`

where `Y` is economic performance and `S_p` is observed pollution signal.

This would align much better with the literature you cite on promotion tournaments and target-based evaluations.

### 2) Clarify the effort FOC as a net promotion-return condition

In the revised framework, the key FOC for environmental effort should reflect a tradeoff:

- **marginal cost of effort**
- equals **promotion gain from cleaner air**
- minus **promotion loss from weaker growth**.

With `Y` decreasing in environmental effort at the margin (short-run tradeoff), and pollution decreasing in effort, the FOC naturally becomes a net-benefit condition. This is the central mechanism your theory should emphasize.

### 3) Model post-2013 as a potential shift in evaluation weights

You should allow `omega_p` to change after 2013. More importantly, discuss whether `omega_y` might also change. If both can change, empirical interpretation becomes more complicated, and your identification section should explicitly acknowledge this.

## Suggested empirical revisions tied to the model

### A) Estimate changes in both pollution and growth gradients in promotion

Use a promotion equation that includes both environmental and economic performance channels, each interacted with post:

- pollution term and `pollution x post`
- growth-performance term and `growth x post`

This directly tests whether environmental weighting rises after monitoring and whether growth weighting changes.

### B) Test the model-implied tradeoff in effort responses

Use your policy-effort proxies and interact them with growth-pressure proxies (for example, industrial dependence, fiscal stress, employment pressure).

Predictions from the revised FOC:

1. Effort response to pollution signals should rise after monitoring.
2. This response should be weaker where marginal growth costs of environmental effort are higher.
3. If `omega_p` rises post-2013, effort increases should be stronger in high-baseline-pollution cities (where marginal pollution benefit is larger).

### C) Clarify what each post interaction identifies

If post captures both information precision and policy re-weighting, disentangle channels using:

- event-study around city monitoring activation,
- heterogeneity by baseline pollution and growth pressure,
- robustness checks for concurrent national environmental campaigns.

### D) Consider a decomposition exercise

A useful addition would be a decomposition of post-period changes into:

1. changing sensitivity of promotion to pollution,
2. changing sensitivity of promotion to growth,
3. behavioral adjustment in local effort.

This would make the model-empirics bridge much clearer.

## Minor comments

1. Keep notation consistent between the conceptual model and empirical equations.
2. Avoid using one symbol for both utility-function object and risk-aversion parameter.
3. Tighten the proof section for the incentive-slope comparative statics so the result is derived directly from your setup rather than mainly cited.

## Closing

I view this as a promising paper with a strong empirical backbone. The key step for a publishable revision is to make the theoretical structure explicitly multi-dimensional (environment plus growth), then align empirical tests tightly with that revised mechanism.
