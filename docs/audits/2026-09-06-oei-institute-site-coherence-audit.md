# OEI Institute Site Coherence Audit

Internal audit only. No remediation performed or authorized by this report.

Date: 2026-09-06. Branch: `oei-institute-site-reframe`. Audited commit: `d47e7f0`. Starting working tree: clean.

## Executive Summary

The Institute About hierarchy and branding are established, but the wider public journey remains organized around the former consulting acquisition model. The most consequential contradictions are definitive homepage/PDF prices during a pricing transition, the missing Services landing route, a methodology page promising engagement deliverables, and institutional contact paths leading into personal consulting intake. Replacing Fletcher with Institute would not resolve those flows.

There are **21 grouped findings: 16 issues/unresolved decisions and five intentional-preservation findings**. Seven are copy-safe; nine require local structural changes or substantive decisions. Strategic risk is predominantly structural/commercial, although there is enough localized naming work for a safe copy pass. Repeated components are grouped, with affected-file inventories below.

The supplied institutional model is the semantic authority. Repository content is evidence of the public projection, not evidence of the full institution. No missing-capability findings were inferred from absent training, certification, software, or canon repositories.

## Classification Summary

| Classification | Count |
|---|---:|
| Class 1: Copy-Safe | 7 |
| Class 2: Small Structural | 3 |
| Class 3: Architectural / Product / Governance Decision | 6 |
| Class 4: Preserve Intentionally | 5 |
| External Verification Needed: F12 and F16, overlapping Class 3 | 2 |
| Total grouped findings | 21 |

External verification is a tag, not a fifth class. It is not a finding that a capability or authority is missing. Severity measures public semantic/journey impact; Low severity on Class 4 entries is a review disposition, not a defect.

## Scope and Evidence Rules

- All 55 tracked HTML files were considered: 25 ordinary public content pages, 27 redirects/compatibility pages, one intentionally preserved assessment, and two internal interfaces. The sitemap contains 26 URLs: the 25 ordinary pages plus the missing `/services/` landing route.
- All three downloadable PDFs, six pages total, were read through text extraction. Their source generator was considered. This was not a print-layout audit.
- Header/footer markup, stylesheets, titles, descriptions, canonical URLs, Open Graph tags, sitemap, robots, directory, redirects, CTAs and README/SITE-STRUCTURE routing guidance were inspected. No JSON-LD/schema.org structured data was found; absence is not a defect.
- The route, metadata and affected-file appendices below identify all manifestations of grouped findings. File groups G01, G07, G08, G13 and G16 are exact membership lists, not proposed remediation scope beyond the corresponding finding.
- References to founders, diagnosis, interventions, services, or assessments were interpreted in context. Educational methods were not declared obsolete. No off-site product or practitioner implementation audit was undertaken.

## Findings

### F01: Repeated footer defines the site identity as a diagnostic tool

**ID:** F01

**CLASS:** 1 — Copy-Safe

**SEVERITY:** Medium

**ROUTE(S):** G01, 24 ordinary public pages; route mapping in Appendix A.

**FILE(S):** G01 in Appendix D.

**CURRENT STATE:** The identity block reads “OEI” and “Operational Entropy Index. A diagnostic tool and intervention process for reducing organizational drag.” About already uses the Institute footer. The preserved assessment also retains the old footer, but is excluded from G01.

**WHY IT CONFLICTS OR APPEARS SUSPICIOUS:** Organization-level chrome redefines the umbrella as the methodology, beneath the new Institute logo.

**UNDERLYING ISSUE:** Duplicated static footer text; there is no shared runtime footer component.

**PROPOSED ACTION:** Later batch-update only the descriptive identity heading/text on the listed ordinary pages. Retain ECH and rights-holder text.

**DEPENDENCIES / DECISIONS:** Copyright is F16; the intentionally preserved assessment is F19.

**RELATED FINDINGS:** F02, F16, F19, F20.

**SUGGESTED COPY DIRECTION:** Reuse About's OEI Institute heading, disciplinary tagline, and governing-institution description. Do not change ownership attribution by analogy.

### F02: Index definition is narrower than the governed methodology

**ID:** F02

**CLASS:** 1 — Copy-Safe

**SEVERITY:** Medium

**ROUTE(S):** `/`, `/about/operational-entropy-index/`.

**FILE(S):** `index.html`; `about/operational-entropy-index/index.html`.

**CURRENT STATE:** Both introductions define the Index as a proprietary diagnostic tool and structured intervention process.

**WHY IT CONFLICTS OR APPEARS SUSPICIOUS:** The supplied model defines a governed methodology. A tool/process-only definition encourages confusion with an implementation or engagement.

**UNDERLYING ISSUE:** Definition-level product/methodology ambiguity.

**PROPOSED ACTION:** Clarify only the opening definition and Institute governance; preserve the detailed method.

**DEPENDENCIES / DECISIONS:** The surrounding homepage and deliverable architectures remain F11/F14.

**RELATED FINDINGS:** F01, F03, F11, F14.

**SUGGESTED COPY DIRECTION:** The Operational Entropy Index is the methodology governed by OEI Institute for examining operational entropy across five pillars. Do not replace valid methodological uses of OEI with Institute.

### F03: Index metadata presents a consulting differentiator

**ID:** F03

**CLASS:** 1 — Copy-Safe

**SEVERITY:** Medium

**ROUTE(S):** `/about/operational-entropy-index/`.

**FILE(S):** `about/operational-entropy-index/index.html`, head metadata.

**CURRENT STATE:** Title/og:title are “Rethinking Operations: Beyond Symptoms”; descriptions begin “We look where other consultants don't.”

**WHY IT CONFLICTS OR APPEARS SUSPICIOUS:** A dedicated methodology destination is advertised as a consulting-company comparison.

**UNDERLYING ISSUE:** Metadata inherited from the former About page.

**PROPOSED ACTION:** Align title, description and Open Graph text with the existing educational purpose.

**DEPENDENCIES / DECISIONS:** None for metadata. Preserve route and canonical.

**RELATED FINDINGS:** F02, F14.

**SUGGESTED COPY DIRECTION:** Operational Entropy Index | OEI Institute; describe the five-pillar methodology and its governance without service promises.

### F04: Primary-page metadata retains ambiguous organizational attribution

**ID:** F04

**CLASS:** 1 — Copy-Safe

**SEVERITY:** Low

**ROUTE(S):** `/`, `/contact/`, `/temp-pricing/`, `/resources/information-packet/`, `/site-navigation/`.

**FILE(S):** Corresponding `index.html` files, including root `index.html`; full values in Appendix B.

**CURRENT STATE:** Primary titles use Operational Entropy as publisher; Contact promises “Fix Your Scaling Process.” Homepage title/OG uses “Revert Operational Drag.” Pricing metadata directs readers to Fletcher.

**WHY IT CONFLICTS OR APPEARS SUSPICIOUS:** On organization-level entry pages, publisher identity is ambiguous and inherited sales promises obscure page purpose. Subject-specific OEI article titles are not automatically wrong.

**UNDERLYING ISSUE:** Publisher naming and localized inherited sales metadata.

**PROPOSED ACTION:** Clarify publisher attribution and remove outcome promises from primary metadata, without describing a new delivery model.

**DEPENDENCIES / DECISIONS:** F11/F13 may require further metadata changes once page purposes are decided. Missing OG fields alone are not defects.

**RELATED FINDINGS:** F03, F11, F13.

**SUGGESTED COPY DIRECTION:** Use OEI Institute for organizational attribution; retain accurate subjects such as Contact and Pricing Update. Remove the misleading homepage “Revert” formulation.

### F05: Secondary ECH summaries imply a prescriptive hiring deliverable

**ID:** F05

**CLASS:** 1 — Copy-Safe

**SEVERITY:** Medium

**ROUTE(S):** `/`, `/site-navigation/`, `/contact/`.

**FILE(S):** `index.html`; `site-navigation/index.html`; `contact/index.html`.

**CURRENT STATE:** Homepage step 05 says “Know exactly who to hire next so the fix holds.” The directory calls ECH a hiring deliverable; Contact lists it as an Add-on.

**WHY IT CONFLICTS OR APPEARS SUSPICIOUS:** ECH's own page explicitly describes standalone software, independent use, role-agnostic evidence and limits on determining hiring suitability.

**UNDERLYING ISSUE:** Outdated product summaries conflate applied software with consulting deliverables.

**PROPOSED ACTION:** Correct these descriptions, without changing placement, purchase terms or product behavior.

**DEPENDENCIES / DECISIONS:** Homepage step placement is F11. The Index's universal inclusion promise is F14.

**RELATED FINDINGS:** F11, F14, F21.

**SUGGESTED COPY DIRECTION:** OEI-derived software for structured behavioral observation, usable independently. Replace Contact's Add-on label with Separate software. Avoid “exactly who to hire.”

### F06: Directory/resource captions lag behind their destinations

**ID:** F06

**CLASS:** 1 — Copy-Safe

**SEVERITY:** Low

**ROUTE(S):** `/site-navigation/`, `/resources/information-packet/`.

**FILE(S):** `site-navigation/index.html`; `resources/information-packet/index.html`.

**CURRENT STATE:** Directory About caption is “Institute overview (content in development).” The Index PDF is described as “An detailed introduction regarding what we do.”

**WHY IT CONFLICTS OR APPEARS SUSPICIOUS:** The first still describes the removed scaffold; the second uses an organizational activity description for a methodology resource.

**UNDERLYING ISSUE:** Stale captions, not absent capability.

**PROPOSED ACTION:** Update captions locally, retaining destinations pending F15.

**DEPENDENCIES / DECISIONS:** Resource publication/currentness is F15; do not call these PDFs canon.

**RELATED FINDINGS:** F15, F20.

**SUGGESTED COPY DIRECTION:** Institute overview and its relationship to the Index; introduction to the Operational Entropy Index methodology.

### F07: Top-level pillar terminology varies

**ID:** F07

**CLASS:** 1 — Copy-Safe

**SEVERITY:** Low

**ROUTE(S):** G07; mapped in Appendix A.

**FILE(S):** G07 in Appendix D.

**CURRENT STATE:** Homepage, Index, entropy explainer, ECH, investigation overview and directory use dimensions/categories for the same five names called pillars on Institute About.

**WHY IT CONFLICTS OR APPEARS SUSPICIOUS:** Readers encounter different labels for the same top-level hierarchy. This does not establish a different scoring model.

**UNDERLYING ISSUE:** Vocabulary consistency only.

**PROPOSED ACTION:** Standardize references explicitly naming the five top-level pillars.

**DEPENDENCIES / DECISIONS:** Preserve subordinate dimensions/vectors, numerical methods, assessment and historical records. PDFs are under F15.

**RELATED FINDINGS:** F02, F17.

**SUGGESTED COPY DIRECTION:** Use five OEI pillars for the collective Founder Dependency, Knowledge Logistics, Workflow Velocity, Tool Discipline and Handoff Integrity hierarchy.

### F08: Services discovery remains active without a landing page

**ID:** F08

**CLASS:** 2 — Small Structural

**SEVERITY:** High

**ROUTE(S):** `/services/` and inbound sources in G08.

**FILE(S):** G08; `services.html`; `sitemap.xml`. `services/index.html` is absent.

**CURRENT STATE:** Shared navigation/footer, homepage “See all service options,” directory listings, sitemap and legacy redirect all target `/services/`. No temporary Services landing page was found.

