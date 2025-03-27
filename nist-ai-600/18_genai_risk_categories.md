---
title: Generative AI Risk Categories
nist_function: Govern
priority_phase: Must
last_reviewed: 2025-03-27
status: draft
---

## Outline

## Purpose
- Identify and define specific risk categories associated with Generative AI, as outlined in NIST AI 600-1 §2.
- Ensure hospital stakeholders are aware of the unique and exacerbated risks GenAI poses in clinical, administrative, and public-facing applications.
- Serve as a reference taxonomy for risk assessments, procurement, and policy enforcement.

## Scope
- Applies to all GenAI systems implemented in the hospital environment, including clinical documentation tools, chatbots, summarization systems, and patient-facing interfaces.
- Informs risk treatment strategies, incident monitoring, procurement checklists, and ethical review.

## Policy Statement
- All hospital GenAI deployments shall be evaluated against the defined risk categories in this section.
- Risk-specific mitigations, reviews, and monitoring shall be prioritized for high-severity categories based on deployment context.

## Generative AI Risk Categories (per NIST AI 600-1 §2)

### 2.1 CBRN Information or Capabilities
- Risk of generating or accessing content related to Chemical, Biological, Radiological, and Nuclear threats.

### 2.2 Confabulation
- Generation of inaccurate, misleading, or entirely fabricated information (hallucinations), particularly in clinical summaries or decision support.

### 2.3 Dangerous, Violent, or Hateful Content
- Output containing or encouraging harmful language or actions, including bias-reinforcing stereotypes or hate speech.

### 2.4 Data Privacy
- Risks to Protected Health Information (PHI) and personally identifiable information (PII), including re-identification and synthetic data leakage.

### 2.5 Environmental Impacts
- Energy consumption and carbon footprint of large-scale GenAI model deployment and inference.

### 2.6 Harmful Bias and Homogenization
- Amplification of systemic inequities; erasure of minority patient populations; over-standardization of clinical responses.

### 2.7 Human-AI Configuration
- Ambiguity in responsibility handoffs, over-reliance, or misuse due to unclear human-AI interaction boundaries.

### 2.8 Information Integrity
- Manipulation or degradation of evidence, records, or summaries—especially when GenAI is used in documentation or legal contexts.

### 2.9 Information Security
- Prompt injection attacks, jailbreaks, model inversion, or adversarial prompting leading to unintended outputs or exposure.

### 2.10 Intellectual Property
- Misuse of copyrighted training data or GenAI outputs creating copyright, licensing, or attribution conflicts.

### 2.11 Obscene, Degrading, and/or Abusive Content
- Output that may violate workplace, ethical, or clinical standards, including sexual, profane, or abusive language.

### 2.12 Value Chain and Component Integration
- Risks from unvetted or third-party GenAI components (e.g., APIs, open models) used in critical hospital workflows.

## Implementation Phases

### Must Do
- Assess each GenAI tool against all 12 risk categories prior to deployment.
- Document and justify risk acceptance or mitigation measures for high-severity risks (e.g., confabulation, data privacy).

### Should Do
- Tag GenAI system inventory entries with applicable risk categories (see `07_ai_system_inventory.md`).
- Use risk categories to guide staff training and prompt engineering protocols.

### Recommended
- Perform quarterly audits of high-risk GenAI systems using these categories.
- Incorporate these categories into bias impact assessments and prompt library reviews.

## References
- NIST AI 600-1: §2.1 – §2.12
- NIST AI RMF Core: GOV-1, MG-1, MG-4, MP-2
- HIPAA Security Rule: §164.308(a)(1) – Risk Analysis
- FDA AI/ML SaMD Action Plan: Algorithm risks and post-deployment harms
- ONC Certification: Audit, access control, transparency expectations

## Review Cycle
- Reviewed annually and upon:
  - Deployment of any new GenAI system
  - Identification of new risk vectors
  - Regulatory updates referencing novel or emerging GenAI threats
