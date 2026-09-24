# OEI Institute Branch Publish-Readiness Audit

Date: 2026-09-24  
Branch: `oei-institute-site-reframe`  
Compared with: `main`  
Audited commit: `0cabbf6` (`update hero`)

## Scope

This audit covers the changes accumulated on the branch since `main`, with emphasis on whether the public site can be published with the OEI Institute branding. It checks canonical routes, the new logo, favicon, and About hero, the Institute / Operational Entropy Index distinction, public assessment discoverability, shared navigation and footer surfaces, metadata, and the pending Services and Pricing routes.

Services and Pricing are treated as pending product and commercial work. Their routes still need to resolve deliberately, but this audit does not require their final information architecture, offers, or pricing model.

## Executive assessment

The branch has a coherent Institute About page, preserves the dedicated Operational Entropy Index journey, adds the Institute logo and favicon, adds the About hero image, and removes the engagement assessment from public discovery. The new assets are present and the canonical sitemap URLs respond from a local static server.

The branch is not yet publish-ready. The highest-risk issue is that `services/index.html` was deleted. `/services/` therefore returns a server directory listing locally rather than a Services page or an intentional pending page. The public navigation and sitemap still advertise `/services/`, so this is a broken public route.

The second major issue is propagation. Twenty-five of the repository's 34 `index.html` files still use the former footer identity, “Operational Entropy Index. A diagnostic tool and intervention process for reducing organizational drag,” and “Fletcher GH Consulting” copyright text. The homepage, Contact page, Site Navigation page, and the preserved Index page also retain old consulting-led descriptions or metadata. Those surfaces still make the old engagement model the default interpretation of OEI even though `/about/` now establishes the Institute as the governing institution.

## Minimum requirements before publication

These are the smallest requirements for publishing the branch with the new branding. They do not require final Services or Pricing copy.

### Release blockers

1. **Restore a deliberate `/services/` route.** Restore the main branch Services landing page, or create a clearly marked pending Services page at `services/index.html`. It must render an intentional page rather than a directory listing, and its links to focused investigations must remain valid.

2. **Propagate the new institutional footer identity.** Replace the old OEI diagnostic-tool footer description and the old company identity wherever they appear on public canonical pages. The minimum viable wording should identify OEI Institute and state that it governs the Operational Entropy Index methodology. Keep ECH as a separate applied product. The new About footer is the suitable local reference.

3. **Resolve the homepage's public ontology.** The homepage currently presents the Operational Entropy Index as a proprietary diagnostic and intervention process, labels the primary page title around “Revert Operational Drag,” and routes visitors through diagnosis, service, pricing, and engagement CTAs. It needs a localized first-pass correction that makes the Institute the institutional identity and the Index the governed methodology. This can preserve the existing commercial sections as pending, but the homepage cannot continue to make the old funnel the site's only meaning.

4. **Resolve the Contact page's public delivery claim.** Contact still presents Fletcher as the sole operator, promises a fixed diagnosis workflow and delivery window, and lists the former engagement package. If Services and Pricing remain pending, Contact needs a short transition treatment that accurately frames direct inquiries without presenting the old package as the settled Institute delivery model.

5. **Verify all public entry routes after remediation.** Test `/`, `/about/`, `/about/operational-entropy-index/`, `/services/`, `/temp-pricing/`, `/contact/`, `/site-navigation/`, the ECH route, all sitemap URLs, and the preserved direct assessment URL. A successful HTTP response alone is insufficient for `/services/`; it must return the intended HTML document.

### Important but not blocking the pending commercial work

6. **Update Index-page metadata and framing.** The dedicated Index route is structurally preserved, but its title, description, and opening language still use the former “consultants” and “proprietary diagnostic tool and structured intervention process” framing. Clarify that the Operational Entropy Index is the methodology governed by the Institute without rewriting the educational explanation.

7. **Update Site Navigation copy.** It still says the Institute overview is “content in development” and describes a path to “complete OEI engagement options.” Replace those stale labels with the current About hierarchy and a neutral pending-services description.

8. **Update repository release documentation.** `SITE-STRUCTURE.md` still calls `/about/` a “placeholder scaffold,” although the page now contains first-pass final copy and the hero image. `README.md` still describes the older page hierarchy. These do not change runtime behavior, but they should be corrected before treating the branch as the publishable branded baseline.

9. **Check legacy redirects and direct legacy pages.** Root aliases such as `about.html`, `services.html`, and `pricing.html` redirect to canonical routes. Keep them only if their redirect targets are valid after the Services decision. The unlisted engagement assessment and its implementation should remain intact and unlinked.

## What is already in acceptable shape

- `images/oei-institute-logo.png` is present and used by the changed canonical pages.
- `images/oei-institute-favicon.png` is present and used by the changed canonical pages.
- `images/oei-institute-hero.png` is present at 1774 × 887 and is used in the About hero with intrinsic dimensions and proportional scaling.
- `/about/` presents OEI Institute as the top-level concept and links to `/about/operational-entropy-index/`.
- The five pillars remain named Founder Dependency, Knowledge Logistics, Workflow Velocity, Tool Discipline, and Handoff Integrity.
- The dedicated Index explanation and downstream insight pages remain present.
- Public links to `/assessments/engagement-path/` were removed. The assessment route and implementation remain preserved for direct access.
- The sitemap includes the new Index route and excludes the engagement assessment route.
- No global typography, color system, or component redesign was introduced in the branch diff.