**WHY IT CONFLICTS OR APPEARS SUSPICIOUS:** Visitors reach an unavailable commercial entry point. A static directory listing is not a functioning landing page.

**UNDERLYING ISSUE:** Pre-existing route/discovery mismatch.

**PROPOSED ACTION:** Apply a local explicit interim treatment or remove invitations to the missing landing route; preserve investigation content. Do not restore the old catalogue automatically.

**DEPENDENCIES / DECISIONS:** Fletcher must approve the interim treatment. Future commercial scope is F12. Missing website route does not mean missing service capability.

**RELATED FINDINGS:** F09, F11, F12.

### F09: Pricing links promise detail unavailable at the destination

**ID:** F09

**CLASS:** 2 — Small Structural

**SEVERITY:** Medium

**ROUTE(S):** `/`, `/site-navigation/`, `/pricing/`, `/pricing.html`, `/temp-pricing/`.

**FILE(S):** `index.html`; `site-navigation/index.html`; `pricing/index.html`; `pricing.html`; `temp-pricing/index.html`.

**CURRENT STATE:** “See full pricing breakdown” and “Review scope and investment” lead to a transition notice and personal contact options. Pricing redirects work.

**WHY IT CONFLICTS OR APPEARS SUSPICIOUS:** Invitation and destination disagree even though the notice is intentional.

**UNDERLYING ISSUE:** CTA promise/destination mismatch.

**PROPOSED ACTION:** Locally relabel or retire detailed-breakdown invitations. Preserve working redirects and the notice.

**DEPENDENCIES / DECISIONS:** Do not infer replacement prices; final scope is F12.

**RELATED FINDINGS:** F11, F12.

### F10: Educational endings impose an engagement entry step

**ID:** F10

**CLASS:** 2 — Small Structural

**SEVERITY:** Medium

**ROUTE(S):** `/insights/operational-drag/`, `/insights/organizational-complexity-tax/`, `/insights/what-is-operational-entropy/`.

**FILE(S):** Corresponding `index.html` files.

**CURRENT STATE:** Closings say every engagement starts with discovery; the complexity-tax call promises “to audit your current complexity.”

**WHY IT CONFLICTS OR APPEARS SUSPICIOUS:** Education ends in a compulsory consulting sequence, and a call is presented as an audit. Contact itself is legitimate.

**UNDERLYING ISSUE:** Local acquisition CTA blocks.

**PROPOSED ACTION:** Remove the universal prerequisite or present the existing Contact option as optional discussion. No replacement funnel.

**DEPENDENCIES / DECISIONS:** Contact's broader purpose is F13. Neutral Contact invitations on Process Drift/Execution Deficit do not need the same removal.

**RELATED FINDINGS:** F13, F17.

### F11: Homepage still organizes OEI as consulting acquisition

**ID:** F11

**CLASS:** 3 — Architectural / Product / Governance Decision

**SEVERITY:** High

**ROUTE(S):** `/`, `/site-navigation/`.

**FILE(S):** `index.html`; `site-navigation/index.html`.

**CURRENT STATE:** Symptoms lead into “How the OEI process works,” discovery, diagnosis, audit/fixes, ECH, fixed-price cards and “Start your diagnosis.” The directory guides engagement selection. Institute identity appears chiefly in the logo/About link.

**WHY IT CONFLICTS OR APPEARS SUSPICIOUS:** The organizing business model remains consulting acquisition. This is not a demand to list all institutional capabilities on the homepage.

**UNDERLYING ISSUE:** Primary entry architecture.

**PROPOSED ACTION:** Decision: what should the homepage's primary purpose and visitor paths be during transition, and what role should direct engagements retain?

**DEPENDENCIES / DECISIONS:** Fletcher's entry-journey decision, then F12/F13. Noun replacement cannot solve a flow decision.

**RELATED FINDINGS:** F02, F05, F08, F09, F12, F13.

### F12: Current-looking packaging conflicts with the commercial transition

**ID:** F12

**CLASS:** 3 — Architectural / Product / Governance Decision

**SEVERITY:** High

**ROUTE(S):** `/`, `/contact/`, `/temp-pricing/`, all six focused-investigation pages, all three public PDFs.

**FILE(S):** `index.html`; `contact/index.html`; `temp-pricing/index.html`; all six `services/focused-operational-investigations/**/index.html` files; three `info/*.pdf` files. Exact paths in Appendices A/C.

**CURRENT STATE:** Homepage publishes $2,000/$15,000/$45,000 and revenue multipliers. Investigation pages advertise $500–$2,000, 1–2 weeks, included 4-Day Diagnosis, and a three-or-more rule leading to Diagnosis + 30-Day Audit + 90-Day Sprint. Other pages/PDFs call the 90-day service Reset. PDFs publish payment terms and prerequisites. Contact promises both four days of founder time and a 5–7-day delivery process.

**WHY IT CONFLICTS OR APPEARS SUSPICIOUS:** These are public commitments despite restructuring. Method descriptions can remain valid, but current inclusion, price and prerequisite semantics cannot be inferred from their names.

**UNDERLYING ISSUE:** Commercial packaging interleaved with methodological requirements.

**PROPOSED ACTION:** Decision: which fees, time commitments, prerequisites and escalation rules remain public commitments, and which are historical or transitional?

**DEPENDENCIES / DECISIONS:** Fletcher's approved scope/pricing and the authoritative status of pathway rules. Copy alone cannot decide what is being sold or what practice requires.

**EXTERNAL VERIFICATION NEEDED:** Check Institute-maintained canon/practice standards for the included-diagnosis and multi-investigation escalation rules, and approved engagement records for fees/commitments. The site cannot establish whether these rules are normative methods or sales packaging. This is not an assertion that the standards are missing.

**RELATED FINDINGS:** F08, F09, F11, F13, F15, F17.

### F13: Institute-wide Contact leads into personal consulting intake

**ID:** F13

**CLASS:** 3 — Architectural / Product / Governance Decision

**SEVERITY:** High

**ROUTE(S):** `/contact/`, `/about/`, `/temp-pricing/`, Get Started sources G13.

**FILE(S):** `contact/index.html`; `about/index.html`; `temp-pricing/index.html`; G13.

**CURRENT STATE:** Shared Get Started and About's help-applying path reach personal calendar/email channels. Contact requests service choices, promises diagnosis delivery, and explains OEI as a scoped engagement. It lists seven-day availability and weekday availability in different sections.

**WHY IT CONFLICTS OR APPEARS SUSPICIOUS:** A personal contact is valid, but the page treats all inquiries as the same consultant-delivered purchase process. Relabeling the speaker would not change intake.

**UNDERLYING ISSUE:** Contact purpose, routing and commitments.

**PROPOSED ACTION:** Decision: should Contact serve institutional/general inquiries, direct consulting intake, or explicitly separated purposes, and what commitments can it make now?

**DEPENDENCIES / DECISIONS:** Fletcher must define intake/provider scope. Scheduling details should then reflect the approved calendar. No practitioner directory or new network is presumed necessary.

**RELATED FINDINGS:** F04, F10, F11, F12, F16.

### F14: Methodology page promises universal engagement deliverables

**ID:** F14

**CLASS:** 3 — Architectural / Product / Governance Decision

**SEVERITY:** High

**ROUTE(S):** `/about/operational-entropy-index/`.

**FILE(S):** `about/operational-entropy-index/index.html`.

**CURRENT STATE:** “Who the OEI is for” leads to “What you get / Every engagement delivers,” including scores, fixes and ECH as a deliverable telling users whom to hire. The page closes in acquisition.

**WHY IT CONFLICTS OR APPEARS SUSPICIOUS:** The Institute bridge lands on a methodology explanation that still defines expected value through buying an engagement.

**UNDERLYING ISSUE:** Educational scope mixed with undefined commercial inclusion.

**PROPOSED ACTION:** Decision: which sections describe the methodology generally, which describe a bounded engagement application, and should the latter remain on this page?

**DEPENDENCIES / DECISIONS:** Fletcher must determine the offer-related scope. ECH's standalone status supports correcting hiring claims, but does not establish inclusion terms. Copy substitution cannot resolve an unconditional deliverable promise.

**RELATED FINDINGS:** F02, F03, F05, F12, F18.

### F15: Public downloads preserve old current-looking commercial authority

**ID:** F15

**CLASS:** 3 — Architectural / Product / Governance Decision

**SEVERITY:** High

**ROUTE(S):** `/resources/information-packet/`, `/site-navigation/`, all three `/info/*.pdf` downloads.

**FILE(S):** `resources/information-packet/index.html`; `site-navigation/index.html`; `info/About the Operational Entropy Index.pdf`; `info/OEI Services and Pricing.pdf`; `info/OEI TLDR.pdf`; `scripts/update_oei_pdfs.py`.

**CURRENT STATE:** Resources are foundational and describe what is offered/priced. PDF subtitles say “A current overview” and “Current engagement paths.” All three have Fletcher GH Consulting and CONFIDENTIAL & PROPRIETARY headers while freely downloadable. About/Services PDFs describe ECH v0.1.0, while its live page advertises v0.1.3.

**WHY IT CONFLICTS OR APPEARS SUSPICIOUS:** These active resources independently recirculate old commercial context. They are not simply historical records stored in the repository.

**UNDERLYING ISSUE:** Public status, versioning and resource authority.

**PROPOSED ACTION:** Decision: what status should each PDF have now (current, historical reference, revised or temporarily unlisted), and which audience/claims are approved?

**DEPENDENCIES / DECISIONS:** F12 for commercial content and F16 for attribution. The generator must be updated with any later approved PDF changes. A wording edit alone cannot choose publication status. No deletion recommended.

**RELATED FINDINGS:** F06, F12, F16, F21.

### F16: Provider, licensor and rights-holder relationships are unspecified

**ID:** F16

**CLASS:** 3 — Architectural / Product / Governance Decision

**SEVERITY:** Medium

**ROUTE(S):** Rights-holder sources G16, `/entropy-compatible-hiring/`, the three PDFs.

**FILE(S):** G16; `entropy-compatible-hiring/index.html`; three `info/*.pdf` files.

**CURRENT STATE:** Footers retain © 2026 Fletcher GH Consulting; PDFs pair that name with Operational Entropy Index. ECH offers a company/individual software license. About names Institute governance without specifying provider/licensor/rights-holder relationships.

**WHY IT CONFLICTS OR APPEARS SUSPICIOUS:** This is unresolved attribution, not proof that copyright is wrong or that Institute must own these assets. Automatic replacement could create a false authority claim.

**UNDERLYING ISSUE:** Governance and commercial/legal attribution are distinct.

**PROPOSED ACTION:** Decision: what approved public relationship should be stated among OEI Institute, Fletcher GH Consulting, and the ECH provider/licensor/rights holder?

**DEPENDENCIES / DECISIONS:** The actual institutional/entity relationship and approved product/license/rights records. Website copy cannot establish ownership or contracting authority. No legal conclusion is made.

**EXTERNAL VERIFICATION NEEDED:** Consult the approved Institute/provider/rights-holder relationships and ECH license attribution. Preserve existing copyright pending that verification. Do not infer an institution's legal form from its name.

**RELATED FINDINGS:** F01, F13, F15, F21.

### F17: Educational methods and bounded investigations remain useful

**ID:** F17

**CLASS:** 4 — Preserve Intentionally

**SEVERITY:** Low

**ROUTE(S):** All ten insights, six focused-investigation pages, `/client-journey/`, `/about/operational-entropy-index/`.

