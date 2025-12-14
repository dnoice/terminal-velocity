<!--
✒ Metadata
    - Title: Evidence Grading System (Terminal Velocity - v1.0)
    - File Name: EVIDENCE_GRADING.md
    - Relative Path: docs/EVIDENCE_GRADING.md
    - Artifact Type: docs
    - Version: 1.0.0
    - Date: 2025-12-14
    - Update: Sunday, December 14, 2025
    - Author: Dennis 'dnoice' Smaltz
    - A.I. Acknowledgement: Anthropic - Claude Opus 4.5
    - Signature:  ︻デ═—··· 🎯 = Aim Twice, Shoot Once!

✒ Description:
    Comprehensive guide to the Terminal Velocity evidence grading system.
    Adapted from clinical medicine's evidence hierarchy for sustainability
    research. Includes decision trees, examples, and quality assessment criteria.
---------
-->

# Evidence Grading System

> *"If we can't verify it, we can't publish it."*

---

## Overview

Terminal Velocity uses a six-tier evidence grading system adapted from clinical medicine. The system exists to:

1. **Distinguish** observation from inference from opinion
2. **Match** claim types to appropriate evidence standards
3. **Communicate** confidence levels to readers
4. **Prevent** unsupported claims from entering the record

This is not gatekeeping—it's quality control. The mechanisms we document have real victims. They deserve evidence, not speculation.

---

## The Six Grades

### Grade I: Direct Measurement

**Definition:** Empirical observations from peer-reviewed monitoring systems, controlled experiments, or validated sensor networks.

**Characteristics:**
- Primary data collection by qualified researchers
- Published in peer-reviewed venues
- Methodology documented and reproducible
- Uncertainty/error quantified
- Raw data often available

**Examples:**
- Satellite observations of deforestation (Hansen et al., Global Forest Watch)
- Air quality monitoring networks (EPA AQS, EEA stations)
- Ocean temperature measurements (Argo floats, NOAA buoys)
- Peer-reviewed field studies measuring species populations
- Controlled experiments on pollutant effects

**Use For:**
- Primary basis for damage quantification
- Establishing baseline conditions
- Measuring change over time

**⚠️ Caution:**
- Single studies can be outliers; look for replication
- Measurement methods evolve; note vintage
- Coverage may be incomplete (geographic, temporal)

---

### Grade II: Official Inventory

**Definition:** Government or multilateral agency accounting, typically compiled from reported data under regulatory frameworks.

**Characteristics:**
- Collected under legal/regulatory mandate
- Standardized methodology (often international)
- Regular update cycle
- Subject to official review processes
- May rely on self-reporting

**Examples:**
- National GHG inventories (UNFCCC submissions)
- FAO agricultural statistics
- World Bank development indicators
- Census data
- EPA Toxics Release Inventory
- IEA energy statistics

**Use For:**
- Baseline metrics and time series
- Cross-country comparisons
- Trend analysis
- Policy evaluation

**⚠️ Caution:**
- Self-reported data may undercount
- Definitions vary by jurisdiction
- Political pressure can affect numbers
- Time lag between collection and publication

---

### Grade III: Validated Model

**Definition:** Peer-reviewed models with documented assumptions, validation against observations, and uncertainty quantification.

**Characteristics:**
- Published methodology
- Assumptions explicitly stated
- Validated against Grade I data
- Sensitivity analysis performed
- Uncertainty ranges provided
- Code often available

**Examples:**
- IPCC climate projections
- Integrated assessment models (IMAGE, GCAM)
- Ecosystem models (InVEST, GLOBIO)
- Epidemiological exposure models
- Economic input-output models

**Use For:**
- Projections and scenarios
- Attribution analysis
- Counterfactuals
- System dynamics understanding

**⚠️ Caution:**
- "All models are wrong, some are useful"
- Assumptions drive results; scrutinize them
- Validation ≠ prediction accuracy
- Ensemble spread indicates uncertainty, not error

---

### Grade IV: Expert Assessment

**Definition:** Consensus statements from scientific bodies, systematic reviews, and meta-analyses that synthesize primary literature.

**Characteristics:**
- Produced by recognized scientific institutions
- Formal review/consensus process
- Synthesizes multiple primary sources
- Authored by subject-matter experts
- Regular updates common

