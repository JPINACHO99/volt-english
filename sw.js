/* Volt English service worker: app files are network-first (so updates arrive on refresh, offline falls back to cache); audio and icons are cache-first. */
const CACHE = 'volt-v36';
const SHELL = ['./', 'index.html', 'css/style.css', 'js/app.js', 'js/exercises.js', 'js/feedback.js', 'data/reading.js', 'data/reading2.js', 'data/reading3.js', 'data/rexp1.js', 'data/rexp2.js', 'data/rexp3.js', 'data/rexp4.js', 'data/vocab.js', 'data/vocab2.js', 'data/vocab3.js', 'data/grammar.js', 'data/grammar_notes.js', 'data/grammar2.js', 'data/grammar3.js', 'data/grammar4.js', 'data/grammar5.js', 'data/grammar6.js', 'data/grammar7.js', 'data/gopt1.js', 'data/gopt2.js', 'data/gopt3.js', 'data/gopt4.js',
  'data/speaking.js', 'data/writing.js', 'data/phrasal.js', 'data/phrasal2.js', 'data/phrasal3.js', 'data/listening.json', 'data/listening2.json', 'data/listening3.json', 'data/topic_job.js', 'data/topic_job2.js', 'data/topic_job3.js', 'data/speak2_b1.js', 'data/speak2_b2.js', 'data/speak2_c1.js', 'data/speak2_c2.js', 'data/write2_b.js', 'data/write2_c.js', 'data/topic_job4.js', 'data/phrasal_job.js', 'data/scenes_art.js', 'data/videos.js', 'data/quiz.js','data/listening4.json', 'data/listening5.json', 'data/words.txt', 'manifest.webmanifest', 'icons/icon-192.png', 'icons/icon-512.png'];

self.addEventListener('install', (e) => {
  e.waitUntil(caches.open(CACHE).then((c) => c.addAll(SHELL)).then(() => self.skipWaiting()));
});
self.addEventListener('activate', (e) => {
  e.waitUntil(caches.keys().then((ks) => Promise.all(ks.filter((k) => k !== CACHE).map((k) => caches.delete(k)))).then(() => self.clients.claim()));
});
self.addEventListener('message', (e) => {
  // The page asks us to store all audio so listening works offline.
  if (e.data && e.data.cacheAudio) caches.open(CACHE).then((c) => e.data.cacheAudio.forEach((u) => c.match(u).then((hit) => hit || c.add(u).catch(() => {}))));
});
self.addEventListener('fetch', (e) => {
  const url = new URL(e.request.url);
  if (e.request.method !== 'GET' || url.origin !== location.origin) return;
  const cacheFirst = /\/(audio|icons|video)\//.test(url.pathname);
  if (e.request.headers.has('range')) { // media seeking: answer from the cached full file when we have it
    e.respondWith(caches.match(e.request.url, { ignoreSearch: true }).then((hit) => hit ? rangeResponse(e.request, hit) : fetch(e.request)));
    return;
  }
  e.respondWith(cacheFirst
    ? caches.match(e.request).then((hit) => hit || fetch(e.request).then((r) => put(e.request, r)))
    : fetch(e.request).then((r) => put(e.request, r)).catch(() => caches.match(e.request, { ignoreSearch: true }).then((hit) => hit || caches.match('index.html'))));
});
function put(req, res) {
  if (res && res.status === 200) { const copy = res.clone(); caches.open(CACHE).then((c) => c.put(req, copy)); }
  return res;
}
async function rangeResponse(req, res) {
  const buf = await res.arrayBuffer(), m = /bytes=(\d+)-(\d*)/.exec(req.headers.get('range')) || [];
  const start = Number(m[1] || 0), end = m[2] ? Number(m[2]) : buf.byteLength - 1;
  return new Response(buf.slice(start, end + 1), { status: 206, headers: { 'Content-Type': res.headers.get('Content-Type') || 'audio/mpeg',
    'Content-Range': 'bytes ' + start + '-' + end + '/' + buf.byteLength, 'Content-Length': String(end - start + 1), 'Accept-Ranges': 'bytes' } });
}
