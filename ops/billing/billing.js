(() => {
  'use strict';
  const KEYS = { catalog: 'oeiBillingCatalogV1', quotes: 'oeiBillingQuotesV1' };
  const defaults = [
    { id:'practitioner', name:'OEI Practitioner Development', description:'Internal practitioner development using the OEI methodology. The same core curriculum and competency standard apply to all practitioners.', model:'fixed', unitPrice:10000, min:10000, max:10000, allowAbove:false, provisional:true, options:[] },
    { id:'team', name:'OEI Team-Delivered Engagements', description:'OEI diagnosis and methodology application performed by qualified practitioners for the organization.', model:'range', unitPrice:20000, min:20000, max:45000, allowAbove:true, provisional:false, options:[] },
    { id:'focused', name:'Focused Investigations', description:'A separately quotable, bounded investigation of a specific operational domain.', model:'range', unitPrice:1000, min:1000, max:4000, allowAbove:true, provisional:false, options:['Founder Absence Simulation','Institutional Memory Recovery Sprint','Workflow Momentum Analysis','Operational Stack Review','Handoff Failure Analysis'] },
    { id:'ai', name:'AI Enablement Through OEI', description:'Optional AI Enablement when OEI findings support an intervention. Scope and price are determined for each proposal.', model:'custom', unitPrice:0, min:0, max:0, allowAbove:true, provisional:false, options:[] }
  ];
  const $ = (s, root=document) => root.querySelector(s);
  const $$ = (s, root=document) => [...root.querySelectorAll(s)];
  const clone = value => JSON.parse(JSON.stringify(value));
  const safeRead = (key, fallback, validate) => { try { const value=JSON.parse(localStorage.getItem(key)); return validate(value) ? value : fallback; } catch { return fallback; } };
  const validCatalog = value => Array.isArray(value) && value.length === defaults.length && defaults.every(d => value.some(x => x && x.id===d.id && typeof x.name==='string' && typeof x.description==='string' && ['fixed','range','custom'].includes(x.model) && Number.isFinite(Number(x.unitPrice)) && Number.isFinite(Number(x.min)) && Number.isFinite(Number(x.max)) && Array.isArray(x.options) && x.options.every(option=>typeof option==='string') && typeof x.allowAbove==='boolean'));
  const validQuotes = value => Array.isArray(value) && value.every(q => q && typeof q.id==='string' && q.data && Array.isArray(q.data.items));
  let catalog = safeRead(KEYS.catalog, clone(defaults), validCatalog);
  let saved = safeRead(KEYS.quotes, [], validQuotes);
  let quote = freshQuote();
  let currentId = null;

  function today() { const d=new Date();return `${d.getFullYear()}-${String(d.getMonth()+1).padStart(2,'0')}-${String(d.getDate()).padStart(2,'0')}`; }
  function refNumber() { const stamp=today().replaceAll('-','');return `OEI-${stamp}-${Math.random().toString(36).slice(2,6).toUpperCase()}`; }
  function freshQuote() { return { organization:'', contactName:'', contactEmail:'', reference:refNumber(), createdAt:today(), expiresAt:'', currency:'USD', clientNotes:'', internalNotes:'', items:[] }; }
  function esc(value) { return String(value ?? '').replace(/[&<>"']/g, ch => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[ch])); }
  function money(value, currency=quote.currency) { try { return new Intl.NumberFormat(undefined,{style:'currency',currency,maximumFractionDigits:currency==='COP'?0:2}).format(Number(value)||0); } catch { return `${currency} ${Number(value)||0}`; } }
  function notice(message, error=false) { const el=$('#notice'); el.textContent=message; el.hidden=false; el.classList.toggle('error',error); clearTimeout(notice.timer); notice.timer=setTimeout(()=>el.hidden=true,4200); }
  function persistQuotes() { localStorage.setItem(KEYS.quotes,JSON.stringify(saved)); }
  function persistCatalog() { localStorage.setItem(KEYS.catalog,JSON.stringify(catalog)); }
  function service(id) { return catalog.find(item=>item.id===id); }
  function validItem(item) { return item && service(item.serviceId) && Number.isFinite(Number(item.unitPrice)) && Number(item.unitPrice)>=0 && Number.isInteger(Number(item.quantity)) && Number(item.quantity)>0; }
  function amountError(item) {
    const svc=item.catalogSnapshot||service(item.serviceId), amount=Number(item.unitPrice), min=Number(svc.min), max=Number(svc.max);
    if (!Number.isFinite(amount)||amount<=0) return 'Enter a unit price greater than zero.';
    if (svc.model==='range' && amount<min) return `Price must be at least ${money(min)}.`;
    if (svc.model==='range' && amount>max && !svc.allowAbove) return `Price must not exceed ${money(max)}.`;
    if (svc.model==='range' && amount>max && svc.allowAbove && !item.overageReason.trim()) return `Add a reason for pricing above ${money(max)}.`;
    return '';
  }
  function switchTab(name) { $$('.bill-tabs button').forEach(b=>{const active=b.dataset.tab===name;b.classList.toggle('is-active',active);b.setAttribute('aria-selected',String(active));}); $$('.bill-tab-panel').forEach(p=>{const active=p.id===`${name}-panel`;p.classList.toggle('is-active',active);p.hidden=!active;}); }
  function syncQuoteFields() { $$('[data-quote]').forEach(field=>{field.value=quote[field.dataset.quote]??'';}); }
  function updateQuoteField(field) { quote[field.dataset.quote]=field.value; if(field.dataset.quote==='currency'){renderLines();} renderPreview(); }
  function addLine(serviceId, options={}) {
    const svc=service(serviceId); if(!svc)return;
    quote.items.push({ id:crypto.randomUUID ? crypto.randomUUID() : `line-${Date.now()}-${Math.random()}`, serviceId, serviceName:svc.name, description:svc.description, catalogSnapshot:clone(svc), option:options.option||'', quantity:1, unitPrice:Number(svc.unitPrice)||0, overageReason:'', scope:'' });
    renderLines();renderPreview();
  }
  function linePriceField(item, index, svc) {
    const label=svc.model==='fixed'?'Unit price':svc.model==='range'?'Unit price':'Manual unit price';
    const limit=svc.model==='range' ? `${money(svc.min)}–${money(svc.max)}${svc.allowAbove?'+':''}` : svc.model==='fixed'&&svc.id==='practitioner'?'Per practitioner':svc.model==='fixed'?'Fixed unit price':'Set for this quote';
    return `<label class="line-field">${label}<input type="number" min="0" step="${quote.currency==='COP'?1:0.01}" inputmode="decimal" data-item="${index}" data-key="unitPrice" value="${esc(item.unitPrice)}" aria-label="${esc(label)}"><span class="price-hint">${esc(limit)}${svc.provisional?' · provisional':''}</span></label>`;
  }
  function renderLines() {
    const box=$('#line-items');
    if (!quote.items.length) box.innerHTML='<div class="saved-empty">No services added. Choose a starting configuration or add a service.</div>';
    else box.innerHTML=quote.items.map((item,i)=>{const svc=item.catalogSnapshot||service(item.serviceId);if(!svc)return '';const err=amountError(item);const optionControl=svc.options.length?`<label class="line-field">Investigation type<select data-item="${i}" data-key="option"><option value="">Select type</option>${svc.options.map(x=>`<option ${item.option===x?'selected':''}>${esc(x)}</option>`).join('')}</select></label>`:'';const reasonVisible=svc.model==='range'&&svc.allowAbove&&Number(item.unitPrice)>Number(svc.max);return `<article class="bill-line" data-line-id="${esc(item.id)}" data-line-index="${i}"><div class="bill-line-head"><div><strong>${esc(item.serviceName)}</strong><small>${esc(svc.model==='fixed'&&svc.provisional?'Provisional fixed price per practitioner':svc.model==='range'?`Catalog range ${money(svc.min)}–${money(svc.max)}${svc.allowAbove?'+':''}`:'Custom-scoped pricing')}</small></div><button class="line-delete" data-remove="${i}" aria-label="Remove ${esc(item.serviceName)}">Remove</button></div><div class="line-fields-grid">${optionControl}<label class="line-field">${svc.id==='practitioner'?'Practitioners':'Quantity'}<input type="number" min="1" step="1" value="${esc(item.quantity)}" data-item="${i}" data-key="quantity"></label>${linePriceField(item,i,svc)}<label class="line-field">Line subtotal<input type="text" readonly value="${esc(money(Number(item.unitPrice)*Number(item.quantity)))}"></label><label class="line-field full">Description / scope note<textarea data-item="${i}" data-key="scope" rows="2" placeholder="Optional client-facing scope note">${esc(item.scope)}</textarea></label>${reasonVisible?`<label class="line-field full above-reason">Reason for amount above ${esc(money(svc.max))}<textarea data-item="${i}" data-key="overageReason" rows="2" placeholder="Explain the reason for exceeding the catalog range">${esc(item.overageReason)}</textarea></label>`:''}</div>${err?`<p class="line-error">${esc(err)}</p>`:''}</article>`;}).join('');
    $('#service-select').innerHTML=catalog.map(s=>`<option value="${esc(s.id)}">${esc(s.name)}</option>`).join('');
  }
  function renderPreview() {
    const valid=quote.items.filter(validItem);const total=valid.reduce((sum,item)=>sum+Number(item.quantity)*Number(item.unitPrice),0);
    const rows=quote.items.map(item=>`<tr><td><strong>${esc(item.serviceName)}</strong>${item.description?`<div class="quote-line-desc">${esc(item.description)}</div>`:''}${item.option?`<div class="quote-line-desc">${esc(item.option)}</div>`:''}${item.scope?`<div class="quote-line-desc">${esc(item.scope)}</div>`:''}${item.overageReason?`<div class="quote-line-desc">Scope note: ${esc(item.overageReason)}</div>`:''}</td><td class="numeric">${esc(item.quantity)}</td><td class="numeric">${esc(money(item.unitPrice))}</td><td class="numeric">${esc(money(Number(item.quantity)*Number(item.unitPrice)))}</td></tr>`).join('');
    const client=quote.organization||quote.contactName||quote.contactEmail?`<div class="quote-client"><span class="quote-doc-label">PREPARED FOR</span>${quote.organization?`<strong>${esc(quote.organization)}</strong>`:''}${quote.contactName?`<p>${esc(quote.contactName)}</p>`:''}${quote.contactEmail?`<p>${esc(quote.contactEmail)}</p>`:''}</div>`:'';
    $('#quote-preview').innerHTML=`<div class="quote-brand"><img src="images/oei-institute-logo.png" alt="OEI Institute"><span>Operational Forensics<br>for Growing Teams</span></div><div class="quote-title"><div><div class="quote-doc-label">COMMERCIAL PROPOSAL</div><h2>QUOTATION</h2></div><div class="quote-ref"><strong>${esc(quote.reference||'Quote reference')}</strong>Created ${esc(quote.createdAt||'—')}<br>${quote.expiresAt?`Valid through ${esc(quote.expiresAt)}`:'No expiration date set'}</div></div>${client}<table class="quote-table"><thead><tr><th>Service and scope</th><th class="numeric">Qty</th><th class="numeric">Unit price</th><th class="numeric">Subtotal</th></tr></thead><tbody>${rows||'<tr><td colspan="4">Add a service to begin this quotation.</td></tr>'}</tbody></table><table class="quote-totals"><tbody><tr><td>Total</td><td>${esc(money(total))}</td></tr></tbody></table>${quote.clientNotes?`<div class="quote-client-notes"><strong>Notes</strong>${esc(quote.clientNotes)}</div>`:''}<div class="quote-disclaimer"><strong>Quotation only.</strong> This document is a proposal for review, not an invoice or payment request. No payment is due by virtue of this quotation.</div>`;
    $('#draft-state').textContent=currentId?'Editing saved draft':'Unsaved draft';
  }
  function renderSaved() {
    $('#draft-count').textContent=String(saved.length);const holder=$('#saved-quotes');
    holder.innerHTML=saved.length?saved.slice().sort((a,b)=>(b.updatedAt||'').localeCompare(a.updatedAt||'')).map(q=>`<article class="saved-quote ${q.id===currentId?'is-current':''}"><button data-open="${esc(q.id)}"><strong>${esc(q.data.organization||'Unnamed client')}</strong><small>${esc(q.data.reference||'No reference')} · ${esc(q.data.createdAt||'')}</small><small>${esc(money(sumQuote(q.data),q.data.currency||'USD'))}</small></button><div class="saved-quote-actions"><button data-duplicate="${esc(q.id)}">Duplicate</button><button data-delete="${esc(q.id)}">Delete</button></div></article>`).join(''):'<div class="saved-empty">No saved quote drafts yet.</div>';
  }
  function sumQuote(data) { return (data.items||[]).reduce((sum,x)=>sum+(Number(x.quantity)||0)*(Number(x.unitPrice)||0),0); }
  function normalizedData(data) { const base=freshQuote();const copy={...base,...data};copy.currency=copy.currency==='COP'?'COP':'USD';copy.items=Array.isArray(copy.items)?copy.items.filter(x=>x&&typeof x==='object').map(x=>({...x,id:String(x.id||`line-${Math.random()}`),serviceId:service(x.serviceId)?x.serviceId:'ai',serviceName:String(x.serviceName||service(x.serviceId)?.name||'Service'),description:String(x.description||''),catalogSnapshot:x.catalogSnapshot&&['fixed','range','custom'].includes(x.catalogSnapshot.model)&&Number.isFinite(Number(x.catalogSnapshot.min))&&Number.isFinite(Number(x.catalogSnapshot.max))&&Array.isArray(x.catalogSnapshot.options)?x.catalogSnapshot:clone(service(x.serviceId)||service('ai')),option:String(x.option||''),quantity:Math.max(1,Math.floor(Number(x.quantity)||1)),unitPrice:Math.max(0,Number(x.unitPrice)||0),overageReason:String(x.overageReason||''),scope:String(x.scope||'')})):[];return copy; }
  function saveDraft() {
    if(quote.contactEmail && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(quote.contactEmail)){notice('Enter a valid client email address or leave it blank.',true);return;}
    const invalid=quote.items.find(item=>!validItem(item)||amountError(item));if(invalid){notice(amountError(invalid)||'Review line item quantities and prices before saving.',true);return;}
    const now=new Date().toISOString();if(currentId){const index=saved.findIndex(x=>x.id===currentId);if(index>=0)saved[index]={...saved[index],data:clone(quote),updatedAt:now};else currentId=null;}
    if(!currentId){currentId=crypto.randomUUID?crypto.randomUUID():`quote-${Date.now()}`;saved.push({id:currentId,data:clone(quote),createdAt:now,updatedAt:now});}
    try{persistQuotes();renderSaved();renderPreview();notice('Draft saved in this browser.');}catch{notice('Could not save this draft. Browser storage may be full or unavailable.',true);}
  }
  function openSaved(id) { const entry=saved.find(x=>x.id===id);if(!entry)return;currentId=id;quote=normalizedData(clone(entry.data));syncQuoteFields();renderLines();renderPreview();renderSaved();switchTab('quotes'); }
  function duplicateSaved(id) { const entry=saved.find(x=>x.id===id);if(!entry)return;quote=normalizedData(clone(entry.data));quote.reference=refNumber();quote.createdAt=today();currentId=null;syncQuoteFields();renderLines();renderPreview();renderSaved();switchTab('quotes');notice('Quote duplicated as a new unsaved draft.'); }
  function deleteSaved(id) { const entry=saved.find(x=>x.id===id);if(!entry)return;if(!confirm(`Delete draft ${entry.data.reference||''}? This cannot be undone.`))return;saved=saved.filter(x=>x.id!==id);if(currentId===id){currentId=null;quote=freshQuote();syncQuoteFields();renderLines();renderPreview();}persistQuotes();renderSaved();notice('Draft deleted.'); }
  function editLineField(field) {
    const item=quote.items[Number(field.dataset.item)];if(!item)return;const key=field.dataset.key;
    if(key==='quantity')item[key]=Math.max(1,Math.floor(Number(field.value)||1));else if(key==='unitPrice')item[key]=Math.max(0,Number(field.value)||0);else item[key]=field.value;
    const line=field.closest('.bill-line');if(line){const subtotal=$('input[readonly]',line);if(subtotal)subtotal.value=money(Number(item.unitPrice)*Number(item.quantity));}
    renderPreview();
  }
  function catalogEditor() {
    $('#catalog-editor').innerHTML=catalog.map((s,i)=>`<article class="catalog-card" data-catalog="${i}">${s.provisional?'<span class="catalog-tag">PROVISIONAL DEFAULT</span>':''}<h3>${esc(s.name)}</h3><p>Pricing model: ${esc(s.model==='fixed'?'Fixed unit price':s.model==='range'?'Range':'Custom-scoped')} · ${s.id==='practitioner'?'Priced per practitioner':s.id==='ai'?'Optional service':'Quantity selectable'}</p><div class="bill-form-grid"><label>Service name<input data-catalog-key="name" value="${esc(s.name)}"></label><label>Pricing model<select data-catalog-key="model"><option value="fixed" ${s.model==='fixed'?'selected':''}>Fixed unit price</option><option value="range" ${s.model==='range'?'selected':''}>Price range</option><option value="custom" ${s.model==='custom'?'selected':''}>Custom-scoped</option></select></label><label class="full">Catalog description<textarea data-catalog-key="description" rows="3">${esc(s.description)}</textarea></label><label class="full">Service options · one per line<textarea data-catalog-key="options" rows="3">${esc(s.options.join('\n'))}</textarea></label><label>Default / minimum unit price<input type="number" min="0" step="0.01" data-catalog-key="unitPrice" value="${esc(s.unitPrice)}"></label><label>Range minimum<input type="number" min="0" step="0.01" data-catalog-key="min" value="${esc(s.min)}"></label><label>Range upper reference<input type="number" min="0" step="0.01" data-catalog-key="max" value="${esc(s.max)}"></label></div><label class="check-label"><input type="checkbox" data-catalog-key="provisional" ${s.provisional?'checked':''}>Mark catalog price as provisional and require quote review</label><label class="check-label"><input type="checkbox" data-catalog-key="allowAbove" ${s.allowAbove?'checked':''}>Allow pricing above upper reference with an explicit reason</label><p class="price-hint">Catalog changes apply to new line items only; existing quote line items keep their snapshots.</p></article>`).join('');
  }
  function updateCatalogField(field) { const card=field.closest('[data-catalog]'), index=Number(card.dataset.catalog), s=catalog[index], key=field.dataset.catalogKey;let value=field.type==='checkbox'?field.checked:field.value;if(key==='options')value=value.split(/\r?\n/).map(x=>x.trim()).filter(Boolean);if(['unitPrice','min','max'].includes(key)){value=Number(value);if(!Number.isFinite(value)||value<0){notice('Catalog prices must be non-negative numbers.',true);catalogEditor();return;}if(key==='min'&&s.model==='range'&&value>Number(s.max)){notice('The range minimum cannot exceed the upper reference.',true);catalogEditor();return;}if(key==='max'&&s.model==='range'&&value<Number(s.min)){notice('The upper reference cannot be below the range minimum.',true);catalogEditor();return;}}s[key]=value;if(key==='model'&&value==='fixed'){s.max=s.min;s.unitPrice=s.unitPrice||s.min;}try{persistCatalog();catalogEditor();renderLines();renderPreview();notice('Catalog default updated. Saved quote snapshots remain unchanged.');}catch{notice('Could not save the catalog to browser storage.',true);} }
  function pathway(which) { quote=freshQuote();currentId=null;const base=which.startsWith('practitioner')?'practitioner':'team';addLine(base);if(which.endsWith('-ai'))addLine('ai');syncQuoteFields();renderSaved();switchTab('quotes'); }

  $('#new-quote').addEventListener('click',()=>{quote=freshQuote();currentId=null;syncQuoteFields();renderLines();renderPreview();renderSaved();switchTab('quotes');});
  $('#save-quote').addEventListener('click',saveDraft);
  $('#add-line').addEventListener('click',()=>addLine($('#service-select').value||catalog[0].id));
  $('#add-selected').addEventListener('click',()=>addLine($('#service-select').value));
  $('#print-quote').addEventListener('click',()=>window.print());
  $$('.bill-tabs button').forEach(button=>button.addEventListener('click',()=>switchTab(button.dataset.tab)));
  $$('[data-quote]').forEach(field=>field.addEventListener('input',()=>updateQuoteField(field)));
  $('#line-items').addEventListener('input',event=>{if(event.target.matches('[data-item]'))editLineField(event.target);});
  $('#line-items').addEventListener('change',event=>{if(event.target.matches('[data-item]')){editLineField(event.target);renderLines();}});
  $('#line-items').addEventListener('click',event=>{const btn=event.target.closest('[data-remove]');if(btn){quote.items.splice(Number(btn.dataset.remove),1);renderLines();renderPreview();}});
  $('#saved-quotes').addEventListener('click',event=>{const target=event.target.closest('[data-open],[data-duplicate],[data-delete]');if(!target)return;if(target.dataset.open)openSaved(target.dataset.open);if(target.dataset.duplicate)duplicateSaved(target.dataset.duplicate);if(target.dataset.delete)deleteSaved(target.dataset.delete);});
  $('#saved-quotes').addEventListener('keydown',()=>{});
  document.addEventListener('click',event=>{const btn=event.target.closest('[data-path]');if(btn)pathway(btn.dataset.path);});
  $('#catalog-editor').addEventListener('change',event=>{if(event.target.matches('[data-catalog-key]'))updateCatalogField(event.target);});
  $('#reset-catalog').addEventListener('click',()=>{if(!confirm('Restore the starting service catalog defaults? Saved quotes will not change.'))return;catalog=clone(defaults);persistCatalog();catalogEditor();renderLines();renderPreview();notice('Starting catalog defaults restored.');});
  syncQuoteFields();renderLines();renderSaved();renderPreview();catalogEditor();
})();
