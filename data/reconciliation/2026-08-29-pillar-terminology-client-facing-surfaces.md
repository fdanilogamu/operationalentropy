---
project: Operational Entropy Index
date: 2026-08-29
title: Use pillar for the five canonical OEI pillars in client-facing copy
change_type: terminology
risk: medium
status: open
source_audit: 2026-08-28 OEI repository operating-knowledge audit
---

## Issue

Several public and report-facing surfaces call Founder Dependency, Knowledge Logistics, Workflow Velocity, Tool Discipline, and Handoff Integrity “dimensions” or “diagnostic categories,” while the established client-facing terminology is “pillars.”

## Canonical truth

OEI has five canonical pillars: Founder Dependency, Knowledge Logistics, Workflow Velocity, Tool Discipline, and Handoff Integrity. “Dimension” may remain an internal scoring implementation term where changing it would alter code or methodology, but client-facing descriptions should call the five constructs pillars.

## Affected surfaces

- about/index.html
- insights/what-is-operational-entropy/index.html
- index.html
- pricing/index.html
- services/index.html
- services/focused-operational-investigations/index.html
- info/About the Operational Entropy Index.pdf source content
- info/OEI TLDR.pdf source content
- admin/diagnosis/report.mjs client-facing report copy

## Current representation

The surfaces variously describe the five constructs as dimensions or diagnostic categories. The pricing and services surfaces promise diagnosis or scoring across five “dimensions,” and the focused-investigations overview routes uncertain clients to a diagnosis across all five “dimensions.” The generated report says it measures friction across five named constructs but labels score rows and narrative sections as dimensions.

## Expected representation

Use “pillar” when naming or collectively describing the five canonical OEI pillars in client-facing copy. Preserve technical identifiers, scoring groupings, and internal implementation terms unless separately authorized.

## Evidence

The five deep-dive pages identify themselves as OEI pillar deep dives; the Engagement Path Assessment promises assessment across five pillars; ECH describes its evidence as relevant to OEI pillars; and the reconciliation brief for this audit explicitly establishes pillar as the canonical term. pricing/index.html, services/index.html, and services/focused-operational-investigations/index.html contain additional client-facing occurrences of “five dimensions.” The five names themselves are unchanged across repository surfaces.

## Resolution notes