**FILE(S):** Corresponding files listed in Appendix A.

**CURRENT STATE:** Pillar explanations, evidence methods, client signals and investigation questions describe operating conditions. Process Drift/Execution Deficit distinguish signals from findings.

**WHY IT CONFLICTS OR APPEARS SUSPICIOUS:** No conflict follows merely from discussing diagnosis, interventions, founders or consulting-related methods. “OEI identifies” can mean applying a framework, not an organizational attribution.

**UNDERLYING ISSUE:** Valid methodology projection separate from commercial wrappers.

**PROPOSED ACTION:** Preserve educational explanations, names, cross-links and inquiry methods. Isolate the separately classified wrappers.

**DEPENDENCIES / DECISIONS:** No canon rewrite. Specific normative pathway status is F12.

**RELATED FINDINGS:** F07, F10, F12.

### F18: Founder provenance is not practitioner exclusivity

**ID:** F18

**CLASS:** 4 — Preserve Intentionally

**SEVERITY:** Low

**ROUTE(S):** `/about/operational-entropy-index/`.

**FILE(S):** `about/operational-entropy-index/index.html`, About the founder section.

**CURRENT STATE:** Fletcher's career, framework origins, current work and portfolio link are described.

**WHY IT CONFLICTS OR APPEARS SUSPICIOUS:** Provenance is legitimate. The biography does not explicitly state that only Fletcher can practice OEI.

**UNDERLYING ISSUE:** Historical attribution differs from delivery architecture.

**PROPOSED ACTION:** Preserve biography/portfolio; do not invent or relocate founder content.

**DEPENDENCIES / DECISIONS:** Surrounding offer structure is F14.

**RELATED FINDINGS:** F13, F14.

### F19: Assessment and compatibility/history references are intentional

**ID:** F19

**CLASS:** 4 — Preserve Intentionally

**SEVERITY:** Low

**ROUTE(S):** `/assessments/engagement-path/`, `/oei_engagement_quiz.html`, conditional `/contact/?recommendation=...`; unlisted internal records.

**FILE(S):** Assessment and alias HTML; `contact/index.html`; `README.md`; `SITE-STRUCTURE.md`; `data/propagation-map.json`; assessment-related identity/reconciliation records and manifest. Exact remaining reference list in Appendix E.

**CURRENT STATE:** Old assessment offers/logic and alias remain accessible directly; Contact accepts the result. Internal records preserve names/routes. No ordinary page or sitemap path leads to the assessment.

**WHY IT CONFLICTS OR APPEARS SUSPICIOUS:** Direct access and implementation were deliberately preserved. These are not residual public funnel CTAs.

**UNDERLYING ISSUE:** Compatibility and provenance.

**PROPOSED ACTION:** Preserve assessment, alias, conditional handoff and internal history; keep them out of public navigation/sitemap.

**DEPENDENCIES / DECISIONS:** Unlisted is not access-controlled or guaranteed deindexed. Robots permits crawling and the assessment retains its canonical. This audit verifies site discovery removal, not external search removal.

**RELATED FINDINGS:** F12, F20.

### F20: About, branding and off-site capability boundaries are coherent

**ID:** F20

**CLASS:** 4 — Preserve Intentionally

**SEVERITY:** Low

**ROUTE(S):** `/about/`; all branded pages; internal `/admin/diagnosis/` and `/ops/propagation/`.

**FILE(S):** `about/index.html`; `images/oei-institute-logo.png`; `images/oei-institute-favicon.png`; `styles.css`; internal interface files; `README.md`; `SITE-STRUCTURE.md`.

**CURRENT STATE:** About differentiates governance and methodology, and describes practitioner certification as developing. All branded HTML uses the Institute assets. Internal interfaces are unlisted/noindex.

**WHY IT CONFLICTS OR APPEARS SUSPICIOUS:** No broad practitioner-availability claim, public certification offer, or blanket canon claim was found. Other institutional assets may legitimately live elsewhere.

**UNDERLYING ISSUE:** Selective public projection, not an institutional inventory.

**PROPOSED ACTION:** Preserve About/branding. Do not manufacture a missing portal, network, canon repository or software inventory. Preserve internal scope/provenance documentation.

**DEPENDENCIES / DECISIONS:** README/SITE-STRUCTURE retain descriptive drift, including About-as-scaffold and generic add-to-sitemap instructions. They do not execute routing or currently expose the quiz. Later documentation maintenance should respect the unlisted-assessment exception.

**RELATED FINDINGS:** F06, F19, F21.

### F21: ECH is a distinct applied software product

**ID:** F21

**CLASS:** 4 — Preserve Intentionally

**SEVERITY:** Low

**ROUTE(S):** `/entropy-compatible-hiring/`.

**FILE(S):** `entropy-compatible-hiring/index.html`.

**CURRENT STATE:** ECH specifies Windows software, independent use, ten derived instruments, a separate employee module, one-time beta pricing, product license terms and evidence/limitations boundaries. Release histories are versioned; the demo is marked fictional.

**WHY IT CONFLICTS OR APPEARS SUSPICIOUS:** A product purchase is compatible with Institute governance. Software licensing is not practitioner licensing. Candidate/employee assessments are not the engagement quiz. Missing product source here does not invalidate claims.

**UNDERLYING ISSUE:** Applied product and methodology coexist without being synonyms.

**PROPOSED ACTION:** Preserve product scope, limitations, demo labeling and release history. Correct conflicting summaries elsewhere.

**DEPENDENCIES / DECISIONS:** No implementation audit is needed solely because source is elsewhere. Attribution is F16; PDF version mismatch is F15.

**RELATED FINDINGS:** F05, F15, F16, F19.

## Cross-Site Patterns

1. Institute-branded headers lead into method-defined identity footers. About is the exception; footer copies do not propagate automatically.
2. OEI process can mean an evidence method, a purchase sequence or personal delivery. Only the first can be preserved without a commercial decision.
3. Transition notices have not propagated to price cards, investigation wrappers, PDFs and destination promises.
4. Quiz removal succeeded, but Contact and homepage still carry much of the acquisition architecture. Optional contact remains legitimate.
5. ECH summaries lag behind its own independent-software positioning and evidence boundaries.
6. PDFs and their generator are a separate authority/propagation surface; version mismatches are visible without an off-site product audit.
7. History, methodological education and internal infrastructure are not inherently public defects.

## Decision Queue

Only Class 3 findings are listed. No outcome is selected.

- **F11:** What primary purpose and visitor paths should the homepage serve during transition, and what role should direct engagements retain?
- **F12:** Which published fees, time commitments, prerequisites and escalation rules remain commitments, and which are historical or transitional?
- **F13:** Should Contact handle institutional inquiries, direct consulting intake, or separated purposes, and what can it promise now?
- **F14:** Which Index-page sections explain the method versus a bounded engagement application, and should the latter remain there?
- **F15:** What current/historical/revised/unlisted status and audience should each PDF have?
- **F16:** What approved relationship should be stated among Institute governance, Fletcher GH Consulting and product provider/licensor/rights holder?

## Safe Remediation Queue

A later copy-only pass is justified. It must exclude assessment/history, preserve page purposes and avoid inventing scope or prices.

- F01: descriptive footer identity on ordinary pages, excluding copyright.
- F02: opening methodology definitions.
- F03: dedicated Index metadata.
- F04: primary-page publisher attribution and localized metadata promises.
- F05: bounded ECH summary descriptions, excluding inclusion terms and placement.
- F06: stale directory/resource captions, excluding publication status.
- F07: five top-level pillar labels, excluding subordinate dimensions and scoring.

## Structural Remediation Queue

- F08: explicit interim treatment of missing Services route/public invitations; no reconstructed catalogue by default.
- F09: pricing CTA promises matched to the transition notice.
- F10: optional discussion endings for the three educational pages; no universal sales prerequisite.

## External Verification Queue

- **F12:** Public claims are the included diagnosis and multi-investigation escalation rule on all five investigation details, plus fees/prerequisites in homepage/Contact/PDFs. Check authoritative practice/canon and approved commercial scope records to distinguish normative requirements from packaging. Website copy alone cannot establish that status.
- **F16:** Public attribution pairs Institute governance with Fletcher GH Consulting copyright/PDF headers and ECH licensing. Check approved entity/provider/rights-holder relationships and license attribution. Website text alone cannot establish legal authority. This is not a finding of missing ownership or capability.

Do not copy internal assets into the website to resolve these questions. Do not infer a missing capability from this queue.

## Intentionally Preserved Material

- F17: methodological education, evidence boundaries, inquiry methods and relevant cross-links.
- F18: founder biography and historical practice provenance.
- F19: unlisted assessment, direct alias, recommendation handoff, historical/internal references.
- F20: Institute About, new assets, bounded practitioner language and internal/off-site scope boundaries.
- F21: ECH independent software, license/product distinctions, limitations and version history.

## Validation and Limits

- All tracked HTML routes, shared chrome, metadata, directory, sitemap and three PDFs considered; inventories follow.
- A read-only homepage/sitemap crawl visited 41 local page/asset paths. Neither assessment nor legacy quiz alias was reachable through that public graph.
- All 25 existing sitemap content pages returned HTTP 200 locally; `/services/` is the pre-existing missing landing file. Direct assessment returned HTTP 200. Local directory-listing responses are not treated as a valid Services page.
- No legacy logo/favicon HTML references were found. Current Institute assets and stylesheet remain unchanged by the audit.
- No public content, routes, metadata, scripts, price claims or branding changed. No remediation, merge, publishing or commit performed.
- Only this unlinked internal documentation report was created. It is absent from public navigation and sitemap; placement in a static repository is not an access-control claim.
- Repository absence was not treated as institutional absence. No completeness backlog, invented practitioner offering or commercial model was produced.
- External indexing/backlinks, checkout results, off-site implementation accuracy, and authoritative canon/entity records are outside this local projection audit.

## Appendix A: Complete Route Disposition

