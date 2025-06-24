---
title: Hospital AI Governance Framework
nist_function: Govern
priority_phase: Must
last_reviewed: 2025-06-24
status: draft
---

## Purpose
To define the formal governance structure for AI and GenAI oversight across the hospital enterprise, integrating compliance, clinical, IT, and ethical controls.

## Scope
Applies to all AI systems managed, developed, or procured across the organization, including those used in diagnostics, ambient documentation, scheduling, patient interaction, and operational optimization.

## Policy Statement
The hospital must maintain an enterprise AI governance framework that enforces clear roles, lifecycle management checkpoints, ethics review, and internal accountability structures. Governance must incorporate sector-specific laws and emerging risks from GenAI technologies.

## Roles and Responsibilities
- **Governance Committee**: Reviews AI/GenAI systems at pre-deployment and annual checkpoints.
- **Legal & Compliance**: Maintains regulatory audit readiness and enforcement procedures.
- **Model Risk Review Panel**: Applies risk rating criteria across model types and vendors.

## Implementation Phases

### Must Do
- Require all GenAI models to pass governance review before deployment (GOV-4.2).
- Create and enforce AI system registration and version logging.
- Document governance decisions and system risk profiles in a central repository.

### Should Do
- Link AI governance checkpoints to hospital incident response and change control (SP 800-61r3).
- Use structured governance artifacts: risk rating matrix, model audit trail, usage logs.

### Recommended
- Implement ethical oversight workflows for models impacting patient consent, diagnosis, or treatment (AI 600-1 §2.5).
- Use governance analytics (e.g., drift detection dashboards, failure mode logs) to guide model reviews.

## References
- NIST AI RMF: GOVERN-4, GOVERN-5
- NIST AI 600-1: §2.1, §2.5
- FDA AI/ML SaMD: PCCP Guidelines (2024)
- HIPAA §164.308(a)(1)(ii)(D) – Evaluation

## Review Cycle
Every 12 months, or following a major incident, drift event, or regulatory change.
