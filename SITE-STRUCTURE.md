# Site structure

The public home page remains at `/`. Content pages use folder URLs so each page
has a clean, durable path:

- `/about/`, `/contact/`, and `/pricing/` — company and commercial pages
- `/services/` — the service overview and individual service pages
- `/insights/` — explanatory articles and OEI pillar deep dives
- `/resources/` — downloadable and reference material
- `/assessments/` — interactive assessments

Every moved page includes `<base href="/">`, so shared CSS, images, PDFs, and
the existing relative internal links resolve from the site root. The original
root-level `.html` files are small compatibility redirects. Keep them in place
while old bookmarks and search results are still in circulation.

When adding a new page, create `section/page-name/index.html`, add it to
`sitemap.xml`, and use root-relative links (for example, `/contact/`) for new
navigation.
