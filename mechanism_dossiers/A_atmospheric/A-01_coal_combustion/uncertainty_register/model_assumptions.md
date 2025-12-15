<!--
Metadata
    - Title: Model Assumptions (Terminal Velocity - v1.0)
    - File Name: model_assumptions.md
    - Relative Path: mechanism_dossiers/A_atmospheric/A-01_coal_combustion/uncertainty_register/model_assumptions.md
    - Artifact Type: docs
    - Version: 1.0.0
    - Date: 2025-12-14
    - Update: Sunday, December 14, 2025
    - Author: Dennis 'dnoice' Smaltz
    - A.I. Acknowledgement: Anthropic - Claude Opus 4.5
    - Signature:  ︻デ═—··· 🎯 = Aim Twice, Shoot Once!

Description:
    Documentation of key assumptions underlying coal combustion chain estimates.
    Makes explicit where analysis relies on estimates, models, or methodological
    choices that could be made differently.

Key Features:
    - Feature 1: Assumption inventory
    - Feature 2: Assumption justification
    - Feature 3: Sensitivity to assumption changes
    - Feature 4: Alternative assumption documentation
    - Feature 5: Transparency for reproducibility
---------
-->

# Model Assumptions: A-01 - Coal Combustion Chain

## Executive Summary

Every quantitative analysis involves assumptions. This document makes explicit the key assumptions underlying our coal combustion impact estimates, provides justification for our choices, and documents how conclusions would change under alternative assumptions. Transparency about assumptions enables scrutiny and builds credibility.

---

## 1. Emissions Assumptions

### 1.1 CO2 Emission Factors

| Assumption | Our Value | Range in Literature | Justification |
|------------|-----------|---------------------|---------------|
| Anthracite EF | 98.3 kg CO2/GJ | 96-100 | IPCC default |
| Bituminous EF | 94.6 kg CO2/GJ | 90-97 | IPCC default |
| Sub-bituminous EF | 96.1 kg CO2/GJ | 93-98 | IPCC default |
| Lignite EF | 101 kg CO2/GJ | 98-105 | IPCC default |
| Average blend | ~2.4 kg CO2/kg coal | 2.2-2.6 | Weighted by production |

**Sensitivity:** ±10% variation changes global emissions by ±1.5 Gt CO2

### 1.2 Complete Combustion

| Assumption | Our Approach | Alternative | Impact |
|------------|--------------|-------------|--------|
| Combustion efficiency | 98% assumed | Actual varies 95-99% | Minor (<5%) |
| Unburnt carbon | Included in ash | Could be separate | Minor |
| Methane slip | Not included | Could add 1-2% | Minor undercount |

### 1.3 Methane Emissions

| Assumption | Our Value | Range | Justification |
|------------|-----------|-------|---------------|
| Global coal methane | 600 Mt CO2e | 400-800 | EPA Global Methane |
| GWP for CH4 | 28 (100-year) | 80+ (20-year) | IPCC AR5 |

**Sensitivity:** Using 20-year GWP would roughly triple methane's contribution

---

## 2. Health Impact Assumptions

### 2.1 Exposure-Response Relationships

| Assumption | Our Approach | Alternative | Impact |
|------------|--------------|-------------|--------|
| PM2.5 mortality shape | Log-linear | Linear, supra-linear | Moderate at low concentrations |
| No threshold | Harm at all levels | Threshold at 5-10 μg/m³ | Would reduce estimates |
| GEMM function | Used for mortality | ACS CPS-II, GBD | Moderate variation |

**Key Sources:**
- Global Exposure Mortality Model (GEMM)
- American Cancer Society studies
- Global Burden of Disease (GBD) methodology

### 2.2 Relative Risk Values

| Outcome | Our RR per 10 μg/m³ PM2.5 | Range | Source |
|---------|--------------------------|-------|--------|
| All-cause mortality | 1.08 | 1.04-1.12 | Meta-analyses |
| Cardiovascular | 1.11 | 1.06-1.16 | ACS studies |
| Respiratory | 1.06 | 1.02-1.10 | Multiple studies |
| Lung cancer | 1.09 | 1.04-1.14 | IARC, ACS |

### 2.3 Population Exposure

| Assumption | Our Approach | Alternative | Impact |
|------------|--------------|-------------|--------|
| Exposure assessment | Satellite + model | Monitoring only | Coverage vs. accuracy |
| Indoor exposure | Included for coal heating | Excluded | Significant in China, India |
| Background attribution | Excess above counterfactual | Total observed | Changes baseline |

### 2.4 Coal Attribution Fraction

| Assumption | Our Value | Range | Justification |
|------------|-----------|-------|---------------|
| Power plant contribution to PM2.5 | 15-25% (varies by region) | 10-40% | Source apportionment |
| Secondary formation | Included | Could exclude | Physical reality |
| Long-range transport | Included | Local only | Observed transport |

**Sensitivity:** Attribution fraction is major uncertainty; ±50% changes death estimates proportionally

---

## 3. Economic Valuation Assumptions

### 3.1 Value of Statistical Life (VSL)

| Assumption | Our Approach | Alternatives | Impact |
|------------|--------------|--------------|--------|
| US VSL | $10 million | $5-15 million | Large |
| Global transfer | GDP-adjusted | Equal VSL | Very large |
| Income elasticity | 1.0 | 0.4-1.5 | Moderate |

**Sensitivity:** VSL choice can change total cost estimates by factor of 2-3

### 3.2 Social Cost of Carbon

