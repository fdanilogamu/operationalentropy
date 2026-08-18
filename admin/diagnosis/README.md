# OEI Diagnosis Workspace

Unlisted, browser-only practitioner workspace at `/admin/diagnosis/`.

## Access configuration

GitHub Pages cannot provide secure server authentication. `access-config.js` contains only the SHA-256 digest of the deployment passphrase; the plaintext must be kept in a password manager and never committed. The local gate deters casual entry only. Use protected hosting or an identity-aware proxy if strong authentication becomes necessary.

To rotate access, generate a new long random passphrase locally, replace only the 64-character lowercase hexadecimal digest in `access-config.js`, and deploy. Existing unlocked tabs remain open until refreshed or closed.

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