| Route | File | Disposition |
|---|---|---|
| `/about.html` | [about.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/about.html>) | Redirect to `/about/` |
| `/about/` | [about/index.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/about/index.html>) | Ordinary public content; reviewed |
| `/about/operational-entropy-index/` | [about/operational-entropy-index/index.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/about/operational-entropy-index/index.html>) | Ordinary public content; reviewed |
| `/admin/diagnosis/` | [admin/diagnosis/index.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/admin/diagnosis/index.html>) | Internal/noindex; F20 |
| `/assessments/engagement-path/` | [assessments/engagement-path/index.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/assessments/engagement-path/index.html>) | Intentionally direct-only in site discovery; F19 |
| `/client-journey/` | [client-journey/index.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/client-journey/index.html>) | Ordinary public content; reviewed |
| `/contact.html` | [contact.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/contact.html>) | Redirect to `/contact/` |
| `/contact/` | [contact/index.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/contact/index.html>) | Ordinary public content; reviewed |
| `/entropy-compatible-hiring/` | [entropy-compatible-hiring/index.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/entropy-compatible-hiring/index.html>) | Ordinary public content; reviewed |
| `/executiondeficit.html` | [executiondeficit.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/executiondeficit.html>) | Redirect to `/insights/execution-deficit/` |
| `/founderdependency.html` | [founderdependency.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/founderdependency.html>) | Redirect to `/insights/founder-dependency/` |
| `/handoffintegrity.html` | [handoffintegrity.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/handoffintegrity.html>) | Redirect to `/insights/handoff-integrity/` |
| `/` | [index.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/index.html>) | Ordinary public content; reviewed |
| `/info.html` | [info.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/info.html>) | Redirect to `/resources/information-packet/` |
| `/insights/execution-deficit/` | [insights/execution-deficit/index.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/insights/execution-deficit/index.html>) | Ordinary public content; reviewed |
| `/insights/founder-dependency/` | [insights/founder-dependency/index.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/insights/founder-dependency/index.html>) | Ordinary public content; reviewed |
| `/insights/handoff-integrity/` | [insights/handoff-integrity/index.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/insights/handoff-integrity/index.html>) | Ordinary public content; reviewed |
| `/insights/knowledge-logistics/` | [insights/knowledge-logistics/index.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/insights/knowledge-logistics/index.html>) | Ordinary public content; reviewed |
| `/insights/operational-drag/` | [insights/operational-drag/index.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/insights/operational-drag/index.html>) | Ordinary public content; reviewed |
| `/insights/organizational-complexity-tax/` | [insights/organizational-complexity-tax/index.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/insights/organizational-complexity-tax/index.html>) | Ordinary public content; reviewed |
| `/insights/process-drift/` | [insights/process-drift/index.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/insights/process-drift/index.html>) | Ordinary public content; reviewed |
| `/insights/tool-discipline/` | [insights/tool-discipline/index.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/insights/tool-discipline/index.html>) | Ordinary public content; reviewed |
| `/insights/what-is-operational-entropy/` | [insights/what-is-operational-entropy/index.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/insights/what-is-operational-entropy/index.html>) | Ordinary public content; reviewed |
| `/insights/workflow-velocity/` | [insights/workflow-velocity/index.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/insights/workflow-velocity/index.html>) | Ordinary public content; reviewed |
| `/investigations.html` | [investigations.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/investigations.html>) | Redirect to `/services/focused-operational-investigations/` |
| `/knowledgelogistics.html` | [knowledgelogistics.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/knowledgelogistics.html>) | Redirect to `/insights/knowledge-logistics/` |
| `/oei_engagement_quiz.html` | [oei_engagement_quiz.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/oei_engagement_quiz.html>) | Redirect to `/assessments/engagement-path/`; unlisted compatibility, F19 |
| `/operationaldrag.html` | [operationaldrag.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/operationaldrag.html>) | Redirect to `/insights/operational-drag/` |
| `/operationaltax.html` | [operationaltax.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/operationaltax.html>) | Redirect to `/insights/organizational-complexity-tax/` |
| `/ops/propagation/` | [ops/propagation/index.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/ops/propagation/index.html>) | Internal/noindex; F20 |
| `/pricing.html` | [pricing.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/pricing.html>) | Redirect to `/temp-pricing/` |
| `/pricing/` | [pricing/index.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/pricing/index.html>) | Redirect to `/temp-pricing/` |
| `/productfd.html` | [productfd.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/productfd.html>) | Redirect to `/services/focused-operational-investigations/founder-absence-simulation/` |
| `/producthi.html` | [producthi.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/producthi.html>) | Redirect to `/services/focused-operational-investigations/handoff-failure-analysis/` |
| `/productkl.html` | [productkl.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/productkl.html>) | Redirect to `/services/focused-operational-investigations/institutional-memory-recovery/` |
| `/producttd.html` | [producttd.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/producttd.html>) | Redirect to `/services/focused-operational-investigations/operational-stack-review/` |
| `/productwv.html` | [productwv.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/productwv.html>) | Redirect to `/services/focused-operational-investigations/workflow-momentum-analysis/` |
| `/resources/information-packet/` | [resources/information-packet/index.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/resources/information-packet/index.html>) | Ordinary public content; reviewed |
| `/services.html` | [services.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/services.html>) | Redirect to `/services/`; missing landing target, F08 |
| `/services/focused-operational-investigations/founder-absence-simulation/` | [services/focused-operational-investigations/founder-absence-simulation/index.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/services/focused-operational-investigations/founder-absence-simulation/index.html>) | Ordinary public content; reviewed |
| `/services/focused-operational-investigations/handoff-failure-analysis/` | [services/focused-operational-investigations/handoff-failure-analysis/index.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/services/focused-operational-investigations/handoff-failure-analysis/index.html>) | Ordinary public content; reviewed |
| `/services/focused-operational-investigations/` | [services/focused-operational-investigations/index.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/services/focused-operational-investigations/index.html>) | Ordinary public content; reviewed |
| `/services/focused-operational-investigations/institutional-memory-recovery/` | [services/focused-operational-investigations/institutional-memory-recovery/index.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/services/focused-operational-investigations/institutional-memory-recovery/index.html>) | Ordinary public content; reviewed |
| `/services/focused-operational-investigations/operational-stack-review/` | [services/focused-operational-investigations/operational-stack-review/index.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/services/focused-operational-investigations/operational-stack-review/index.html>) | Ordinary public content; reviewed |
| `/services/focused-operational-investigations/workflow-momentum-analysis/` | [services/focused-operational-investigations/workflow-momentum-analysis/index.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/services/focused-operational-investigations/workflow-momentum-analysis/index.html>) | Ordinary public content; reviewed |
| `/services/founder-absence-simulation/` | [services/founder-absence-simulation/index.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/services/founder-absence-simulation/index.html>) | Redirect to `/services/focused-operational-investigations/founder-absence-simulation/` |
| `/services/handoff-failure-analysis/` | [services/handoff-failure-analysis/index.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/services/handoff-failure-analysis/index.html>) | Redirect to `/services/focused-operational-investigations/handoff-failure-analysis/` |
| `/services/institutional-memory-recovery/` | [services/institutional-memory-recovery/index.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/services/institutional-memory-recovery/index.html>) | Redirect to `/services/focused-operational-investigations/institutional-memory-recovery/` |
| `/services/operational-stack-review/` | [services/operational-stack-review/index.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/services/operational-stack-review/index.html>) | Redirect to `/services/focused-operational-investigations/operational-stack-review/` |
| `/services/workflow-momentum-analysis/` | [services/workflow-momentum-analysis/index.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/services/workflow-momentum-analysis/index.html>) | Redirect to `/services/focused-operational-investigations/workflow-momentum-analysis/` |
| `/site-navigation/` | [site-navigation/index.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/site-navigation/index.html>) | Ordinary public content; reviewed |
| `/temp-pricing/` | [temp-pricing/index.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/temp-pricing/index.html>) | Ordinary public content; reviewed |
| `/tooldiscipline.html` | [tooldiscipline.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/tooldiscipline.html>) | Redirect to `/insights/tool-discipline/` |
| `/whatisoei.html` | [whatisoei.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/whatisoei.html>) | Redirect to `/insights/what-is-operational-entropy/` |
| `/workflowvelocity.html` | [workflowvelocity.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/workflowvelocity.html>) | Redirect to `/insights/workflow-velocity/` |
| `/services/` | No landing file | In navigation/sitemap; F08 |

No independent temporary Services landing file was found. This is a route observation, not a capability finding. All aliases were inspected for refresh, script and canonical destinations; legacy naming alone is not a defect.

## Appendix B: Metadata Inventory

Every title, canonical, description and Open Graph field was inspected. Missing fields alone are not defects. Redirect titles/canonicals are listed as well as content pages. No JSON-LD/schema.org structured data was found.

### `/about.html`

- File: [about.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/about.html>)
- Title: Moved | Operational Entropy
- Canonical: https://operationalentropy.com/about/

### `/about/`

- File: [about/index.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/about/index.html>)
- Title: About the OEI Institute | Operational Entropy
- Canonical: https://operationalentropy.com/about/
- description: The OEI Institute governs the Operational Entropy Index methodology and maintains its practice standards. Operational Forensics for Growing Teams.
- og:title: About the OEI Institute | Operational Entropy
- og:description: The OEI Institute governs the Operational Entropy Index methodology and maintains its practice standards. Operational Forensics for Growing Teams.
- og:image: (none)
- robots: (none)

### `/about/operational-entropy-index/`

- File: [about/operational-entropy-index/index.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/about/operational-entropy-index/index.html>)
- Title: Rethinking Operations: Beyond Symptoms | Operational Entropy
- Canonical: https://operationalentropy.com/about/operational-entropy-index/
- description: We look where other consultants don't. Discover our unique methodology for identifying the structural 'connective tissue' failures in your organization.
- og:title: Rethinking Operations: Beyond Symptoms | Operational Entropy
- og:description: We look where other consultants don't. Discover our unique methodology for identifying the structural 'connective tissue' failures in your company.
- og:image: (none)
- robots: (none)

### `/admin/diagnosis/`

- File: [admin/diagnosis/index.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/admin/diagnosis/index.html>)
- Title: OEI Diagnosis Workspace
- Canonical: (none)
- description: (none)
- og:title: (none)
- og:description: (none)
- og:image: (none)
- robots: noindex,nofollow,noarchive

### `/assessments/engagement-path/`

- File: [assessments/engagement-path/index.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/assessments/engagement-path/index.html>)
- Title: Find Your Engagement Path | Operational Entropy
- Canonical: https://operationalentropy.com/assessments/engagement-path/
- description: Answer a few quick questions to discover which OEI service package is right for your organization.
- og:title: Find Your Engagement Path | Operational Entropy
- og:description: Answer a few quick questions to discover which OEI service package is right for your company.
- og:image: (none)
- robots: (none)

### `/client-journey/`

- File: [client-journey/index.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/client-journey/index.html>)
- Title: Your Client's Journey Reflects Your Entropy | OEI
- Canonical: https://operationalentropy.com/client-journey/
- description: See how internal operational entropy becomes visible through repeated questions, missed commitments, broken handoffs, and other client expectation violations.
- og:title: (none)
- og:description: (none)
- og:image: (none)
- robots: (none)

### `/contact.html`

- File: [contact.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/contact.html>)
- Title: Moved | Operational Entropy
- Canonical: https://operationalentropy.com/contact/

### `/contact/`

- File: [contact/index.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/contact/index.html>)
- Title: Contact Operational Entropy | Fix Your Scaling Process
- Canonical: https://operationalentropy.com/contact/
- description: Ready to diagnose your organizational drag? Reach out for an initial conversation about stabilizing your scaling process.
- og:title: Contact Operational Entropy | Fix Your Scaling Process
- og:description: Ready to diagnose your organizational drag? Reach out for an initial conversation about stabilizing your scaling process.
- og:image: (none)
- robots: (none)

### `/entropy-compatible-hiring/`

- File: [entropy-compatible-hiring/index.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/entropy-compatible-hiring/index.html>)
- Title: Entropy Compatible Hiring Software - Version 0.1.3 BETA | OEI
- Canonical: https://operationalentropy.com/entropy-compatible-hiring/
- description: Structured hiring instruments and existing-employee contribution mapping for observing behaviors that can reduce operational entropy.
- og:title: Entropy Compatible Hiring Software - Version 0.1.3 BETA
- og:description: Observe operational behavior through structured hiring exercises and existing-employee contribution mapping.
- og:image: (none)
- robots: (none)

### `/executiondeficit.html`

- File: [executiondeficit.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/executiondeficit.html>)
- Title: Moved | Operational Entropy
- Canonical: https://operationalentropy.com/insights/execution-deficit/

### `/founderdependency.html`

- File: [founderdependency.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/founderdependency.html>)
- Title: Moved | Operational Entropy
- Canonical: https://operationalentropy.com/insights/founder-dependency/

