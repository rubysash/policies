---
title: Risk Treatment and Controls
nist_function: Manage
priority_phase: Must
last_reviewed: 2025-03-27
status: draft
---

## Outline

## Purpose
- Define control strategies and mitigation actions for risks posed by AI and GenAI systems.
- Address both general AI risks and GenAI-specific threats such as hallucination, prompt injection, and synthetic data misuse.

## Scope
- Applies to all operational, clinical, and administrative GenAI systems deployed or under evaluation.
- Controls span model selection, tuning, access, output moderation, and post-deployment oversight.

## Policy Statement
- AI and GenAI risks shall be mitigated through technical, administrative, and procedural controls.
- High-risk systems require documented mitigation plans tailored to their specific GenAI vulnerabilities.

## Risk Categories & Controls

### Hallucination Control
- Implement factuality scoring, output filtering, and human validation for clinical outputs.

### Prompt Injection Mitigation
- Enforce input sanitization, prompt logging, and system instruction hardening.

### PHI/PII Exposure Control
- Apply differential privacy, synthetic data validation, and prompt-level redaction where applicable.

### Bias Mitigation
- Conduct subgroup analysis, fairness audits, and training data provenance review.

### Drift and Degradation Monitoring
- Establish alerting for performance degradation or prompt-context misalignment.

### Output Moderation
- Use post-generation filters to detect harmful, profane, or biased outputs.

## Roles and Responsibilities
- **System Owners**: Develop and maintain system-specific risk control plans.
- **Security & Privacy Teams**: Oversee data protection and prompt security controls.
- **Clinical & Ethics Boards**: Evaluate acceptability of residual risks in patient-facing tools.

## Implementation Phases

### Must Do
- Identify and document at least one control per high-risk GenAI function (e.g., hallucination, PHI leakage).
- Track risk acceptance decisions and residual risk justifications.

### Should Do
- Apply tiered control frameworks based on system impact (e.g., decision support vs. communication tool).
- Use LLM guardrails (e.g., output constraints, content filters) in GenAI deployments.

### Recommended
- Adopt GenAI-specific risk scoring tools to guide treatment selection.
- Incorporate risk controls into contracts for vendor-hosted GenAI systems.

## References
- NIST AI RMF Core: MG-1, MG-2, MG-4
- NIST AI 600-1: §2.2 Use Restrictions, §2.3.4 Prompt Controls, §2.5.1 Risk Treatment
- HIPAA: §164.308(a)(1)(ii)(A) – Risk management
- FDA AI/ML: Risk mitigation strategies under SaMD frameworks
- ONC: Data integrity and access controls

## Review Cycle
- Reviewed annually and whenever:
  - New risk vectors are identified (e.g., from GenAI audits)
  - Controls are found insufficient during incident reviews