**Examples:**
- IPCC Assessment Reports (synthesis chapters)
- National Academy of Sciences consensus studies
- Cochrane-style systematic reviews
- IARC carcinogen classifications
- WHO/UNEP scientific assessments

**Use For:**
- Establishing scientific consensus
- Context and synthesis
- Confidence calibration
- Literature overview

**⚠️ Caution:**
- Consensus can lag cutting-edge research
- Expert judgment ≠ data
- Scope may not match your question exactly
- Read methodology, not just conclusions

---

### Grade V: Qualified Report

**Definition:** Industry reporting under regulatory requirement, investigative journalism with named sources, legal proceedings with evidence standards.

**Characteristics:**
- Some accountability mechanism exists
- Named sources or legal liability
- May have verification but not peer review
- Often more current than academic sources
- Variable quality

**Examples:**
- Corporate sustainability reports (GRI-compliant)
- SEC filings with environmental disclosures
- Investigative journalism (major outlets)
- Court documents and legal findings
- Government audits and inspections

**Use For:**
- Current events and recent developments
- Corporate-specific information
- Named actors and decisions
- Supplementary corroboration

**⚠️ Caution:**
- Corporate reports have obvious incentives
- Journalism varies in rigor
- Legal findings may be narrow
- Cross-reference with other sources

---

### Grade VI: Contextual

**Definition:** Opinion, commentary, advocacy documents, anonymous sources, and unverified claims.

**Characteristics:**
- No formal verification
- May reflect author's perspective
- Often useful for framing/context
- Variable expertise
- Not reproducible

**Examples:**
- Op-eds and commentary
- Advocacy organization reports (without methodology)
- Blog posts
- Anonymous sources
- Social media
- Unverified leaks

**Use For:**
- Background context only
- Understanding framing/debates
- Identifying questions to investigate
- **NEVER as proof of factual claims**

**⚠️ Caution:**
- Must be explicitly labeled as contextual
- Cannot support factual claims in dossiers
- May contain misinformation
- Advocacy ≠ evidence

---

## Usage Rules

### Mandatory Standards

| Claim Type | Minimum Grade | Notes |
|------------|---------------|-------|
| **Damage quantification** | I-II | No exceptions. Numbers need data. |
| **Causal pathway** | I-III | Must include uncertainty. |
| **Driver identification** | II-V | Multiple corroborating sources. |
| **Named actors** | II-V | Public record only. Legal exposure is real. |
| **Intervention assessment** | IV-V | Expert judgment acceptable with flagging. |
| **Context/framing** | Any | Must be labeled as such. |

### Red Lines

These will trigger automatic rejection:

- ❌ Damage claims citing only Grade V-VI sources
- ❌ Grade VI material presented as evidence
- ❌ Missing evidence grade labels
- ❌ Claims without any source
- ❌ "Common knowledge" as justification

---

## Decision Tree

```
Is this claim about specific damage?
├─ YES → Do you have Grade I-II evidence?
│        ├─ YES → ✅ Include with citation
│        └─ NO  → ❌ Do not include OR flag as unquantified
│
└─ NO → Is this claim about causation?
         ├─ YES → Do you have Grade I-III evidence?
         │        ├─ YES → ✅ Include with uncertainty statement
         │        └─ NO  → ❌ Do not include OR state as hypothesis
         │
         └─ NO → Is this about actors/decisions?
                  ├─ YES → Do you have Grade II-V evidence?
                  │        ├─ YES → ✅ Include with source
                  │        └─ NO  → ❌ Do not name without evidence
                  │
                  └─ NO → Is this context/framing?
                           └─ YES → ✅ Include, clearly labeled
```

---

## Claim Traceability Format

Every factual claim in a dossier must appear in `sources/claim_trace.md`:

```markdown
| Claim ID | Claim | Source | Grade | Notes |
|----------|-------|--------|-------|-------|
| DMG-01 | Coal combustion released 14.5 Gt CO2 in 2022 | IEA (2023), doi:10.xxxx | II | Global total, includes lignite |
| PTH-01 | PM2.5 exposure increases mortality risk by 8% per 10 μg/m³ | Pope et al. (2020), doi:10.xxxx | I | Meta-analysis of cohort studies |
| DRV-01 | Peabody Energy lobbied against EPA regulations | OpenSecrets (2023), [url] | V | Based on lobbying disclosures |
```

