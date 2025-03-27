---
title: AI System Inventory
nist_function: Map
priority_phase: Must
last_reviewed: 2025-03-27
status: draft
---

## Outline

## Purpose
- Maintain an up-to-date inventory of all AI and GenAI systems operating in the hospital environment.
- Enable risk visibility, accountability, and audit-readiness across clinical and operational domains.

## Scope
- Applies to all AI/GenAI models, APIs, services, or tools used within hospital infrastructure or patient workflows.
- Includes both in-house and third-party systems.

## Policy Statement
- All AI/GenAI systems must be logged in a centralized inventory including metadata on function, risk, and ownership.
- Inventory must be accessible for governance, compliance, and performance monitoring teams.

## Required Inventory Attributes

- System name and type (e.g., LLM, classification model, chatbot)
- Purpose and use case (e.g., documentation assistant, triage support)
- GenAI capabilities (e.g., generation, summarization, translation)
- Owner or responsible department
- Risk tier (low/medium/high) based on impact
- Deployment status (pilot, production, retired)
- Last validation date
- Known limitations (hallucination risk, training gaps, prompt injection exposure)

## Roles and Responsibilities
- **IT Governance**: Hosts and maintains inventory platform.
- **Model Owners / Project Leads**: Provide accurate metadata and update statuses.
- **Risk & Compliance Teams**: Use inventory for audits and risk reviews.

## Implementation Phases

### Must Do
- Register all new AI/GenAI systems before deployment.
- Include risk and capability classification in inventory entries.

### Should Do
- Integrate inventory with incident response and validation tracking tools.
- Tag systems with applicable GenAI risk categories from `18_genai_risk_categories.md`.

### Recommended
- Link inventory to monitoring dashboards and model lifecycle checkpoints.
- Conduct annual inventory audits and cleanup processes.

## References
- NIST AI RMF Core: MP-4
- NIST AI 600-1: §2.1.1 Use Transparency, §2.5.3 System Logging
- HIPAA: §164.308(a)(1) – Risk management process
- FDA AI/ML: Transparency and traceability recommendations
- ONC: Certification for system transparency and traceability

## Review Cycle
- Reviewed quarterly and following:
  - New system additions
  - Decommissioning or sunset of GenAI tools
  - Internal audit findings
