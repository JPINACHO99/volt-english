/* Volt English — exercises: building sessions, rendering each exercise type, feedback. */
(function () {
  'use strict';
  const V = window.V, D = window.DATA, h = V.h, S = V.S, FB = window.FB;
  V.VERDICT = { good: 'Good', ok: 'Okay', weak: 'Needs work', na: 'Not checked', bad: 'Wrong' };
  const shuffle = (a) => { a = a.slice(); for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; };
  const norm = (s) => s.toLowerCase().replace(/[’`]/g, "'").replace(/[.,!?;:"]/g, '').replace(/\s+/g, ' ').trim();
  const topicName = (t) => V.TOPICS.find((x) => x.id === t).n;
  const instr = (t) => h('p', { class: 'muted small' }, t);

  /* ---------- error bank (for "Review mistakes") ---------- */
  function record(ref, ok) {
    const k = JSON.stringify(ref);
    if (ok) delete S.errors[k]; else S.errors[k] = 1;
    V.save();
  }
  function itemFromRef(ref) {
    if (ref.k === 'g') return grammarItem(ref.i);
    if (ref.k === 'v') return defineItem(ref.t, ref.l, ref.i);
    if (ref.k === 'r') { const r = D.reading.find((x) => x.id === ref.id), q = r.mc[ref.q]; const x = ((D.rexp || {})[r.id] || [])[ref.q] || {}; return { type: 'choice', ref, context: r, prompt: q.q, options: q.o, answer: q.a, note: x.e, optNotes: x.w, instr: 'Read the text again if you need to, then answer.' }; }
    if (ref.k === 'p') return phrasalItem(ref.i, ref.m);
    if (ref.k === 'l') { const a = D.listening.find((x) => x.id === ref.id), g = a.gaps[ref.i]; return { type: 'input', ref, audio: a, sentence: g.s, answers: [g.a], instr: 'Listen and write the exact word you hear.' }; }
  }

  /* ---------- item builders ---------- */
  function grammarItem(i) {
    const g = D.grammar[i], ref = { k: 'g', i };
    const note = g[g[0] === 'kt' ? 7 : g[0] === 'open' ? 5 : 6] || (D.gnotes || [])[i] || '';
    if (g[0] === 'mc') return { type: 'choice', ref, note, optNotes: (D.gopt || {})[g[3]], prompt: g[3], options: g[4], answer: g[5], instr: 'Choose the correct option.' };
    if (g[0] === 'open') return { type: 'input', ref, note, sentence: g[3], answers: g[4], instr: 'Write ONE word in the gap.' };
    if (g[0] === 'wf') return { type: 'input', ref, note, sentence: g[3], root: g[4], answers: g[5], instr: 'Use the word in capitals to form a word that fits the gap.' };
    return { type: 'input', ref, note, pre: g[3], root: g[4], sentence: g[5], answers: g[6], instr: 'Complete the second sentence so that it means the same as the first. Use the word given without changing it (2–6 words).' };
  }
  function judgeItem(i) {
    const g = D.grammar[i], wrong = [0, 1, 2, 3].filter((k) => k !== g[5]), use = Math.random() < 0.5 ? g[5] : wrong[Math.floor(Math.random() * 3)];
    const notes = (D.gopt || {})[g[3]] || [], note = g[6] || (D.gnotes || [])[i] || '';
    return { type: 'judge', ref: { k: 'g', i }, sentence: g[3].replace('___', g[4][use]), right: g[3].replace('___', g[4][g[5]]), ok: use === g[5], chosen: g[4][use], wrongNote: notes[use] || '', note };
  }
  const pvPlain = (ex) => ex.replace(/[\[\]]/g, '');
  function phrasalItem(i, m) {
    const p = D.phrasal[i], ref = { k: 'p', i, m }, same = D.phrasal.map((x, j) => j).filter((j) => j !== i && D.phrasal[j][1] === p[1] && D.phrasal[j][0] !== p[0]);
    const others = shuffle(same).slice(0, 3), note = p[0] + ' = ' + p[2] + '. Example: ' + pvPlain(p[3]);
    const pvNote = (j) => (j === i ? '' : m === 'm' ? 'That is the meaning of “' + D.phrasal[j][0] + '”, as in: ' + pvPlain(D.phrasal[j][3]) : '“' + D.phrasal[j][0] + '” means ' + D.phrasal[j][2] + ', as in: ' + pvPlain(D.phrasal[j][3]));
    if (m === 'm') { const o = shuffle([i].concat(others)); return { type: 'choice', ref, note, optNotes: o.map(pvNote), say: p[0], prompt: pvPlain(p[3]), sub: 'What does “' + p[0] + '” mean here?', options: o.map((j) => D.phrasal[j][2]), answer: o.indexOf(i), instr: 'Choose the meaning of the phrasal verb.' }; }
    if (m === 'c') { const o = shuffle([i].concat(others)); return { type: 'choice', ref, note, optNotes: o.map(pvNote), prompt: 'Which phrasal verb means: “' + p[2] + '”?', options: o.map((j) => D.phrasal[j][0]), answer: o.indexOf(i), instr: 'Choose the phrasal verb.' }; }
    const parts = p[3].match(/\[[^\]]+\]/g), particle = p[0].split(' ').slice(1).join(' ');
    let sentence;
    if (parts.length > 1) sentence = p[3].replace(parts[parts.length - 1], '___').replace(/[\[\]]/g, '');
    else { const words = parts[0].slice(1, -1).split(' '); sentence = p[3].replace(parts[0], words[0] + ' ___'); }
    return { type: 'input', ref, note, hint: p[2], sentence, answers: [particle], instr: 'Complete the phrasal verb with the missing particle(s).' };
  }
  function phrasalList(level, job) {
    const all = D.phrasal.filter((p) => p[1] === level && (!job || p[4] === 'job')).sort((a, b) => a[0].localeCompare(b[0])), box = h('div');
    const draw = (q) => box.replaceChildren(all.filter((p) => !q || (p[0] + ' ' + p[2]).toLowerCase().includes(q)).map((p) => h('div', { class: 'card', style: 'margin:8px 0;padding:12px' },
      h('div', { class: 'row' }, h('b', { class: 'grow' }, p[0]), V.sayBtn(p[0]), h('button', { class: 'ic', title: 'Add to My words', onclick: (e) => { V.addMyWord(p[0], p[2], pvPlain(p[3])); e.target.textContent = '✓'; } }, '＋')),
      h('div', null, p[2]), h('div', { class: 'muted small' }, '“' + pvPlain(p[3]) + '”'))));
    const search = h('input', { type: 'text', placeholder: 'Search a verb or a meaning…', oninput: () => draw(search.value.trim().toLowerCase()) });
    draw('');
    V.go(() => ({ title: (job ? 'Interview phrasal verbs · ' : 'Phrasal verbs · ') + level, body: [h('p', { class: 'muted' }, all.length + (job ? ' interview phrasal verbs at this level.' : ' phrasal verbs at this level.')), search, box] }));
  }
  function defineItem(t, l, i) {
    const w = D.vocab[t][l].w[i];
    return { type: 'input', ref: { k: 'v', t, l, i }, pre: w[1], sentence: '___', answers: [w[0]], word: w, instr: 'Write the word or phrase that matches the definition. (' + w[0].length + ' characters, starts with “' + w[0][0] + '”)' };
  }

  V.start = function (sec, level, topic, mode) {
    let items = [];
    const cell = (list) => { // several items can share a topic and level: pick one, avoiding the last one shown
      const all = list.filter((x) => x.t === topic && x.l === level), fresh = all.filter((x) => x.id !== S.lastItem);
      const pick = (fresh.length ? fresh : all)[Math.floor(Math.random() * (fresh.length ? fresh.length : all.length))];
      if (pick) { S.lastItem = pick.id; V.save(); }
      return pick;
    };
    if (sec === 'phrasal') {
      if (mode === 'list' || mode === 'joblist') return phrasalList(level, mode === 'joblist');
      const idx = shuffle(D.phrasal.map((p, i) => i).filter((i) => D.phrasal[i][1] === level && (mode !== 'jobpv' || D.phrasal[i][4] === 'job')));
      if (mode === 'jobpv') items = idx.slice(0, 10).map((i, k) => phrasalItem(i, ['m', 'c', 'p'][k % 3]));
      if (mode === 'pmatch') { const g = idx.slice(0, 10); items = [g.slice(0, 5), g.slice(5, 10)].map((part) => ({ type: 'pairs', left: part.map((i) => D.phrasal[i][0]), right: part.map((i) => D.phrasal[i][2]), say: true, instr: 'Tap a phrasal verb, then tap its meaning.' })); }
      else if (mode === 'pcards') return V.startCards(idx.slice(0, 15).map((i) => { const p = D.phrasal[i]; V.srsAdd(p[0], p[2], pvPlain(p[3])); return p[0]; }));
      if (!items.length) items = idx.slice(0, 10).map((i) => phrasalItem(i, mode === 'meaning' ? 'm' : mode === 'choose' ? 'c' : 'p'));
    } else if (sec === 'grammar') {
      let idx = D.grammar.map((g, i) => i).filter((i) => D.grammar[i][1] === level && (mode === 'mix' || D.grammar[i][0] === (mode === 'judge' ? 'mc' : mode)));
      idx = shuffle(idx).sort((a, b) => (D.grammar[b][2] === topic) - (D.grammar[a][2] === topic)).slice(0, 10);
      items = idx.map(mode === 'judge' ? judgeItem : grammarItem);
    } else if (sec === 'vocab') {
      const n = D.vocab[topic][level].w.length;
      const cw = D.vocab[topic][level].w;
      if (mode === 'define') items = shuffle([...Array(n).keys()]).slice(0, 8).map((i) => defineItem(topic, level, i));
      else if (mode === 'match') { const g = shuffle([...Array(n).keys()]).slice(0, 10); items = [g.slice(0, 5), g.slice(5, 10)].map((part) => ({ type: 'pairs', left: part.map((i) => cw[i][0]), right: part.map((i) => cw[i][1]), refs: part.map((i) => ({ k: 'v', t: topic, l: level, i })), say: true, instr: 'Tap a word, then tap its meaning.' })); }
      else if (mode === 'spell') items = shuffle([...Array(n).keys()]).slice(0, 8).map((i) => ({ type: 'input', ref: { k: 'v', t: topic, l: level, i }, speakWord: cw[i][0], hint: cw[i][1], sentence: '___', answers: [cw[i][0]], word: cw[i], instr: 'Listen and write the word or phrase you hear. Play it as many times as you like.' }));
      else if (mode === 'cards') return V.startCards(D.vocab[topic][level].w.map((w) => { V.srsAdd(w[0], w[1], w[2]); return w[0]; }));
      else { const c2 = D.vocab[topic][level], n2 = c2.para3 ? 3 : c2.para2 ? 2 : 1; S.paraTurn = ((S.paraTurn || 0) + 1) % 3; items = [{ type: 'gappara', t: topic, l: level, bank: mode === 'bank', which: S.paraTurn % n2 }]; }
    } else if (sec === 'reading') items = [{ type: mode === 'mc' ? 'readmc' : mode === 'gapped' ? 'gaptext' : 'match', r: cell(D.reading) }];
    else if (sec === 'listening') items = [{ type: mode === 'open' ? 'listenopen' : mode === 'who' ? 'listenwho' : 'listengaps', a: cell(D.listening) }];
    else if (sec === 'speaking') {
      const sc = D.scenes[topic];
      if (mode === 'describe') { const s = sc[Math.floor(Math.random() * 2)]; items = [{ type: 'speak', kind: 'describe', prompt: 'Describe this picture in as much detail as you can. Say what you can see, what is probably happening and how the people might feel.', scenes: [s], model: s.model }]; }
      else if (mode === 'compare') items = [{ type: 'speak', kind: 'compare', prompt: D.compareQ[topic], scenes: sc, model: D.compareModel }];
      else {
        const sets = [D.speak[topic][level][mode], (((D.speak2 || {})[topic] || {})[level] || {})[mode]].filter(Boolean);
        const key = 'sp:' + topic + level + mode; S.turns = S.turns || {}; S.turns[key] = ((S.turns[key] || 0) + 1) % sets.length; V.save();
        const p = sets[S.turns[key]]; items = [{ type: 'speak', kind: mode, prompt: p[0], model: p[1] }];
      }
    } else if (sec === 'writing') {
      const ws = [D.writing[topic][level], ((D.writing2 || {})[topic] || {})[level]].filter(Boolean);
      const wk = 'wr:' + topic + level + mode; S.turns = S.turns || {}; S.turns[wk] = ((S.turns[wk] || 0) + 1) % ws.length; V.save();
      const w = ws[S.turns[wk]];
      items = [mode === 'essay' ? { type: 'write', wtype: 'essay', prompt: w.essay[0], model: w.essay[1] } : { type: 'write', wtype: w.task[0], prompt: w.task[1], model: w.task[2] }];
    }
    items = items.filter((x) => x && (x.type.indexOf('listen') ? true : x.a) && (/readmc|gaptext|match/.test(x.type) ? x.r : true));
    const sn = V.SECTIONS.find((s) => s.id === sec);
    run({ sec, level, title: sn.n + ' · ' + level + (topic ? ' · ' + topicName(topic) : ''), items, again: () => V.start(sec, level, topic, mode) });
  };
  V.startReview = function () {
    const items = shuffle(Object.keys(S.errors)).slice(0, 10).map((k) => { try { return itemFromRef(JSON.parse(k)); } catch (e) { delete S.errors[k]; return null; } }).filter(Boolean);
    run({ sec: 'review', level: S.lastLevel || 'B2', title: 'Review mistakes', items });
  };
  V.startCards = function (words) {
    run({ sec: 'cards', level: S.lastLevel || 'B2', title: 'Flashcards', items: shuffle(words).slice(0, 20).map((w) => ({ type: 'card', w })) });
  };

  /* ---------- session runner ---------- */
  function run(cfg) {
    let i = 0, ok = 0, tot = 0; const weak = [];
    const root = h('div');
    function step() {
      root.replaceChildren();
      if (!cfg.items.length) { root.append(h('p', { class: 'muted center' }, 'There is no content for this combination yet.'), h('div', { class: 'row end' }, h('button', { class: 'btn', onclick: V.goHome }, 'Home'))); return; }
      if (i >= cfg.items.length) return summary();
      const it = cfg.items[i], box = h('div', { class: 'card' }), foot = h('div', { class: 'row end' });
      root.append(h('div', { class: 'row small muted' }, h('span', { class: 'grow' }, 'Exercise ' + (i + 1) + ' of ' + cfg.items.length), tot ? h('span', null, Math.round(ok * 10) / 10 + ' / ' + tot + ' correct') : null),
        h('div', { class: 'prog' }, h('i', { style: 'width:' + (i * 100) / cfg.items.length + '%' })), box, foot);
      RENDER[it.type](it, box, {
        level: cfg.level,
        finish(res) { // res: {ok, tot, weak:[labels]} — tot 0 for unscored work
          if (res) { ok += res.ok || 0; tot += res.tot || 0; (res.weak || []).forEach((w) => weak.push(w)); }
          foot.replaceChildren(h('button', { class: 'btn', onclick: () => { i++; step(); window.scrollTo(0, 0); } }, i + 1 < cfg.items.length ? 'Next →' : 'Finish'));
        }
      });
    }
    function summary() {
      if (cfg.sec !== 'cards') V.addStat(cfg.sec === 'review' ? 'grammar' : cfg.sec, cfg.sec === 'review' ? 0 : ok, cfg.sec === 'review' ? 0 : tot); else { S.days[V.today()] = (S.days[V.today()] || 0) + 1; V.save(); }
      const pct = tot ? Math.round((ok * 100) / tot) : null;
      const col = pct == null ? 'var(--good)' : pct >= 80 ? 'var(--good)' : pct >= 50 ? 'var(--ok)' : 'var(--bad)', C = 2 * Math.PI * 56;
      const R = ringSvg(col, C), fg = R.fg;
      const num = h('b', null, '0%');
      const ring = pct == null ? h('div', { class: 'big-emoji' }, '✅') : h('div', { class: 'ring' }, R.svg, num);
      requestAnimationFrame(() => setTimeout(() => {
        if (pct == null) return; fg.style.strokeDashoffset = C * (1 - pct / 100);
        const t0 = performance.now(); (function tick(t) { const k = Math.min(1, (t - t0) / 1100); num.textContent = Math.round(pct * (1 - Math.pow(1 - k, 3))) + '%'; if (k < 1) requestAnimationFrame(tick); })(t0);
        if (pct >= 80) confetti();
      }, 120));
      root.append(h('div', { class: 'prog' }, h('i', { style: 'width:100%' })), h('div', { class: 'card center' }, ring, pct == null ? null : h('div', { class: 'big-emoji', style: 'font-size:1.8rem;animation-delay:.9s' }, pct >= 80 ? '🏆' : pct >= 50 ? '👍' : '💪'),
        h('h2', null, pct == null ? 'Session complete' : Math.round(ok * 10) / 10 + ' / ' + tot + ' correct (' + pct + '%)'),
        weak.length ? h('div', { style: 'text-align:left' }, h('h3', null, 'Weak points'), h('ul', null, [...new Set(weak)].slice(0, 8).map((w) => h('li', null, w))), h('p', { class: 'muted small' }, 'Wrong answers were added to “Review mistakes”.')) : (pct != null ? h('p', { class: 'muted' }, 'No weak points this time.') : null),
        h('div', { class: 'row', style: 'justify-content:center;margin-top:12px' }, cfg.again ? h('button', { class: 'btn sec', onclick: () => { history.back(); setTimeout(cfg.again, 60); } }, 'Practise again') : null, h('button', { class: 'btn', onclick: V.goHome }, 'Home'))));
    }
    V.go(() => ({ title: cfg.title, body: [root] }));
    step();
  }

  function ringSvg(col, C) {
    const NS = 'http://www.w3.org/2000/svg', svg = document.createElementNS(NS, 'svg');
    svg.setAttribute('viewBox', '0 0 132 132'); svg.setAttribute('width', '132'); svg.setAttribute('height', '132');
    const mk = (cls) => { const c = document.createElementNS(NS, 'circle'); c.setAttribute('cx', 66); c.setAttribute('cy', 66); c.setAttribute('r', 56); c.setAttribute('class', cls); svg.append(c); return c; };
    mk('bgc'); const fg = mk('fgc'); fg.style.stroke = col; fg.style.strokeDasharray = C; fg.style.strokeDashoffset = C;
    return { svg, fg };
  }
  function confetti() {
    if (window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    const cols = ['#facc15', '#4ade80', '#60a5fa', '#f87171', '#c084fc'];
    for (let i = 0; i < 40; i++) {
      const p = h('i', { class: 'confetti', style: 'background:' + cols[i % 5] + ';--dx:' + Math.round(Math.random() * 520 - 260) + 'px;--dy:' + Math.round(Math.random() * 380 - 60) + 'px;--rot:' + Math.round(Math.random() * 720 - 360) + 'deg;animation-delay:' + Math.random() * 0.25 + 's' });
      document.body.append(p); setTimeout(() => p.remove(), 1700);
    }
  }

  /* ---------- shared widgets ---------- */
  function audioBlock(a) {
    const au = h('audio', { controls: true, preload: 'metadata', src: 'audio/' + a.id + '.mp3' });
    const sp = h('select', { style: 'width:auto', 'aria-label': 'Speed', onchange: () => { au.playbackRate = Number(sp.value); } }, [['0.75', '0.75×'], ['1', '1×'], ['1.25', '1.25×']].map((o) => h('option', { value: o[0], selected: o[0] === '1' }, o[1])));
    V.cleanup.push(() => au.pause());
    return h('div', null, h('div', { class: 'row' }, h('b', { class: 'grow' }, '🎧 ' + a.title), sp), au);
  }
  function transcript(a) {
    return h('details', { class: 'card', open: true }, h('summary', null, 'Transcript (tap any word for its meaning)'), h('div', { class: 'text' }, a.lines.map((l) => h('p', null, h('b', null, l[0] + ': '), V.tappable(l[1])))));
  }
  function readingText(r, labels) {
    return h('div', { class: 'text' }, h('h2', null, r.title), r.p.map((p, i) => h('p', null, labels ? h('b', { class: 'kw' }, 'ABC'[i] + '  ') : null, V.tappable(p))));
  }
  function checkBtn(label, fn) { const b = h('button', { class: 'btn', onclick: () => fn(b) }, label || 'Check'); return h('div', { class: 'row end', style: 'margin-top:12px' }, b); }
  function hintBtn(hint) { if (!hint) return null; const b = h('button', { class: 'btn ghost', onclick: () => b.replaceWith(h('p', { class: 'muted' }, '💡 Meaning: ' + hint)) }, '💡 See the meaning'); return b; }
  function yourAnswer(opt, note) { return note ? h('div', { class: 'fb bad' }, h('span', { class: 'tag bad' }, 'Why your answer is wrong'), h('div', null, h('b', null, opt + ': '), note)) : null; }
  function why(note) { return note ? h('div', { class: 'fb na' }, h('span', { class: 'tag na' }, 'Why'), h('div', null, note)) : null; }
  function verdictLine(ok, text) { return h('div', { class: 'fb ' + (ok ? 'good' : 'bad') }, h('span', { class: 'tag ' + (ok ? 'good' : 'bad') }, ok ? '✓ Correct' : '✗ Not quite'), text ? h('div', null, text) : null); }

  /** Microphone with live transcript into an editable textarea. */
  function micBlock(ta, clock) {
    const SR = window.SpeechRecognition || window.webkitSpeechRecognition;
    if (!SR) return h('p', { class: 'muted small center' }, 'Voice input is not available in this browser (use Chrome, Edge or Safari). You can type your answer instead.');
    let rec = null, on = false, base = '', t0 = 0, tick = null;
    const btn = h('button', { class: 'mic', 'aria-label': 'Start or stop recording' }, '🎙️');
    const st = h('p', { class: 'muted small center' }, 'Tap the microphone and speak. Tap again to stop.');
    const stop = () => { on = false; btn.classList.remove('on'); clearInterval(tick); if (rec) try { rec.stop(); } catch (e) { /* ignore */ } st.textContent = 'Stopped. Check the text below and correct anything the microphone misheard.'; };
    function begin() {
      rec = new SR(); rec.lang = 'en-US'; rec.continuous = true; rec.interimResults = true;
      rec.onresult = (e) => { let s = ''; for (let i = 0; i < e.results.length; i++) s += e.results[i][0].transcript + ' '; ta.value = (base + ' ' + s).replace(/\s+/g, ' ').trim(); ta.dispatchEvent(new Event('input')); };
      rec.onend = () => { base = ta.value; if (on) try { begin(); } catch (e) { stop(); } };
      rec.onerror = (e) => { if (e.error === 'not-allowed' || e.error === 'service-not-allowed') { stop(); st.textContent = 'Microphone permission was denied. Allow it in the browser, or type your answer.'; } };
      rec.start();
    }
    btn.onclick = () => {
      if (on) return stop();
      on = true; base = ta.value; t0 = Date.now(); btn.classList.add('on'); st.textContent = 'Listening… speak now.';
      tick = setInterval(() => { const s = Math.floor((Date.now() - t0) / 1000); clock.textContent = Math.floor(s / 60) + ':' + String(s % 60).padStart(2, '0'); }, 500);
      try { begin(); } catch (e) { stop(); }
    };
    V.cleanup.push(stop);
    return h('div', null, btn, st);
  }

  /** Runs the free checker (+ AI examiner if a key is set) and renders the result. Returns the aspects for the history. */
  async function feedback(box, o) {
    const wait = h('p', { class: 'muted' }, 'Analysing your answer…'); box.append(wait);
    const res = await FB.analyze(o.text, o);
    wait.remove();
    box.append(h('h3', null, 'Feedback'), res.aspects.map((a) => h('div', { class: 'fb ' + a.v }, h('span', { class: 'tag ' + a.v }, a.name + ' · ' + V.VERDICT[a.v]), h('div', { class: 'small' }, a.d))));
    if (res.issues.length) box.append(h('h3', null, 'Possible mistakes'), h('ul', null, res.issues.slice(0, 12).map((x) => h('li', { class: 'small' }, h('del', null, x.bad), x.sug ? [' → ', h('ins', null, x.sug)] : null, ' — ' + x.msg))));
    let aspects = res.aspects.map((a) => ({ name: a.name, v: a.v, d: a.d }));
    if (S.gemKey) {
      const w2 = h('p', { class: 'muted' }, 'Asking the AI examiner…'); box.append(w2);
      try {
        const ai = await FB.aiProduction(S.gemKey, S.gemModel, o);
        w2.remove();
        box.append(h('h3', null, 'AI examiner'), (ai.aspects || []).map((a) => h('div', { class: 'fb ' + a.verdict }, h('span', { class: 'tag ' + a.verdict }, a.name + ' · ' + (V.VERDICT[a.verdict] || a.verdict)), h('div', { class: 'small' }, a.comment))));
        if ((ai.corrections || []).length) box.append(h('h3', null, 'Corrections'), h('ul', null, ai.corrections.map((c) => h('li', { class: 'small' }, h('del', null, c.original), ' → ', h('ins', null, c.corrected), c.why ? ' — ' + c.why : ''))));
        if (ai.improved) box.append(h('h3', null, 'Your answer at a strong ' + o.level + ' level'), h('p', { class: 'text' }, V.tappable(ai.improved)));
        aspects = aspects.concat((ai.aspects || []).map((a) => ({ name: 'AI · ' + a.name, v: a.verdict, d: a.comment })));
      } catch (e) { w2.textContent = 'The AI examiner is not available right now (' + e.message + '). The built-in feedback above still applies.'; }
    }
    S.history.unshift({ d: Date.now(), sec: o.kind === 'speaking' ? 'Speaking' : 'Writing', level: o.level, prompt: o.prompt, text: o.text, words: res.words, fb: aspects });
    S.history.length = Math.min(S.history.length, 100); V.save();
    return res;
  }
  function modelBlock(text) {
    return h('details', { class: 'card', open: true }, h('summary', null, 'Model answer — compare it with yours'), h('div', { class: 'row end' }, V.sayBtn(text)), h('div', { class: 'text' }, text.split('\n').filter(Boolean).map((p) => h('p', null, V.tappable(p)))));
  }

  /* ---------- renderers ---------- */
  const RENDER = {
    pairs(it, box, ctx) {
      const n = it.left.length, order = shuffle([...Array(n).keys()]), missed = new Set(); let selL = -1, done = 0;
      const L = it.left.map((t, i) => h('button', { class: 'opt', onclick: () => { if (L[i].disabled) return; selL = i; L.forEach((b, j) => b.classList.toggle('sel', j === i)); if (it.say) V.say(t); } }, t));
      const Rb = order.map((ri) => h('button', { class: 'opt', onclick: () => {
        if (selL < 0 || Rb[order.indexOf(ri)].disabled) return;
        const b = Rb[order.indexOf(ri)];
        if (ri === selL) {
          [L[selL], b].forEach((x) => { x.classList.remove('sel'); x.classList.add('good'); x.disabled = true; });
          if (it.refs) record(it.refs[selL], !missed.has(selL));
          selL = -1; done++;
          if (done === n) { const ok = n - missed.size; box.append(verdictLine(ok === n, ok + ' of ' + n + ' matched at the first try.')); ctx.finish({ ok, tot: n, weak: [...missed].map((k) => it.left[k] + ' — ' + it.right[k]) }); }
        } else { missed.add(selL); b.classList.add('bad'); setTimeout(() => b.classList.remove('bad'), 600); }
      } }, it.right[ri]));
      box.append(instr(it.instr), h('div', { class: 'pairs' }, h('div', { class: 'opts' }, L), h('div', { class: 'opts' }, Rb)));
    },
    judge(it, box, ctx) {
      let done = false;
      const pick = (said) => {
        if (done) return; done = true; btns.forEach((b) => (b.disabled = true));
        const good = said === it.ok; btns[said ? 0 : 1].classList.add(good ? 'good' : 'bad'); record(it.ref, good);
        box.append(verdictLine(good, it.ok ? 'The sentence is correct.' : 'The sentence is wrong. Correct version: ' + it.right),
          !it.ok && it.wrongNote ? h('div', { class: 'fb bad' }, h('span', { class: 'tag bad' }, 'What is wrong'), h('div', null, h('b', null, it.chosen + ': '), it.wrongNote)) : null, why(it.note));
        ctx.finish({ ok: good ? 1 : 0, tot: 1, weak: good ? [] : [it.right] });
      };
      const btns = [h('button', { class: 'opt', onclick: () => pick(true) }, '✓ Correct'), h('button', { class: 'opt', onclick: () => pick(false) }, '✗ Wrong')];
      box.append(instr('Is this sentence grammatically correct?'), h('p', { class: 'text' }, h('b', null, it.sentence)), h('div', { class: 'opts' }, btns));
    },
    listenwho(it, box, ctx) {
      const a = it.a, seen = new Set(), lines = shuffle(a.lines.filter((l) => !seen.has(l[1]) && seen.add(l[1]))).slice(0, 5), picks = lines.map(() => null), groups = [];
      box.append(instr('Listen to the dialogue. Who says each sentence: the man or the woman?'), audioBlock(a));
      lines.forEach((l, li) => {
        const bs = ['A', 'B'].map((sp) => h('button', { class: 'opt', onclick: () => { if (groups.done) return; picks[li] = sp; bs.forEach((b) => b.classList.toggle('sel', b === bs[sp === 'A' ? 0 : 1])); } }, sp === 'A' ? '👨 The man' : '👩 The woman'));
        groups.push(bs); box.append(h('p', { class: 'text' }, '“' + l[1] + '”'), h('div', { class: 'scenes' }, bs));
      });
      box.append(checkBtn('Check', (b) => {
        if (picks.includes(null)) return; b.disabled = true; groups.done = true; let ok = 0; const weak = [];
        lines.forEach((l, li) => { const good = picks[li] === l[0]; groups[li][l[0] === 'A' ? 0 : 1].classList.add('good'); if (!good) { groups[li][l[0] === 'A' ? 1 : 0].classList.add('bad'); weak.push('“' + l[1].slice(0, 60) + '…”'); } else ok++; });
        box.append(transcript(a)); ctx.finish({ ok, tot: lines.length, weak });
      }));
    },
    choice(it, box, ctx) {
      let sel = -1, done = false;
      const opts = it.options.map((o, i) => h('button', { class: 'opt', onclick: () => { if (done) return; sel = i; opts.forEach((b, j) => b.classList.toggle('sel', j === i)); } }, o));
      box.append(instr(it.instr), it.context ? h('details', null, h('summary', null, 'Show the text: ' + it.context.title), readingText(it.context)) : null, h('p', { class: 'text' }, h('b', null, it.prompt)), it.sub ? h('p', null, it.sub) : null, h('div', { class: 'opts' }, opts),
        checkBtn('Check', (b) => {
          if (sel < 0 || done) return; done = true; b.disabled = true;
          const ok = sel === it.answer; opts[it.answer].classList.add('good'); if (!ok) opts[sel].classList.add('bad');
          record(it.ref, ok); box.append(verdictLine(ok, ok ? '' : 'Correct answer: ' + it.options[it.answer]), ok ? null : yourAnswer(it.options[sel], (it.optNotes || [])[sel]), why(it.note));
          ctx.finish({ ok: ok ? 1 : 0, tot: 1, weak: ok ? [] : [it.prompt] });
        }));
    },
    input(it, box, ctx) {
      let done = false;
      const inp = h('input', { class: 'gap', type: 'text', autocomplete: 'off', autocapitalize: 'off', spellcheck: 'false', style: 'min-width:' + (it.pre && !it.root ? 180 : 110) + 'px' });
      const parts = it.sentence.split('___');
      const go = (b) => {
        if (done || !inp.value.trim()) return; done = true; b.disabled = true; inp.disabled = true;
        const ok = it.answers.some((a) => norm(a) === norm(inp.value)); inp.classList.add(ok ? 'good' : 'bad');
        record(it.ref, ok);
        if (it.word && !ok) V.srsAdd(it.word[0], it.word[1], it.word[2]);
        box.append(verdictLine(ok, ok ? '' : 'Correct answer: ' + it.answers[0]), why(it.note), it.word ? h('p', { class: 'muted' }, h('span', { class: 'row' }, V.sayBtn(it.word[0]), '“' + it.word[2] + '”')) : null);
        ctx.finish({ ok: ok ? 1 : 0, tot: 1, weak: ok ? [] : [it.word ? it.word[0] + ' — ' + it.word[1] : it.sentence.replace('___', '[' + it.answers[0] + ']')] });
      };
      const btn = checkBtn('Check', go);
      inp.addEventListener('keydown', (e) => { if (e.key === 'Enter') go(btn.firstChild); });
      box.append(instr(it.instr), it.speakWord ? h('div', { class: 'row', style: 'justify-content:center;margin:10px 0' }, h('button', { class: 'btn sec', onclick: () => V.say(it.speakWord) }, '🔊 Play the word')) : null, it.audio ? audioBlock(it.audio) : null, it.pre ? h('p', { class: 'text' }, it.pre) : null, it.root ? h('p', null, h('span', { class: 'pill kw' }, it.root)) : null,
        h('p', { class: 'text' }, parts[0], inp, parts[1] || ''), hintBtn(it.hint), btn);
      setTimeout(() => inp.focus(), 50);
    },
    gappara(it, box, ctx) {
      const cell = D.vocab[it.t][it.l], inputs = [], used = [];
      const para = h('p', { class: 'text' });
      [cell.para, cell.para2, cell.para3][it.which || 0].split(/\{(\d)\}/).forEach((p, i) => {
        if (i % 2) { const n = Number(p) + [0, cell.off2, cell.off3][it.which || 0], inp = h('input', { class: 'gap', type: 'text', autocomplete: 'off', autocapitalize: 'off', spellcheck: 'false' }); inp._n = n; inputs.push(inp); used.push(n); para.append(inp); } else para.append(p);
      });
      box.append(instr('Complete the paragraph with the missing words' + (it.bank ? ' from the list.' : '. No list this time!')), it.bank ? h('div', { class: 'bank' }, shuffle(used).map((n) => h('span', null, cell.w[n][0]))) : null, para,
        checkBtn('Check', (b) => {
          b.disabled = true; let ok = 0; const weak = [];
          inputs.forEach((inp) => {
            const w = cell.w[inp._n], good = norm(inp.value) === norm(w[0]); inp.disabled = true; inp.classList.add(good ? 'good' : 'bad');
            record({ k: 'v', t: it.t, l: it.l, i: inp._n }, good);
            if (good) ok++; else { weak.push(w[0] + ' — ' + w[1]); V.srsAdd(w[0], w[1], w[2]); inp.value = (inp.value ? inp.value + ' → ' : '→ ') + w[0]; inp.style.minWidth = '170px'; }
          });
          box.append(h('h3', null, 'Words in this paragraph'), used.map((n) => h('div', { class: 'row small' }, V.sayBtn(cell.w[n][0]), h('span', { class: 'grow' }, h('b', null, cell.w[n][0]), ': ' + cell.w[n][1]))));
          ctx.finish({ ok, tot: inputs.length, weak });
        }));
    },
    readmc(it, box, ctx) {
      const r = it.r, sel = r.mc.map(() => -1), groups = [];
      box.append(instr('Read the text and choose the best answer. Tap any word to see what it means.'), readingText(r), h('hr'));
      r.mc.forEach((q, qi) => {
        const opts = q.o.map((o, i) => h('button', { class: 'opt', onclick: () => { if (groups.done) return; sel[qi] = i; opts.forEach((b, j) => b.classList.toggle('sel', j === i)); } }, o));
        groups.push(opts); box.append(h('p', null, h('b', null, qi + 1 + '. ' + q.q)), h('div', { class: 'opts' }, opts));
      });
      box.append(checkBtn('Check', (b) => {
        if (sel.includes(-1)) return; b.disabled = true; groups.done = true; let ok = 0; const weak = [];
        const ex = (D.rexp || {})[r.id] || [];
        r.mc.forEach((q, qi) => {
          const good = sel[qi] === q.a, x = ex[qi] || {}; groups[qi][q.a].classList.add('good'); if (!good) { groups[qi][sel[qi]].classList.add('bad'); weak.push(q.q); } else ok++; record({ k: 'r', id: r.id, q: qi }, good);
          const after = groups[qi][0].parentNode;
          after.after(h('div', null, good ? null : yourAnswer(q.o[sel[qi]], (x.w || [])[sel[qi]]), why(x.e)));
        });
        ctx.finish({ ok, tot: r.mc.length, weak });
      }));
    },
    gaptext(it, box, ctx) {
      const r = it.r, options = shuffle(r.rm.concat([r.dis])), sels = [];
      const text = h('div', { class: 'text' }, h('h2', null, r.title));
      r.p.forEach((p) => {
        const para = h('p'); let rest = p;
        r.rm.forEach((s, si) => {
          const at = rest.indexOf(s); if (at < 0) return;
          const sel = h('select', { class: 'gap' }, h('option', { value: '' }, '— choose the missing sentence —'), options.map((o) => h('option', { value: o }, o))); sel._a = s; sels.push(sel);
          para.append(V.tappable(rest.slice(0, at)), sel, ' '); rest = rest.slice(at + s.length).replace(/^ /, '');
        });
        para.append(V.tappable(rest)); text.append(para);
      });
      box.append(instr('Two sentences have been removed from the text. Choose the one that fits each gap. There is one extra sentence you do not need.'), text,
        checkBtn('Check', (b) => {
          if (sels.some((s) => !s.value)) return; b.disabled = true; let ok = 0; const weak = [];
          sels.forEach((s) => { const good = s.value === s._a; s.disabled = true; s.classList.add(good ? 'good' : 'bad'); if (good) ok++; else weak.push('Gapped text: ' + r.title); });
          if (ok < sels.length) box.append(h('div', { class: 'fb bad' }, h('span', { class: 'tag bad' }, 'Correct sentences'), sels.map((s, i) => h('div', { class: 'small' }, 'Gap ' + (i + 1) + ': ' + s._a))));
          else box.append(verdictLine(true));
          ctx.finish({ ok, tot: sels.length, weak });
        }));
    },
    match(it, box, ctx) {
      const r = it.r, rows = shuffle(r.match.map((s, i) => ({ s, a: i })));
      box.append(instr('Which paragraph (A, B or C) does each statement refer to?'), readingText(r, true), h('hr'));
      rows.forEach((row) => { row.sel = h('select', { class: 'gap', style: 'min-width:70px' }, h('option', { value: '' }, '—'), ['A', 'B', 'C'].map((x, i) => h('option', { value: i }, x))); box.append(h('p', null, row.sel, ' ' + row.s)); });
      box.append(checkBtn('Check', (b) => {
        if (rows.some((x) => x.sel.value === '')) return; b.disabled = true; let ok = 0; const weak = [];
        rows.forEach((x) => { const good = Number(x.sel.value) === x.a; x.sel.disabled = true; x.sel.classList.add(good ? 'good' : 'bad'); if (good) ok++; else { weak.push('Matching: ' + r.title); x.sel.after(h('b', { class: 'kw' }, ' → ' + 'ABC'[x.a])); } });
        ctx.finish({ ok, tot: rows.length, weak });
      }));
    },
    listengaps(it, box, ctx) {
      const a = it.a, inputs = [];
      box.append(instr('Listen and complete each sentence with the exact word you hear. You can listen as many times as you need.'), audioBlock(a));
      a.gaps.forEach((g, gi) => { const parts = g.s.split('___'), inp = h('input', { class: 'gap', type: 'text', autocomplete: 'off', autocapitalize: 'off', spellcheck: 'false' }); inp._g = g; inp._i = gi; inputs.push(inp); box.append(h('p', { class: 'text' }, gi + 1 + '. ' + parts[0], inp, parts[1] || '')); });
      box.append(checkBtn('Check', (b) => {
        b.disabled = true; let ok = 0; const weak = [];
        inputs.forEach((inp) => { const good = norm(inp.value) === norm(inp._g.a); inp.disabled = true; inp.classList.add(good ? 'good' : 'bad'); record({ k: 'l', id: a.id, i: inp._i }, good); if (good) ok++; else { weak.push(inp._g.s.replace('___', '[' + inp._g.a + ']')); inp.value = (inp.value ? inp.value + ' → ' : '→ ') + inp._g.a; inp.style.minWidth = '170px'; } });
        box.append(transcript(a)); ctx.finish({ ok, tot: inputs.length, weak });
      }));
    },
    listenopen(it, box, ctx) {
      const a = it.a, tas = [];
      box.append(instr('Listen to the dialogue and answer in your own words. There are no options: explain what you understood.'), audioBlock(a));
      a.q.forEach((q, qi) => { const ta = h('textarea', { style: 'min-height:70px', placeholder: 'Your answer…' }); tas.push(ta); box.append(h('p', null, h('b', null, qi + 1 + '. ' + q.q)), ta); });
      box.append(checkBtn('Check my answers', async (b) => {
        if (tas.every((t) => !t.value.trim())) return; b.disabled = true; tas.forEach((t) => (t.disabled = true));
        let results = null, note = null;
        if (S.gemKey) {
          const w = h('p', { class: 'muted' }, 'The AI examiner is checking your answers…'); box.append(w);
          try { const r = await FB.aiListening(S.gemKey, S.gemModel, { level: ctx.level, transcript: a.lines.map((l) => l[0] + ': ' + l[1]).join('\n'), qa: a.q.map((q, i) => ({ q: q.q, a: q.a, u: tas[i].value.trim() })) }); results = r.results; }
          catch (e) { note = 'The AI examiner is not available right now, so your answers were checked by key ideas.'; }
          w.remove();
        } else note = 'Checked by key ideas. Compare your answer with the model answer to be sure. (Add a free Gemini key in Settings for a full AI check.)';
        let ok = 0; const weak = [];
        a.q.forEach((q, i) => {
          let v, comment;
          if (results && results[i]) { v = results[i].verdict === 'correct' ? 'good' : results[i].verdict === 'partial' ? 'ok' : 'weak'; comment = results[i].comment; }
          else { const u = ' ' + norm(tas[i].value) + ' ', hit = q.k.filter((g) => g.some((t) => u.includes(norm(t)))).length; v = hit === q.k.length ? 'good' : hit ? 'ok' : 'weak'; comment = hit + ' of ' + q.k.length + ' key ideas found in your answer.'; }
          ok += v === 'good' ? 1 : v === 'ok' ? 0.5 : 0; if (v !== 'good') weak.push(q.q);
          tas[i].after(h('div', { class: 'fb ' + v }, h('span', { class: 'tag ' + v }, v === 'good' ? '✓ Correct' : v === 'ok' ? '◐ Partly correct' : '✗ Not correct'), h('div', { class: 'small' }, comment), h('div', { class: 'small' }, h('b', null, 'Model answer: '), q.a)));
        });
        if (note) box.append(h('p', { class: 'muted small' }, note));
        box.append(transcript(a)); ctx.finish({ ok, tot: a.q.length, weak });
      }));
    },
    speak(it, box, ctx) {
      const clock = h('span', { class: 'timer' }, '0:00'), ta = h('textarea', { placeholder: 'Your words will appear here. You can also type.' });
      const out = h('div');
      box.append(h('div', { class: 'row' }, h('span', { class: 'pill grow', style: 'flex:0 1 auto' }, D.help[it.kind].title), h('span', { class: 'grow' }), clock, h('button', { class: 'ic', 'aria-label': 'Help', onclick: () => V.helpSheet(it.kind) }, '?')),
        it.scenes ? h('div', { class: it.scenes.length > 1 ? 'scenes' : '' }, it.scenes.map((s) => h('div', { class: 'scene', style: 'background:' + s.bg, role: 'img', 'aria-label': s.cap }, s.items))) : null,
        h('p', { class: 'text' }, h('b', null, it.prompt)), it.kind === 'mono' ? instr('Try to keep talking for about one minute.') : null,
        micBlock(ta, clock), h('p', { class: 'small muted', style: 'margin-bottom:4px' }, 'Your answer — read it before sending and fix anything the microphone got wrong:'), ta,
        checkBtn('Send for feedback', async (b) => {
          const text = ta.value.trim(); if (text.split(/\s+/).length < 3) return;
          V.cleanup.splice(0).forEach((f) => f()); b.disabled = true; ta.disabled = true;
          const base = { B1: 30, B2: 45, C1: 60, C2: 70 }[ctx.level];
          await feedback(out, { text, level: ctx.level, kind: 'speaking', prompt: it.prompt, targetWords: it.kind === 'mono' ? Math.round(base * 1.7) : it.kind === 'q' ? base : Math.round(base * 1.2) });
          out.append(modelBlock(it.model)); ctx.finish({ ok: 0, tot: 0 });
        }), out);
    },
    write(it, box, ctx) {
      const target = Number((/about (\d+) words/.exec(it.prompt) || [])[1]) || 150;
      const count = h('span', { class: 'muted small' }, '0 / ' + target + ' words'), ta = h('textarea', { style: 'min-height:260px', placeholder: 'Write here…', spellcheck: 'false' }), out = h('div');
      ta.addEventListener('input', () => { count.textContent = (ta.value.trim() ? ta.value.trim().split(/\s+/).length : 0) + ' / ' + target + ' words'; });
      box.append(h('div', { class: 'row' }, h('span', { class: 'pill' }, D.help[it.wtype].title), h('span', { class: 'grow' }), h('button', { class: 'ic', 'aria-label': 'Help', onclick: () => V.helpSheet(it.wtype) }, '?')),
        h('p', { class: 'text' }, h('b', null, it.prompt)), ta, h('div', { class: 'row end' }, count),
        checkBtn('Send for feedback', async (b) => {
          const text = ta.value.trim(); if (text.split(/\s+/).length < 10) return;
          b.disabled = true; ta.disabled = true;
          await feedback(out, { text, level: ctx.level, kind: 'writing', prompt: it.prompt, targetWords: target });
          out.append(modelBlock(it.model)); ctx.finish({ ok: 0, tot: 0 });
        }), out);
    },
    card(it, box, ctx) {
      const c = S.srs[it.w] || V.vocabIndex.get(it.w) || { def: '', ex: '' };
      const back = h('div', { hidden: true }, h('div', { class: 'row', style: 'justify-content:center' }, h('span', { class: 'big' }, it.w), V.sayBtn(it.w)), c.ex ? h('p', { class: 'muted' }, '“' + c.ex + '”') : null,
        h('div', { class: 'row', style: 'justify-content:center' }, h('button', { class: 'btn sec', onclick: () => answer(false) }, "✗ I didn't know it"), h('button', { class: 'btn', onclick: () => answer(true) }, '✓ I knew it')));
      const show = h('button', { class: 'btn', onclick: () => { show.hidden = true; back.hidden = false; } }, 'Show the word');
      let done = false;
      function answer(knew) { if (done) return; done = true; V.srsAnswer(it.w, knew); back.querySelectorAll('button.btn').forEach((b) => (b.disabled = true)); ctx.finish({ ok: knew ? 1 : 0, tot: 1, weak: knew ? [] : [it.w + ' — ' + (c.def || '')] }); }
      box.append(h('div', { class: 'flash' }, h('p', { class: 'muted small' }, 'Which word is this?'), h('p', { class: 'text' }, c.def || '(no definition saved — do you remember what it means?)'), show, back));
    }
  };

  V.boot();
})();
