---
title: Incident Response for AI
nist_function: Manage
priority_phase: Must
last_reviewed: 2025-03-27
status: draft
---

## Outline

## Purpose
- Establish a structured process for detecting, reporting, managing, and resolving incidents related to AI and GenAI system failures or harms.
- Address GenAI-specific events such as hallucinations, bias amplification, prompt exploits, and unauthorized disclosures.

## Scope
- Applies to all AI and GenAI systems operating in the hospital environment.
- Covers incidents involving clinical care, administrative processes, patient communications, and third-party systems.

## Policy Statement
- All AI-related incidents, including those involving GenAI misuse or failure, must be reported and investigated in accordance with this policy.
- Special emphasis shall be placed on detecting hallucinations, harmful outputs, prompt injection, and breaches of PHI/PII.

## Incident Categories

- **Clinical Misalignment** (e.g., incorrect diagnosis suggestion from GenAI)
- **Hallucination or Fabrication**
- **Bias-Driven Harm**
- **Prompt Injection or Jailbreaking**
- **Inappropriate or Harmful Content**
- **Unauthorized Disclosure of Sensitive Data**
- **Performance Drift Leading to Safety Risks**

## Roles and Responsibilities
- **AI Risk Manager**: Coordinates investigation, documentation, and follow-up.
- **IT Security**: Assesses technical cause and containment strategies.
- **Clinical Oversight**: Evaluates patient impact and risk mitigation.
- **Legal & Compliance**: Ensures regulatory notifications and audit trails.

## Implementation Phases

### Must Do
- Establish an AI/GenAI incident reporting system accessible to all staff.
- Document all incidents using the standardized AI Incident Report Template.
- Notify legal/compliance of any GenAI-related PHI exposure or clinical harm.

### Should Do
- Classify GenAI incidents by severity, recurrence, and affected system type.
- Maintain a centralized log for all AI/GenAI incidents and resolutions.

### Recommended
- Conduct quarterly reviews of GenAI incident trends and root causes.
- Simulate GenAI-specific incident scenarios in tabletop exercises.

## References
- NIST AI RMF Core: MG-5, MG-6
- NIST AI 600-1: §2.3.2 Incident Documentation
- HIPAA: §164.308(a)(6) – Security incident procedures
- FDA AI/ML: Post-market monitoring for adaptive algorithms
- ONC: Health IT audit log and transparency criteria

## Review Cycle
- Reviewed after each major incident and at minimum annually.
