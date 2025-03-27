---
title: Policy Templates
nist_function: Manage
priority_phase: Recommended
last_reviewed: 2025-03-27
status: draft
---

## Outline

## Purpose
- Provide standardized templates to support the consistent evaluation, approval, and documentation of AI and GenAI systems.
- Enable traceable, repeatable risk assessments and governance actions across clinical and administrative uses.

## Scope
- Applies to all teams submitting, reviewing, or managing AI/GenAI systems.
- Supports documentation for intake, evaluation, incident response, and governance checkpoints.

## Policy Statement
- All AI and GenAI tools must be accompanied by completed documentation templates as outlined in this section.
- Templates shall be reviewed and updated to reflect evolving GenAI risks and regulatory standards.

## Available Templates

### AI/GenAI Use Case Intake Form
- Description of proposed AI/GenAI system
- Intended use, user roles, deployment environment
- Expected benefits, risks, and decision impact
- Responsible department and sponsor

### Bias and Risk Impact Assessment (BRIA)
- Population-level impact analysis
- Equity, bias, and disparity assessment
- Risk mitigation strategies
- Human-in-loop and override mechanisms

### AI Incident Report Form
- Nature and scope of AI/GenAI error
- Impacted systems, data, and patient population
- Root cause analysis (e.g., hallucination, prompt injection)
- Mitigation and disclosure actions

### Prompt Library Management Template
- Prompt categories and approval status
- Clinical vs. non-clinical prompt classifications
- Version control and testing status
- Access and usage tracking

## Implementation Phases

### Must Do
- Require completed intake forms for all new GenAI system deployments.
- Mandate incident reports for any GenAI-related clinical error or breach.

### Should Do
- Apply BRIA to all GenAI tools with patient-facing outputs or decision support roles.
- Use prompt templates for prompt tuning or scripted workflows.

### Recommended
- Automate form submission workflows within risk management or EHR systems.
- Publish anonymized case examples to support training and transparency.

## References
- NIST AI RMF Core: MG-1, MG-5, MG-7
- NIST AI 600-1: §2.3.2 Incident Documentation, §2.2.3 Prompt Controls
- HIPAA Security Rule: §164.308(a)(6)
- FDA AI/ML SaMD Action Plan: Post-market monitoring expectations
- ONC Certification: Documentation and audit trail requirements

## Review Cycle
- Templates reviewed annually and upon:
  - Major GenAI-related incident or system drift
  - Regulatory updates impacting documentation needs