### `/handoffintegrity.html`

- File: [handoffintegrity.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/handoffintegrity.html>)
- Title: Moved | Operational Entropy
- Canonical: https://operationalentropy.com/insights/handoff-integrity/

### `/`

- File: [index.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/index.html>)
- Title: Revert Operational Drag & Scalability | Operational Entropy
- Canonical: https://operationalentropy.com/
- description: Stop losing money to wasted time. We analyze your company's 'connective tissue' to identify and fix the structural drag draining your growth.
- og:title: Revert Operational Drag | Operational Entropy
- og:description: Stop losing money to wasted time. We analyze your company's 'connective tissue' to identify and fix the structural drag draining your growth.
- og:image: (none)
- robots: (none)

### `/info.html`

- File: [info.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/info.html>)
- Title: Moved | Operational Entropy
- Canonical: https://operationalentropy.com/resources/information-packet/

### `/insights/execution-deficit/`

- File: [insights/execution-deficit/index.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/insights/execution-deficit/index.html>)
- Title: The Execution Deficit: Intent vs. Reliable Execution | OEI
- Canonical: https://operationalentropy.com/insights/execution-deficit/
- description: Understand the gap between organizational intent and reliable execution, how the five OEI pillars may contribute, and how compensation can conceal it.
- og:title: (none)
- og:description: (none)
- og:image: (none)
- robots: (none)

### `/insights/founder-dependency/`

- File: [insights/founder-dependency/index.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/insights/founder-dependency/index.html>)
- Title: OEI Pillar Deep Dive: Founder Dependency
- Canonical: https://operationalentropy.com/insights/founder-dependency/
- description: Understand the impact of Founder Dependency on organizational scalability and how to transition from individual leadership to robust operational systems.
- og:title: (none)
- og:description: (none)
- og:image: (none)
- robots: (none)

### `/insights/handoff-integrity/`

- File: [insights/handoff-integrity/index.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/insights/handoff-integrity/index.html>)
- Title: Handoff Integrity | Operational Entropy
- Canonical: https://operationalentropy.com/insights/handoff-integrity/
- description: Explore Handoff Integrity: the measure of how effectively information, context, and accountability transfer between teams to ensure seamless execution.
- og:title: (none)
- og:description: (none)
- og:image: (none)
- robots: (none)

### `/insights/knowledge-logistics/`

- File: [insights/knowledge-logistics/index.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/insights/knowledge-logistics/index.html>)
- Title: OEI Pillar Deep Dive: Knowledge Logistics
- Canonical: https://operationalentropy.com/insights/knowledge-logistics/
- description: Discover how Knowledge Logistics impacts your organization's ability to preserve, discover, and apply knowledge as it scales.
- og:title: (none)
- og:description: (none)
- og:image: (none)
- robots: (none)

### `/insights/operational-drag/`

- File: [insights/operational-drag/index.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/insights/operational-drag/index.html>)
- Title: Operational Drag: Meaning, Causes & Solutions | OEI
- Canonical: https://operationalentropy.com/insights/operational-drag/
- description: Operational drag is the friction that makes work take longer as a company grows. Learn its causes, warning signs, examples, and practical ways to reduce it.
- og:title: (none)
- og:description: (none)
- og:image: (none)
- robots: (none)

### `/insights/organizational-complexity-tax/`

- File: [insights/organizational-complexity-tax/index.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/insights/organizational-complexity-tax/index.html>)
- Title: The Organizational Complexity Tax | Operational Entropy
- Canonical: https://operationalentropy.com/insights/organizational-complexity-tax/
- description: Understand the hidden cost of organizational complexity. Learn how to identify the 'complexity tax' draining your team's productivity and how the OEI helps you reclaim your margins.
- og:title: (none)
- og:description: (none)
- og:image: (none)
- robots: (none)

### `/insights/process-drift/`

- File: [insights/process-drift/index.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/insights/process-drift/index.html>)
- Title: Process Drift: Meaning, Signals & Investigation | OEI
- Canonical: https://operationalentropy.com/insights/process-drift/
- description: Learn how OEI understands Process Drift, why compensation can conceal it, which operating conditions contribute, and how evidence distinguishes drift from useful adaptation.
- og:title: (none)
- og:description: (none)
- og:image: (none)
- robots: (none)

### `/insights/tool-discipline/`

- File: [insights/tool-discipline/index.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/insights/tool-discipline/index.html>)
- Title: OEI Pillar Deep Dive: Tool Discipline
- Canonical: https://operationalentropy.com/insights/tool-discipline/
- description: Learn how Tool Discipline ensures your software ecosystem supports your organizational goals.
- og:title: (none)
- og:description: (none)
- og:image: (none)
- robots: (none)

### `/insights/what-is-operational-entropy/`

- File: [insights/what-is-operational-entropy/index.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/insights/what-is-operational-entropy/index.html>)
- Title: Operational Entropy: Definition, Examples & Solutions | OEI
- Canonical: https://operationalentropy.com/insights/what-is-operational-entropy/
- description: Operational entropy is the disorder and friction that accumulate as companies grow. Learn its causes, warning signs, examples, and ways to reduce it.
- og:title: (none)
- og:description: (none)
- og:image: (none)
- robots: (none)

### `/insights/workflow-velocity/`

- File: [insights/workflow-velocity/index.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/insights/workflow-velocity/index.html>)
- Title: OEI Pillar Deep Dive: Workflow Velocity
- Canonical: https://operationalentropy.com/insights/workflow-velocity/
- description: Understand how Workflow Velocity measures uninterrupted progress and identifies the structural friction preventing your team from turning effort into output.
- og:title: (none)
- og:description: (none)
- og:image: (none)
- robots: (none)

### `/investigations.html`

- File: [investigations.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/investigations.html>)
- Title: Moved | Operational Entropy
- Canonical: https://operationalentropy.com/services/focused-operational-investigations/

### `/knowledgelogistics.html`

- File: [knowledgelogistics.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/knowledgelogistics.html>)
- Title: Moved | Operational Entropy
- Canonical: https://operationalentropy.com/insights/knowledge-logistics/

### `/oei_engagement_quiz.html`

- File: [oei_engagement_quiz.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/oei_engagement_quiz.html>)
- Title: Moved | Operational Entropy
- Canonical: https://operationalentropy.com/assessments/engagement-path/

### `/operationaldrag.html`

- File: [operationaldrag.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/operationaldrag.html>)
- Title: Moved | Operational Entropy
- Canonical: https://operationalentropy.com/insights/operational-drag/

### `/operationaltax.html`

- File: [operationaltax.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/operationaltax.html>)
- Title: Moved | Operational Entropy
- Canonical: https://operationalentropy.com/insights/organizational-complexity-tax/

### `/ops/propagation/`

- File: [ops/propagation/index.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/ops/propagation/index.html>)
- Title: Identity Propagation | OEI Operations
- Canonical: (none)
- description: OEI identity change and propagation dashboard.
- og:title: (none)
- og:description: (none)
- og:image: (none)
- robots: noindex, nofollow

### `/pricing.html`

- File: [pricing.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/pricing.html>)
- Title: Pricing Update | Operational Entropy
- Canonical: https://operationalentropy.com/temp-pricing/

### `/pricing/`

- File: [pricing/index.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/pricing/index.html>)
- Title: Pricing Update | Operational Entropy
- Canonical: https://operationalentropy.com/temp-pricing/

### `/productfd.html`

- File: [productfd.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/productfd.html>)
- Title: Moved | Operational Entropy
- Canonical: https://operationalentropy.com/services/focused-operational-investigations/founder-absence-simulation/

### `/producthi.html`

- File: [producthi.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/producthi.html>)
- Title: Moved | Operational Entropy
- Canonical: https://operationalentropy.com/services/focused-operational-investigations/handoff-failure-analysis/

### `/productkl.html`

- File: [productkl.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/productkl.html>)
- Title: Moved | Operational Entropy
- Canonical: https://operationalentropy.com/services/focused-operational-investigations/institutional-memory-recovery/

### `/producttd.html`

- File: [producttd.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/producttd.html>)
- Title: Moved | Operational Entropy
- Canonical: https://operationalentropy.com/services/focused-operational-investigations/operational-stack-review/

### `/productwv.html`

- File: [productwv.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/productwv.html>)
- Title: Moved | Operational Entropy
- Canonical: https://operationalentropy.com/services/focused-operational-investigations/workflow-momentum-analysis/

### `/resources/information-packet/`

- File: [resources/information-packet/index.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/resources/information-packet/index.html>)
- Title: Information Packet | Operational Entropy
- Canonical: https://operationalentropy.com/resources/information-packet/
- description: (none)
- og:title: (none)
- og:description: (none)
- og:image: (none)
- robots: (none)

### `/services.html`

- File: [services.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/services.html>)
- Title: Moved | Operational Entropy
- Canonical: https://operationalentropy.com/services/

### `/services/focused-operational-investigations/founder-absence-simulation/`

- File: [services/focused-operational-investigations/founder-absence-simulation/index.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/services/focused-operational-investigations/founder-absence-simulation/index.html>)
- Title: OEI Service: Founder Absence Simulation
- Canonical: https://operationalentropy.com/services/focused-operational-investigations/founder-absence-simulation/
- description: An operational stress test designed to identify business dependencies and determine what breaks when the founder is no longer available.
- og:title: (none)
- og:description: (none)
- og:image: (none)
- robots: (none)

### `/services/focused-operational-investigations/handoff-failure-analysis/`

- File: [services/focused-operational-investigations/handoff-failure-analysis/index.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/services/focused-operational-investigations/handoff-failure-analysis/index.html>)
- Title: OEI Service: Handoff Failure Analysis
- Canonical: https://operationalentropy.com/services/focused-operational-investigations/handoff-failure-analysis/
- description: An operational investigation designed to identify where information, context, and execution readiness break down as work moves between teams.
- og:title: (none)
- og:description: (none)
- og:image: (none)
- robots: (none)

### `/services/focused-operational-investigations/`

- File: [services/focused-operational-investigations/index.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/services/focused-operational-investigations/index.html>)
- Title: Focused Operational Investigations | Operational Entropy
- Canonical: https://operationalentropy.com/services/focused-operational-investigations/
- description: Identify root causes and restore momentum with our targeted Focused Operational Investigations.
- og:title: Focused Operational Investigations | Operational Entropy
- og:description: Identify root causes and restore momentum with our targeted Focused Operational Investigations.
- og:image: (none)
- robots: (none)

### `/services/focused-operational-investigations/institutional-memory-recovery/`

- File: [services/focused-operational-investigations/institutional-memory-recovery/index.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/services/focused-operational-investigations/institutional-memory-recovery/index.html>)
- Title: OEI Service: Institutional Memory Recovery Sprint
- Canonical: https://operationalentropy.com/services/focused-operational-investigations/institutional-memory-recovery/
- description: A process to identify critical knowledge trapped inside people and transform it into operational assets your company can retain, access, and use.
- og:title: (none)
- og:description: (none)
- og:image: (none)
- robots: (none)

### `/services/focused-operational-investigations/operational-stack-review/`

- File: [services/focused-operational-investigations/operational-stack-review/index.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/services/focused-operational-investigations/operational-stack-review/index.html>)
- Title: OEI Service: Operational Stack Review
- Canonical: https://operationalentropy.com/services/focused-operational-investigations/operational-stack-review/
- description: An investigation designed to determine whether your technology ecosystem supports the way your company operates, or if it's creating operational entropy.
- og:title: (none)
- og:description: (none)
- og:image: (none)
- robots: (none)

