<!--
Metadata
    - Title: Measurement Limits (Terminal Velocity - v1.0)
    - File Name: measurement_limits.md
    - Relative Path: mechanism_dossiers/A_atmospheric/A-01_coal_combustion/uncertainty_register/measurement_limits.md
    - Artifact Type: docs
    - Version: 1.0.0
    - Date: 2025-12-14
    - Update: Sunday, December 14, 2025
    - Author: Dennis 'dnoice' Smaltz
    - A.I. Acknowledgement: Anthropic - Claude Opus 4.5
    - Signature:  ︻デ═—··· 🎯 = Aim Twice, Shoot Once!

Description:
    Documentation of data quality issues and measurement limitations in coal
    combustion chain analysis. Identifies systematic biases, coverage gaps,
    and precision limits that affect conclusions.

Key Features:
    - Feature 1: Data quality assessment
    - Feature 2: Measurement uncertainty quantification
    - Feature 3: Coverage gap identification
    - Feature 4: Systematic bias documentation
    - Feature 5: Improvement recommendations
---------
-->

# Measurement Limits: A-01 - Coal Combustion Chain

## Executive Summary

Data on coal combustion and its impacts varies significantly in quality across dimensions. Production and consumption data are generally reliable; emissions measurements have known biases; health attribution involves complex epidemiology; and economic valuations depend on contested methodological choices. Understanding these limits is essential for appropriate confidence levels.

---

## 1. Data Quality Overview

### 1.1 Quality by Data Category

| Data Category | Quality Rating | Key Limitations | Confidence |
|---------------|---------------|-----------------|------------|
| Coal production volumes | High | Minor reporting gaps | 95% |
| Consumption statistics | High | Small-scale use undercounted | 90% |
| CO2 emissions | High | ±5% uncertainty | 90% |
| Criteria pollutant emissions | Medium | Monitoring gaps, estimates | 70-80% |
| Mercury emissions | Medium-Low | Measurement difficult | 60-70% |
| Health outcomes | Medium | Attribution challenges | 70-80% |
| Economic costs | Low-Medium | Methodological variation | 50-70% |
| Political economy | Qualitative | Interpretation varies | Context-dependent |

---

## 2. Production and Consumption Data

### 2.1 Data Sources

| Source | Coverage | Quality | Update Frequency |
|--------|----------|---------|------------------|
| IEA World Energy Balances | Global | High | Annual |
| BP Statistical Review | Global | High | Annual |
| National statistics agencies | Country-specific | Variable | Variable |
| Company reports | Company-level | High (listed companies) | Quarterly/Annual |

### 2.2 Known Limitations

| Limitation | Description | Impact |
|------------|-------------|--------|
| Small-scale production | Artisanal mining undercounted | 5-10% undercount (some regions) |
| Inventory discrepancies | Production ≠ consumption + trade | Reconciliation challenges |
| Quality differentiation | Tonnes vs. energy content | Conversion factors needed |
| Stockpile changes | Not always reported | Annual totals affected |
| Self-consumption | Mine-mouth power not always captured | Coverage gaps |

### 2.3 Measurement Uncertainty

| Metric | Uncertainty Range | Notes |
|--------|------------------|-------|
| Global production | ±3% | Statistical reporting variation |
| Country-level | ±5-10% | Depends on governance |
| Company-level | ±2% | Audited figures more reliable |
| Trade flows | ±5% | Import-export discrepancies |

---

## 3. Emissions Data

### 3.1 CO2 Emissions

| Measurement Approach | Accuracy | Limitations |
|---------------------|----------|-------------|
| Fuel consumption × emission factor | ±5% | Emission factor variation |
| Continuous emissions monitoring (CEMS) | ±2-3% | Not universally deployed |
| Atmospheric measurement + inversion | ±10-20% | Global/regional only |

**Systematic Biases:**
- Emission factors assume complete combustion (reality varies)
- National reporting may understate (political incentives)
- Inventory methods differ across countries

