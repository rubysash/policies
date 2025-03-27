# NIST AI Risk Management Policy Framework for Hospitals  
**Based on NIST AI RMF Core + NIST AI 600-1 Generative AI Profile**

This repository provides a modular, phased AI Risk Management Policy tailored for hospital environments. It aligns with the **NIST AI Risk Management Framework (AI RMF Core)** and extends compliance with the **NIST AI 600-1 Generative AI Profile**, addressing risks unique to generative AI technologies such as large language models (LLMs), synthetic data generation, and AI-based summarization in clinical and administrative settings.

Each policy module corresponds to a core function of the NIST AI RMF: **Govern**, **Map**, **Measure**, and **Manage**, and has been cross-referenced with applicable GenAI-specific guidance per NIST AI 600-1.

---

## A. Overview and Governance (GV)

- `01_policy_overview.md`  
  High-level summary of the hospital’s AI risk policy, including trustworthiness goals, GenAI use principles, and compliance alignment.

- `02_roles_responsibilities.md`  
  Defines governance structure, multi-disciplinary oversight bodies, and accountability roles for AI systems and GenAI deployments.

- `03_ai_governance_framework.md`  
  Hospital-wide governance model including ethical review boards, clinical integration oversight, and AI policy enforcement aligned with 600-1.

- `04_policy_enforcement_phases.md`  
  Phased implementation approach: **Must Do**, **Should Do**, and **Recommended** guidelines, incorporating GenAI readiness and system maturity.

---

## B. Map Function (MP)

- `05_context_and_use_cases.md`  
  Defines intended AI system and GenAI use cases, including clinical documentation, decision support, triage, scheduling, and patient communication.

- `06_data_origin_and_provenance.md`  
  Details on training data for AI/GenAI models, lineage tracking, synthetic data use, consent, and data quality for sensitive environments.

- `07_ai_system_inventory.md`  
  Maintains an inventory of all deployed AI and GenAI systems, noting model types (e.g., LLMs), intended use, ownership, and associated risks.

---

## C. Measure Function (MS)

- `08_trustworthiness_metrics.md`  
  KPIs and metrics for transparency, explainability, hallucination rate, data quality, and system robustness, with GenAI-specific risk criteria.

- `09_model_performance_and_drift.md`  
  Procedures for continuous monitoring, hallucination checks, GenAI drift tracking, and model degradation.

- `10_validation_and_testing.md`  
  Pre-deployment testing protocols including factuality, clinical alignment, human-AI review loops, and bias detection in generative outputs.

---

## D. Manage Function (MG)

- `11_risk_treatment_and_controls.md`  
  Mitigation strategies for generative model misuse, prompt injection, data leakage, PHI re-identification, and other GenAI-related harms.

- `12_incident_response_ai.md`  
  Incident reporting process for GenAI errors, hallucinations, bias events, ethical failures, and regulatory non-compliance.

- `13_ai_lifecycle_and_monitoring.md`  
  Lifecycle governance with checkpoints for generative model fine-tuning, prompt library controls, and continuous monitoring.

- `14_third_party_ai_vendor_risks.md`  
  Vendor risk due diligence for hosted GenAI APIs, SaaS models, proprietary LLMs, and integration into EHR or patient-facing tools.

---

## E. Appendices / Supporting Documents

- `15_glossary.md`  
  Definitions for AI and GenAI terms: hallucination, prompt injection, fine-tuning, synthetic data, zero-shot, etc.

- `16_compliance_mapping.md`  
  Crosswalk to **NIST AI RMF Core**, **NIST AI 600-1**, **HIPAA**, **FDA AI/ML**, and **ONC** standards.

- `17_policy_templates.md`  
  Templates for:
  - AI/GenAI Use Case Intake
  - Bias Impact Assessments
  - AI Incident Reports
  - Prompt Library Management

---

## Framework References

- **NIST AI RMF Core (January 2023)**  
- **NIST AI 600-1 Generative AI Profile (October 2023)**  
- **HIPAA Security Rule (§164.308)**  
- **FDA AI/ML-Based SaMD Action Plan (2021-26824)**  
- **ONC Health IT Certification Criteria**

This modular structure enables phased adoption of AI governance practices while scaling to address the emerging risk landscape of generative AI in healthcare.




## Compliance Mappings

| Section File                          | Title                                          | NIST AI RMF Controls        |
|--------------------------------------|------------------------------------------------|-----------------------------|
| 01_policy_overview.md               | AI Policy Overview                             | GOV-1, GOV-2                |
| 02_roles_responsibilities.md        | Roles and Responsibilities                     | GOV-3, GOV-4, GOV-5         |
| 03_ai_governance_framework.md       | AI Governance Framework                        | GOV-1, GOV-6                |
| 04_policy_enforcement_phases.md     | Policy Enforcement Phases                      | GOV-7                       |
| 05_context_and_use_cases.md         | Context and Use Cases                          | MP-1, MP-2                  |
| 06_data_origin_and_provenance.md    | Data Origin and Provenance                     | MP-3, MP-5, MP-6            |
| 07_ai_system_inventory.md           | AI System Inventory                            | MP-4                        |
| 08_trustworthiness_metrics.md       | Trustworthiness Metrics                        | MS-1, MS-3, MS-4            |
| 09_model_performance_and_drift.md   | Model Performance and Drift                    | MS-2, MS-5                  |
| 10_validation_and_testing.md        | Validation and Testing                         | MS-6, MS-7                  |
| 11_risk_treatment_and_controls.md   | Risk Treatment and Controls                    | MG-1, MG-2, MG-4            |
| 12_incident_response_ai.md          | Incident Response for AI                       | MG-5, MG-6                  |
| 13_ai_lifecycle_and_monitoring.md   | AI Lifecycle and Monitoring                    | MG-3, MG-7, MG-8            |
| 14_third_party_ai_vendor_risks.md   | Third-Party AI Vendor Risk Management          | MG-9, GOV-6                 |
| 15_glossary.md                      | Glossary                                       | —                           |
| 16_compliance_mapping.md            | Compliance Mapping                             | All RMF categories          |
| 17_policy_templates.md              | Policy Templates                               | Depends on template         |
| 18_genai_risk_categories.md         | Category mapping from NIST AI 600-1            | -                           |

