<!--
Metadata
    - Title: Physical Flows (Terminal Velocity - v1.0)
    - File Name: physical_flows.md
    - Relative Path: mechanism_dossiers/A_atmospheric/A-01_coal_combustion/pathway_analysis/physical_flows.md
    - Artifact Type: docs
    - Version: 1.0.0
    - Date: 2025-12-14
    - Update: Sunday, December 14, 2025
    - Author: Dennis 'dnoice' Smaltz
    - A.I. Acknowledgement: Anthropic - Claude Opus 4.5
    - Signature:  ︻デ═—··· 🎯 = Aim Twice, Shoot Once!

Description:
    Material and energy accounting for the coal combustion chain. Quantifies
    mass flows, energy conversions, waste streams, and atmospheric loading
    from extraction through combustion.

Key Features:
    - Feature 1: Mass balance accounting
    - Feature 2: Energy flow analysis
    - Feature 3: Waste stream quantification
    - Feature 4: Atmospheric loading rates
    - Feature 5: Resource depletion tracking
---------
-->

# Physical Flows: A-01 - Coal Combustion Chain

## Executive Summary

Coal combustion represents one of humanity's largest material flows, moving 8.8 billion tonnes annually from geological deposits to atmospheric and waste sinks. For every tonne of coal burned, approximately 2.4 tonnes of CO2 enters the atmosphere, along with kilograms of particulates, sulfur, nitrogen oxides, and trace toxics.

---

## 1. Global Mass Balance (2024)

### 1.1 Annual Material Flow Summary

```text
INPUTS                              OUTPUTS
────────────────────────────────────────────────────────────
Coal Extraction: 8,800 Mt    ──►    CO2:        15,500 Mt
Mining Overburden: 25,000 Mt ──►    Fly Ash:       450 Mt
Water (mining): 5,000 GL     ──►    Bottom Ash:    150 Mt
Water (power): 200,000 GL    ──►    FGD Waste:     100 Mt
Limestone (FGD): 50 Mt       ──►    SO2:            35 Mt
Air (O2): 18,000 Mt          ──►    NOx:            25 Mt
Auxiliary fuels: 50 Mt       ──►    PM:             10 Mt
                             ──►    Mercury:        50 t
                             ──►    Wastewater: 180,000 GL
                             ──►    Methane:       600 Mt CO2e
```

### 1.2 Mass Conversion Factors

| Input | Output | Conversion Factor |
|-------|--------|-------------------|
| 1 kg coal | CO2 | 2.4 kg |
| 1 kg coal | Ash (total) | 0.10-0.15 kg |
| 1 kg coal | SO2 (uncontrolled) | 0.02-0.04 kg |
| 1 kg coal | NOx | 0.003-0.006 kg |
| 1 kg coal | PM (uncontrolled) | 0.05-0.15 kg |
| 1 kg coal | Mercury | 0.1-0.3 mg |

---

## 2. Extraction Phase Flows

### 2.1 Mining Material Balance

| Flow | Quantity (Annual) | Notes |
|------|-------------------|-------|
| **Coal extracted** | 8,800 Mt | Gross production |
| Overburden removed | 25,000 Mt | 3:1 ratio average |
| Mine water pumped | 50,000 GL | Groundwater intrusion |
| Methane released | 600 Mt CO2e | Coal seam methane |
| Coal fines lost | 200 Mt | Processing waste |

### 2.2 Energy Input for Extraction

| Activity | Energy Use | Primary Source |
|----------|------------|----------------|
| Mining operations | 200 TWh/year | Electricity, diesel |
| Processing | 50 TWh/year | Electricity |
| Ventilation | 30 TWh/year | Electricity |
| Water pumping | 20 TWh/year | Electricity |
| **Total extraction energy** | **300 TWh/year** | ~3% of coal energy content |

---

## 3. Transportation Phase Flows

### 3.1 Transport Modes and Volumes

| Mode | Volume (Mt/year) | Distance (avg) | Fuel Consumption |
|------|------------------|----------------|------------------|
| Rail | 4,500 | 500 km | 150 ML diesel |
| Ship (seaborne) | 1,500 | 8,000 km | 50 ML bunker fuel |
| Barge (inland) | 500 | 200 km | 20 ML diesel |
| Truck | 300 | 100 km | 30 ML diesel |
| Conveyor/pipeline | 2,000 | 50 km | 100 TWh electricity |

