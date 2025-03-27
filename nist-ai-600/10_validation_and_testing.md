---
title: Validation and Testing
nist_function: Measure
priority_phase: Must
last_reviewed: 2025-03-27
status: draft
---

## Outline

## Purpose
- Establish validation protocols to evaluate the safety, effectiveness, and factual accuracy of AI and GenAI systems before deployment.
- Ensure GenAI outputs—particularly in clinical and administrative settings—meet hospital standards and regulatory expectations.

## Scope
- Applies to all GenAI and AI systems prior to go-live, including third-party tools, LLMs, NLP applications, and summarization engines.
- Includes internal testing, human-in-loop validation, and bias/factuality evaluations.

## Policy Statement
- All GenAI systems must undergo documented validation procedures prior to deployment.
- Validation must include checks for hallucinations, clinical inaccuracy, prompt robustness, and harmful bias.

## Validation Criteria

- **Factual Accuracy**: Outputs should reflect verifiable and clinically sound content.
- **Clinical Alignment**: Systems should support—not contradict—evidence-based guidelines.
- **Prompt Safety**: Systems should be tested for prompt injection resilience and edge-case behaviors.
- **Bias Detection**: Validation must include subgroup performance checks.
- **Explainability & Traceability**: Outputs must be auditable, explainable, and reviewable by designated stakeholders.

## Roles and Responsibilities
- **AI Development Team / Vendor**: Conducts initial testing and produces validation documentation.
- **Clinical Reviewers**: Validate outputs for patient safety and usability.
- **Risk/Compliance**: Confirms GenAI-specific criteria are addressed before go-live.

## Implementation Phases

### Must Do
- Require all GenAI systems to pass pre-defined validation protocols prior to deployment.
- Retain validation records as part of system audit logs.

### Should Do
- Conduct simulated clinical scenario testing for GenAI systems with high-stakes output.
- Test outputs for hallucination under stress conditions (e.g., ambiguous prompts, incomplete data).

### Recommended
- Establish a hospital-wide validation framework with reusable GenAI testing templates.
- Periodically re-validate models following major updates or re-training events.

## References
- NIST AI RMF Core: MS-6, MS-7
- NIST AI 600-1: §2.3.1 Pre-Deployment Testing
- HIPAA: §164.308(a)(8) – System evaluation
- FDA AI/ML: Validation of SaMD under Good Machine Learning Practice (GMLP)
- ONC: Transparency and testing criteria for certified health IT modules

## Review Cycle
- Reviewed annually and after:
  - Introduction of new GenAI tools
  - Major software/model updates
  - Testing failures or adverse events
