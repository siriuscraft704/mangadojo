/* Home: preenche os números e o índice do curso a partir do catálogo (sem duplicar dados no HTML). */
(() => {
  'use strict';
  const lessons = window.MANGADOJO_LESSONS || [];
  const course = window.MANGADOJO_COURSE || {modules: []};
  if (!lessons.length) return;

  const totals = {
    aulas: lessons.length,
    etapas: lessons.reduce((s, l) => s + l.steps.length, 0),
    modulos: course.modules.length,
    pranchas: lessons.filter(l => l.lessonType === 'board-study').length
  };
  document.querySelectorAll('[data-n]').forEach(n => { if (totals[n.dataset.n] != null) n.textContent = totals[n.dataset.n]; });

  const el = (tag, cls, text) => { const n = document.createElement(tag); if (cls) n.className = cls; if (text != null) n.textContent = text; return n; };
  const list = document.getElementById('indice');
  if (!list) return;
  const ORDER = ['Iniciante', 'Intermediário', 'Avançado'];
  course.modules.forEach((m, i) => {
    const items = lessons.filter(l => l.category === m.category);
    if (!items.length) return;
    const levels = ORDER.filter(x => items.some(l => l.level === x));
    const li = el('li'), a = el('a');
    a.href = 'trilhas.html#modulo-' + m.id;
    a.append(
      el('span', 'indice__n num', String(i + 1).padStart(2, '0')),
      el('span', 'indice__t', m.title),
      el('span', 'indice__s', m.summary)
    );
    const meta = el('span', 'indice__m');
    meta.append(el('span', 'num', items.length + (items.length === 1 ? ' aula' : ' aulas') + ' · ' + levels.join(' e ')));
    const arrow = el('span', 'seta'); arrow.setAttribute('aria-hidden', 'true'); meta.append(arrow);
    a.append(meta); li.append(a); list.append(li);
  });
})();
