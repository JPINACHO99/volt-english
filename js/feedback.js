/* Free correction engine: local rules + LanguageTool public API, plus optional Gemini (free tier, user's own key). */
(function () {
  const FB = (window.FB = {});
  let rank = null; // word -> frequency rank (1 = most common)

  FB.loadWords = async function () {
    try {
      const t = await (await fetch('data/words.txt')).text();
      rank = new Map();
      t.split(/\r?\n/).forEach((w, i) => { if (w) rank.set(w, i + 1); });
    } catch (e) { rank = null; }
  };

  const tokens = (s) => (s.toLowerCase().match(/[a-z]+(?:'[a-z]+)?/g) || []);
  function wordRank(w) {
    if (!rank) return 0;
    w = w.replace(/n't$/, '').replace(/'(s|d|ll|ve|re|m)$/, '');
    const tries = [w, w.replace(/s$/, ''), w.replace(/es$/, ''), w.replace(/ies$/, 'y'), w.replace(/ed$/, ''), w.replace(/ed$/, 'e'),
      w.replace(/ing$/, ''), w.replace(/ing$/, 'e'), w.replace(/ly$/, ''), w.replace(/er$/, ''), w.replace(/est$/, ''), w.replace(/(.)\1(ed|ing)$/, '$1')];
    let best = Infinity;
    for (const t of tries) { const r = rank.get(t); if (r && r < best) best = r; }
    return best; // Infinity = not in the 10k list
  }

  const PP = 'been|done|gone|seen|taken|given|made|known|written|spoken|broken|chosen|found|built|bought|brought|thought|told|sold|sent|spent|left|kept|felt|held|heard|read|run|come|become|begun|got|gotten|put|set|cut|lost|won|paid|said|met|led|shown|grown|drawn|driven|eaten|fallen|forgotten|taught|caught|understood|worn|born|meant|dealt|sat|stood';
  const PAST = 'was|were|went|had|did|saw|took|gave|made|knew|wrote|spoke|broke|chose|found|built|bought|brought|thought|told|sold|sent|spent|left|kept|felt|held|heard|ran|came|became|began|got|put|lost|won|paid|said|met|led|grew|drove|ate|fell|forgot|taught|caught|understood|wore|meant|sat|stood|could';
  const STRUCT = [
    ['Past simple', new RegExp("\\b(" + PAST + ")\\b|\\b[a-z]{2,}ed\\b")],
    ['Present perfect', new RegExp("\\b(have|has|'ve|haven't|hasn't)\\s+(not\\s+|never\\s+|already\\s+|just\\s+|always\\s+)?(" + PP + "|[a-z]{2,}ed)\\b|\\b(i|you|we|they)'ve\\b")],
    ['Past perfect', new RegExp("\\b(had|hadn't|'d)\\s+(not\\s+|never\\s+|already\\s+|just\\s+)?(" + PP + "|[a-z]{3,}ed)\\b")],
    ['Continuous forms', /\b(am|is|are|was|were|been|be|'m|'re|'s)\s+(not\s+)?[a-z]{2,}ing\b/],
    ['Future forms', /\b(will|won't|shall)\b|'ll\b|\bgoing to\b/],
    ['Conditionals', /\bif\b[^.?!]*\b(would|will|could|might|had|were)\b|\b(would|could|might)\b[^.?!]*\bif\b|\b(unless|provided that|as long as)\b/],
    ['Would / could / might', /\b(would|wouldn't|could|couldn't|might|'d rather|'d like)\b/],
    ['Passive voice', new RegExp("\\b(is|are|was|were|be|been|being)\\s+(not\\s+)?(" + PP + "|[a-z]{3,}ed)\\b")],
    ['Modals of obligation / advice', /\b(should|shouldn't|must|mustn't|have to|has to|had to|ought to|need to|needn't)\b/],
    ['Relative & complex clauses', /\b(which|whose|whom|whereas|although|even though|despite|in spite of|while|whereby)\b/],
    ['Perfect modals / inversion', /\b(should|could|would|might|must)(n't)?\s+have\b|\b(not only|no sooner|hardly|rarely|seldom|never)\s+(did|do|does|had|have|has|was|were)\b|\bhad i\b/]
  ];
  const LINK = {
    1: ['and', 'but', 'because', 'so', 'then', 'also', 'first', 'when', 'after', 'before'],
    2: ['however', 'although', 'for example', 'for instance', 'on the other hand', 'in addition', 'as a result', 'besides', 'finally', 'in my opinion', 'actually', 'instead', 'while', 'since', 'unless', 'in conclusion', 'to sum up', 'that said', 'even though'],
    3: ['moreover', 'furthermore', 'nevertheless', 'nonetheless', 'whereas', 'therefore', 'consequently', 'despite', 'in spite of', 'on balance', 'having said that', 'by contrast', 'in contrast', 'admittedly', 'to my mind', 'provided that', 'thus', 'hence', 'albeit', 'on the whole', 'as far as', 'rather than']
  };
  const TARGET = { // per level: advanced-word ratio, structures, connector score, words (speaking question)
    B1: { adv: 0.05, st: 3, link: 3, words: 30 }, B2: { adv: 0.08, st: 4, link: 5, words: 45 },
    C1: { adv: 0.12, st: 5, link: 8, words: 60 }, C2: { adv: 0.16, st: 6, link: 10, words: 70 }
  };
  const verdict = (v, target) => (v >= target ? 'good' : v >= target * 0.6 ? 'ok' : 'weak');

  async function languageTool(text) {
    const body = new URLSearchParams({ text, language: 'en-GB' });
    const r = await fetch('https://api.languagetool.org/v2/check', { method: 'POST', body });
    if (!r.ok) throw new Error('LT ' + r.status);
    return (await r.json()).matches || [];
  }

  /** opts: {level, kind:'speaking'|'writing', targetWords} -> {aspects, issues, words} */
  FB.analyze = async function (text, opts) {
    const T = TARGET[opts.level] || TARGET.B2, low = ' ' + text.toLowerCase().replace(/\s+/g, ' ') + ' ';
    const toks = tokens(text), n = toks.length, aspects = [], issues = [];
    // grammar & spelling (LanguageTool, free public service)
    let misspelt = new Set(), ltOk = true;
    try {
      const skip = opts.kind === 'speaking' ? /TYPOGRAPHY|PUNCTUATION|CASING|TYPOS|MISC|STYLE|REDUNDANCY/ : /TYPOGRAPHY|STYLE|REDUNDANCY/;
      for (const m of await languageTool(text)) {
        const bad = text.substr(m.offset, m.length);
        if (m.rule.category.id === 'TYPOS') misspelt.add(bad.toLowerCase());
        if (skip.test(m.rule.category.id) || /UPPERCASE_SENTENCE_START|COMMA|WHITESPACE/.test(m.rule.id)) continue;
        issues.push({ bad, sug: (m.replacements || []).slice(0, 2).map((x) => x.value).join(' / '), msg: m.message });
      }
    } catch (e) { ltOk = false; }
    if (ltOk) {
      const per100 = n ? (issues.length * 100) / n : 0;
      aspects.push({ name: 'Grammar accuracy', v: !n ? 'weak' : per100 <= 1.5 ? 'good' : per100 <= 4 ? 'ok' : 'weak',
        d: issues.length ? issues.length + ' possible mistake' + (issues.length > 1 ? 's' : '') + ' found (see below).' : 'No mistakes detected by the automatic checker.' });
    } else aspects.push({ name: 'Grammar accuracy', v: 'na', d: 'The grammar checker needs an internet connection. The other aspects were analysed offline.' });
    // vocabulary range
    if (rank && n) {
      const adv = [...new Set(toks.filter((w) => !misspelt.has(w) && w.length > 3 && wordRank(w) > 2500))];
      const ratio = toks.filter((w) => !misspelt.has(w) && w.length > 3 && wordRank(w) > 2500).length / n;
      const variety = new Set(toks).size / n;
      const v = verdict(ratio, T.adv);
      aspects.push({ name: 'Vocabulary', v, d: (v === 'good' ? 'Good range for ' + opts.level + '. ' : v === 'ok' ? 'Acceptable, but mostly common words for ' + opts.level + '. ' : 'Mostly basic words for ' + opts.level + '. Try more precise vocabulary. ') +
        (adv.length ? 'Less common words you used: ' + adv.slice(0, 8).join(', ') + '. ' : '') + (n > 40 && variety < 0.45 ? 'You repeat words quite often.' : '') });
    }
    // verb forms
    const found = STRUCT.filter(([, re]) => re.test(low)).map(([name]) => name);
    const missing = STRUCT.map((s) => s[0]).filter((x) => !found.includes(x));
    const vt = verdict(found.length, T.st);
    aspects.push({ name: 'Verb tenses & structures', v: n ? vt : 'weak', d: (found.length ? 'Used: ' + found.join(', ') + '. ' : 'Only present simple detected. ') +
      (vt !== 'good' && missing.length ? 'To sound more ' + opts.level + ', try adding: ' + missing.slice(0, 3).join(', ') + '.' : '') });
    // connectors
    let score = 0; const used = [];
    for (const tier of [1, 2, 3]) for (const c of LINK[tier]) if (low.includes(' ' + c + ' ') || low.includes(' ' + c + ',')) { score += tier; used.push(c); }
    const vl = verdict(score, T.link);
    aspects.push({ name: 'Linking & organisation', v: n ? vl : 'weak', d: (used.length ? 'Connectors used: ' + used.slice(0, 8).join(', ') + '. ' : 'No connectors found. ') +
      (vl !== 'good' ? 'Add linkers such as ' + LINK[opts.level === 'B1' ? 2 : 3].filter((c) => !used.includes(c)).slice(0, 3).join(', ') + '.' : '') });
    // development
    const target = opts.targetWords || T.words;
    const vd = verdict(n, target * 0.85);
    aspects.push({ name: 'Development', v: vd, d: n + ' words (target: about ' + target + '). ' + (vd === 'good' ? 'Well developed.' : 'Develop your ideas more: add reasons, examples or details.') });
    return { aspects, issues, words: n };
  };

  /* ---------- Optional Gemini (free tier) ---------- */
  FB.gemini = async function (key, model, prompt) {
    const url = 'https://generativelanguage.googleapis.com/v1beta/models/' + encodeURIComponent(model || 'gemini-flash-latest') + ':generateContent?key=' + encodeURIComponent(key);
    const r = await fetch(url, { method: 'POST', headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ contents: [{ parts: [{ text: prompt }] }], generationConfig: { responseMimeType: 'application/json', temperature: 0.3 } }) });
    if (!r.ok) throw new Error('Gemini error ' + r.status);
    const j = await r.json();
    return JSON.parse(j.candidates[0].content.parts.map((p) => p.text || '').join(''));
  };
  FB.aiProduction = (key, model, o) => FB.gemini(key, model,
    'You are an experienced Cambridge English examiner. A learner aiming at CEFR level ' + o.level + ' produced this ' + (o.kind === 'speaking' ? 'SPOKEN answer (automatic transcript: ignore punctuation, capitalisation and pronunciation)' : 'WRITTEN text') +
    '.\nTask: ' + o.prompt + '\nLearner answer: """' + o.text + '"""\n' +
    'Assess it against level ' + o.level + ' using Cambridge criteria. Return JSON only: {"aspects":[{"name":string,"verdict":"good"|"ok"|"weak","comment":string}],"corrections":[{"original":string,"corrected":string,"why":string}],"improved":string}. ' +
    'Aspects must be exactly: ' + (o.kind === 'speaking' ? '"Vocabulary", "Verb tenses & grammar", "Development of ideas", "Linking & coherence"' : '"Content", "Communicative achievement", "Organisation", "Language"') +
    '. Comments: one or two short sentences in simple English, quoting the learner. corrections: up to 6 real mistakes copied exactly from the answer. improved: the same answer rewritten at a strong ' + o.level + ' level, similar length.');
  FB.aiListening = (key, model, o) => FB.gemini(key, model,
    'A learner (level ' + o.level + ') listened to this dialogue:\n"""' + o.transcript + '"""\nThey answered comprehension questions in their own words. Judge only comprehension, not grammar or spelling.\n' +
    o.qa.map((x, i) => (i + 1) + '. Question: ' + x.q + '\n   Expected: ' + x.a + '\n   Learner: ' + (x.u || '(no answer)')).join('\n') +
    '\nReturn JSON only: {"results":[{"verdict":"correct"|"partial"|"wrong","comment":string}]} with one entry per question, in order. Comment: one short sentence saying what was right or missing.');
})();
