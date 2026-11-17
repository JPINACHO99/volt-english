/* Volt English — core: state, navigation, home and secondary screens. Exercises live in exercises.js */
(function () {
  'use strict';
  const V = (window.V = {});
  const D = window.DATA;
  const TOPICS = (V.TOPICS = [{ id: 'eng', n: 'Engineering', e: '⚙️' }, { id: 'elec', n: 'Electricity', e: '⚡' }, { id: 'work', n: 'Work', e: '💼' },
    { id: 'daily', n: 'Daily life', e: '🏠' }, { id: 'cook', n: 'Cooking', e: '🍳' }, { id: 'foot', n: 'Football', e: '⚽' }, { id: 'job', n: 'Job interviews', e: '🤝' }]);
  const LEVELS = ['B1', 'B2', 'C1', 'C2'];
  const LEVEL_NAME = { B1: 'Intermediate', B2: 'Upper-intermediate', C1: 'Advanced', C2: 'Proficiency' };
  const SECTIONS = (V.SECTIONS = [
    { id: 'speaking', n: 'Speaking', e: '🎙️', d: 'Talk, check the transcript, get feedback', modes: [['q', 'Answer a question', '💬'], ['describe', 'Describe an image', '🖼️'], ['compare', 'Compare two images', '🆚'], ['mono', 'One-minute talk', '⏱️'], ['op', 'Give your opinion', '⚖️'], ['rp', 'Role-play', '🎭']] },
    { id: 'listening', n: 'Listening', e: '🎧', d: 'Dialogues with open questions', modes: [['open', 'Open questions', '✍️', 'Answer in your own words'], ['gaps', 'Complete the sentences', '🧩', 'Type the exact word you hear (no AI needed)'], ['who', 'Who said it?', '🗣️', 'The man or the woman?']] },
    { id: 'reading', n: 'Reading', e: '📖', d: 'Cambridge-style reading tasks', modes: [['mc', 'Comprehension questions', '❓'], ['gapped', 'Gapped text', '🧩', 'Put the missing sentences back'], ['match', 'Matching', '🔗', 'Match statements to paragraphs']] },
    { id: 'writing', n: 'Writing', e: '✍️', d: 'Essays, emails, reports and more', modes: [['essay', 'Essay', '📝'], ['task', 'Second task', '📨']] },
    { id: 'grammar', n: 'Grammar', e: '🧠', d: 'Use of English', modes: [['mc', 'Multiple choice', '🔘'], ['open', 'Open gap', '␣', 'One word per gap'], ['wf', 'Word formation', '🔤'], ['kt', 'Key word transformation', '🔁'], ['judge', 'Right or wrong?', '✅', 'Decide if the sentence is correct'], ['mix', 'Mixed practice', '🎲']] },
    { id: 'phrasal', n: 'Phrasal verbs', e: '🧲', d: 'Meanings, particles and usage', noTopic: true, modes: [['list', 'Browse & learn', '📚', 'All the verbs of this level with meaning and example'], ['meaning', 'Choose the meaning', '💡'], ['particle', 'Complete the particle', '🧩', 'get ___ , put ___ with…'], ['choose', 'Choose the phrasal verb', '🎯'], ['pmatch', 'Match verbs and meanings', '🔗'], ['pcards', 'Flashcards', '🃏']] },
    { id: 'vocab', n: 'Vocabulary', e: '🗂️', d: 'Words by topic', modes: [['bank', 'Fill the gaps', '🧩', 'With the list of words'], ['nobank', 'Fill the gaps (no help)', '🔥', 'Without the list of words'], ['define', 'Definition → word', '💡'], ['match', 'Match words and meanings', '🔗'], ['spell', 'Listen and spell', '👂', 'Hear a word and write it'], ['cards', 'Flashcards', '🃏']] }
  ]);

  /* append/replaceChildren that accept arrays and skip null (the native ones would print "null") */
  ['append', 'replaceChildren'].forEach((m) => {
    const native = Element.prototype[m];
    Element.prototype[m] = function () { return native.apply(this, [].slice.call(arguments).flat(3).filter((x) => x != null && x !== false)); };
  });

  /* ---------- tiny DOM helper ---------- */
  const h = (V.h = function (tag, props) {
    const e = document.createElement(tag);
    if (props) for (const k in props) {
      const v = props[k];
      if (v == null || v === false) continue;
      if (k === 'class') e.className = v; else if (k === 'html') e.innerHTML = v;
      else if (k.slice(0, 2) === 'on') e.addEventListener(k.slice(2), v); else e.setAttribute(k, v === true ? '' : v);
    }
    for (let i = 2; i < arguments.length; i++) [].concat(arguments[i]).flat(3).forEach((c) => { if (c != null && c !== false) e.append(c.nodeType ? c : document.createTextNode(c)); });
    return e;
  });
  const $app = document.getElementById('app'), $bar = document.getElementById('bar'), $sheet = document.getElementById('sheet');

  /* ---------- state (saved in this browser only) ---------- */
  const KEY = 'volt.v1';
  const defaults = () => ({ theme: 'dark', stats: {}, days: {}, errors: {}, srs: {}, my: [], history: [], gemKey: '', gemModel: 'gemini-flash-latest', lastTopic: null, lastLevel: null });
  let S = defaults();
  try { S = Object.assign(S, JSON.parse(localStorage.getItem(KEY) || '{}')); } catch (e) { /* storage unavailable: progress lasts for this visit only */ }
  V.S = S;
  const save = (V.save = () => { try { localStorage.setItem(KEY, JSON.stringify(S)); } catch (e) { /* ignore */ } });
  const dayKey = (d) => { d = d || new Date(); return d.getFullYear() + '-' + String(d.getMonth() + 1).padStart(2, '0') + '-' + String(d.getDate()).padStart(2, '0'); };
  V.today = dayKey;
  function streak() {
    let n = 0; const d = new Date();
    if (!S.days[dayKey(d)]) d.setDate(d.getDate() - 1);
    while (S.days[dayKey(d)]) { n++; d.setDate(d.getDate() - 1); }
    return n;
  }
  V.addStat = function (sec, ok, tot) {
    const st = (S.stats[sec] = S.stats[sec] || { s: 0, ok: 0, tot: 0 });
    st.s++; st.ok += ok; st.tot += tot;
    S.days[dayKey()] = (S.days[dayKey()] || 0) + 1; save();
  };

  /* ---------- vocabulary index, SRS, my words ---------- */
  const vocabIndex = new Map();
  TOPICS.forEach((t) => LEVELS.forEach((l) => D.vocab[t.id][l].w.forEach((w, i) => vocabIndex.set(w[0], { w: w[0], def: w[1], ex: w[2], t: t.id, l, i }))));
  V.vocabIndex = vocabIndex;
  const GAPS = [0, 1, 3, 7, 21];
  V.srsAdd = function (word, def, ex) { if (!S.srs[word]) { S.srs[word] = { box: 0, due: dayKey(), def, ex }; save(); } };
  V.srsAnswer = function (word, knew) {
    const c = S.srs[word]; if (!c) return;
    c.box = knew ? Math.min(4, c.box + 1) : 0;
    const d = new Date(); d.setDate(d.getDate() + GAPS[c.box]); c.due = dayKey(d); save();
  };
  const dueCards = (V.dueCards = () => Object.keys(S.srs).filter((w) => S.srs[w].due <= dayKey()));
  V.addMyWord = function (w, def, ex) {
    if (!S.my.some((x) => x.w === w)) { S.my.unshift({ w, def: def || '', ex: ex || '' }); V.srsAdd(w, def || '', ex || ''); save(); }
  };

  /* ---------- speech output, word lookup ---------- */
  const say = (V.say = function (text) {
    if (!('speechSynthesis' in window)) return;
    speechSynthesis.cancel();
    const u = new SpeechSynthesisUtterance(text); u.lang = 'en-GB'; u.rate = 0.95;
    const v = speechSynthesis.getVoices().find((x) => /^en[-_]GB/i.test(x.lang)) || speechSynthesis.getVoices().find((x) => /^en/i.test(x.lang));
    if (v) u.voice = v;
    speechSynthesis.speak(u);
  });
  V.sayBtn = (text) => h('button', { class: 'ic', title: 'Listen', 'aria-label': 'Listen', onclick: (e) => { e.stopPropagation(); say(text); } }, '🔊');
  /** Text whose words can be tapped to see their meaning. */
  V.tappable = function (text) {
    const f = document.createDocumentFragment();
    text.split(/([A-Za-z][A-Za-z'’-]*)/).forEach((p, i) => f.append(i % 2 ? h('span', { class: 'w', onclick: () => lookup(p) }, p) : p));
    return f;
  };
  async function lookup(raw) {
    const word = raw.toLowerCase().replace(/’/g, "'").replace(/'s$/, '');
    const body = h('div', null, h('p', { class: 'muted' }, 'Looking it up…'));
    let def = '', ex = '';
    const addBtn = h('button', { class: 'btn sec', onclick: () => { V.addMyWord(word, def, ex); addBtn.textContent = '✓ Saved to My words'; addBtn.disabled = true; } }, '＋ Add to My words');
    sheet([h('div', { class: 'row' }, h('h2', { class: 'grow' }, word), V.sayBtn(word)), body, h('div', { class: 'row' }, addBtn, h('button', { class: 'btn ghost', onclick: closeSheet }, 'Close'))]);
    const local = vocabIndex.get(word);
    if (local) { def = local.def; ex = local.ex; }
    else {
      try {
        const r = await fetch('https://api.dictionaryapi.dev/api/v2/entries/en/' + encodeURIComponent(word));
        if (r.ok) {
          const m = (await r.json())[0].meanings || [];
          const d0 = m[0] && m[0].definitions[0];
          if (d0) { def = (m[0].partOfSpeech ? '(' + m[0].partOfSpeech + ') ' : '') + d0.definition; ex = d0.example || ''; }
        }
      } catch (e) { /* offline */ }
    }
    body.replaceChildren(def ? h('p', null, def) : h('p', { class: 'muted' }, 'No definition found (the dictionary needs an internet connection). You can still save the word.'), ex ? h('p', { class: 'muted' }, '“' + ex + '”') : null);
  }
  function sheet(nodes) {
    $sheet.replaceChildren(h('div', { class: 'box', onclick: (e) => e.stopPropagation() }, nodes));
    $sheet.hidden = false;
  }
  function closeSheet() { $sheet.hidden = true; $sheet.replaceChildren(); }
  $sheet.addEventListener('click', closeSheet);
  V.sheet = sheet; V.closeSheet = closeSheet;
  V.helpSheet = function (key) {
    const x = D.help[key]; if (!x) return;
    sheet([h('h2', null, '? ' + x.title), h('h3', null, 'Structure'), h('ol', null, x.structure.map((s) => h('li', null, s))),
      h('h3', null, 'Tips'), h('ul', null, x.tips.map((s) => h('li', null, s))), h('div', { class: 'row end' }, h('button', { class: 'btn sec', onclick: closeSheet }, 'Got it'))]);
  };

  /* ---------- navigation ---------- */
  const stack = [];
  V.cleanup = [];
  function render() {
    V.cleanup.splice(0).forEach((f) => { try { f(); } catch (e) { /* ignore */ } });
    if ('speechSynthesis' in window) speechSynthesis.cancel();
    closeSheet();
    const v = stack[stack.length - 1]();
    $bar.replaceChildren(stack.length > 1 ? h('button', { class: 'ic', 'aria-label': 'Back', onclick: () => history.back() }, '←') : h('span', { class: 'ic logo' }, '⚡'),
      h('h1', null, v.title), v.right || h('span', { class: 'pill', title: 'Days in a row' }, '🔥 ' + streak()));
    $app.replaceChildren.apply($app, [].concat(v.body).filter(Boolean));
    window.scrollTo(0, 0);
  }
  const go = (V.go = function (fn) { stack.push(fn); history.pushState({ n: stack.length }, ''); render(); });
  V.goHome = function () { if (stack.length > 1) history.go(-(stack.length - 1)); else render(); };
  V.rerender = render;
  window.addEventListener('popstate', (e) => {
    const n = Math.max(1, Math.min(stack.length, (e.state && e.state.n) || 1));
    stack.length = n; render();
  });

  /* ---------- screens ---------- */
  function wordOfDay() {
    const pool = [...vocabIndex.values()].filter((x) => (!S.lastTopic || x.t === S.lastTopic) && (!S.lastLevel || x.l === S.lastLevel));
    const list = pool.length ? pool : [...vocabIndex.values()];
    return list[Math.floor(Date.now() / 864e5) % list.length];
  }
  function homeView() {
    const w = wordOfDay(), nErr = Object.keys(S.errors).length, nDue = dueCards().length;
    const tool = (e, name, sub, fn, dis) => h('button', { class: 'tile', onclick: fn, disabled: dis }, h('span', { class: 'em' }, e), h('b', null, name), h('span', null, sub));
    return {
      title: 'Volt English',
      right: h('div', { class: 'row' }, h('span', { class: 'pill' }, '🔥 ' + streak()),
        h('button', { class: 'ic', 'aria-label': 'Theme', onclick: () => { S.theme = S.theme === 'dark' ? 'light' : 'dark'; applyTheme(); save(); } }, S.theme === 'dark' ? '☀️' : '🌙'),
        h('button', { class: 'ic', 'aria-label': 'Settings', onclick: () => go(settingsView) }, '⚙️')),
      body: [
        h('div', { class: 'card' }, h('div', { class: 'row' }, h('div', { class: 'grow' }, h('span', { class: 'pill' }, 'Word of the day · ' + w.l), h('h2', { style: 'margin:.3em 0 0' }, w.w)), V.sayBtn(w.w),
          h('button', { class: 'ic', title: 'Add to My words', onclick: (e) => { V.addMyWord(w.w, w.def, w.ex); e.target.textContent = '✓'; } }, '＋')),
          h('p', null, w.def), h('p', { class: 'muted small' }, '“' + w.ex + '”')),
        h('h3', null, 'Practise'),
        h('div', { class: 'grid' }, SECTIONS.map((s) => h('button', { class: 'tile', onclick: () => go(() => levelView(s)) }, h('span', { class: 'em' }, s.e), h('b', null, s.n), h('span', null, s.d)))),
        h('h3', null, 'Review'),
        h('div', { class: 'grid' },
          tool('🩹', 'Review mistakes', nErr ? nErr + ' to fix' : 'Nothing to review', () => V.startReview(), !nErr),
          tool('🃏', 'Flashcards', nDue ? nDue + ' due today' : 'No cards due', () => V.startCards(dueCards()), !nDue),
          tool('⭐', 'My words', S.my.length + ' saved', () => go(myWordsView)),
          tool('🕘', 'History', S.history.length + ' answers', () => go(historyView)),
          tool('📊', 'Stats', 'Streak and accuracy', () => go(statsView)))
      ]
    };
  }
  function levelView(sec) {
    return { title: sec.n + ' · level', body: [h('p', { class: 'muted' }, 'Which level do you want to practise?'),
      h('div', { class: 'list' }, LEVELS.map((l) => h('button', { class: 'tile', onclick: () => { if (sec.noTopic) { S.lastLevel = l; save(); go(() => modeView(sec, l, null)); } else go(() => topicView(sec, l)); } }, h('span', { class: 'em' }, l), h('div', null, h('b', null, LEVEL_NAME[l])))))] };
  }
  function topicView(sec, level) {
    const pick = (t) => { S.lastTopic = t; S.lastLevel = level; save(); go(() => modeView(sec, level, t)); };
    return { title: sec.n + ' · ' + level + ' · topic', body: [h('p', { class: 'muted' }, 'Choose a topic.'),
      h('div', { class: 'grid' }, TOPICS.map((t) => h('button', { class: 'tile', onclick: () => pick(t.id) }, h('span', { class: 'em' }, t.e), h('b', null, t.n))),
        h('button', { class: 'tile', onclick: () => pick(TOPICS[Math.floor(Math.random() * TOPICS.length)].id) }, h('span', { class: 'em' }, '🎲'), h('b', null, 'Free topic'), h('span', null, 'Pick one at random')))] };
  }
  function modeView(sec, level, topic) {
    const tn = TOPICS.find((t) => t.id === topic) || { n: '', e: '' };
    return { title: sec.n + ' · ' + level + (tn.n ? ' · ' + tn.n : ''), body: [h('p', { class: 'muted' }, (tn.n ? tn.e + ' ' + tn.n + ' — c' : 'C') + 'hoose an exercise.'),
      h('div', { class: 'list' }, sec.modes.map((m) => {
        let name = m[1], sub = m[3];
        if (sec.id === 'writing' && m[0] === 'task') { const ty = D.writing[topic][level].task[0]; name = D.help[ty].title; sub = 'Second task'; }
        return h('button', { class: 'tile', onclick: () => V.start(sec.id, level, topic, m[0]) }, h('span', { class: 'em' }, m[2] || '•'), h('div', null, h('b', null, name), sub ? h('span', null, h('br'), sub) : null));
      }))] };
  }
  function myWordsView() {
    const w = h('input', { type: 'text', placeholder: 'Word or phrase (e.g. leeway)', autocapitalize: 'off' }), m = h('input', { type: 'text', placeholder: 'Meaning or note, in any language (optional)' });
    const addOwn = () => { const word = w.value.trim(), def = m.value.trim(); if (!word) { w.focus(); return; } const old = S.my.find((x) => x.w.toLowerCase() === word.toLowerCase()); if (old) { if (def) { old.def = def; if (S.srs[old.w]) S.srs[old.w].def = def; save(); } } else V.addMyWord(word, def, ''); render(); };
    [w, m].forEach((i) => i.addEventListener('keydown', (e) => { if (e.key === 'Enter') addOwn(); }));
    const form = h('div', { class: 'card' }, h('h3', { style: 'margin-top:0' }, 'Add your own word'), w, h('div', { style: 'height:8px' }), m, h('div', { class: 'row end', style: 'margin-top:10px' }, h('button', { class: 'btn', onclick: addOwn }, '＋ Add')));
    return { title: 'My words', body: S.my.length ? [form, h('p', { class: 'muted' }, 'Saved words also appear in your flashcards.'),
      S.my.map((x) => h('div', { class: 'card' }, h('div', { class: 'row' }, h('b', { class: 'grow' }, x.w), V.sayBtn(x.w),
        h('button', { class: 'ic', 'aria-label': 'Delete', onclick: () => { S.my = S.my.filter((y) => y !== x); delete S.srs[x.w]; save(); render(); } }, '🗑️')),
      x.def ? h('p', null, x.def) : null, x.ex ? h('p', { class: 'muted small' }, '“' + x.ex + '”') : null))]
      : [form, h('p', { class: 'muted center' }, 'No words yet. Add one above, tap any word in a text, or use the ＋ on the word of the day.')] };
  }
  function historyView() {
    const open = (x) => sheet([h('span', { class: 'pill' }, x.sec + ' · ' + x.level), h('p', { class: 'muted small' }, new Date(x.d).toLocaleString()), h('h3', null, 'Task'), h('p', null, x.prompt),
      h('h3', null, 'Your answer'), h('p', null, x.text), h('h3', null, 'Feedback'), (x.fb || []).map((a) => h('div', { class: 'fb ' + a.v }, h('span', { class: 'tag ' + a.v }, a.name + ' · ' + V.VERDICT[a.v]), h('div', { class: 'small' }, a.d))),
      h('div', { class: 'row end' }, h('button', { class: 'btn sec', onclick: closeSheet }, 'Close'))]);
    return { title: 'History', body: S.history.length ? [h('p', { class: 'muted' }, 'Your speaking and writing answers, newest first.'),
      h('div', { class: 'list' }, S.history.map((x) => h('button', { class: 'tile', onclick: () => open(x) }, h('span', { class: 'em' }, x.sec === 'Speaking' ? '🎙️' : '✍️'),
        h('div', null, h('b', null, x.prompt.slice(0, 70) + (x.prompt.length > 70 ? '…' : '')), h('span', null, h('br'), new Date(x.d).toLocaleDateString() + ' · ' + x.level + ' · ' + x.words + ' words')))))]
      : [h('p', { class: 'muted center' }, 'Nothing yet. Your speaking and writing answers will be kept here with their feedback.')] };
  }
  function statsView() {
    const total = Object.values(S.days).reduce((a, b) => a + b, 0);
    return { title: 'Stats', body: [h('div', { class: 'stat' }, h('div', null, h('b', null, '🔥 ' + streak()), 'day streak'), h('div', null, h('b', null, Object.keys(S.days).length), 'days practised'), h('div', null, h('b', null, total), 'sessions')),
      h('div', { class: 'card' }, h('h3', { style: 'margin-top:0' }, 'Accuracy by section'), SECTIONS.map((s) => {
        const st = S.stats[s.id] || { s: 0, ok: 0, tot: 0 }, pct = st.tot ? Math.round((st.ok * 100) / st.tot) : 0;
        return h('div', { class: 'barrow' }, h('span', null, s.e + ' ' + s.n), h('div', { class: 'prog' }, h('i', { style: 'width:' + pct + '%' })), h('em', null, st.tot ? pct + '% · ' + st.s : st.s + ' done'));
      }), h('p', { class: 'muted small' }, 'Speaking and writing are not scored with a number; they show sessions completed.'))] };
  }
  function settingsView() {
    const key = h('input', { type: 'password', value: S.gemKey, placeholder: 'Paste your free Gemini API key (optional)', autocomplete: 'off' });
    const model = h('input', { type: 'text', value: S.gemModel });
    const msg = h('p', { class: 'muted small' });
    return { title: 'Settings', right: h('span'), body: [
      h('div', { class: 'card' }, h('h3', { style: 'margin-top:0' }, 'AI examiner (optional, free)'),
        h('p', { class: 'small muted' }, 'Volt always corrects you with its built-in checker. If you add a free Google Gemini key, speaking, writing and listening answers are also reviewed by an AI examiner. The key is stored only in this browser. Get one at aistudio.google.com → “Get API key” (no payment needed).'),
        key, h('p', { class: 'small muted', style: 'margin-bottom:2px' }, 'Model'), model,
        h('div', { class: 'row', style: 'margin-top:10px' }, h('button', { class: 'btn', onclick: async () => {
          S.gemKey = key.value.trim(); S.gemModel = model.value.trim() || 'gemini-flash-latest'; save();
          if (!S.gemKey) { msg.textContent = 'Saved. AI examiner is off.'; return; }
          msg.textContent = 'Testing the key…';
          try { await window.FB.gemini(S.gemKey, S.gemModel, 'Return the JSON {"ok":true}'); msg.textContent = '✓ Key works. AI examiner is on.'; }
          catch (e) { msg.textContent = '✗ The key or model did not work (' + e.message + '). Volt will keep using the built-in checker.'; }
        } }, 'Save & test')), msg),
      h('div', { class: 'card' }, h('h3', { style: 'margin-top:0' }, 'Appearance'), h('button', { class: 'btn sec', onclick: () => { S.theme = S.theme === 'dark' ? 'light' : 'dark'; applyTheme(); save(); render(); } }, S.theme === 'dark' ? '☀️ Switch to light mode' : '🌙 Switch to dark mode')),
      h('div', { class: 'card' }, h('h3', { style: 'margin-top:0' }, 'Progress'), h('p', { class: 'small muted' }, 'Progress is saved on this device only.'),
        h('button', { class: 'btn sec', onclick: () => { if (confirm('Delete all progress, history and saved words on this device?')) { const k = S.gemKey, m = S.gemModel, t = S.theme; Object.assign(S, defaults(), { gemKey: k, gemModel: m, theme: t }); save(); V.goHome(); } } }, 'Reset progress'))] };
  }
  function applyTheme() { document.documentElement.setAttribute('data-theme', S.theme); const m = document.querySelector('meta[name=theme-color]'); if (m) m.content = S.theme === 'dark' ? '#0f172a' : '#f1f5f9'; if (stack.length === 1) render(); }

  /* ---------- boot ---------- */
  V.boot = async function () {
    document.documentElement.setAttribute('data-theme', S.theme);
    D.listening = [];
    for (const f of ['data/listening.json', 'data/listening2.json', 'data/listening3.json']) { try { D.listening = D.listening.concat(await (await fetch(f)).json()); } catch (e) { /* skip */ } }
    window.FB.loadWords();
    history.replaceState({ n: 1 }, '');
    stack.push(homeView); render();
    if ('serviceWorker' in navigator && location.protocol === 'https:') {
      navigator.serviceWorker.register('sw.js').then(() => navigator.serviceWorker.ready).then((reg) => {
        if (reg.active) reg.active.postMessage({ cacheAudio: D.listening.map((a) => 'audio/' + a.id + '.mp3') });
      }).catch(() => {});
    }
  };
})();
