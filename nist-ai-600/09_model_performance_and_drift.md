---
title: Model Performance and Drift
nist_function: Measure
priority_phase: Must
last_reviewed: 2025-03-27
status: draft
---

## Outline

## Purpose
- Monitor AI and GenAI systems for degradation in performance, output quality, or alignment with clinical expectations over time.
- Detect concept, data, and prompt drift—especially in high-impact or adaptive GenAI systems.

## Scope
- Applies to all deployed AI and GenAI tools in the hospital.
- Includes monitoring for both static and continuously learning models.

## Policy Statement
- GenAI models must be monitored for accuracy, hallucination rate, prompt responsiveness, and safety over time.
- Drift detection processes must be in place for high-risk systems and logged for auditability.

## Types of Drift

### 1. Concept Drift
- Changes in real-world conditions or data patterns not reflected in the model’s assumptions.

### 2. Data Drift
- Shifts in input data distribution (e.g., new patient populations, updated vocabularies).

### 3. Prompt Drift (GenAI-Specific)
- Unintended changes in model responses due to evolving prompt libraries, API behavior, or fine-tuning events.

### 4. Output Drift
- Gradual change in system behavior or tone, especially in generative outputs used for documentation or patient interaction.

## Monitoring Criteria

- Output accuracy vs. baseline
- Hallucination frequency trends
- Prompt effectiveness over time
- Latency or system instability
- Alert thresholds for safety events

## Roles and Responsibilities
- **Model Owners / IT Analytics**: Define monitoring thresholds and automated alerts.
- **Clinical Champions**: Identify degradation impacting workflow or patient care.
- **Compliance / Risk**: Audit model behavior for regulatory alignment.

## Implementation Phases

### Must Do
- Implement drift monitoring for all GenAI systems used in clinical or documentation contexts.
- Flag and investigate significant deviations in output or safety metrics.

### Should Do
- Use dashboards to track KPIs over time across departments.
- Require revalidation after major updates or prompt set revisions.

### Recommended
- Integrate drift detection with EHR/CDS monitoring systems.
- Notify end users of known performance degradation or expected updates.

## References
- NIST AI RMF Core: MS-2, MS-5
- NIST AI 600-1: §2.3.3 Ongoing Monitoring, §2.4.2 Drift Detection
- HIPAA: §164.308(a)(1)(ii)(D) – Information system activity review
- FDA AI/ML: Post-deployment monitoring of algorithm change protocols
- ONC: Audit and change tracking requirements

## Review Cycle
- Reviewed quarterly and after:
  - Performance alerts
  - Prompt or model updates
  - Clinical incident reports linked to GenAI system drift