### 3.2 Transport Emissions

| Emission | Quantity (Annual) |
|----------|-------------------|
| CO2 from transport | 150 Mt |
| Coal dust losses | 50 Mt |
| Transport share of chain | ~1% of total emissions |

---

## 4. Combustion Phase Flows

### 4.1 Power Plant Mass Balance (Per 1,000 MW Plant)

```text
INPUTS (per hour)                   OUTPUTS (per hour)
────────────────────────────────────────────────────────────
Coal:           400 tonnes    ──►   Electricity:    1,000 MWh
Air:            4,000 tonnes  ──►   Flue Gas:       4,400 tonnes
Water:          100,000 m³    ──►   CO2:            960 tonnes
Limestone:      20 tonnes     ──►   H2O vapor:      200 tonnes
                              ──►   Fly Ash:        40 tonnes
                              ──►   Bottom Ash:     15 tonnes
                              ──►   FGD Gypsum:     35 tonnes
                              ──►   Wastewater:     90,000 m³
```

### 4.2 Global Power Sector Combustion

| Metric | Value (2024) |
|--------|--------------|
| Coal burned for power | 6,500 Mt |
| Electricity generated | 10,000 TWh |
| Efficiency (average) | 33% |
| Heat rejected | 67% (as waste heat) |
| Cooling water used | 200,000 GL |

### 4.3 Flue Gas Composition (Uncontrolled)

| Component | Concentration | Mass Flow (Global) |
|-----------|---------------|-------------------|
| N2 | 75% | ~12,000 Mt/year |
| CO2 | 15% | 15,500 Mt/year |
| H2O | 8% | ~1,300 Mt/year |
| O2 | 2% | ~300 Mt/year |
| SO2 | 2,000 ppm | 100 Mt (before control) |
| NOx | 500 ppm | 50 Mt (before control) |
| PM | 10,000 mg/m³ | 200 Mt (before control) |

---

## 5. Atmospheric Loading Rates

### 5.1 Emissions After Control

| Pollutant | Uncontrolled | After Control | Control Rate |
|-----------|--------------|---------------|--------------|
| CO2 | 15,500 Mt | 15,500 Mt | 0% (no CCS deployed) |
| SO2 | 100 Mt | 35 Mt | 65% average |
| NOx | 50 Mt | 25 Mt | 50% average |
| PM2.5 | 200 Mt | 10 Mt | 95% average |
| Mercury | 150 t | 50 t | 67% average |

### 5.2 Atmospheric Residence and Fate

| Pollutant | Atmospheric Lifetime | Primary Removal |
|-----------|---------------------|-----------------|
| CO2 | Centuries | Ocean uptake, vegetation |
| SO2 | Days | Oxidation to sulfate, deposition |
| NOx | Hours-days | Oxidation, deposition |
| PM2.5 | Days-weeks | Settling, washout |
| Mercury | 6-12 months | Deposition, methylation |

### 5.3 Cumulative Atmospheric Loading

| Timeframe | CO2 Added (from coal) | Atmospheric Increase |
|-----------|----------------------|---------------------|
| Since 1750 | ~900 Gt | ~100 ppm |
| Since 2000 | ~300 Gt | ~40 ppm |
| Annual (2024) | 15.5 Gt | ~2 ppm |

---

## 6. Waste Stream Quantification

### 6.1 Solid Waste Generation

| Waste Type | Global Quantity | Primary Constituents |
|------------|-----------------|---------------------|
| Fly ash | 450 Mt/year | SiO2, Al2O3, Fe2O3, CaO |
| Bottom ash | 150 Mt/year | Same as fly ash, coarser |
| FGD sludge/gypsum | 100 Mt/year | CaSO4, CaSO3 |
| Coal refuse | 200 Mt/year | Rock, clay, pyrite |
| **Total solid waste** | **900 Mt/year** | |

### 6.2 Toxic Constituents in Ash

