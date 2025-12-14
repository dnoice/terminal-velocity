<!--
✒ Metadata
    - Title: Contribution Guidelines (Terminal Velocity - v1.0)
    - File Name: CONTRIBUTING.md
    - Relative Path: CONTRIBUTING.md
    - Artifact Type: docs
    - Version: 1.0.0
    - Date: 2025-12-14
    - Update: Sunday, December 14, 2025
    - Author: Dennis 'dnoice' Smaltz
    - A.I. Acknowledgement: Anthropic - Claude Opus 4.5
    - Signature:  ︻デ═—··· 🎯 = Aim Twice, Shoot Once!

✒ Description:
    Guidelines for contributing to the Terminal Velocity research framework.
    Covers mechanism proposals, evidence standards, code contributions, and
    the review process. Maintains the forensic integrity of the project.
---------
-->

# Contributing to Terminal Velocity

> *"We are coroners, not commentators. Every contribution must meet autopsy standards."*

---

## Table of Contents

1. [Philosophy](#philosophy)
2. [What We Accept](#what-we-accept)
3. [What We Don't Accept](#what-we-dont-accept)
4. [Contribution Types](#contribution-types)
5. [Process](#process)
6. [Quality Standards](#quality-standards)
7. [Review Criteria](#review-criteria)

---

## Philosophy

This is a forensic research project. We document mechanisms of destruction with clinical precision. Contributions must:

- **Be evidence-based** — Claims require sources. No exceptions.
- **Be specific** — "Pollution is bad" is commentary. "Facility X released Y kg of Z in year W" is evidence.
- **Be reproducible** — If you ran code, others must be able to run it and get the same results.
- **Name names** — Where public record supports it, identify specific actors, not just "industry."
- **Acknowledge uncertainty** — "We don't know" is a valid finding.

We are building a permanent record. Act accordingly.

---

## What We Accept

✅ **New mechanism dossiers** — Well-researched additions to the inventory  
✅ **Evidence upgrades** — Better data, newer sources, higher-grade evidence  
✅ **Computational contributions** — Analysis notebooks, data pipelines, visualizations  
✅ **Corrections** — Factual errors, outdated information, broken links  
✅ **Connection mapping** — Documented links between mechanisms  
✅ **Tooling improvements** — Enhancements to the scaffold and utilities  
✅ **Documentation** — Clarifications, examples, translations  

---

## What We Don't Accept

❌ **Commentary without evidence** — Opinions don't belong in dossiers  
❌ **Unverifiable claims** — If we can't check it, we can't publish it  
❌ **Advocacy framing** — We document, we don't campaign  
❌ **Hand-edited data** — All transformations must be scripted  
❌ **Grade VI evidence as proof** — Commentary provides context only  
❌ **Accusations without public record** — Legal exposure is real  
❌ **AI-generated content without verification** — LLMs hallucinate; verify everything  

---

## Contribution Types

### 1. Mechanism Proposals

Want to add a new mechanism to the inventory?

**Requirements:**
- Mechanism must represent a distinct, documentable pattern of human-caused damage
- At least one Grade I-II source must exist for damage quantification
- Mechanism must not substantially overlap with existing dossiers
- Must fit within an existing damage vector (A-F) or propose a new vector with justification

**Process:**
1. Open an issue using the "Mechanism Proposal" template
2. Include: proposed code, name, vector, preliminary sources, damage summary
3. Wait for triage and assignment
4. If approved, create dossier using `tv_scaffold.py` or manually following structure
5. Submit PR when ready for review

### 2. Evidence Contributions

Upgrading or adding evidence to existing dossiers.

**Requirements:**
- New evidence must be higher grade or more current than existing
- Sources must be verifiable (DOIs preferred, URLs archived)
- Claim-to-source mapping must be explicit

**Process:**
1. Fork and branch from `main`
2. Update relevant files in the dossier
3. Update `claim_trace.md` with new mappings
4. Submit PR with clear description of what evidence was added/upgraded

### 3. Computational Contributions

Notebooks, scripts, analysis pipelines.

**Requirements:**
- Must run end-to-end from pinned environment
- Must produce documented outputs
- Must not require proprietary software or paid APIs
- Must follow project code style

**Process:**
1. Test locally with clean environment
2. Document all dependencies in `environment.yml`
3. Include sample output or screenshot
4. Submit PR with reproduction instructions

### 4. Tooling & Infrastructure

Improvements to `tv_scaffold.py` or shared utilities.

**Requirements:**
- Maintain backward compatibility or document breaking changes
- Include tests for new functionality
- Update documentation to match

---

## Process

### For All Contributions

```
1. FORK         → Create your own copy
2. BRANCH       → Create a feature branch (mechanism/A-XX-name or fix/description)
3. WORK         → Make your changes locally
4. TEST         → Verify everything runs/renders
5. COMMIT       → Clear, descriptive commit messages
6. PR           → Submit pull request against main
7. REVIEW       → Address feedback
8. MERGE        → Maintainer merges when approved
```

### Branch Naming

```
mechanism/A-11-new-mechanism-name
evidence/B-03-updated-sources
fix/broken-notebook-link
tooling/scaffold-new-feature
docs/quickstart-improvements
```

### Commit Messages

```
[MECHANISM] Add A-11 Industrial Agriculture Ammonia

- Create full dossier structure
- Include 3 Grade II sources for damage quantification
- Notebooks run end-to-end
- Connected to A-08 (N2O) and C-05 (dead zones)
```

---

## Quality Standards

### For Dossiers

| Requirement | Standard |
|-------------|----------|
| Executive Summary | 3-5 sentences, no placeholders |
| Damage Quantification | Grade I-II evidence minimum |
| Causal Chain | Step-by-step, specific |
| Named Actors | Public record only |
| Uncertainty Register | Complete, honest |
| Notebooks | Run end-to-end, documented |
| Bibliography | BibTeX format, DOIs where available |
| Claim Trace | Every factual claim mapped to source |

### For Code

| Requirement | Standard |
|-------------|----------|
| Environment | Pinned versions in `environment.yml` |
| Execution | Runs without intervention |
| Output | All outputs documented |
| Style | Black formatting, type hints preferred |
| Comments | Explain *why*, not just *what* |

### For Documentation

| Requirement | Standard |
|-------------|----------|
| Voice | Clinical, specific, no hedging |
| Format | Markdown, proper heading hierarchy |
| Links | Relative paths within repo |
| Examples | Concrete, realistic |

---

## Review Criteria

PRs are evaluated on:

1. **Evidence Quality** — Are sources verifiable and appropriately graded?
2. **Specificity** — Are claims concrete and quantified?
3. **Reproducibility** — Can we run the code and get the same results?
4. **Completeness** — Are all required sections present and populated?
5. **Accuracy** — Is the information factually correct?
6. **Voice** — Does it match the project's forensic tone?
7. **Connections** — Are links to other mechanisms documented?

### Red Lines (Automatic Rejection)

- ❌ Damage claims without Grade I-II evidence
- ❌ Undocumented code
- ❌ Broken computational pipelines
- ❌ Accusations without public record support
- ❌ Placeholder text in submitted dossiers
- ❌ AI-generated content presented as original research

---

## Recognition

Contributors are credited in:

- `meta/contributors.md` — Project-level acknowledgment
- Individual dossier metadata — "Contributors" field
- Release notes — For significant contributions

---

## Questions?

Open an issue with the "Question" label. We don't bite.

---

**Filed under: Causes of Death, Preventable**

*︻デ═—··· 🎯 = Aim Twice, Shoot Once!*
