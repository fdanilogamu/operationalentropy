---
project: Entropy Compatible Hiring
date: 2026-08-29
title: Update stale ECH version references in OEI information PDFs
change_type: legacy copy
risk: low
status: open
source_audit: 2026-08-28 OEI repository operating-knowledge audit
---

## Issue

Two OEI information PDFs identify Entropy Compatible Hiring as Version 0.1.0 BETA, while the repository’s current ECH release is Version 0.1.3 BETA.

## Canonical truth

The current repository-supported ECH release is Version 0.1.3 BETA and includes Existing Employee Contribution Mapping as a distinct exploratory module alongside candidate-hiring instruments.

## Affected surfaces

- info/About the Operational Entropy Index.pdf source content
- info/OEI Services and Pricing.pdf source content

## Current representation

Both PDFs describe ECH as Version 0.1.0 BETA and therefore omit the later release identity.

## Expected representation

Bring the version reference and concise product description into alignment with Version 0.1.3 BETA without changing ECH pricing, assessment boundaries, or product behavior.

## Evidence

entropy-compatible-hiring/index.html identifies Version 0.1.3 BETA and documents its release contents. data/identity-changes/2026-08-28-ech-existing-employee-contribution-mapping.md records the current product expansion. The earlier 2026-08-20 release record documents Version 0.1.0 as the initial release rather than the current version.

## Resolution notes


