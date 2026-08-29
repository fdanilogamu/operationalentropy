---
project: Operational Entropy Index
date: 2026-08-29
title: Align focused-investigation prerequisite language with the diagnosis-first route
change_type: service description
risk: medium
status: open
source_audit: 2026-08-28 OEI repository operating-knowledge audit
---

## Issue

The Services and Pricing PDF says focused investigations may be accessed independently, while current routing records and each investigation page place the 4-Day Diagnosis before the selected investigation.

## Canonical truth

For one or two clearly identified operational constraints, the current OEI route is a 4-Day Diagnosis followed by the relevant focused investigation. “Focused” means the investigation avoids the broader audit pathway; it does not mean the diagnosis is omitted.

## Affected surfaces

- info/OEI Services and Pricing.pdf source content
- info/OEI TLDR.pdf source content

## Current representation

The Services and Pricing PDF says “Focused investigations and ECH may be accessed independently.” The TLDR says neither focused investigations nor ECH requires a formal OEI engagement.

## Expected representation

Keep ECH’s independent-purchase statement, but describe focused investigations as following or including the 4-Day Diagnosis in accordance with the current known-issue route.

## Evidence

data/identity-changes/2026-08-11-assessment-separates-investigations.md explicitly states that one or two identified constraints produce a 4-Day Diagnosis followed by the relevant focused investigation. The Engagement Path Assessment implements that rule, and all five current focused-investigation pages state that they include a 4-Day Diagnosis.

## Resolution notes