| Assumption | Our Approach | Alternatives | Impact |
|------------|--------------|--------------|--------|
| Central estimate | $80/tonne | $50-400+ | Large |
| Discount rate | 2.5% | 1-5% | Very large |
| Damage function | DICE/FUND/PAGE | Varied | Moderate |
| Equity weighting | No | Yes increases SCC | Moderate |

**Sensitivity:** SCC range spans nearly order of magnitude

### 3.3 Discount Rate

| Assumption | Our Approach | Justification | Alternative |
|------------|--------------|---------------|-------------|
| Climate damages | 2.5% | Stern-like, intergenerational | 3-5% (market rates) |
| Near-term health | 3% | Standard health economics | 0-5% |
| Investment analysis | 5-7% | Market returns | Social rate lower |

### 3.4 Subsidy Calculation

| Assumption | Our Approach | Alternative | Impact |
|------------|--------------|-------------|--------|
| Include implicit subsidies | Yes (IMF approach) | Explicit only | Very large (~$6T difference) |
| Externality valuation | SCC + health costs | Market prices only | Very large |
| Counterfactual price | Efficient price | Current alternatives | Moderate |

---

## 4. Scenario Assumptions

### 4.1 Baseline Projections

| Assumption | Our Approach | Range | Source |
|------------|--------------|-------|--------|
| Global coal trajectory | IEA STEPS | Varies by scenario | IEA WEO 2024 |
| Regional breakdown | IEA estimates | Alternative models | Model variation |
| No additional policy | Stated policies only | Could include announced | Conservative |

### 4.2 Phase-Out Scenarios

| Assumption | Our Approach | Alternative | Impact |
|------------|--------------|-------------|--------|
| Net Zero timing | 2050 | 2040-2070 | Timeline shifts |
| Regional differentiation | OECD earlier | Uniform | Equity implications |
| Technology availability | Current + learning | Breakthrough | Pace changes |

---

## 5. Attribution Assumptions

### 5.1 Causal Attribution

| Assumption | Our Approach | Alternative | Justification |
|------------|--------------|-------------|---------------|
| Emissions → warming | Linear relationship | Log relationship | Conservative |
| Coal share of forcing | Proportional to emissions | Include aerosol offset | Complex, partially offset |
| Historical responsibility | Cumulative emissions | Current emissions | Both relevant |

### 5.2 Company Attribution

| Assumption | Our Approach | Alternative | Impact |
|------------|--------------|-------------|--------|
| Scope 3 inclusion | Yes (use phase) | Scope 1+2 only | Large difference |
| Attribution methodology | Carbon Majors | Alternative allocation | Some variation |

---

## 6. Methodological Choices

### 6.1 Aggregation

| Choice | Our Approach | Alternative | Trade-off |
|--------|--------------|-------------|-----------|
| Geographic scale | Global totals | Regional breakdown | Detail vs. comparability |
| Temporal scale | Annual | Cumulative | Different insights |
| Units | Mass (Mt, Gt) | Energy (EJ) | Consistency |

### 6.2 Data Sources

| Data Type | Primary Source | Backup Source | Why |
|-----------|---------------|---------------|-----|
| Production | IEA | BP | Coverage, consistency |
| Emissions | EDGAR | National inventories | Global coverage |
| Health | GBD | IHME | Peer-reviewed methodology |
| Economics | IMF, World Bank | Academic literature | Authority |

### 6.3 Time Periods

| Analysis | Period | Justification |
|----------|--------|---------------|
| Current state | 2023-2024 | Most recent data |
| Historical trends | 2000-2024 | Modern energy era |
| Cumulative | 1750-present | Full attribution |
| Projections | 2024-2050 | Standard planning horizon |

---

## 7. Assumption Sensitivity Summary

### 7.1 High-Sensitivity Assumptions

| Assumption | If Changed | Impact on Conclusions |
|------------|------------|----------------------|
| Social cost of carbon | ±100% | Economic cost estimates change proportionally |
| Value of statistical life | ±50% | Health cost estimates change proportionally |
| PM2.5 coal attribution | ±50% | Mortality estimates change proportionally |
| Discount rate | ±2% | Future damage valuations change significantly |

### 7.2 Low-Sensitivity Assumptions

| Assumption | If Changed | Impact on Conclusions |
|------------|------------|----------------------|
| Emission factors | ±10% | Minor change in totals |
| Combustion efficiency | ±3% | Negligible |
| Exact health RR | ±20% | Moderate, doesn't change conclusions |
| Data source choice | Varies | Generally small differences |

---

## 8. Assumption Transparency Summary

### 8.1 Assumptions Made Explicit

| Category | Number of Key Assumptions | Documented |
|----------|--------------------------|------------|
| Emissions | 6 | Yes |
| Health | 8 | Yes |
| Economics | 7 | Yes |
| Scenarios | 4 | Yes |
| Attribution | 4 | Yes |
| Methods | 6 | Yes |

### 8.2 Assumptions Favoring Conservative Estimates

| Assumption | Direction | Rationale |
|------------|-----------|-----------|
| Moderate SCC ($80/t) | Conservative | Literature range goes much higher |
| IPCC emission factors | Conservative | Country-specific may be higher |
| Published health RRs | Conservative | Meta-analyses tend to underestimate |
| Exclude ecosystem services | Conservative | Hard to monetize, very large |

---

**Filed under: Causes of Death, Preventable**

*︻デ═—··· 🎯 = Aim Twice, Shoot Once!*
