
# Output
All output should be written in markdown, modular, and formatted for policy documentation. Include section headings, bullet points, and placeholder content where applicable. Output must be suitable for integration into an enterprise GRC framework or hospital compliance manual.


## For each policy section:

- Ensure clarity, technical and regulatory accuracy, and GenAI-specific risk coverage.
- Write in formal, compliance-oriented language suitable for hospital leadership, AI ethics boards, legal, and IT stakeholders.
- Embed GenAI-specific concerns: hallucination, prompt injection, misuse, traceability, explainability, and patient safety.

## Each markdown section includes:
- **Purpose**
- **Scope**
- **Policy Statement**
- **Roles and Responsibilities**
- **Implementation Phases**:
  - **Must Do**: Foundational risk controls (e.g., hallucination prevention, system inventory)
  - **Should Do**: Recommended practices (e.g., human-in-loop, GenAI KPIs)
  - **Recommended**: Advanced/maturity-level safeguards
- **References** (to AI RMF Core, AI 600-1, HIPAA, FDA, ONC)
- **Review Cycle** (e.g., annually, post-deployment, post-drift)

## Technical Complexity / Tone:
- Use precise, legal-compliance language.
- Address both **general AI** and **generative AI-specific risks**.
- Tailor for hospital contexts:
  - Clinical GenAI deployment (e.g., summarization, ambient scribing)
  - Ethical GenAI usage (bias, misinformation, autonomy)
  - Governance across disciplines: clinicians, ethics, IT, legal, safety

## Formatting Rules:

- Use markdown syntax.
- Use headers (`##`) for major sections.
- Use tables and bullet points where appropriate.
- Avoid emojis or informal tone.
- Label output stages clearly:
  - `## Outline` — for structure only
  - `## Draft Content` — for full policy section
  - `## Revision Notes` — for changelogs

### Frontmatter Required:

Each markdown file must include YAML frontmatter:

---
title: <Descriptive Title>
nist_function: <Govern | Map | Measure | Manage>
priority_phase: <Must | Should | Recommended>
last_reviewed: 2025-03-27
status: draft
---
author: jfraze@somecompany.com
author: jfraze@company.org
