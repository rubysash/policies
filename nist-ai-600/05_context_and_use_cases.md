---
title: Context and Use Cases
nist_function: Map
priority_phase: Must
last_reviewed: 2025-03-27
status: draft
---

## Outline

## Purpose
- Define the intended applications of AI and GenAI within the hospital, enabling context-specific risk assessments and governance.

## Scope
- Covers current and proposed use cases for AI/GenAI across clinical, operational, and administrative domains.

## Policy Statement
- All AI/GenAI deployments must be mapped to approved use cases and evaluated for context-specific risk and ethical impact.
- GenAI tools with novel or high-risk functions (e.g., diagnostic inference, synthetic summaries) must receive heightened review.

## Approved Use Case Categories

### 1. Clinical Documentation and Ambient Scribing
- LLMs/NLP tools assisting with visit summaries, SOAP notes, or transcription.

### 2. Clinical Decision Support
- GenAI suggestions for diagnosis, triage, or treatment (non-autonomous).

### 3. Patient Communication and Education
- Chatbots, translation models, and FAQ generators with guardrails.

### 4. Operational Optimization
- GenAI for scheduling, supply forecasting, or staffing recommendations.

### 5. Imaging and Summarization
- Models producing synthetic imaging captions or radiology summaries.

### 6. Administrative Automation
- Use in billing code suggestion, prior authorization, or policy drafting.

## Risk Tiering Based on Context

- **Tier 1 – High Risk**: Diagnostic, autonomous, or patient-facing GenAI systems
- **Tier 2 – Medium Risk**: Decision support, documentation, and ambient tools
- **Tier 3 – Low Risk**: Administrative or backend support models

## Roles and Responsibilities
- **Department Leads**: Propose use cases and risk tier
- **Clinical Review Boards**: Approve Tier 1/2 systems before deployment
- **IT & Compliance**: Ensure proper tagging in system inventory

## Implementation Phases

### Must Do
- Map all GenAI systems to a declared use case and risk tier.
- Reject or escalate undeclared or unapproved use cases.

### Should Do
- Maintain an evolving catalog of approved GenAI use scenarios.
- Tag use cases in inventory, incident logs, and testing protocols.

### Recommended
- Use context-driven risk scores to prioritize governance resources.
- Validate outputs for clinical alignment in context-specific environments.

## References
- NIST AI RMF Core: MP-1, MP-2
- NIST AI 600-1: §2.1.1 Intended Use, §2.5.4 Use Categorization
- HIPAA: §164.308 – Contextual access controls
- FDA: Use-case based SaMD classification
- ONC: Application context in health IT transparency standards

## Review Cycle
- Reviewed annually or when new high-impact use cases are proposed.
