# Site structure

The public home page remains at `/`. Content pages use folder URLs so each page
has a clean, durable path:

- `/about/`, `/contact/`, and `/pricing/` — company and commercial pages
- `/services/` — the service overview; focused-investigation offerings live under
  `/services/focused-operational-investigations/`
- `/insights/` — explanatory articles and OEI pillar deep dives
- `/resources/` — downloadable and reference material
- `/assessments/` — interactive assessments

Every moved page includes `<base href="/">`, so shared CSS, images, and PDFs
resolve from the site root. Navigation uses the clean folder URLs directly;
the repository root contains only the home page.

When adding a new page, create `section/page-name/index.html`, add it to
`sitemap.xml`, and use root-relative links (for example, `/contact/`) for new
navigation.
