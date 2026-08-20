(() => {
  const $ = selector => document.querySelector(selector);
  const $$ = selector => [...document.querySelectorAll(selector)];
  const escapeHtml = value => String(value ?? '').replace(/[&<>'"]/g, char => ({'&':'&amp;','<':'&lt;','>':'&gt;',"'":'&#39;','"':'&quot;'}[char]));
  const niceDate = value => new Intl.DateTimeFormat('en', { year:'numeric', month:'short', day:'2-digit', timeZone:'UTC' }).format(new Date(`${value}T00:00:00Z`));
  const slug = value => value.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
  let records = [], map = null, activeProject = 'All projects';

  function parseRecord(markdown, file) {
    const front = markdown.match(/^---\s*\r?\n([\s\S]*?)\r?\n---\s*\r?\n/);
    if (!front) throw new Error(`Missing front matter in ${file}`);
    const meta = {}; let listKey = null;
    front[1].split(/\r?\n/).forEach(line => {
      const item = line.match(/^\s+-\s+(.+)$/);
      if (item && listKey) { meta[listKey].push(item[1].trim()); return; }
      const field = line.match(/^([\w/ -]+):\s*(.*)$/);
      if (!field) return;
      listKey = field[1].trim();
      meta[listKey] = field[2].trim() || [];
    });
    const body = markdown.slice(front[0].length);
    const section = name => (body.match(new RegExp(`## ${name}\\s*\\r?\\n([\\s\\S]*?)(?=\\r?\\n## |$)`, 'i')) || [,''])[1].trim();
    const propagation = section('Propagation').split(/\r?\n/).map(line => line.match(/^\s*-\s*\[([ xX])\]\s*(.+)$/)).filter(Boolean).map(match => ({ complete: match[1].toLowerCase() === 'x', target: match[2].trim() }));
    return {...meta, file, change:section('Change'), notes:section('Notes'), propagation};
  }

  const debtFor = record => record.propagation.filter(item => !item.complete);
  function switchView(id) {
    $$('.prop-view').forEach(view => view.classList.toggle('is-active', view.id === id));
    $$('.prop-tabs [data-view]').forEach(tab => tab.classList.toggle('is-active', tab.dataset.view === id));
    window.scrollTo({top: $('.prop-tabs').offsetTop, behavior:'smooth'});
  }

  function renderOverview() {
    const projects = [...new Set(records.map(record => record.project))];
    const debt = records.flatMap(debtFor);
    const debtProjects = new Set(records.filter(record => debtFor(record).length).map(record => record.project));
    const latest = records[0];
    const metrics = [
      [records.length,'Total identity changes',''], [projects.length,'Projects represented',''], [debt.length,'Unresolved propagation items',''],
      [latest ? latest.title : 'None','Most recent identity change','is-text'], [debtProjects.size,'Projects carrying propagation debt','']
    ];
    $('#metrics').innerHTML = metrics.map(([value,label,klass]) => `<article class="prop-metric ${klass}"><strong>${escapeHtml(value)}</strong><span>${escapeHtml(label)}</span></article>`).join('');
    $('#recent-changes').innerHTML = records.slice(0,4).map(record => `<div class="prop-recent-item"><time>${escapeHtml(niceDate(record.date))}</time><div><strong>${escapeHtml(record.title)}</strong><small>${escapeHtml(record.project)}</small></div><span class="prop-status ${debtFor(record).length ? 'has-debt':''}">${debtFor(record).length ? `${debtFor(record).length} open` : 'reconciled'}</span></div>`).join('');
    $('#debt-summary').innerHTML = projects.map(project => {
      const items = records.filter(r => r.project === project).flatMap(debtFor);
      if (!items.length) return '';
      return `<div class="prop-debt-project"><div><strong>${escapeHtml(project)}</strong><b>${items.length}</b></div><p>${escapeHtml(items.slice(0,3).map(i => i.target).join(' · '))}${items.length > 3 ? '…':''}</p></div>`;
    }).join('') || '<p>No propagation debt recorded.</p>';
    $('#debt-tab-count').textContent = debt.length;
  }

  function recordCard(record) {
    const completed = record.propagation.filter(item => item.complete).length;
    return `<article class="prop-entry" data-project="${escapeHtml(record.project)}"><time class="prop-entry-date">${escapeHtml(niceDate(record.date))}</time><details><summary><div class="prop-entry-meta"><span>${escapeHtml(record.project)}</span><span>·</span><span>${completed}/${record.propagation.length} propagated</span></div><h3>${escapeHtml(record.title)}</h3><div class="prop-tags">${record.categories.map(category => `<span class="prop-tag">${escapeHtml(category)}</span>`).join('')}</div></summary><div class="prop-entry-body"><div><h4>CHANGE</h4><p>${escapeHtml(record.change)}</p>${record.notes ? `<h4>NOTES</h4><p>${escapeHtml(record.notes)}</p>`:''}</div><div><h4>PROPAGATION</h4><ul>${record.propagation.map(item => `<li><span class="prop-check ${item.complete ? '':'open'}">${item.complete ? '✓':'○'}</span>${escapeHtml(item.target)}</li>`).join('')}</ul></div><div class="prop-provenance">SOURCE · ${escapeHtml(record.source)} · <a href="/data/identity-changes/${encodeURIComponent(record.file)}">Open Markdown ↗</a></div></div></details></article>`;
  }
  function renderTimeline() {
    const projects = ['All projects', ...new Set([...map.surfaces.map(surface => surface.project), ...records.map(record => record.project)])];
    $('#project-filters').innerHTML = projects.map(project => `<button class="${project === activeProject ? 'is-active':''}" data-project-filter="${escapeHtml(project)}">${escapeHtml(project)}</button>`).join('');
    const visibleRecords = records.filter(record => activeProject === 'All projects' || record.project === activeProject);
    $('#timeline-list').innerHTML = visibleRecords.length ? visibleRecords.map(recordCard).join('') : `<div class="prop-panel"><p>No identity-change records are currently logged for ${escapeHtml(activeProject)}.</p></div>`;
    $$('[data-project-filter]').forEach(button => button.addEventListener('click', () => { activeProject = button.dataset.projectFilter; renderTimeline(); }));
  }
  function renderOutstanding() {
    const projects = [...new Set(records.map(record => record.project))];
    $('#outstanding-list').innerHTML = projects.map(project => {
      const changes = records.filter(record => record.project === project && debtFor(record).length);
      if (!changes.length) return '';
      const count = changes.flatMap(debtFor).length;
      return `<section class="prop-outstanding-project"><header><h3>${escapeHtml(project)}</h3><span>${count} unresolved ${count === 1 ? 'surface':'surfaces'}</span></header>${changes.map(record => `<article class="prop-debt-change"><div><time>${escapeHtml(niceDate(record.date))}</time><h4>${escapeHtml(record.title)}</h4><div class="prop-tags">${record.categories.map(c => `<span class="prop-tag">${escapeHtml(c)}</span>`).join('')}</div></div><ul>${debtFor(record).map(item => `<li>${escapeHtml(item.target)}</li>`).join('')}</ul></article>`).join('')}</section>`;
    }).join('') || '<div class="prop-panel"><p>No outstanding propagation is recorded.</p></div>';
  }
  function renderMatrix() {
    const select = $('#matrix-project');
    const projects = ['All projects', ...new Set(map.surfaces.map(surface => surface.project))];
    select.innerHTML = projects.map(project => `<option>${escapeHtml(project)}</option>`).join('');
    const draw = () => {
      const surfaces = map.surfaces.filter(surface => select.value === 'All projects' || surface.project === select.value);
      $('#matrix-count').textContent = `${surfaces.length} surfaces · ${map.categories.length} identity categories`;
      $('#matrix-table thead').innerHTML = `<tr><th>Surface</th>${map.categories.map(category => `<th>${escapeHtml(category)}</th>`).join('')}</tr>`;
      $('#matrix-table tbody').innerHTML = surfaces.map(surface => `<tr><th>${escapeHtml(surface.name)}<small>${escapeHtml(surface.path)}</small></th>${map.categories.map(category => `<td>${surface.categories.includes(category) ? `<span class="prop-matrix-hit" aria-label="Depends on ${escapeHtml(category)}">✓</span>`:''}</td>`).join('')}</tr>`).join('');
    };
    select.addEventListener('change', draw); draw();
  }

  $$('.prop-tabs [data-view]').forEach(button => button.addEventListener('click', () => switchView(button.dataset.view)));
  $$('[data-jump]').forEach(button => button.addEventListener('click', () => switchView(button.dataset.jump)));

  async function discoverRecordFiles() {
    try {
      const response = await fetch('data/identity-changes/');
      if (response.ok && (response.headers.get('content-type') || '').includes('text/html')) {
        const document = new DOMParser().parseFromString(await response.text(), 'text/html');
        const discovered = [...document.querySelectorAll('a[href]')].map(link => decodeURIComponent(link.getAttribute('href').split('/').pop())).filter(file => file.endsWith('.md') && !file.startsWith('_'));
        if (discovered.length) return [...new Set(discovered)];
      }
    } catch (_) { /* Static hosts do not normally expose directory listings. */ }
    const response = await fetch('data/identity-changes/manifest.json');
    if (!response.ok) throw new Error('Could not read the identity-change manifest.');
    return (await response.json()).filter(file => !file.startsWith('_'));
  }

  Promise.all([discoverRecordFiles(), fetch('data/propagation-map.json').then(r => { if(!r.ok) throw new Error('Could not read the propagation map.'); return r.json(); })])
    .then(async ([files, propagationMap]) => {
      map = propagationMap;
      records = await Promise.all(files.map(file => fetch(`data/identity-changes/${file}`).then(r => { if(!r.ok) throw new Error(`Could not read ${file}.`); return r.text(); }).then(text => parseRecord(text,file))));
      records.sort((a,b) => b.date.localeCompare(a.date) || a.title.localeCompare(b.title));
      renderOverview(); renderTimeline(); renderOutstanding(); renderMatrix(); $('#loading').hidden = true;
    }).catch(error => { $('#loading').hidden = true; $('#error').hidden = false; $('#error').textContent = `${error.message} Serve the repository through a local web server rather than opening this file directly.`; });
})();
