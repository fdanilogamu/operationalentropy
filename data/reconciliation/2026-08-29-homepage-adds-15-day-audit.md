---
project: Operational Entropy Index
date: 2026-08-29
title: Bring homepage audit options into alignment with the 15- and 30-Day model
change_type: service description
risk: low
status: open
source_audit: 2026-08-28 OEI repository operating-knowledge audit
---

## Issue

The homepage pricing summary presents only the 30-Day Audit, while current service architecture offers both a 15-Day and a 30-Day Audit.

## Canonical truth

OEI audit work is offered at two depths: a 15-Day Audit for simpler or more focused analysis and a 30-Day Audit for broader or deeper analysis. Both require the Initial Diagnosis.

## Affected surfaces

- index.html

## Current representation

The homepage pricing cards list “30-Day Audit” as the sole audit option.

## Expected representation

Represent both current audit depths, or use a semantically accurate combined label that makes both the 15-Day and 30-Day options discoverable without changing pricing or prerequisites.

## Evidence

data/identity-changes/2026-08-12-oei-adds-15-day-audit.md establishes the change. services/index.html, pricing/index.html, the Engagement Path Assessment, and info/OEI Services and Pricing.pdf already represent both depths.

## Resolution notes


