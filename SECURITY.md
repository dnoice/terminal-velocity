<!--
✒ Metadata
    - Title: Security Policy (Terminal Velocity - v1.0)
    - File Name: SECURITY.md
    - Relative Path: SECURITY.md
    - Artifact Type: docs
    - Version: 1.0.0
    - Date: 2025-12-14
    - Update: Sunday, December 14, 2025
    - Author: Dennis 'dnoice' Smaltz
    - A.I. Acknowledgement: Anthropic - Claude Opus 4.5
    - Signature:  ︻デ═—··· 🎯 = Aim Twice, Shoot Once!

✒ Description:
    Security policy for Terminal Velocity. Covers supported versions,
    vulnerability reporting, and responsible disclosure procedures.
---------
-->

# Security Policy

## Scope

Terminal Velocity is primarily a research framework and documentation project. Security concerns are most likely to relate to:

1. **Tooling vulnerabilities** — Issues in `tv_scaffold.py` or utility scripts
2. **Dependency vulnerabilities** — Known CVEs in project dependencies
3. **Data integrity** — Compromised or malicious content in dossiers
4. **Access control** — Repository permission issues

---

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | ✅ Yes             |
| < 1.0   | ❌ No              |

Only the latest minor version receives security updates.

---

## Reporting a Vulnerability

### For Code/Tooling Issues

If you discover a security vulnerability in the codebase:

1. **Do NOT** open a public issue
2. **Do NOT** disclose publicly until resolved
3. **DO** email: [security contact - to be added]
4. **DO** include:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if any)

### Expected Response

- **Acknowledgment:** Within 48 hours
- **Initial assessment:** Within 7 days
- **Resolution timeline:** Communicated after assessment
- **Credit:** Security researchers credited in release notes (unless anonymity requested)

---

## For Data/Content Issues

If you identify potentially malicious, falsified, or compromised research content:

1. Open an issue with the "data-integrity" label
2. Specify which dossier/file is affected
3. Explain the concern

Content integrity issues are not embargoed—transparency serves the project's mission.

---

## Dependencies

We monitor dependencies for known vulnerabilities using:

- GitHub Dependabot
- Manual review of critical packages

Report dependency concerns via standard issue templates.

---

## Responsible Disclosure

We follow responsible disclosure principles:

1. Researchers report privately
2. We confirm and assess
3. We develop and test fixes
4. We release patches
5. We disclose publicly after patch is available
6. We credit researchers

We will not pursue legal action against security researchers acting in good faith.

---

## Out of Scope

The following are **not** security vulnerabilities:

- Factual errors in research content (use evidence update process)
- Disagreements about methodology (open discussion issue)
- Feature requests (use standard issue templates)
- Support questions (use question label)

---

**Filed under: Causes of Death, Preventable**

*︻デ═—··· 🎯 = Aim Twice, Shoot Once!*
