---
title: Trustworthiness Metrics
nist_function: Measure
priority_phase: Should
last_reviewed: 2025-03-27
status: draft
---

## Outline

## Purpose
- Define quantitative and qualitative metrics to evaluate the trustworthiness of AI and GenAI systems.
- Support transparency, explainability, bias monitoring, and safety assessment in hospital contexts.

## Scope
- Applies to all AI and GenAI tools deployed in clinical, operational, or patient-facing capacities.
- Metrics are relevant for pre-deployment evaluation and continuous monitoring.

## Policy Statement
- Trustworthiness of GenAI systems shall be assessed using defined KPIs related to reliability, fairness, transparency, and robustness.
- Metrics must be documented and reviewed regularly for high-impact systems.

## Key Metric Categories

### 1. Hallucination Rate
- Percentage of outputs deemed factually incorrect or misleading.
- Measured through human review or automated factuality scoring.

### 2. Explainability
- Degree to which output rationale or underlying logic can be explained to users.
- Includes use of model cards, decision traceability, and attention maps (if applicable).

### 3. Bias Indicators
- Disparate outcomes across protected classes or patient cohorts.
- Detected via subgroup performance analysis and fairness testing.

### 4. Robustness
- Model consistency across inputs, including adversarial prompts and edge cases.
- Includes stress testing results.

### 5. Transparency and Documentation
- Availability of system-level documentation, data lineage, prompt libraries, and version history.

### 6. User Trust Feedback
- Ratings from clinical users on usability, trust, and perceived reliability.

## Roles and Responsibilities
- **Data Science / Model Owners**: Define, compute, and report trust metrics.
- **Clinical Risk Boards**: Validate appropriateness of trust thresholds for clinical systems.
- **Compliance Teams**: Ensure metrics align with audit and regulatory expectations.

## Implementation Phases

### Must Do
- Define at least 3 trust metrics per GenAI system prior to deployment.
- Track hallucination and transparency KPIs quarterly for high-risk systems.

### Should Do
- Include explainability and bias metrics in vendor-provided evaluation reports.
- Share trust scores with clinical end-users to support informed use.

### Recommended
- Benchmark trust metrics across systems and departments.
- Publicly disclose aggregate trust scores for transparency (where feasible).

## References
- NIST AI RMF Core: MS-1, MS-3, MS-4
- NIST AI 600-1: §2.1.1 Trustworthiness, §2.4.3 Performance Measures
- HIPAA: §164.308(a)(8) – Evaluation
- FDA: Good Machine Learning Practice (GMLP) transparency and safety principles
- ONC: Transparency, fairness, and explainability criteria

## Review Cycle
- Reviewed every 6 months or following:
  - Drift events
  - Model upgrades
  - User-reported trust concerns
