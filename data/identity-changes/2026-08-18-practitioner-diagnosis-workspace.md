---
project: Operational Entropy Index
date: 2026-08-18
title: OEI Diagnosis gains a browser-only practitioner workspace
categories:
  - product architecture
  - workflow
  - methodology
  - deliverables
  - technical
  - privacy/security
source: git commits 2d683a7 and 73e3baa
---

## Change

The OEI Diagnosis is supported by an unlisted, browser-only practitioner workspace for structured intake, evidence, scoring, findings, recommendations, checkpoints, and client-safe report generation.

## Propagation

- [x] Practitioner diagnosis workspace
- [x] Diagnosis workspace README
- [x] Scoring and controlled-value tests
- [x] Access configuration
- [x] Report export workflow

## Notes

Diagnosis data stays in JavaScript memory and is not stored in browser storage, cookies, or an API. Checkpoints and reports are exported explicitly by the practitioner. The client-side passphrase gate deters casual access but is not secure authentication.
