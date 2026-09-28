# House Style Exemplars

The living anchor for `manuscript-writing-style.md` (same folder). Shared by every project: read it
before drafting or revising manuscript prose, and add to it from any project. Each entry is a **pair**:
a version the authors disliked, the version they approved, and the reason in their words. Add a pair
every time a passage is approved or rejected, including Claude drafts. When the same reason recurs in
three or more pairs, distill it into a principle in the rule (§4 there).

Format per entry: heading `N. date · [project] · section · who judged`; then reason (one line) ·
disliked · approved · what changed. Pairs quote real papers, so their subject matter is the source
paper's; the lesson is in the reason and the change.

---

## 1. 2026-09-23 · [Regulation Coordination] · §6.1 Enforcement results · Xiongfei

**Reason (author):** the old version "sounds more like part of a report, not a paper"; the third paragraph
should merge into the second, shortened; the closing paragraph especially reads like a report.

**What changed:** opens on the finding, not the table; the three-margin list became a claim about regulator
behaviour ("sanction more often rather than more heavily"); the supply-chain check shrank to one clause
inside that paragraph; the benchmark gained a ratio ("roughly one-third"); the "Overall ... establishes the
paper's first result" paragraph was cut and its binscatter point moved to the first paragraph; numbers were
recomputed from the current table and put on one specification.

**Disliked:**

> \Cref{tab: penalty} reports the effect of export-weighted EU carbon-cost exposure on environmental enforcement.\footnote{Effects are reported per standard deviation of exposure throughout. The standard deviation is 1.31 for $\mathrm{Exp}^{\mathrm{ihs}}_{ckt}$ in the city-sector panel and 1.50 for the corresponding city-level measure; multiplying a coefficient by the corresponding standard deviation gives the reported percentage effect.} For each of three outcomes---the number of penalties, total monetary fines, and the average fine per penalty---we report an \emph{Exp-only} specification and a specification that additionally controls for upstream and downstream exposure.
>
> A one-standard-deviation increase in export exposure raises the number of environmental penalties by approximately 1.06 percent and total fines by approximately 1.50 percent. The average fine per penalty also increases, by approximately 0.58 percent. The adjustment therefore occurs primarily through the number of enforcement actions, with a smaller contribution from penalty severity.
>
> Adding upstream and downstream exposure leaves the export-exposure coefficient essentially unchanged, while the coefficients on the two additional channels are small and statistically insignificant. The stability of the export coefficient suggests that the enforcement response is associated primarily with same-sector export exposure rather than with correlated supply-chain exposure.
>
> For scale, moving an exposed city-sector from the 10th to the 90th percentile of exposure, a gap of 4.6 standard deviations, raises penalty counts by approximately 4.7 percent and total fines by 6.4 percent. Centralizing personnel authority over local environmental bureaus raised penalty counts by 13 percent and total fines by 19 percent \citep{kong2023centralization}, and the 2016 vertical-management reform raised the probability of a county-level administrative penalty by 3.6 percentage points \citep{li2025organizing}.
>
> Overall, \Cref{tab: penalty} establishes the paper's first result: environmental enforcement increases in Chinese city-sectors that are more exposed to EU carbon costs. A binscatter in \Cref{fig:app_binscatter_enforcement} shows that the relationship is smooth across the support of the exposure measure rather than being driven by a small number of extreme observations.

**Approved:**

> Environmental enforcement rises with exposure to EU carbon costs. \Cref{tab: penalty} reports estimates of equation~\eqref{eq:main_sector} for the number of penalties, total fines, and the average fine per penalty.\footnote{Effects are reported per standard deviation of exposure throughout. The standard deviation is 1.31 for $\mathrm{Exp}^{\mathrm{ihs}}_{ckt}$ in the city-sector panel and 1.50 for the corresponding city-level measure; multiplying a coefficient by the corresponding standard deviation gives the reported percentage effect.} A one-standard-deviation increase in export exposure raises penalty counts by approximately 1.1 percent and total fines by 1.4 percent. The relationship holds across the whole range of exposure rather than being concentrated in its upper tail (\Cref{fig:app_binscatter_enforcement}).
>
> The response operates mainly through how often regulators enforce. The average fine per penalty rises by approximately 0.55 percent, about half the response of penalty counts, so regulators sanction more often rather than more heavily. The response is also tied to the sector's own exports: controlling for upstream and downstream exposure leaves the export coefficient unchanged, and neither supply-chain channel is statistically significant.
>
> Moving a city-sector from the 10th to the 90th percentile of exposure, a gap of 4.6 standard deviations, raises penalty counts by approximately 4.9 percent and total fines by 6.6 percent. This is roughly one-third of the effect of centralizing personnel authority over local environmental bureaus, which raised penalty counts by 13 percent and total fines by 19 percent \citep{kong2023centralization}. The 2016 vertical-management reform, whose interaction with exposure \cref{sec:results-institutions} examines, raised the probability of a county-level administrative penalty by 3.6 percentage points \citep{li2025organizing}.
>
> \subsection{Trade Responses and the Carbon-Leakage Channel}

