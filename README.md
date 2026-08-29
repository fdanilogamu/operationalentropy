# Operational Entropy Index

The public website for Operational Entropy Index (OEI), hosted with GitHub
Pages.

## Local preview

Open `index.html` in a browser, or serve the repository with any static-file
server.

## Site structure

- `index.html`: homepage
- `about/`, `contact/`, `pricing/`: primary pages
- `services/`: service overview and focused-investigation offerings
- `insights/`: OEI articles and pillar deep dives
- `resources/`: information packet and downloadable material
- `assessments/`: engagement-path assessment
- `images/`: shared image assets
- `styles.css`: shared site styling
- `sitemap.xml`: public URL list for search engines

See [SITE-STRUCTURE.md](SITE-STRUCTURE.md) for URL conventions and the detailed
content hierarchy.

## Adding a page

1. Create `section/page-name/index.html`.
2. Use root-relative links, such as `/contact/`.
3. Add the public URL to `sitemap.xml`.
4. Put shared image assets in `images/`.

## Recording an identity change

The unlisted dashboard at `/ops/propagation/` renders durable Markdown records
from `data/identity-changes/` and uses `data/propagation-map.json` to show where
project truths are represented.

1. Duplicate `data/identity-changes/_TEMPLATE.md`.
2. Rename it using `YYYY-MM-DD-short-description.md`.
3. Fill in the change and relevant categories.
4. Add or confirm propagation targets.
5. Save the file.
6. The dashboard picks it up automatically when the repository is served
   locally; add the filename to `data/identity-changes/manifest.json` before
   publishing to GitHub Pages, whose static hosting does not expose directory
   listings.

Files beginning with `_` are templates or helpers and are never rendered as
identity changes.

The propagation matrix also includes a **Build new log entry** tool. Select the
project and every identity category affected by a decision. The dashboard uses
`data/propagation-map.json` to calculate the union of dependent surfaces and
downloads a dated Markdown draft with those surfaces ready as unchecked
propagation targets. Complete the remaining fields, rename the draft if needed,
place it in `data/identity-changes/`, and add its filename to `manifest.json`
when publishing through GitHub Pages.

To update the manifest, use either method:

- Serve the repository locally in Chrome or Edge, open `/ops/propagation/`,
  select **Update manifest**, and choose the `data/identity-changes/` folder.
- From any computer with Node.js and a clone of the repository, run
  `node scripts/update_identity_change_manifest.mjs`.

Both methods include `.md` files, ignore files beginning with `_`, sort records
predictably, and replace `data/identity-changes/manifest.json`. Commit the
updated manifest together with the new identity-change record.

## Recording a semantic reconciliation item

The **Reconciliation** tab on `/ops/propagation/` is an adjacent audit queue,
not an identity-change record. Use it only when repository evidence establishes
the canonical truth and an existing surface can be corrected without changing
methodology, product behavior, or business policy.

1. Use **Build reconciliation item** or duplicate
   `data/reconciliation/_TEMPLATE.md`.
2. Record the issue, canonical truth, affected surfaces, current and expected
   representations, provenance, risk, and status.
3. Save the Markdown in `data/reconciliation/`.
4. Run `node scripts/update_reconciliation_manifest.mjs`.
5. Change `status` from `open` to `in_review` or `resolved` as work progresses;
   resolved records should include verification in **Resolution notes**.

Reconciliation records never contribute to propagation debt, never appear in
the identity timeline, and never trigger the propagation matrix.

## Publishing

GitHub Pages publishes this repository as a static site. The `.nojekyll` file
is intentional: it prevents Jekyll processing because the site is plain
HTML/CSS.