### 3.2 Criteria Pollutants (PM, SO2, NOx)

| Pollutant | Measurement Quality | Key Issues |
|-----------|-------------------|------------|
| SO2 | Medium-High | Well-monitored at large plants |
| NOx | Medium-High | Well-monitored at large plants |
| PM2.5 (primary) | Medium | Emission factors variable |
| PM2.5 (secondary) | Low-Medium | Formation in atmosphere complex |
| PM (fugitive) | Low | Mining/transport hard to measure |

**Coverage Gaps:**
- Many countries lack continuous emissions monitoring
- Small sources (industrial boilers) often estimated
- Fugitive emissions from mining poorly quantified

### 3.3 Mercury Emissions

| Issue | Description | Impact |
|-------|-------------|--------|
| Speciation | Three forms with different fates | Transport modeling affected |
| Control efficiency | Varies with coal type, controls | Estimates uncertain |
| Global background | Natural vs. anthropogenic unclear | Attribution difficult |
| Measurement difficulty | Low concentrations, reactive | Monitoring limited |

---

## 4. Health Outcome Data

### 4.1 Epidemiological Limitations

| Limitation | Description | Impact |
|------------|-------------|--------|
| Confounding | Multiple exposures overlap | Attribution uncertainty |
| Long latency | Effects emerge years after exposure | Difficult to link |
| Ecological fallacy | Group-level ≠ individual risk | Interpretation caution |
| Healthy worker effect | Occupational studies biased | Underestimates harm |
| Publication bias | Positive results more published | May overstate effects |

### 4.2 Exposure Assessment

| Approach | Accuracy | Limitations |
|----------|----------|-------------|
| Personal monitoring | High | Expensive, limited scale |
| Fixed-site monitoring | Medium | Spatial interpolation needed |
| Satellite-derived | Medium-Low | Resolution limits, calibration |
| Modeled exposure | Medium | Depends on model quality |

### 4.3 Mortality Attribution

| Challenge | Description | Typical Approach |
|-----------|-------------|-----------------|
| Multiple causes | Air pollution + other factors | Relative risk models |
| Baseline rates | Vary by population | Age-standardization |
| Exposure-response | Shape uncertain at low levels | Linear or log-linear |
| Lag structure | Acute vs. chronic effects | Multiple lag models |

**Uncertainty Range:**
- PM2.5 mortality estimates: ±30-50% (methodological variation)
- Mercury neurological effects: ±50% (dose-response uncertainty)

---

## 5. Economic Valuation Limits

### 5.1 Valuation Methodology Issues

| Issue | Description | Impact |
|-------|-------------|--------|
| Value of Statistical Life (VSL) | Varies $1M-$10M+ | Major impact on totals |
| Discount rate | 0-7% range in literature | Future damages affected |
| Non-market values | Ecosystems, existence values | Hard to monetize |
| Equity weighting | Whose damage counts equally? | Ethical choice |
| Damage function | Unknown at high temperatures | Tail risk uncertain |

### 5.2 Subsidy Measurement

| Challenge | Description | Impact |
|-----------|-------------|--------|
| Direct vs. implicit | Explicit budget vs. externality | IMF uses both |
| Price counterfactual | What "should" coal cost? | Contested |
| Scope boundaries | Which support counts? | Variable definitions |
| Data availability | Especially developing countries | Coverage gaps |

### 5.3 Stranded Asset Valuation

| Uncertainty | Description | Range |
|-------------|-------------|-------|
| Asset lives | Technical vs. economic | 15-50 years |
| Discount rate | Market vs. social | Affects NPV |
| Future policy | Phase-out timing | Scenario-dependent |
| Alternative use | Repurposing potential | Site-specific |

---

## 6. Coverage Gaps

### 6.1 Geographic Gaps