### `/services/focused-operational-investigations/workflow-momentum-analysis/`

- File: [services/focused-operational-investigations/workflow-momentum-analysis/index.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/services/focused-operational-investigations/workflow-momentum-analysis/index.html>)
- Title: OEI Service: Workflow Momentum Analysis
- Canonical: https://operationalentropy.com/services/focused-operational-investigations/workflow-momentum-analysis/
- description: An operational investigation designed to identify where work loses momentum, why it stalls, and how to restore reliable execution.
- og:title: (none)
- og:description: (none)
- og:image: (none)
- robots: (none)

### `/services/founder-absence-simulation/`

- File: [services/founder-absence-simulation/index.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/services/founder-absence-simulation/index.html>)
- Title: Moved | Operational Entropy
- Canonical: https://operationalentropy.com/services/focused-operational-investigations/founder-absence-simulation/

### `/services/handoff-failure-analysis/`

- File: [services/handoff-failure-analysis/index.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/services/handoff-failure-analysis/index.html>)
- Title: Moved | Operational Entropy
- Canonical: https://operationalentropy.com/services/focused-operational-investigations/handoff-failure-analysis/

### `/services/institutional-memory-recovery/`

- File: [services/institutional-memory-recovery/index.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/services/institutional-memory-recovery/index.html>)
- Title: Moved | Operational Entropy
- Canonical: https://operationalentropy.com/services/focused-operational-investigations/institutional-memory-recovery/

### `/services/operational-stack-review/`

- File: [services/operational-stack-review/index.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/services/operational-stack-review/index.html>)
- Title: Moved | Operational Entropy
- Canonical: https://operationalentropy.com/services/focused-operational-investigations/operational-stack-review/

### `/services/workflow-momentum-analysis/`

- File: [services/workflow-momentum-analysis/index.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/services/workflow-momentum-analysis/index.html>)
- Title: Moved | Operational Entropy
- Canonical: https://operationalentropy.com/services/focused-operational-investigations/workflow-momentum-analysis/

### `/site-navigation/`

- File: [site-navigation/index.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/site-navigation/index.html>)
- Title: Site Navigation | Operational Entropy
- Canonical: https://operationalentropy.com/site-navigation/
- description: Follow organized paths through Operational Entropy concepts, diagnostic categories, services, investigations, pricing, and resources.
- og:title: (none)
- og:description: (none)
- og:image: (none)
- robots: (none)

### `/temp-pricing/`

- File: [temp-pricing/index.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/temp-pricing/index.html>)
- Title: Pricing Update | Operational Entropy
- Canonical: https://operationalentropy.com/temp-pricing/
- description: The Operational Entropy pricing structure is being overhauled. Contact Fletcher or schedule a discovery call to discuss your needs.
- og:title: Pricing Update | Operational Entropy
- og:description: The Operational Entropy pricing structure is being overhauled. Get in touch to discuss your needs.
- og:image: (none)
- robots: (none)

### `/tooldiscipline.html`

- File: [tooldiscipline.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/tooldiscipline.html>)
- Title: Moved | Operational Entropy
- Canonical: https://operationalentropy.com/insights/tool-discipline/

### `/whatisoei.html`

- File: [whatisoei.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/whatisoei.html>)
- Title: Moved | Operational Entropy
- Canonical: https://operationalentropy.com/insights/what-is-operational-entropy/

### `/workflowvelocity.html`

- File: [workflowvelocity.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/workflowvelocity.html>)
- Title: Moved | Operational Entropy
- Canonical: https://operationalentropy.com/insights/workflow-velocity/

## Appendix C: PDF Evidence

| Public file | Pages reviewed | Evidence | Findings |
|---|---|---|---|
| `info/About the Operational Entropy Index.pdf` | 1–2 | Current overview; tool/process definition; consulting ways to work; ECH v0.1.0; Fletcher GH Consulting and confidentiality headers | F12, F15, F16 |
| `info/OEI Services and Pricing.pdf` | 1–3 | Current engagement paths; fees/revenue tiers, payment terms, prerequisites, independent investigations/ECH v0.1.0 | F12, F15, F16 |
| `info/OEI TLDR.pdf` | 1 | Baseline fee table, pathway rule and provider/confidentiality headers | F12, F15, F16 |

`scripts/update_oei_pdfs.py` is the regeneration source. Public packet/directory links continue to distribute these PDFs as current references. No PDF was edited.

## Appendix D: Exact Affected-File Groups and Evidence Anchors

These lists enumerate repeated occurrences without multiplying strategic findings. Routes map one-to-one through Appendix A. All paths below are clickable source references.

### G01 / F01 (24 ordinary pages)

- `/about/operational-entropy-index/`: [about/operational-entropy-index/index.html:244](<C:/Users/Fletch/Documents/GitHub/operationalentropy/about/operational-entropy-index/index.html:244>)
- `/client-journey/`: [client-journey/index.html:157](<C:/Users/Fletch/Documents/GitHub/operationalentropy/client-journey/index.html:157>)
- `/contact/`: [contact/index.html:278](<C:/Users/Fletch/Documents/GitHub/operationalentropy/contact/index.html:278>)
- `/entropy-compatible-hiring/`: [entropy-compatible-hiring/index.html:442](<C:/Users/Fletch/Documents/GitHub/operationalentropy/entropy-compatible-hiring/index.html:442>)
- `/`: [index.html:231](<C:/Users/Fletch/Documents/GitHub/operationalentropy/index.html:231>)
- `/insights/execution-deficit/`: [insights/execution-deficit/index.html:103](<C:/Users/Fletch/Documents/GitHub/operationalentropy/insights/execution-deficit/index.html:103>)
- `/insights/founder-dependency/`: [insights/founder-dependency/index.html:160](<C:/Users/Fletch/Documents/GitHub/operationalentropy/insights/founder-dependency/index.html:160>)
- `/insights/handoff-integrity/`: [insights/handoff-integrity/index.html:141](<C:/Users/Fletch/Documents/GitHub/operationalentropy/insights/handoff-integrity/index.html:141>)
- `/insights/knowledge-logistics/`: [insights/knowledge-logistics/index.html:140](<C:/Users/Fletch/Documents/GitHub/operationalentropy/insights/knowledge-logistics/index.html:140>)
- `/insights/operational-drag/`: [insights/operational-drag/index.html:129](<C:/Users/Fletch/Documents/GitHub/operationalentropy/insights/operational-drag/index.html:129>)
- `/insights/organizational-complexity-tax/`: [insights/organizational-complexity-tax/index.html:87](<C:/Users/Fletch/Documents/GitHub/operationalentropy/insights/organizational-complexity-tax/index.html:87>)
- `/insights/process-drift/`: [insights/process-drift/index.html:123](<C:/Users/Fletch/Documents/GitHub/operationalentropy/insights/process-drift/index.html:123>)
- `/insights/tool-discipline/`: [insights/tool-discipline/index.html:140](<C:/Users/Fletch/Documents/GitHub/operationalentropy/insights/tool-discipline/index.html:140>)
- `/insights/what-is-operational-entropy/`: [insights/what-is-operational-entropy/index.html:194](<C:/Users/Fletch/Documents/GitHub/operationalentropy/insights/what-is-operational-entropy/index.html:194>)
- `/insights/workflow-velocity/`: [insights/workflow-velocity/index.html:140](<C:/Users/Fletch/Documents/GitHub/operationalentropy/insights/workflow-velocity/index.html:140>)
- `/resources/information-packet/`: [resources/information-packet/index.html:61](<C:/Users/Fletch/Documents/GitHub/operationalentropy/resources/information-packet/index.html:61>)
- `/services/focused-operational-investigations/founder-absence-simulation/`: [services/focused-operational-investigations/founder-absence-simulation/index.html:174](<C:/Users/Fletch/Documents/GitHub/operationalentropy/services/focused-operational-investigations/founder-absence-simulation/index.html:174>)
- `/services/focused-operational-investigations/handoff-failure-analysis/`: [services/focused-operational-investigations/handoff-failure-analysis/index.html:183](<C:/Users/Fletch/Documents/GitHub/operationalentropy/services/focused-operational-investigations/handoff-failure-analysis/index.html:183>)
- `/services/focused-operational-investigations/`: [services/focused-operational-investigations/index.html:150](<C:/Users/Fletch/Documents/GitHub/operationalentropy/services/focused-operational-investigations/index.html:150>)
- `/services/focused-operational-investigations/institutional-memory-recovery/`: [services/focused-operational-investigations/institutional-memory-recovery/index.html:174](<C:/Users/Fletch/Documents/GitHub/operationalentropy/services/focused-operational-investigations/institutional-memory-recovery/index.html:174>)
- `/services/focused-operational-investigations/operational-stack-review/`: [services/focused-operational-investigations/operational-stack-review/index.html:181](<C:/Users/Fletch/Documents/GitHub/operationalentropy/services/focused-operational-investigations/operational-stack-review/index.html:181>)
- `/services/focused-operational-investigations/workflow-momentum-analysis/`: [services/focused-operational-investigations/workflow-momentum-analysis/index.html:184](<C:/Users/Fletch/Documents/GitHub/operationalentropy/services/focused-operational-investigations/workflow-momentum-analysis/index.html:184>)
- `/site-navigation/`: [site-navigation/index.html:127](<C:/Users/Fletch/Documents/GitHub/operationalentropy/site-navigation/index.html:127>)
- `/temp-pricing/`: [temp-pricing/index.html:49](<C:/Users/Fletch/Documents/GitHub/operationalentropy/temp-pricing/index.html:49>)

### G07 / F07 (7 ordinary pages)

- `/about/`: [about/index.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/about/index.html>)
- `/about/operational-entropy-index/`: [about/operational-entropy-index/index.html:69](<C:/Users/Fletch/Documents/GitHub/operationalentropy/about/operational-entropy-index/index.html:69>)
- `/entropy-compatible-hiring/`: [entropy-compatible-hiring/index.html:64](<C:/Users/Fletch/Documents/GitHub/operationalentropy/entropy-compatible-hiring/index.html:64>)
- `/`: [index.html:106](<C:/Users/Fletch/Documents/GitHub/operationalentropy/index.html:106>)
- `/insights/what-is-operational-entropy/`: [insights/what-is-operational-entropy/index.html:50](<C:/Users/Fletch/Documents/GitHub/operationalentropy/insights/what-is-operational-entropy/index.html:50>)
- `/services/focused-operational-investigations/`: [services/focused-operational-investigations/index.html:140](<C:/Users/Fletch/Documents/GitHub/operationalentropy/services/focused-operational-investigations/index.html:140>)
- `/site-navigation/`: [site-navigation/index.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/site-navigation/index.html>)

### G08 / F08 (25 ordinary pages)

