# OEI Diagnosis Workspace

Unlisted, browser-only practitioner workspace at `/admin/diagnosis/`.

## Access configuration

GitHub Pages cannot provide secure server authentication. Copy `access-config.example.js` to `access-config.js` in the deployed environment and replace the placeholder with a SHA-256 passphrase digest. The real file is gitignored. This local gate only deters casual entry; use protected hosting or an identity-aware proxy for strong authentication.

## Privacy model

Diagnosis data stays in JavaScript memory. The app does not use localStorage, sessionStorage, IndexedDB, cookies, or an API. Refreshing or closing the tab removes unexported work. JSON checkpoints and report exports are initiated explicitly by the practitioner.

## Run locally

Serve the repository root with any static server, configure `access-config.js`, and open `/admin/diagnosis/`. Native ES modules do not work reliably from a `file://` URL.

## Tests

Run `node --test admin/diagnosis/tests/scoring.test.mjs` from the repository root.

## Current static-host limitations

- Access control is not secure authentication.
- Final reports export as structured Markdown and print-ready HTML/PDF through the browser; direct DOCX generation is not included.
- Diagnosis data cannot be recovered after a refresh unless a checkpoint was exported.
- Client-side source code, including methodology configuration, is inspectable.
