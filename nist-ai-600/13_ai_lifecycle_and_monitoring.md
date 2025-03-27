---
title: AI Lifecycle and Monitoring
nist_function: Manage
priority_phase: Should
last_reviewed: 2025-03-27
status: draft
---

## Outline

## Purpose
- Define governance checkpoints across the AI/GenAI system lifecycle, from intake to retirement.
- Ensure safe, effective, and continuously monitored GenAI system performance.

## Scope
- Applies to all stages of AI/GenAI system use in the hospital: evaluation, approval, deployment, monitoring, and decommissioning.
- Includes both internal systems and vendor-supplied solutions.

## Policy Statement
- AI/GenAI systems shall be subject to ongoing lifecycle governance, with clear criteria for go/no-go decisions, monitoring, and retirement.
- Lifecycle oversight must account for GenAI-specific risks such as prompt evolution, context drift, and re-tuning impacts.

## Lifecycle Phases

### 1. Intake and Risk Review
- Documented use case, ownership, and risk classification
- GenAI-specific risk screening (e.g., hallucination, misuse)

### 2. Pre-Deployment Testing
- Validation and testing protocols per `10_validation_and_testing.md`
- Stakeholder sign-off from legal, clinical, and IT

### 3. Deployment and Go-Live
- Monitoring strategy defined and initiated
- Access control and prompt logging in place

### 4. Post-Deployment Monitoring
- KPIs tracked: factuality, performance drift, hallucination rate
- Clinical safety events monitored and triaged

### 5. Modification and Re-Tuning
- Change control for model updates, prompt libraries, or fine-tuning
- Re-validation of outputs and updated risk classification

### 6. Retirement / Decommissioning
- Archival of system metadata and logs
- Removal from active inventory and compliance logs

## Implementation Phases

### Must Do
- Define lifecycle checkpoints in AI/GenAI project plans.
- Document performance monitoring strategies for each deployed system.

### Should Do
- Include prompt engineering governance in lifecycle reviews.
- Conduct annual “AI portfolio health checks” across all GenAI systems.

### Recommended
- Integrate lifecycle governance into EHR change advisory boards or QI/QA committees.
- Automate model and prompt change tracking within vendor management platforms.

## References
- NIST AI RMF Core: MG-3, MG-7, MG-8
- NIST AI 600-1: §2.3.3 Ongoing Monitoring
- HIPAA: §164.308(a)(8) – Evaluation
- FDA AI/ML: Lifecycle-based regulation and modification monitoring
- ONC: System updates and audit traceability requirements

## Review Cycle
- Reviewed annually and whenever major changes are made to a monitored AI/GenAI system.
