---
author: jfraze@mycomp.org
title: AI System Inventory and Classification
nist_function: Map
priority_phase: Must
last_reviewed: 2025-06-24
status: draft
---

## Purpose

To maintain an accurate and auditable inventory of all AI and GenAI systems deployed across the hospital, with classifications based on use case, risk level, and ownership.

## Scope

Includes all AI technologies actively deployed, in trial use, or procured for clinical, operational, or administrative functions.

## Policy Statement

Hospitals must maintain a living AI inventory with system classifications that reflect deployment stage, responsible parties, and GenAI-specific risk vectors.

## Roles and Responsibilities

- **IT Asset Management**: Owns inventory maintenance and audit trail.
- **Governance Committee**: Reviews classifications and change control.
- **AI Product Owners**: Report deployments, version changes, and drift status.

## Implementation Phases

### Must Do
- Record each AI system’s function, owner, and data interaction level.
- Flag GenAI systems and those accessing PHI or decision-critical pathways.
- Require registration of all third-party or embedded AI tools (MAP-4.1).

### Should Do
- Integrate inventory with GRC and CMDB systems.
- Use metadata fields for model type (e.g., LLM, diffusion), plugin access, and API scope.

### Recommended
- Link inventory to output logging systems and incident trackers.
- Publish inventory summary to internal stakeholders for transparency.

## References
- NIST AI RMF: MAP-4
- NIST AI 600-1: §2.5.2
- ONC Certification: 45 CFR Part 170.315(g)(4)

## Review Cycle

Updated quarterly or upon any deployment or decommissioning event.