| Element | Concentration (ppm) | Annual Global Load (tonnes) |
|---------|--------------------|-----------------------------|
| Arsenic | 50-200 | 30,000-120,000 |
| Selenium | 5-20 | 3,000-12,000 |
| Lead | 50-200 | 30,000-120,000 |
| Cadmium | 1-10 | 600-6,000 |
| Mercury | 0.1-1 | 60-600 |
| Uranium | 10-50 | 6,000-30,000 |
| Thorium | 20-50 | 12,000-30,000 |

### 6.3 Ash Disposal Pathways

| Pathway | Percentage | Volume (Mt/year) |
|---------|------------|------------------|
| Landfill | 40% | 240 |
| Surface impoundments | 25% | 150 |
| Beneficial use (cement, roads) | 30% | 180 |
| Abandoned/unmanaged | 5% | 30 |

---

## 7. Water Flows

### 7.1 Water Consumption by Stage

| Stage | Consumption (GL/year) | Primary Use |
|-------|----------------------|-------------|
| Mining | 5,000 | Dust suppression, processing |
| Washing | 2,000 | Coal preparation |
| Cooling (evaporative) | 180,000 | Power plant cooling |
| FGD systems | 10,000 | Scrubber operation |
| Ash handling | 5,000 | Sluicing, dust control |
| **Total** | **~200,000 GL/year** | |

### 7.2 Water Quality Impacts

| Discharge Type | Volume | Key Contaminants |
|----------------|--------|------------------|
| Acid mine drainage | 10,000 GL | Fe, Al, Mn, sulfate, low pH |
| Cooling water blowdown | 20,000 GL | Thermal, biocides, metals |
| Ash pond seepage | Unknown | Heavy metals, sulfate |
| FGD wastewater | 5,000 GL | Selenium, mercury, chloride |

---

## 8. Energy Flow Analysis

### 8.1 Energy Balance (Global Coal Power)

| Energy Flow | Quantity | Share |
|-------------|----------|-------|
| Coal chemical energy input | 180 EJ | 100% |
| Electricity output | 36 EJ (10,000 TWh) | 20% |
| Stack losses (flue gas) | 30 EJ | 17% |
| Condenser losses (waste heat) | 100 EJ | 55% |
| Auxiliary consumption | 10 EJ | 6% |
| Other losses | 4 EJ | 2% |

### 8.2 Efficiency by Technology

| Technology | Efficiency | CO2 Intensity |
|------------|------------|---------------|
| Subcritical (old) | 33% | 1,000 g/kWh |
| Subcritical (new) | 38% | 880 g/kWh |
| Supercritical | 42% | 800 g/kWh |
| Ultra-supercritical | 46% | 730 g/kWh |
| IGCC | 42% | 800 g/kWh |
| IGCC + CCS | 32% net | 100-200 g/kWh |

### 8.3 Energy Return on Energy Invested (EROEI)

| System Boundary | EROEI |
|-----------------|-------|
| Coal at mine mouth | 40-80:1 |
| Coal power (mine to grid) | 10-30:1 |
| Coal power + pollution control | 8-25:1 |
| Coal + CCS (hypothetical) | 5-15:1 |

---

## 9. Resource Depletion

### 9.1 Reserve Status

| Category | Quantity | Years at Current Rate |
|----------|----------|----------------------|
| Proven reserves | 1,074 Bt | 120 years |
| Economically recoverable | 500 Bt | 55 years |
| High-quality coking coal | 150 Bt | 100 years |

### 9.2 Quality Degradation Trend

| Metric | 1990 | 2024 | Trend |
|--------|------|------|-------|
| Average energy content | 25 MJ/kg | 22 MJ/kg | Declining |
| Average ash content | 10% | 15% | Increasing |
| Average sulfur | 1.5% | 1.8% | Increasing |
| Mining depth | 200m avg | 400m avg | Deepening |

---

## 10. Key Physical Flow Statistics

| Metric | Value |
|--------|-------|
| Coal extracted annually | 8,800 Mt |
| CO2 emitted annually | 15,500 Mt |
| Mass amplification (coal → CO2) | 1.76x |
| Solid waste generated | 900 Mt/year |
| Water consumed | 200,000 GL/year |
| Average power plant efficiency | 33% |
| Waste heat rejected | 100+ EJ/year |

---

**Filed under: Causes of Death, Preventable**

*︻デ═—··· 🎯 = Aim Twice, Shoot Once!*