- `/about/`: [about/index.html:25](<C:/Users/Fletch/Documents/GitHub/operationalentropy/about/index.html:25>)
- `/about/operational-entropy-index/`: [about/operational-entropy-index/index.html:25](<C:/Users/Fletch/Documents/GitHub/operationalentropy/about/operational-entropy-index/index.html:25>)
- `/client-journey/`: [client-journey/index.html:20](<C:/Users/Fletch/Documents/GitHub/operationalentropy/client-journey/index.html:20>)
- `/contact/`: [contact/index.html:26](<C:/Users/Fletch/Documents/GitHub/operationalentropy/contact/index.html:26>)
- `/entropy-compatible-hiring/`: [entropy-compatible-hiring/index.html:25](<C:/Users/Fletch/Documents/GitHub/operationalentropy/entropy-compatible-hiring/index.html:25>)
- `/`: [index.html:24](<C:/Users/Fletch/Documents/GitHub/operationalentropy/index.html:24>)
- `/insights/execution-deficit/`: [insights/execution-deficit/index.html:17](<C:/Users/Fletch/Documents/GitHub/operationalentropy/insights/execution-deficit/index.html:17>)
- `/insights/founder-dependency/`: [insights/founder-dependency/index.html:23](<C:/Users/Fletch/Documents/GitHub/operationalentropy/insights/founder-dependency/index.html:23>)
- `/insights/handoff-integrity/`: [insights/handoff-integrity/index.html:23](<C:/Users/Fletch/Documents/GitHub/operationalentropy/insights/handoff-integrity/index.html:23>)
- `/insights/knowledge-logistics/`: [insights/knowledge-logistics/index.html:23](<C:/Users/Fletch/Documents/GitHub/operationalentropy/insights/knowledge-logistics/index.html:23>)
- `/insights/operational-drag/`: [insights/operational-drag/index.html:23](<C:/Users/Fletch/Documents/GitHub/operationalentropy/insights/operational-drag/index.html:23>)
- `/insights/organizational-complexity-tax/`: [insights/organizational-complexity-tax/index.html:23](<C:/Users/Fletch/Documents/GitHub/operationalentropy/insights/organizational-complexity-tax/index.html:23>)
- `/insights/process-drift/`: [insights/process-drift/index.html:18](<C:/Users/Fletch/Documents/GitHub/operationalentropy/insights/process-drift/index.html:18>)
- `/insights/tool-discipline/`: [insights/tool-discipline/index.html:23](<C:/Users/Fletch/Documents/GitHub/operationalentropy/insights/tool-discipline/index.html:23>)
- `/insights/what-is-operational-entropy/`: [insights/what-is-operational-entropy/index.html:23](<C:/Users/Fletch/Documents/GitHub/operationalentropy/insights/what-is-operational-entropy/index.html:23>)
- `/insights/workflow-velocity/`: [insights/workflow-velocity/index.html:23](<C:/Users/Fletch/Documents/GitHub/operationalentropy/insights/workflow-velocity/index.html:23>)
- `/resources/information-packet/`: [resources/information-packet/index.html:21](<C:/Users/Fletch/Documents/GitHub/operationalentropy/resources/information-packet/index.html:21>)
- `/services/focused-operational-investigations/founder-absence-simulation/`: [services/focused-operational-investigations/founder-absence-simulation/index.html:23](<C:/Users/Fletch/Documents/GitHub/operationalentropy/services/focused-operational-investigations/founder-absence-simulation/index.html:23>)
- `/services/focused-operational-investigations/handoff-failure-analysis/`: [services/focused-operational-investigations/handoff-failure-analysis/index.html:23](<C:/Users/Fletch/Documents/GitHub/operationalentropy/services/focused-operational-investigations/handoff-failure-analysis/index.html:23>)
- `/services/focused-operational-investigations/`: [services/focused-operational-investigations/index.html:25](<C:/Users/Fletch/Documents/GitHub/operationalentropy/services/focused-operational-investigations/index.html:25>)
- `/services/focused-operational-investigations/institutional-memory-recovery/`: [services/focused-operational-investigations/institutional-memory-recovery/index.html:23](<C:/Users/Fletch/Documents/GitHub/operationalentropy/services/focused-operational-investigations/institutional-memory-recovery/index.html:23>)
- `/services/focused-operational-investigations/operational-stack-review/`: [services/focused-operational-investigations/operational-stack-review/index.html:22](<C:/Users/Fletch/Documents/GitHub/operationalentropy/services/focused-operational-investigations/operational-stack-review/index.html:22>)
- `/services/focused-operational-investigations/workflow-momentum-analysis/`: [services/focused-operational-investigations/workflow-momentum-analysis/index.html:23](<C:/Users/Fletch/Documents/GitHub/operationalentropy/services/focused-operational-investigations/workflow-momentum-analysis/index.html:23>)
- `/site-navigation/`: [site-navigation/index.html:20](<C:/Users/Fletch/Documents/GitHub/operationalentropy/site-navigation/index.html:20>)
- `/temp-pricing/`: [temp-pricing/index.html:22](<C:/Users/Fletch/Documents/GitHub/operationalentropy/temp-pricing/index.html:22>)

### G13 / F13 (24 ordinary pages)

- `/about/`: [about/index.html:30](<C:/Users/Fletch/Documents/GitHub/operationalentropy/about/index.html:30>)
- `/about/operational-entropy-index/`: [about/operational-entropy-index/index.html:30](<C:/Users/Fletch/Documents/GitHub/operationalentropy/about/operational-entropy-index/index.html:30>)
- `/client-journey/`: [client-journey/index.html:24](<C:/Users/Fletch/Documents/GitHub/operationalentropy/client-journey/index.html:24>)
- `/contact/`: [contact/index.html:31](<C:/Users/Fletch/Documents/GitHub/operationalentropy/contact/index.html:31>)
- `/`: [index.html:29](<C:/Users/Fletch/Documents/GitHub/operationalentropy/index.html:29>)
- `/insights/execution-deficit/`: [insights/execution-deficit/index.html:18](<C:/Users/Fletch/Documents/GitHub/operationalentropy/insights/execution-deficit/index.html:18>)
- `/insights/founder-dependency/`: [insights/founder-dependency/index.html:28](<C:/Users/Fletch/Documents/GitHub/operationalentropy/insights/founder-dependency/index.html:28>)
- `/insights/handoff-integrity/`: [insights/handoff-integrity/index.html:28](<C:/Users/Fletch/Documents/GitHub/operationalentropy/insights/handoff-integrity/index.html:28>)
- `/insights/knowledge-logistics/`: [insights/knowledge-logistics/index.html:28](<C:/Users/Fletch/Documents/GitHub/operationalentropy/insights/knowledge-logistics/index.html:28>)
- `/insights/operational-drag/`: [insights/operational-drag/index.html:28](<C:/Users/Fletch/Documents/GitHub/operationalentropy/insights/operational-drag/index.html:28>)
- `/insights/organizational-complexity-tax/`: [insights/organizational-complexity-tax/index.html:28](<C:/Users/Fletch/Documents/GitHub/operationalentropy/insights/organizational-complexity-tax/index.html:28>)
- `/insights/process-drift/`: [insights/process-drift/index.html:20](<C:/Users/Fletch/Documents/GitHub/operationalentropy/insights/process-drift/index.html:20>)
- `/insights/tool-discipline/`: [insights/tool-discipline/index.html:28](<C:/Users/Fletch/Documents/GitHub/operationalentropy/insights/tool-discipline/index.html:28>)
- `/insights/what-is-operational-entropy/`: [insights/what-is-operational-entropy/index.html:28](<C:/Users/Fletch/Documents/GitHub/operationalentropy/insights/what-is-operational-entropy/index.html:28>)
- `/insights/workflow-velocity/`: [insights/workflow-velocity/index.html:28](<C:/Users/Fletch/Documents/GitHub/operationalentropy/insights/workflow-velocity/index.html:28>)
- `/resources/information-packet/`: [resources/information-packet/index.html:26](<C:/Users/Fletch/Documents/GitHub/operationalentropy/resources/information-packet/index.html:26>)
- `/services/focused-operational-investigations/founder-absence-simulation/`: [services/focused-operational-investigations/founder-absence-simulation/index.html:28](<C:/Users/Fletch/Documents/GitHub/operationalentropy/services/focused-operational-investigations/founder-absence-simulation/index.html:28>)
- `/services/focused-operational-investigations/handoff-failure-analysis/`: [services/focused-operational-investigations/handoff-failure-analysis/index.html:28](<C:/Users/Fletch/Documents/GitHub/operationalentropy/services/focused-operational-investigations/handoff-failure-analysis/index.html:28>)
- `/services/focused-operational-investigations/`: [services/focused-operational-investigations/index.html:30](<C:/Users/Fletch/Documents/GitHub/operationalentropy/services/focused-operational-investigations/index.html:30>)
- `/services/focused-operational-investigations/institutional-memory-recovery/`: [services/focused-operational-investigations/institutional-memory-recovery/index.html:28](<C:/Users/Fletch/Documents/GitHub/operationalentropy/services/focused-operational-investigations/institutional-memory-recovery/index.html:28>)
- `/services/focused-operational-investigations/operational-stack-review/`: [services/focused-operational-investigations/operational-stack-review/index.html:27](<C:/Users/Fletch/Documents/GitHub/operationalentropy/services/focused-operational-investigations/operational-stack-review/index.html:27>)
- `/services/focused-operational-investigations/workflow-momentum-analysis/`: [services/focused-operational-investigations/workflow-momentum-analysis/index.html:28](<C:/Users/Fletch/Documents/GitHub/operationalentropy/services/focused-operational-investigations/workflow-momentum-analysis/index.html:28>)
- `/site-navigation/`: [site-navigation/index.html:24](<C:/Users/Fletch/Documents/GitHub/operationalentropy/site-navigation/index.html:24>)
- `/temp-pricing/`: [temp-pricing/index.html:26](<C:/Users/Fletch/Documents/GitHub/operationalentropy/temp-pricing/index.html:26>)

### G16 / F16 (24 ordinary pages)