## Services and Pricing status

Pricing is already represented by the deliberate pending route `/temp-pricing/`, and `/pricing/` redirects there. Its commercial language can remain pending for this release, subject to the footer and branding propagation requirements above.

Services is different. The branch deleted `services/index.html` while leaving `/services/` in navigation, the sitemap, and the Site Navigation page. The current local server exposes a directory listing. A pending Services page is acceptable, but an absent landing file is not.

## Audit findings

### P1 — Missing Services landing document

- **Class:** Structural release blocker
- **Routes:** `/services/`
- **Files:** `services/index.html` deleted; navigation and sitemap still reference `/services/`
- **Evidence:** local static server returns `Directory listing for /services/`
- **Required action:** restore the former landing page or add an intentional pending page. Do not leave directory exposure as the public response.

### P2 — Footer identity has not propagated

- **Class:** Copy and shared-surface release blocker
- **Routes:** homepage, Contact, Site Navigation, Pricing, ECH, insights, investigations, resources, and other canonical pages
- **Evidence:** 25 of 34 `index.html` files still contain the old OEI diagnostic-tool description and Fletcher GH Consulting copyright; only the About footer was reframed.
- **Required action:** apply the approved Institute / methodology distinction to the shared footer surfaces, preserving ECH as its own product identity.

### P3 — Homepage still organizes OEI around the former engagement funnel

- **Class:** Copy and user-journey release blocker
- **Routes:** `/`
- **Evidence:** old title and description, “proprietary diagnostic tool and structured intervention process,” diagnosis-first CTAs, pricing preview, and “start your diagnosis.”
- **Required action:** make the minimum copy and CTA changes needed to establish the Institute / methodology hierarchy. Keep pending commercial sections only where they are clearly labelled as pending.

### P4 — Contact still makes the old Fletcher-delivered model definitive

- **Class:** Copy and commercial-boundary release blocker
- **Routes:** `/contact/`
- **Evidence:** first-person Fletcher delivery language, fixed 4-day diagnosis and 5–7 day delivery claims, old core-engagement list, and old package-specific FAQ content.
- **Required action:** add a concise transition treatment or otherwise neutralize definitive claims until Services and Pricing are decided. Do not invent a replacement delivery model.

### P5 — Index page metadata predates the Institute hierarchy

- **Class:** Copy-safe
- **Routes:** `/about/operational-entropy-index/`
- **Evidence:** title and description refer to “consultants” and a proprietary diagnostic/intervention process.
- **Required action:** update metadata and opening bridge copy so the page clearly identifies the Index as the Institute-governed methodology. Preserve the educational body.

### P6 — Site Navigation contains stale transition language

- **Class:** Small structural / copy
- **Routes:** `/site-navigation/`
- **Evidence:** “content in development” for the Institute overview and “complete OEI engagement options” as a visitor path.
- **Required action:** point visitors to the completed Institute page and describe Services as pending without making the old engagement catalogue the default journey.

### P7 — Internal release documentation is stale

- **Class:** Documentation-safe
- **Files:** `SITE-STRUCTURE.md`, `README.md`
- **Evidence:** About is still described as a placeholder scaffold and the older hierarchy remains in the README.
- **Required action:** update documentation to reflect the branch's actual canonical hierarchy before publication.

## Intentionally preserved material

- The engagement assessment remains directly accessible at `/assessments/engagement-path/`; its source and behavior were not changed. Its public discovery links remain removed.
- Focused Operational Investigations and other engagement descriptions remain as historical or potentially valid methodology applications. Their presence alone is not a reason to delete them; their commercial framing should be revisited with the Services decision.
- ECH remains a distinct applied product and should not be collapsed into the Index or Institute identity.
- Founder history and legacy root redirect files preserve provenance and URL continuity.

## Validation performed

- Branch: `oei-institute-site-reframe`
- Audited commit: `0cabbf6`
- Working tree was clean before this report was created.
- `git diff --check main...HEAD` passed.
- All 29 sitemap URLs responded with HTTP 200 from the local server, but `/services/` returned a directory listing rather than a page.
- `/about/`, `/about/operational-entropy-index/`, `/temp-pricing/`, `/contact/`, and `/site-navigation/` loaded from the local server.
- New logo, favicon, and hero files exist in `images/`.
- Assessment discovery references remain absent from public HTML/XML; preserved implementation references remain where expected.
- No site content was changed while conducting this audit. This report is the only new working-tree file produced by this audit.

## Publish decision

**Do not publish yet.** The minimum sequence is: restore a deliberate Services landing route, propagate the Institute footer identity, correct the homepage and Contact ontology, then rerun route, asset, metadata, and link checks. Services and Pricing can remain pending after those safeguards are in place.
