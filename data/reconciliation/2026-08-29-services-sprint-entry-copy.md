---
project: Operational Entropy Index
date: 2026-08-29
title: Correct services-page copy that suggests a Sprint can be the starting engagement
change_type: service description
risk: medium
status: open
source_audit: 2026-08-28 OEI repository operating-knowledge audit
---

## Issue

The services page says a company that already knows its bottleneck can “start with a Sprint,” but the same page and current pricing architecture require diagnosis plus audit before the 30-Day Sprint.

## Canonical truth

The 30-Day Single Pain Point Sprint requires both an Initial Diagnosis and an Audit. A known, bounded problem may instead enter through the Focused Operational Investigation path, which remains distinct from the 30-Day Sprint.

## Affected surfaces

- services/index.html

## Current representation

The closing engagement-path copy says, “If you know exactly what your bottleneck is, start with a Sprint.”

## Expected representation

Remove the implication that the 30-Day Sprint bypasses its prerequisites. Refer known, bounded problems to the focused-investigation path or otherwise preserve the established diagnosis-plus-audit prerequisite.

## Evidence

services/index.html and pricing/index.html both label the Sprint as requiring diagnosis plus audit. info/OEI Services and Pricing.pdf and info/OEI TLDR.pdf state the same pathway rule. data/identity-changes/2026-08-11-assessment-separates-investigations.md establishes focused investigations as the route for known constraints.

## Resolution notes


