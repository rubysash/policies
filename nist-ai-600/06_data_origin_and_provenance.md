---
title: Data Origin and Provenance
nist_function: Map
priority_phase: Must
last_reviewed: 2025-03-27
status: draft
---

## Outline

## Purpose
- Ensure the traceability, integrity, and quality of training, fine-tuning, and input data used by AI and GenAI systems.
- Identify risks associated with synthetic data, third-party data sources, and lack of consent or lineage transparency.

## Scope
- Applies to all datasets used for training, validating, or operating AI and GenAI systems, including LLMs, NLP tools, and patient-facing GenAI applications.
- Covers internal, vendor-supplied, and publicly sourced data.

## Policy Statement
- All AI/GenAI systems must document data origin, licensing, and intended use.
- Synthetic, third-party, or externally trained models must include provenance declarations and known limitations.

## Data Categories

### 1. Training Data
- Source origin, licensing, and purpose
- Inclusion/exclusion of PHI/PII
- Synthetic vs. real-world representation

### 2. Fine-Tuning Data
- Local adaptation for hospital-specific workflows
- Transparency around prompt-data pairing

### 3. Input Data (Runtime)
- Live EHR data, notes, or patient inputs used in GenAI responses
- Consent mechanisms and prompt structure tracking

## Provenance Requirements

- Data source traceability logs
- Version control and data drift alerts
- Consent and de-identification history
- Bias audits and demographic representativeness

## Roles and Responsibilities
- **Data Governance Teams**: Maintain dataset registries and provenance metadata.
- **Model Owners**: Ensure datasets meet clinical and regulatory quality standards.
- **Compliance and Legal**: Review IP rights, licensing, and PHI handling.

## Implementation Phases

### Must Do
- Require provenance documentation for all AI/GenAI model submissions.
- Flag systems trained with unverifiable, high-risk, or unconsented data.

### Should Do
- Implement lineage tracking across model lifecycle (training → prompt → output).
- Apply automated tools to assess data drift and source degradation.

### Recommended
- Participate in data transparency consortia or registries.
- Score models based on data quality and diversity benchmarks.

## References
- NIST AI RMF Core: MP-3, MP-5, MP-6
- NIST AI 600-1: §2.1.2 Data Quality and Traceability
- HIPAA: §164.308(a)(1), §164.502 – Use and disclosure of PHI
- FDA AI/ML: Dataset representativeness in SaMD
- ONC: Provenance and audit criteria for certified health IT

## Review Cycle
- Reviewed annually and when:
  - New datasets are introduced or updated
  - New model fine-tuning activities occur
  - Data-related GenAI failures or incidents are reported
