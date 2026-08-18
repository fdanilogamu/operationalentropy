/* Copy to access-config.js during deployment. Do not commit that file.
   Generate SHA-256 in a browser console:
   crypto.subtle.digest('SHA-256', new TextEncoder().encode('your passphrase')).then(value => console.log([...new Uint8Array(value)].map(x => x.toString(16).padStart(2, '0')).join('')))
*/
window.OEI_ACCESS_CONFIG = { passphraseSha256: "REPLACE_WITH_SHA256_HEX" };