---

## 2. 2026-09-24 · [Regulation Coordination] · §6 opening paragraph · Xiongfei

**Reason (author):** approved as "fine". The old paragraph was a roadmap of subsections that stated no finding.

**What changed:** each subsection appears as its finding, with the section reference in parentheses;
the paragraph opens with the mechanism; the framework's abstract objects (target, monitor, budget) are
named as the actual 2013 and 2016 events.

**Disliked:**

> The results follow the chain in the framework. \Cref{sec:results-enforcement} reports the enforcement response to EU carbon-cost exposure, the paper's central estimate. \Cref{sec:results-trade} reports the export response through which the exposure reaches Chinese producers, and \cref{sec:results-pollution} the responses of production, energy use, regulated discharges, and city-level environmental outcomes. \Cref{sec:results-strategic} tests whether the enforcement response exceeds what the scale of regulated activity alone would produce, and \cref{sec:results-institutions} how it varies with the three objects in the regulator's problem: the target, the monitor, and the enforcement budget. \Cref{sec:results-dynamic} traces the timing of the responses and \cref{sec:results-robustness} the robustness of the enforcement estimate.

**Approved:**

> Carbon costs borne by EU producers reach Chinese regulators through Chinese exporters, and the results trace that path. Environmental enforcement rises in the city-sectors most exposed to EU carbon costs (\cref{sec:results-enforcement}). The exposure works through exports, which rise most toward the EU market (\cref{sec:results-trade}), and through the energy use and emissions that come with expanded production, while regulated discharges do not rise (\cref{sec:results-pollution}). Enforcement rises by more than the scale of regulated activity alone would produce (\cref{sec:results-strategic}). The response strengthens after air quality entered the performance assessment of local officials in 2013 and after provincial authorities took over local environmental monitoring in 2016, and it is accompanied by lower enforcement in non-tradable sectors (\cref{sec:results-institutions}). Exposure predicts no change in enforcement before the EU~ETS, and exports respond before enforcement does (\cref{sec:results-dynamic}). The enforcement estimate holds across alternative exposure measures, concurrent policies, samples, placebo shocks, and inference procedures (\cref{sec:results-robustness}).

---

## 3. 2026-09-24 · [Regulation Coordination] · §6.2 Trade responses · Xiongfei