- `/about/`: [about/index.html:140](<C:/Users/Fletch/Documents/GitHub/operationalentropy/about/index.html:140>)
- `/about/operational-entropy-index/`: [about/operational-entropy-index/index.html:272](<C:/Users/Fletch/Documents/GitHub/operationalentropy/about/operational-entropy-index/index.html:272>)
- `/client-journey/`: [client-journey/index.html:162](<C:/Users/Fletch/Documents/GitHub/operationalentropy/client-journey/index.html:162>)
- `/contact/`: [contact/index.html:304](<C:/Users/Fletch/Documents/GitHub/operationalentropy/contact/index.html:304>)
- `/entropy-compatible-hiring/`: [entropy-compatible-hiring/index.html:447](<C:/Users/Fletch/Documents/GitHub/operationalentropy/entropy-compatible-hiring/index.html:447>)
- `/`: [index.html:257](<C:/Users/Fletch/Documents/GitHub/operationalentropy/index.html:257>)
- `/insights/execution-deficit/`: [insights/execution-deficit/index.html:108](<C:/Users/Fletch/Documents/GitHub/operationalentropy/insights/execution-deficit/index.html:108>)
- `/insights/founder-dependency/`: [insights/founder-dependency/index.html:186](<C:/Users/Fletch/Documents/GitHub/operationalentropy/insights/founder-dependency/index.html:186>)
- `/insights/handoff-integrity/`: [insights/handoff-integrity/index.html:167](<C:/Users/Fletch/Documents/GitHub/operationalentropy/insights/handoff-integrity/index.html:167>)
- `/insights/knowledge-logistics/`: [insights/knowledge-logistics/index.html:166](<C:/Users/Fletch/Documents/GitHub/operationalentropy/insights/knowledge-logistics/index.html:166>)
- `/insights/operational-drag/`: [insights/operational-drag/index.html:155](<C:/Users/Fletch/Documents/GitHub/operationalentropy/insights/operational-drag/index.html:155>)
- `/insights/organizational-complexity-tax/`: [insights/organizational-complexity-tax/index.html:113](<C:/Users/Fletch/Documents/GitHub/operationalentropy/insights/organizational-complexity-tax/index.html:113>)
- `/insights/process-drift/`: [insights/process-drift/index.html:128](<C:/Users/Fletch/Documents/GitHub/operationalentropy/insights/process-drift/index.html:128>)
- `/insights/tool-discipline/`: [insights/tool-discipline/index.html:166](<C:/Users/Fletch/Documents/GitHub/operationalentropy/insights/tool-discipline/index.html:166>)
- `/insights/what-is-operational-entropy/`: [insights/what-is-operational-entropy/index.html:220](<C:/Users/Fletch/Documents/GitHub/operationalentropy/insights/what-is-operational-entropy/index.html:220>)
- `/insights/workflow-velocity/`: [insights/workflow-velocity/index.html:166](<C:/Users/Fletch/Documents/GitHub/operationalentropy/insights/workflow-velocity/index.html:166>)
- `/services/focused-operational-investigations/founder-absence-simulation/`: [services/focused-operational-investigations/founder-absence-simulation/index.html:201](<C:/Users/Fletch/Documents/GitHub/operationalentropy/services/focused-operational-investigations/founder-absence-simulation/index.html:201>)
- `/services/focused-operational-investigations/handoff-failure-analysis/`: [services/focused-operational-investigations/handoff-failure-analysis/index.html:210](<C:/Users/Fletch/Documents/GitHub/operationalentropy/services/focused-operational-investigations/handoff-failure-analysis/index.html:210>)
- `/services/focused-operational-investigations/`: [services/focused-operational-investigations/index.html:176](<C:/Users/Fletch/Documents/GitHub/operationalentropy/services/focused-operational-investigations/index.html:176>)
- `/services/focused-operational-investigations/institutional-memory-recovery/`: [services/focused-operational-investigations/institutional-memory-recovery/index.html:201](<C:/Users/Fletch/Documents/GitHub/operationalentropy/services/focused-operational-investigations/institutional-memory-recovery/index.html:201>)
- `/services/focused-operational-investigations/operational-stack-review/`: [services/focused-operational-investigations/operational-stack-review/index.html:208](<C:/Users/Fletch/Documents/GitHub/operationalentropy/services/focused-operational-investigations/operational-stack-review/index.html:208>)
- `/services/focused-operational-investigations/workflow-momentum-analysis/`: [services/focused-operational-investigations/workflow-momentum-analysis/index.html:211](<C:/Users/Fletch/Documents/GitHub/operationalentropy/services/focused-operational-investigations/workflow-momentum-analysis/index.html:211>)
- `/site-navigation/`: [site-navigation/index.html:132](<C:/Users/Fletch/Documents/GitHub/operationalentropy/site-navigation/index.html:132>)
- `/temp-pricing/`: [temp-pricing/index.html:66](<C:/Users/Fletch/Documents/GitHub/operationalentropy/temp-pricing/index.html:66>)

### Local evidence anchors

- **F02:** [index.html:41](<C:/Users/Fletch/Documents/GitHub/operationalentropy/index.html:41>); [about/operational-entropy-index/index.html:45](<C:/Users/Fletch/Documents/GitHub/operationalentropy/about/operational-entropy-index/index.html:45>)
- **F03:** [about/operational-entropy-index/index.html:10](<C:/Users/Fletch/Documents/GitHub/operationalentropy/about/operational-entropy-index/index.html:10>)
- **F05:** [index.html:169](<C:/Users/Fletch/Documents/GitHub/operationalentropy/index.html:169>); [site-navigation/index.html:99](<C:/Users/Fletch/Documents/GitHub/operationalentropy/site-navigation/index.html:99>); [contact/index.html:165](<C:/Users/Fletch/Documents/GitHub/operationalentropy/contact/index.html:165>)
- **F06:** [site-navigation/index.html:54](<C:/Users/Fletch/Documents/GitHub/operationalentropy/site-navigation/index.html:54>); [resources/information-packet/index.html:46](<C:/Users/Fletch/Documents/GitHub/operationalentropy/resources/information-packet/index.html:46>)
- **F09:** [index.html:212](<C:/Users/Fletch/Documents/GitHub/operationalentropy/index.html:212>); [site-navigation/index.html:78](<C:/Users/Fletch/Documents/GitHub/operationalentropy/site-navigation/index.html:78>)
- **F10:** [insights/operational-drag/index.html:119](<C:/Users/Fletch/Documents/GitHub/operationalentropy/insights/operational-drag/index.html:119>); [insights/organizational-complexity-tax/index.html:77](<C:/Users/Fletch/Documents/GitHub/operationalentropy/insights/organizational-complexity-tax/index.html:77>); [insights/what-is-operational-entropy/index.html:184](<C:/Users/Fletch/Documents/GitHub/operationalentropy/insights/what-is-operational-entropy/index.html:184>)
- **F11:** [index.html:141](<C:/Users/Fletch/Documents/GitHub/operationalentropy/index.html:141>)
- **F12:** [services/focused-operational-investigations/founder-absence-simulation/index.html:38](<C:/Users/Fletch/Documents/GitHub/operationalentropy/services/focused-operational-investigations/founder-absence-simulation/index.html:38>); [services/focused-operational-investigations/handoff-failure-analysis/index.html:38](<C:/Users/Fletch/Documents/GitHub/operationalentropy/services/focused-operational-investigations/handoff-failure-analysis/index.html:38>); [services/focused-operational-investigations/institutional-memory-recovery/index.html:38](<C:/Users/Fletch/Documents/GitHub/operationalentropy/services/focused-operational-investigations/institutional-memory-recovery/index.html:38>); [services/focused-operational-investigations/operational-stack-review/index.html:36](<C:/Users/Fletch/Documents/GitHub/operationalentropy/services/focused-operational-investigations/operational-stack-review/index.html:36>); [services/focused-operational-investigations/workflow-momentum-analysis/index.html:38](<C:/Users/Fletch/Documents/GitHub/operationalentropy/services/focused-operational-investigations/workflow-momentum-analysis/index.html:38>); [contact/index.html:238](<C:/Users/Fletch/Documents/GitHub/operationalentropy/contact/index.html:238>); [contact/index.html:96](<C:/Users/Fletch/Documents/GitHub/operationalentropy/contact/index.html:96>)
- **F13:** [contact/index.html:40](<C:/Users/Fletch/Documents/GitHub/operationalentropy/contact/index.html:40>); [contact/index.html:214](<C:/Users/Fletch/Documents/GitHub/operationalentropy/contact/index.html:214>)
- **F14:** [about/operational-entropy-index/index.html:179](<C:/Users/Fletch/Documents/GitHub/operationalentropy/about/operational-entropy-index/index.html:179>)
- **F15:** [resources/information-packet/index.html:35](<C:/Users/Fletch/Documents/GitHub/operationalentropy/resources/information-packet/index.html:35>)
- **F18:** [about/operational-entropy-index/index.html:211](<C:/Users/Fletch/Documents/GitHub/operationalentropy/about/operational-entropy-index/index.html:211>)
- **F20:** [about/index.html:79](<C:/Users/Fletch/Documents/GitHub/operationalentropy/about/index.html:79>)
- **F21:** [entropy-compatible-hiring/index.html:171](<C:/Users/Fletch/Documents/GitHub/operationalentropy/entropy-compatible-hiring/index.html:171>); [entropy-compatible-hiring/index.html:190](<C:/Users/Fletch/Documents/GitHub/operationalentropy/entropy-compatible-hiring/index.html:190>)

## Appendix E: Remaining Assessment References and Scope

Exact route/name searches and a public-graph crawl were repeated. The following tracked files retain explicit engagement-assessment references. These are not newly introduced paths.

- [README.md](<C:/Users/Fletch/Documents/GitHub/operationalentropy/README.md>): B: internal documentation, propagation data, or historical record; not in ordinary public graph.
- [assessments/engagement-path/index.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/assessments/engagement-path/index.html>): C: preserved assessment implementation and own metadata.
- [contact/index.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/contact/index.html>): C: conditional recommendation handoff and template; no link back to assessment.
- [data/identity-changes/2026-06-22-engagement-path-assessment-introduced.md](<C:/Users/Fletch/Documents/GitHub/operationalentropy/data/identity-changes/2026-06-22-engagement-path-assessment-introduced.md>): B: internal documentation, propagation data, or historical record; not in ordinary public graph.
- [data/identity-changes/2026-08-11-assessment-separates-investigations.md](<C:/Users/Fletch/Documents/GitHub/operationalentropy/data/identity-changes/2026-08-11-assessment-separates-investigations.md>): B: internal documentation, propagation data, or historical record; not in ordinary public graph.
- [data/identity-changes/2026-08-12-oei-adds-15-day-audit.md](<C:/Users/Fletch/Documents/GitHub/operationalentropy/data/identity-changes/2026-08-12-oei-adds-15-day-audit.md>): B: internal documentation, propagation data, or historical record; not in ordinary public graph.
- [data/propagation-map.json](<C:/Users/Fletch/Documents/GitHub/operationalentropy/data/propagation-map.json>): B: internal documentation, propagation data, or historical record; not in ordinary public graph.
- [data/reconciliation/2026-08-29-focused-investigation-escalation-reset-name.md](<C:/Users/Fletch/Documents/GitHub/operationalentropy/data/reconciliation/2026-08-29-focused-investigation-escalation-reset-name.md>): B: internal documentation, propagation data, or historical record; not in ordinary public graph.
- [data/reconciliation/2026-08-29-focused-investigation-prerequisite-copy.md](<C:/Users/Fletch/Documents/GitHub/operationalentropy/data/reconciliation/2026-08-29-focused-investigation-prerequisite-copy.md>): B: internal documentation, propagation data, or historical record; not in ordinary public graph.
- [data/reconciliation/2026-08-29-homepage-adds-15-day-audit.md](<C:/Users/Fletch/Documents/GitHub/operationalentropy/data/reconciliation/2026-08-29-homepage-adds-15-day-audit.md>): B: internal documentation, propagation data, or historical record; not in ordinary public graph.
- [data/reconciliation/2026-08-29-institutional-memory-recovery-sprint-name.md](<C:/Users/Fletch/Documents/GitHub/operationalentropy/data/reconciliation/2026-08-29-institutional-memory-recovery-sprint-name.md>): B: internal documentation, propagation data, or historical record; not in ordinary public graph.
- [data/reconciliation/2026-08-29-pillar-terminology-client-facing-surfaces.md](<C:/Users/Fletch/Documents/GitHub/operationalentropy/data/reconciliation/2026-08-29-pillar-terminology-client-facing-surfaces.md>): B: internal documentation, propagation data, or historical record; not in ordinary public graph.
- [oei_engagement_quiz.html](<C:/Users/Fletch/Documents/GitHub/operationalentropy/oei_engagement_quiz.html>): C: legacy direct-link compatibility; no public inbound link.

Generic references in SITE-STRUCTURE to interactive assessments, admin diagnosis/report terminology, PDF-generator consulting pathways, and ECH/practitioner assessment descriptions are not references to the retired discovery funnel. The internal propagation dashboard is noindex/unlisted, not an ordinary navigation path. Robots allows crawling and retains only a sitemap URL; its outdated “5-page sitemap” comment does not affect routing. The direct assessment remains indexable in principle; no search-removal guarantee is asserted.
