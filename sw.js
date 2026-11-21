/* MangaDojo PWA: shell cached, lessons fetched on demand */
const CACHE='mangadojo-v8-shell';
const IMAGES='mangadojo-v8-images';
const CORE=['./','./index.html','./catalog.generated.js','./manifest.webmanifest','./studio.html'];
self.addEventListener('install',event=>{event.waitUntil(caches.open(CACHE).then(c=>c.addAll(CORE)));self.skipWaiting()});
self.addEventListener('activate',event=>{event.waitUntil(caches.keys().then(keys=>Promise.all(keys.filter(k=>k.startsWith('mangadojo-')&&!([CACHE,IMAGES].includes(k))).map(k=>caches.delete(k)))));self.clients.claim()});
self.addEventListener('fetch',event=>{const request=event.request;if(request.method!=='GET'||new URL(request.url).origin!==self.location.origin)return;const u=new URL(request.url);
if(u.pathname.match(/\.(webp|png|jpe?g|svg)$/i)) {event.respondWith(caches.open(IMAGES).then(async cache=>{const hit=await cache.match(request);if(hit)return hit;const res=await fetch(request);if(res.ok){await cache.put(request,res.clone());const all=await cache.keys();if(all.length>100) await cache.delete(all[0]);}return res}));return}
event.respondWith(fetch(request).then(async res=>{if(res.ok){const cache=await caches.open(CACHE);cache.put(request,res.clone())}return res}).catch(()=>caches.match(request).then(r=>r||caches.match('./index.html'))));});