### Claim ID Format

- `DMG-XX` — Damage claims
- `PTH-XX` — Pathway/causation claims
- `DRV-XX` — Driver/actor claims
- `INT-XX` — Intervention claims
- `CTX-XX` — Context (Grade VI allowed)

---

## Source Quality Assessment

For each source in `sources/source_reliability.md`:

```markdown
## [Source Name]

- **Type:** [Journal / Agency / Report / News / Other]
- **Grade:** [I-VI]
- **Coverage:** [Geographic, temporal, topical scope]
- **Update frequency:** [Annual / Irregular / One-time]
- **Access:** [Open / Paywalled / Registration required]
- **Methodology:** [Published / Partial / Not documented]
- **Known limitations:** [List specific issues]
- **Used for claims:** [List Claim IDs]
```

---

## Handling Conflicts

When sources disagree:

1. **Note the conflict explicitly** in the dossier
2. **Assess potential reasons:**
   - Different definitions/boundaries
   - Different time periods
   - Different methodologies
   - Actual disagreement
3. **Prefer higher-grade sources** when conflict is methodological
4. **Present range** when conflict reflects genuine uncertainty
5. **Do not cherry-pick** the number that serves a narrative

Example language:

> "Estimates of methane leakage rates vary significantly. EPA inventory data (Grade II) suggests 1.4%, while direct measurement studies (Grade I) range from 2.3% to 4.1%. The discrepancy likely reflects underreporting in self-reported data. We use the measured range with explicit uncertainty."

---

## Uncertainty Documentation

Every dossier must include uncertainty documentation:

### In `uncertainty_register/known_unknowns.md`:

- What data doesn't exist?
- What questions can't be answered with current evidence?
- What would change our conclusions if we learned it?

### In `uncertainty_register/measurement_limits.md`:

- What are the error bars on key numbers?
- Where is coverage incomplete?
- What definitions are contested?

### In `uncertainty_register/sensitivity_tests.md`:

- Which parameters most affect conclusions?
- What happens if assumptions are wrong?
- What's the range of plausible outcomes?

---

## Examples by Grade

### Grade I Example

> **Claim:** Global mean surface temperature has increased 1.1°C since pre-industrial.
>
> **Source:** Berkeley Earth Surface Temperature dataset, NASA GISTEMP, HadCRUT5
>
> **Why Grade I:** Direct instrumental measurements, multiple independent datasets, peer-reviewed methodology, uncertainty quantified.

### Grade II Example

> **Claim:** Global CO2 emissions from coal were 14.5 Gt in 2022.
>
> **Source:** IEA Global Energy Review 2023
>
> **Why Grade II:** Compiled from national energy statistics reported under international frameworks, standardized methodology, regular publication.

### Grade III Example

> **Claim:** Without mitigation, global temperature will rise 2.4-4.4°C by 2100.
>
> **Source:** IPCC AR6 WG1, SSP3-7.0 scenario
>
> **Why Grade III:** Climate model projections, validated against observations, explicit assumptions (SSP scenario), uncertainty range provided.

### Grade IV Example

> **Claim:** There is high confidence that human activities have caused approximately 1.0°C of warming.
>
> **Source:** IPCC AR6 Summary for Policymakers
>
> **Why Grade IV:** Expert assessment synthesizing thousands of studies, formal consensus process, confidence language standardized.

### Grade V Example

> **Claim:** Company X spent $2.3M on climate lobbying in 2022.
>
> **Source:** OpenSecrets lobbying database, company SEC filings
>
> **Why Grade V:** Regulatory disclosure requirement, legal liability for false reporting, but not peer-reviewed.

### Grade VI Example

> **Claim:** Industry insiders describe regulatory capture as "standard operating procedure."
>
> **Source:** Anonymous interview in news article
>
> **Why Grade VI:** No verification possible, reflects one perspective, cannot support factual claims. Use only as context.

---

## Final Principle

**When in doubt, leave it out.**

An incomplete dossier with verified claims is infinitely more valuable than a comprehensive dossier with unsupported assertions. We are building a permanent record. Errors compound. Verify everything.

---

**Filed under: Causes of Death, Preventable**

*︻デ═—··· 🎯 = Aim Twice, Shoot Once!*
