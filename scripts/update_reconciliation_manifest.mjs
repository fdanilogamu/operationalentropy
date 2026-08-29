import { readdir, writeFile } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const scriptDirectory = path.dirname(fileURLToPath(import.meta.url));
const repositoryRoot = path.resolve(scriptDirectory, '..');
const recordsDirectory = path.join(repositoryRoot, 'data', 'reconciliation');
const manifestPath = path.join(recordsDirectory, 'manifest.json');

const entries = await readdir(recordsDirectory, { withFileTypes: true });
const records = entries
  .filter(entry => entry.isFile() && entry.name.endsWith('.md') && !entry.name.startsWith('_'))
  .map(entry => entry.name)
  .sort((a, b) => b.localeCompare(a));

await writeFile(manifestPath, `${JSON.stringify(records, null, 2)}\n`, 'utf8');

console.log(`Updated ${manifestPath}`);
console.log(`Included ${records.length} reconciliation record${records.length === 1 ? '' : 's'}.`);