| Region | Data Quality | Key Gaps |
|--------|-------------|----------|
| China | Improving | Provincial data, small sources |
| India | Medium | State-level, industrial boilers |
| Sub-Saharan Africa | Low | Limited monitoring |
| Central Asia | Low | Legacy Soviet data |
| Southeast Asia | Medium | Rapid change, lag |

### 6.2 Temporal Gaps

| Period | Data Quality | Issues |
|--------|-------------|--------|
| Pre-1900 | Low | Estimates only |
| 1900-1970 | Medium | Historical reconstruction |
| 1970-2000 | Medium-High | IEA coverage |
| 2000-present | High | Good coverage most countries |
| Future projections | Scenario-dependent | Inherent uncertainty |

### 6.3 Sectoral Gaps

| Sector | Coverage | Key Gaps |
|--------|----------|----------|
| Power generation | High | Good monitoring |
| Steel/industry | Medium | Some undercounting |
| Residential heating | Low | Informal use |
| Artisanal mining | Low | Unregulated activity |

---

## 7. Systematic Biases

### 7.1 Known Biases and Direction

| Bias | Direction | Source |
|------|-----------|--------|
| Self-reported emissions | Underestimate | Incentives to underreport |
| National inventories | Variable | Political pressure possible |
| Health studies | Possible overestimate | Publication bias |
| Economic valuation | Underestimate | Non-market values excluded |
| Climate models | Uncertain | Structural uncertainty |

### 7.2 Bias Mitigation

| Strategy | Application |
|----------|-------------|
| Multiple data sources | Cross-validate production, emissions |
| Independent monitoring | Satellite, atmospheric measurement |
| Meta-analysis | Pool health studies |
| Sensitivity analysis | Test valuation assumptions |
| Ensemble models | Climate projections |

---

## 8. Data Quality Improvements Needed

### 8.1 Priority Improvements

| Improvement | Benefit | Feasibility |
|-------------|---------|-------------|
| Universal CEMS | Accurate plant emissions | Medium (cost) |
| Expanded air quality monitoring | Better exposure assessment | High |
| Standardized health attribution | Comparable mortality estimates | Medium |
| Transparent economic methods | Reproducible valuations | High |
| Real-time coal tracking | Improved consumption data | Medium |

### 8.2 Emerging Capabilities

| Technology | Application | Status |
|------------|-------------|--------|
| Satellite CO2 measurement | Verify national inventories | Operational |
| Machine learning | Exposure modeling | Developing |
| Blockchain | Supply chain tracking | Pilot |
| Low-cost sensors | Air quality networks | Expanding |

---

## 9. Implications for Analysis

### 9.1 Confidence Levels by Claim

| Claim | Confidence | Measurement Basis |
|-------|------------|-------------------|
| Coal is major CO2 source | Very High | Multiple measurement approaches agree |
| Coal kills hundreds of thousands annually | High | Epidemiology with acknowledged uncertainty |
| Externalities exceed $1 trillion | High | Conservative estimates still large |
| Specific death counts | Medium | Attribution methodology varies |
| Specific economic costs | Medium | Valuation method-dependent |

### 9.2 Reporting Approach

| Data Type | Reporting Approach |
|-----------|-------------------|
| Production/consumption | Point estimates with source |
| Emissions | Ranges where available |
| Health impacts | Central estimate with uncertainty |
| Economic values | Range reflecting methods |
| Projections | Scenarios, not forecasts |

---

## 10. Key Measurement Statistics

| Metric | Uncertainty |
|--------|-------------|
| Global coal production | ±3% |
| CO2 emissions from coal | ±5% |
| Health mortality attribution | ±30-50% |
| Economic valuation | ±50-100% |
| Climate sensitivity | ±40% (range width) |
| Data coverage (global) | 90%+ major sources |
| Monitoring gaps (developing countries) | Significant |

---

**Filed under: Causes of Death, Preventable**

*︻デ═—··· 🎯 = Aim Twice, Shoot Once!*
