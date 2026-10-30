# B2B Lead Quality Scoring Matrix & Spam Submission Filter

> Automatically filter fake phone numbers, personal emails, and junk submissions from your B2B marketing funnels before sending to sales.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Format: CLI_SCRIPT](https://img.shields.io/badge/Format-CLI--SCRIPT-green.svg)](#)
[![Tier: 2](https://img.shields.io/badge/Tier-2-orange.svg)](#)
[![Region: MENA](https://img.shields.io/badge/Region-Egypt%20%7C%20GCC%20%7C%20Saudi-purple.svg)](#)
[![Tests: Passing](https://img.shields.io/badge/Tests-Passing-brightgreen.svg)](#)
[![Owner: mahmoudabdelnaby1](https://img.shields.io/badge/Owner-mahmoudabdelnaby1-blue.svg)](https://github.com/mahmoudabdelnaby1)

---

## 📌 Problem Statement & Target Persona

### Target Persona
**PRO** operating in high-growth e-commerce, digital publishing, and direct-response marketing across Saudi Arabia, UAE, and Egypt.

### Core Problem
Build an open-source B2B lead scoring and spam filtering package: 1) Python scoring script (`lead_scorer.py`) evaluating email domain (blocking free providers), phone number validity (E.164 and sequential number traps), company name length, and job title keywords, 2) Curated JSON list of 4,000+ disposable and free consumer email domains, 3) Marketing-Sales SLA agreement template.

---

## 🛠️ Repository Architecture & Deliverables

This repository provides self-contained, documented implementations and specifications:

- `config/scoring_rules.json`
- `data/disposable_and_free_email_domains.json`
- `examples/b2b_inbound_leads.csv`
- `examples/sample_inbound_leads.csv`
- `LICENSE`
- `README.md`
- `reports/scored_leads.csv`
- `src/lead_scorer.py`
- `templates/mql-sla-framework.md`
- `tests/test_scorer.py`


---

## 🚀 Quick Start & How to Run Locally

### Run Test Suite Locally
```bash
# Ensure no bytecode generation
export PYTHONDONTWRITEBYTECODE=1  # Linux / macOS
$env:PYTHONDONTWRITEBYTECODE="1"  # Windows PowerShell

# Run Python unittest discovery
python -m unittest discover -s tests
```

### Run CLI Script
```bash
python src/lead_scorer.py --help
```

---

## 📊 Sample Input & Output Fixtures

> **Data Disclosure:** Any included sample data is illustrative and may be synthetic; it is not a measured customer result or market benchmark unless a source and collection method are stated alongside it. These files run offline with standard libraries and require no paid third-party API credentials.

```json
{
  "domain": "cro",
  "repository": "b2b-lead-quality-scoring-matrix",
  "status": "READY_FOR_LOCAL_REVIEW",
  "license": "MIT"
}
```

---

## ⚠️ Known Technical & Domain Constraints

- **Disposable Domain Detection:** Flags and down-ranks disposable/temporary email domains (e.g. mailinator, tempmail) in B2B inbound submissions.
- **Free Webmail Deprioritization:** Assigns weighted scoring differentiating free consumer webmail (gmail.com, yahoo.com) from corporate business domains.
- **Form Honeypot & Bot Defense:** Implements zero-friction CSS-hidden honeypots to filter automated spam without annoying legitimate B2B prospects.

---

## 📚 Primary Documentation & Verifiable References

- [HubSpot Research: B2B Lead Scoring & MQL Qualification](https://www.hubspot.com/) - Methodology for scoring explicit fit versus implicit behavioral engagement.
- [Salesforce B2B Marketing Automation Best Practices](https://www.salesforce.com/) - Frameworks for lead qualification and sales pipeline handoff.
- [RFC 5322: Internet Message Format & Domain Validation](https://datatracker.ietf.org/doc/html/rfc5322) - Technical standards for email address syntax and domain verification.

---


## 👤 Maintainer & License

- **Author & Maintainer:** [Mahmoud Abdelnaby](https://github.com/mahmoudabdelnaby1) (`@mahmoudabdelnaby1`)
- **License:** [MIT License](LICENSE) - Open-source, auditable, and freely adaptable for internal enterprise or commercial use.
