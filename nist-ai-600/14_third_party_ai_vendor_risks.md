---
title: Third-Party AI Vendor Risk Management
nist_function: Manage
priority_phase: Should
last_reviewed: 2025-03-27
status: draft
---

## Outline

## Purpose
- Define procedures to assess and manage risks introduced by third-party AI and GenAI tools, APIs, and service providers.
- Ensure appropriate due diligence, risk controls, and contractual protections are applied to external vendors.

## Scope
- Applies to all third-party vendors providing AI/GenAI solutions integrated into hospital infrastructure, workflows, or patient interfaces.
- Includes APIs, SaaS platforms, proprietary LLMs, and embedded models in EHR systems or clinical decision support tools.

## Policy Statement
- All external AI/GenAI vendors must undergo security, clinical, and compliance due diligence prior to deployment.
- Vendor contracts must include clauses addressing GenAI-specific risks, such as hallucination liability, prompt security, and data use transparency.

## Roles and Responsibilities
- **Procurement**: Ensures GenAI vendor assessment is included in procurement workflows.
- **Legal & Compliance**: Validates regulatory compliance and data sharing agreements.
- **IT Security**: Conducts security risk reviews and integration testing.
- **Clinical Oversight**: Evaluates patient safety implications of third-party GenAI tools.

## Implementation Phases

### Must Do
- Maintain a list of all third-party AI/GenAI vendors with system descriptions and ownership.
- Require risk assessments (including hallucination, bias, and prompt security) for GenAI vendors.

### Should Do
- Include model update and monitoring clauses in contracts with GenAI providers.
- Require transparency statements from vendors on model architecture, training data lineage, and known risks.

### Recommended
- Establish an AI vendor onboarding checklist tailored to GenAI risks.
- Participate in shared due diligence efforts (e.g., health system consortia or third-party risk rating services).

## References
- NIST AI RMF Core: MG-9, GOV-6
- NIST AI 600-1: §2.12 Value Chain Risks
- HIPAA: §164.308(b) – Business associate contracts
- FDA: SaMD third-party component risk guidance
- ONC: Certification for modular/interfaced health IT systems

## Review Cycle
- Reviewed annually and when:
  - New vendors are integrated
  - Contract terms are renegotiated
  - GenAI systems are embedded in third-party platforms
