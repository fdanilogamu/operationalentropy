# Operational Entropy Index

The public website for Operational Entropy Index (OEI), hosted with GitHub
Pages.

## Local preview

Open `index.html` in a browser, or serve the repository with any static-file
server.

## Site structure

- `index.html` — homepage
- `about/`, `contact/`, `pricing/` — primary pages
- `services/` — service overview and focused-investigation offerings
- `insights/` — OEI articles and pillar deep dives
- `resources/` — information packet and downloadable material
- `assessments/` — engagement-path assessment
- `images/` — shared image assets
- `styles.css` — shared site styling
- `sitemap.xml` — public URL list for search engines

See [SITE-STRUCTURE.md](SITE-STRUCTURE.md) for URL conventions and the detailed
content hierarchy.

## Adding a page

1. Create `section/page-name/index.html`.
2. Use root-relative links, such as `/contact/`.
3. Add the public URL to `sitemap.xml`.
4. Put shared image assets in `images/`.

## Publishing

GitHub Pages publishes this repository as a static site. The `.nojekyll` file
is intentional: it prevents Jekyll processing because the site is plain
HTML/CSS.