**Reason (author):** approved; asked to include the rise in imports from the EU (a fact a referee would
raise), and not to add the downstream-exposure coefficient (true, but not part of this subsection's argument).

**What changed:** opens on the finding instead of "We next ask whether"; the margins list became a
statement about exporters ("sell more at unchanged prices"); "particularly informative" replaced by the
comparison itself (15 vs 6.1 percent, about 2.5 times); the closing "Together ..." summary folded into the
mechanism sentence; stale utilized-FDI claim ("positive but imprecise") corrected to no response.

**Lesson worth watching:** include the facts that cut against or complicate the argument; leave out facts
that are true but do not bear on the subsection's claim.

**Disliked:**

> We next ask whether export exposure generates the trade response underlying the proposed mechanism. If EU carbon pricing raises the relative cost of EU production, Chinese producers competing in those markets should expand exports to the EU.
>
> \Cref{tab: trade} decomposes the export response into nominal export values, real export values, and export unit values.\footnote{Customs data are available for 2000--2016, so the trade sample is shorter than the enforcement panel. City-level CO$_2$ emissions cover 2000--2017, and sector-level production and pollution data cover 2000--2014. Outcome-specific sample windows are reported in the corresponding table notes.} The sample is every city-sector pair with a customs record in some year, in every year, so a pair-year without a record is a zero and the estimates combine the intensive and extensive margins. Because an inverse-hyperbolic-sine outcome with zeros yields coefficients whose scale depends on the unit of measurement \citep{chen2024logs}, we quote magnitudes from Poisson pseudo-maximum likelihood on export levels, reported together with the two margins in \Cref{tab: app_trade_margins}. A one-standard-deviation increase in export exposure raises nominal exports by approximately 7.3 percent. The response runs mainly through city-sectors that already export: the probability of exporting rises by 0.2 percentage points, statistically indistinguishable from zero, while exports among trading cells rise by approximately 3.6 percent. Real export values increase as well, and export unit values show no detectable response, so the increase in export values is not generated by higher export prices.
>
> The destination of the trade response is particularly informative. \Cref{tab: app_mechanism_trade_eu} and \Cref{tab: app_trade_margins} show that the increase is concentrated in Chinese exports to the EU: 14.9 percent per standard deviation against 6.1 percent to other destinations, and the extensive-margin response, 1.2 percentage points, is confined to the EU. A generic Chinese export boom or aggregate macroeconomic shock would be expected to affect multiple destinations. The concentration of the response in EU trade is instead consistent with higher EU carbon costs improving the relative competitiveness of Chinese producers in those markets.
>
> Inward foreign investment moves in the same direction. A one-standard-deviation increase in city-level export exposure raises the number of newly contracted FDI projects by approximately 16.4 percent, while the response of utilized FDI value is positive but imprecisely estimated (\Cref{tab: app_fdi_relocation}). The contracted-project margin records investment commitments rather than realized productive capacity.
>
> Together, the trade and FDI responses are the trade signature of carbon leakage: EU carbon costs shift export demand and investment commitments toward Chinese producers in the same sectors, concentrated in EU destinations and unaccompanied by higher export prices.

**Approved:**

> Exposure to EU carbon costs raises Chinese exports. \Cref{tab: trade} reports the response of nominal exports, real exports, and export unit values.\footnote{Customs data are available for 2000--2016, so the trade sample is shorter than the enforcement panel. City-level CO$_2$ emissions cover 2000--2017, and sector-level production and pollution data cover 2000--2014. Outcome-specific sample windows are reported in the corresponding table notes.} The sample includes every city-sector pair that ever records a customs flow, in every year, with a zero where no flow is recorded, so the estimates combine the intensive and extensive margins. Because inverse-hyperbolic-sine coefficients on outcomes with zeros depend on the unit of measurement \citep{chen2024logs}, we quote magnitudes from Poisson pseudo-maximum likelihood on export levels (\Cref{tab: app_trade_margins}). A one-standard-deviation increase in export exposure raises nominal exports by approximately 7.3 percent.
>
> The increase comes from city-sectors that already export. Among trading cells, exports rise by approximately 3.6 percent per standard deviation, while the probability of exporting rises by only 0.2 percentage points, statistically indistinguishable from zero. Real export values rise and export unit values do not respond, so exporters sell more at unchanged prices.
>
> The destination of the increase separates it from a general export expansion. Exports to the EU rise by approximately 15 percent per standard deviation, about two and a half times the 6.1 percent increase to other destinations, and the only extensive-margin response, 1.2 percentage points, is in exports to the EU (\Cref{tab: app_mechanism_trade_eu,tab: app_trade_margins}). A Chinese export boom or an aggregate demand shock would raise exports to all destinations alike. A carbon price borne by EU producers raises the relative competitiveness of Chinese goods most in the EU market, which is the pattern the data show and the trade signature of carbon leakage. Imports from the EU rise as well, by about a third as much as exports to the EU on the same scale, while imports from other origins do not respond (\Cref{tab: app_mechanism_trade_eu}), consistent with exporters sourcing more inputs from the EU as their EU sales expand.
>
> Foreign investment moves in the same direction. A one-standard-deviation increase in city-level export exposure raises the number of newly contracted FDI projects by approximately 16 percent, while utilized FDI does not respond (\Cref{tab: app_fdi_relocation}). Contracted projects record investment commitments rather than capacity already in place.

---

## 4. 2026-09-24 · [Regulation Coordination] · §6.3 Production and environmental outcomes · Xiongfei

**Reason (author):** approved ("apply the 6.3 rewrite"); kept the multitask paragraph as drafted.

**What changed:** each paragraph opens with a claim; `\paragraph{}` headings removed; the footnote states
coverage facts instead of "can be underestimated due to data limitation"; the CO$_2$ result reports its
Romano--Wolf loss of significance; the city outcomes the old text never mentioned (NO$_x$, particulates,
wastewater) are stated; "we treat the contrast as directional" (reader-direction) replaced by the direct test;
the stringency-index paragraph no longer argues for its null; §6.2's number is not repeated here.

**Disliked:**

> We next examine whether the increase in exports is accompanied by changes in domestic production, energy use and environmental outcomes.
>
> \paragraph{Production and energy use.}
>
> Panel~A of \Cref{tab: pollution} reports city-sector production and energy use from the National Tax Survey. A one-standard-deviation increase in export exposure raises industrial output by approximately 0.8 to 1.1 percent and employment by approximately 2.0 to 2.2 percent, with the employment response statistically significant at the ten-percent level. Energy use moves with production: coal rises by approximately 1.5 to 2.1 percent per standard deviation, oil by approximately 2.7 to 3.1 percent, and electricity by approximately 1.8 to 2.1 percent. The output and energy estimates are individually imprecise, with minimum detectable effects between 4.2 and 7.4 percent per standard deviation.
>
> The combination of trade and production responses distinguishes additional production from pure destination switching. Pure switching would raise EU exports while leaving domestic output unchanged and rest-of-world exports declining. \Cref{tab: app_mechanism_trade_eu} shows EU exports rising and rest-of-world exports rising by less rather than falling, and total exports rise by approximately 7.3 percent per standard deviation, which a fixed quantity redirected across destinations cannot deliver. Domestic output and employment move in the same direction.
>
> \paragraph{Regulated pollution.}
>
> Panel~B reports the five regulated discharges from the Green Development Database\footnote{The tax survey covers 79 to 91 percent of city-sector cells and extends through 2016, against roughly a third of cells ending in 2013 for the Green Development Database. Since penalties are concentrated after 2013, the production and pollution results can be underestimated due to data limitation.}. A one-standard-deviation increase in exposure reduces SO$_2$ by approximately 1.9 to 2.1 percent, NO$_x$ by approximately 2.2 to 2.5 percent, and dust by approximately 5.3 to 5.6 percent, while COD and wastewater increase by approximately 0.9 to 1.9 percent. None is statistically distinguishable from zero, with minimum detectable effects between 6.1 and 11.8 percent per standard deviation. The five series do not share a window: SO$_2$, COD and wastewater run through 2014, NO$_x$ is reported from 2006, and dust only through 2010.
>
> Energy use and regulated discharges therefore move differently on the same panel and under the same specification: fossil inputs rise while regulated discharges do not. Because the two sets of outcomes come from different sources with different samples, we treat the contrast as directional rather than as an estimated gap.
>
> The informative comparison estimates production and pollution on one sample where both are observed. As reported in \Cref{tab: app_asymmetry}, the SO$_2$ response is approximately 3.8 percentage points smaller than the output response, and this difference is statistically significant. That test uses the Green Development Database measure of output rather than the tax survey, because it requires production and discharge observed for the same cells and years.
>
>
>
> \paragraph{City-level environmental outcomes.}
>
> \Cref{tab: city_outcomes} turns to aggregate environmental outcomes. A one-standard-deviation increase in city-level export exposure raises CO$_2$ emissions by approximately 1.8 percent in the Exp-only specification and 2.2 percent in the three-channel specification. Satellite PM$_{2.5}$ concentrations increase by approximately 1 percent in both specifications. Both responses are statistically significant.
>
> The increase in CO$_2$ is consistent with the expansion in fossil-energy use in \Cref{tab: pollution} Panel~A. The PM$_{2.5}$ response indicates that the economic expansion associated with foreign carbon-cost exposure has detectable consequences for local ambient pollution. Panel~B of the same table relates exposure to the environmental regulation stringency index. Both the contemporaneous and the lagged estimates are positive and neither is statistically distinguishable from zero; the sign is the one the enforcement response implies, and the index is a coarse annual measure of regulatory posture rather than of enforcement actions.
>
> The contrast between regulated sector-level pollutants and city-level CO$_2$ is consistent with a multitask regulatory problem. Local environmental regulators have direct mandates over conventional pollutants but not over CO$_2$ during most of our sample, so enforcement can contain regulated emissions without preventing increases in carbon emissions associated with expanded production. The sector-level and city-level estimates use different samples, time windows, and fixed-effect structures, and when the carbon and regulated-pollutant responses are estimated on a common sample equality cannot be rejected (\Cref{tab: app_asymmetry}).
>
> A formal accounting of realized and counterfactual carbon leakage is provided in \Cref{sec:policy_leakage_measurement}.

**Approved:**

> Exposure raises production and the energy that production uses. Panel~A of \Cref{tab: pollution} reports output, employment, and energy use from the National Tax Survey, which covers 79 to 91 percent of city-sector cells through 2016. A one-standard-deviation increase in export exposure raises industrial output by approximately 0.8 to 1.1 percent and employment by 2.0 to 2.2 percent, the latter statistically significant at the ten percent level. Energy use rises with output: coal by 1.5 to 2.1 percent, oil by 2.7 to 3.1 percent, and electricity by 1.8 to 2.1 percent per standard deviation. Each estimate is imprecise on its own, with minimum detectable effects of 4.2 to 7.4 percent, but all ten point estimates are positive.
>
> The expansion is additional production rather than exports redirected from other markets. Pure destination switching would raise exports to the EU, lower exports to ROW, and leave domestic output unchanged. Exports to ROW instead rise, by less than exports to the EU (\Cref{tab: app_mechanism_trade_eu}), total exports rise (\cref{sec:results-trade}), and output and employment move in the same direction.
>
> Regulated discharges do not rise with production. Panel~B reports the five discharges that local environmental bureaus regulate, from the Green Development Database.\footnote{The Green Development Database covers roughly a third of city-sector cells, most of them ending in 2013, the year the penalty registry becomes thick; the tax survey extends through 2016.} A one-standard-deviation increase in exposure lowers SO$_2$ by approximately 1.9 to 2.1 percent, NO$_x$ by 2.2 to 2.5 percent, and particulates by 5.3 to 5.6 percent, and raises COD and wastewater by 0.9 to 1.9 percent. None is statistically distinguishable from zero, with minimum detectable effects of 6.1 to 11.8 percent. SO$_2$, COD, and wastewater run through 2014, NO$_x$ starts in 2006, and particulates end in 2010.
>
> Where output and discharges are observed for the same cells and years, the gap between them can be estimated directly. On that sample, the SO$_2$ response is approximately 3.8 percentage points per standard deviation smaller than the output response, a difference statistically significant at the five percent level (\Cref{tab: app_asymmetry}). Emissions per unit of output fall in exposed city-sectors, consistent with the enforcement response in \cref{sec:results-enforcement}.
>
> At the city level, carbon emissions and ambient particulate concentrations rise. A one-standard-deviation increase in city-level export exposure raises CO$_2$ emissions by approximately 2 percent and satellite PM$_{2.5}$ concentrations by approximately 1 percent (\Cref{tab: city_outcomes}). Both are statistically significant individually; after the Romano--Wolf correction for the family of environmental outcomes, the PM$_{2.5}$ response remains significant and the CO$_2$ response does not (\Cref{tab: app_romano_wolf}). City emissions of NO$_x$, particulates, and wastewater show no statistically significant response. The environmental regulation stringency index does not respond either: its contemporaneous and lagged estimates are positive and statistically indistinguishable from zero (Panel~B). The index is an annual composite of regulatory posture, not a count of enforcement actions.
>
> Carbon rises while regulated pollutants do not, the pattern a multitask regulator produces. For most of the sample, local environmental bureaus were accountable for conventional pollutants but not for CO$_2$, so enforcement could hold regulated discharges down while the carbon from expanded production went unchecked. The contrast runs across data sets: estimated on a common city-year sample, the CO$_2$ and regulated-pollutant responses are not statistically different (\Cref{tab: app_asymmetry}). \Cref{sec:policy_leakage_measurement} quantifies realized and counterfactual carbon leakage.
