---
author: jfraze@mycomp.org
title: Model Retirement and Decommissioning Procedures
nist_function: Manage
priority_phase: Must
last_reviewed: 2025-06-24
status: draft
---

## Purpose

To define structured procedures for retiring, replacing, or decommissioning generative AI systems—ensuring safe offboarding, risk mitigation, and regulatory closure.

## Scope

Applies to all GenAI systems approaching end-of-life status, whether due to model performance degradation, contractual expiration, technological obsolescence, or identified safety concerns.

## Policy Statement

All decommissioned GenAI systems must be retired in a controlled, auditable, and reversible manner that preserves hospital data, revokes system access, and aligns with incident response and drift detection insights.

## Roles and Responsibilities

- **Model Owners**: Initiate and document decommissioning activities.
- **IT Security**: Revoke credentials, disable APIs, and retire associated infrastructure.
- **Compliance Team**: Confirm that PHI, logs, and artifacts are archived or purged per policy.

## Implementation Phases

### Must Do
- Apply formal decommissioning checklist (e.g., NIST AI RMF MANAGE-4.1).
- Retire and isolate models triggering repeated hallucinations, drift, or misuse alerts.
- Log model retirement in the AI system inventory (MAP-4.2).

### Should Do
- Perform final performance validation and produce an end-of-life report.
- Update governance registry and notify stakeholders.
- Retain explainability documentation and audit logs for regulatory audits.

### Recommended
- Conduct post-retirement review of system impact and lessons learned.
- Store decommissioned artifacts in secured long-term archive with access controls.
