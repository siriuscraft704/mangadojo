/* Página do Curso: monta módulos e cartões a partir de catalog.generated.js, curso.generated.js e do progresso salvo. */
(() => {
  'use strict';
  const lessons = window.MANGADOJO_LESSONS || [];
  const course = window.MANGADOJO_COURSE || {modules: []};
  const STORAGE = 'mangadojo-v3-state';

  let state = {};
  try { state = JSON.parse(localStorage.getItem(STORAGE) || '{}') || {}; } catch (e) { state = {}; }
  const done = new Set(Array.isArray(state.done) ? state.done : []);
  const steps = state.step && typeof state.step === 'object' ? state.step : {};

  const LEVEL_ORDER = {'Iniciante': 0, 'Intermediário': 1, 'Avançado': 2};
  const TYPE_LABEL = {'board-study': 'Prancha de estudo', 'reference-studies': 'Estudo de referências'};
  const typeOf = l => TYPE_LABEL[l.lessonType] || 'Passo a passo';
  const href = id => 'index.html?lesson=' + encodeURIComponent(id) + '#workspace';
  const el = (tag, cls, text) => { const n = document.createElement(tag); if (cls) n.className = cls; if (text != null) n.textContent = text; return n; };
  const hours = min => { const h = min / 60; return h >= 10 ? Math.round(h) + ' h' : (Math.round(h * 10) / 10).toString().replace('.', ',') + ' h'; };
  const plural = (n, one, many) => n + ' ' + (n === 1 ? one : many);

  // Ordem dentro do módulo: aulas passo a passo primeiro, depois pranchas; do mais simples ao mais difícil.
  const order = l => [l.lessonType === 'board-study' ? 1 : 0, LEVEL_ORDER[l.level] ?? 9];
  const byOrder = (a, b) => {
    const x = order(a), y = order(b);
    return x[0] - y[0] || x[1] - y[1] || a.id.localeCompare(b.id, 'pt-BR', {numeric: true});
  };

  const modules = course.modules.map((m, i) => {
    const list = lessons.filter(l => l.category === m.category).sort(byOrder);
    return {...m, index: i + 1, list, finished: list.filter(l => done.has(l.id)).length, minutes: list.reduce((s, l) => s + (l.min || 0), 0)};
  }).filter(m => m.list.length);

  const nextOf = m => m.list.find(l => !done.has(l.id) && Number(steps[l.id] || 0) > 0) || m.list.find(l => !done.has(l.id)) || null;

  // Resumo
  const totalLessons = modules.reduce((s, m) => s + m.list.length, 0);
  const totalMin = modules.reduce((s, m) => s + m.minutes, 0);
  const totalDone = modules.reduce((s, m) => s + m.finished, 0);
  const stats = document.getElementById('stats');
  for (const [value, label] of [[modules.length, 'módulos'], [totalLessons, 'aulas e pranchas'], [hours(totalMin), 'de prática'], [totalDone + ' de ' + totalLessons, 'concluídas']]) {
    const li = el('li'); li.append(el('b', '', String(value)), el('span', '', label)); stats.append(li);
  }
  document.getElementById('intro').textContent = course.intro || '';

  // Continue de onde parou
  const current = lessons.find(l => l.id === state.lesson);
  const box = document.getElementById('continuar');
  const started = current && (Number(steps[current.id] || 0) > 0 || done.has(current.id));
  const firstModule = modules[0];
  const nextModule = modules.find(m => m.finished < m.list.length);
  let target = null, kicker = 'Comece por aqui', note = '';
  if (started && !done.has(current.id)) {
    target = current; kicker = 'Continue de onde parou';
    note = 'Etapa ' + (Number(steps[current.id] || 0) + 1) + ' de ' + current.steps.length;
  } else if (nextModule) {
    target = nextOf(nextModule); kicker = totalDone ? 'Sua próxima aula' : 'Comece por aqui';
    note = 'Módulo ' + nextModule.index + ' · ' + nextModule.title;
  } else if (firstModule) {
    target = firstModule.list[0]; kicker = 'Curso concluído. Que tal revisar?'; note = 'Módulo 1 · ' + firstModule.title;
  }
  if (target) {
    const img = el('img', 'continue__thumb'); img.src = target.images[target.images.length - 1]; img.alt = ''; img.loading = 'lazy';
    const text = el('div', 'continue__text');
    text.append(el('small', '', kicker), el('strong', '', target.name), el('span', '', note + ' · ' + target.level + ' · ' + target.min + ' min'));
    const go = el('a', 'md-btn md-btn--primary', started && !done.has(current.id) ? 'Continuar aula' : 'Começar agora'); go.href = href(target.id);
    box.append(img, text, go); box.hidden = false;
  }

  // Módulos
  const root = document.getElementById('modulos');
  modules.forEach(m => {
    const complete = m.finished === m.list.length;
    const sec = el('section', 'md-card mod'); sec.id = 'modulo-' + m.id; sec.setAttribute('aria-labelledby', 'titulo-' + m.id);
    const head = el('div', 'mod__head');
    head.append(el('div', 'mod__num', String(m.index)));
    const info = el('div');
    const h = el('h3', 'mod__title', m.title); h.id = 'titulo-' + m.id;
    const out = el('p', 'mod__outcome'); out.append(el('b', '', 'Ao final: '), document.createTextNode(m.outcome.replace(/^Você\s+/, 'você ')));
    const meta = el('div', 'mod__meta');
    const bar = el('div', 'md-progress'); bar.setAttribute('role', 'progressbar'); bar.setAttribute('aria-label', 'Progresso do módulo ' + m.title);
    bar.setAttribute('aria-valuemin', '0'); bar.setAttribute('aria-valuemax', String(m.list.length)); bar.setAttribute('aria-valuenow', String(m.finished));
    const fill = el('span'); fill.style.width = Math.round(100 * m.finished / m.list.length) + '%'; bar.append(fill);
    meta.append(el('span', '', plural(m.list.length, 'aula', 'aulas') + ' · ' + hours(m.minutes)), bar, el('span', '', m.finished + ' concluídas'));
    info.append(h, el('p', 'mod__summary', m.summary), out, meta);
    head.append(info);
    const next = nextOf(m);
    const actionWrap = el('div', 'mod__action');
    const action = el('a', complete ? 'md-btn md-btn--ghost' : 'md-btn md-btn--primary', complete ? 'Revisar módulo' : (m.finished || Number(steps[(next || {}).id] || 0) ? 'Continuar módulo' : 'Começar módulo'));
    action.href = href((next || m.list[0]).id); actionWrap.append(action); head.append(actionWrap);
    sec.append(head);

    const details = el('details');
    if (nextModule && nextModule.id === m.id) details.open = true;
    details.append(el('summary', '', 'Ver as ' + m.list.length + ' ' + (m.list.length === 1 ? 'aula' : 'aulas') + ' deste módulo'));
    const ul = el('ul', 'lessons');
    for (const l of m.list) {
      const li = el('li'); const a = el('a', 'lesson'); a.href = href(l.id);
      const img = el('img', 'lesson__img'); img.src = l.images[l.lessonType === 'board-study' ? 0 : l.images.length - 1]; img.alt = 'Prévia: ' + l.name; img.loading = 'lazy'; img.decoding = 'async';
      const body = el('div', 'lesson__body'); body.append(el('span', 'lesson__name', l.name));
      const tags = el('div', 'lesson__tags');
      tags.append(el('span', 'md-pill md-pill--level', l.level), el('span', 'md-pill', l.min + ' min'), el('span', 'md-pill', typeOf(l)));
      if (done.has(l.id)) tags.append(el('span', 'md-pill md-pill--ok', '✓ Concluída'));
      else if (Number(steps[l.id] || 0) > 0) tags.append(el('span', 'md-pill md-pill--wip', 'Em andamento'));
      body.append(tags); a.append(img, body); li.append(a); ul.append(li);
    }
    details.append(ul); sec.append(details); root.append(sec);
  });
})();
