---
project: Operational Entropy Index
date: 2026-08-29
title: Use the canonical 90-Day Reset name in focused-investigation escalation copy
change_type: naming
risk: medium
status: open
source_audit: 2026-08-29 OEI Focused Investigations Repository Operating-Knowledge Audit
---

## Issue

The Engagement Path Assessment and all five focused-investigation pages call the multi-issue 90-day engagement a “90-Day Sprint,” while the current core service architecture names it the 90-Day Reset.

## Canonical truth

The multi-issue 90-day implementation engagement is the 90-Day Reset. The separate 30-day implementation engagement is the 30-Day Sprint.

## Affected surfaces

- assessments/engagement-path/index.html result-path titles
- services/focused-operational-investigations/founder-absence-simulation/index.html eligibility copy
- services/focused-operational-investigations/institutional-memory-recovery/index.html eligibility copy
- services/focused-operational-investigations/workflow-momentum-analysis/index.html eligibility copy
- services/focused-operational-investigations/operational-stack-review/index.html eligibility copy
- services/focused-operational-investigations/handoff-failure-analysis/index.html eligibility copy

## Current representation

These surfaces recommend “4-Day Diagnosis + 30-Day Audit + 90-Day Sprint” when broader or multiple conditions apply.

## Expected representation

Use the canonical 90-Day Reset name in the existing escalation route without changing its duration, prerequisites, implementation scope, selection behavior, or any other service architecture.

## Evidence

services/index.html defines the 90-Day Operational Entropy Reset as the fourth core engagement and separately defines the 30-Day Single Pain Point Sprint. pricing/index.html, index.html, contact/index.html, scripts/update_oei_pdfs.py, info/OEI Services and Pricing.pdf, and info/OEI TLDR.pdf consistently use 90-Day Reset for the 90-day engagement. The pricing comparison describes it as the diagnosis-plus-audit engagement for multiple interconnected issues and distinguishes it from the 30-Day Sprint for one bottleneck.

## Resolution notes


