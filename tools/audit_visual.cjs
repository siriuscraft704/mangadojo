#!/usr/bin/env node
// Auditoria visual do site renderizado (precisa do Playwright; não roda no CI do GitHub).
// Falha se alguma página usar fonte fora do sistema, texto com matiz fora da paleta ou rolagem horizontal.
// Uso: node tools/audit_visual.cjs [URL_BASE=http://127.0.0.1:8811]   (sirva a pasta do site antes)
const {chromium}=require('playwright');
const base=process.argv[2]||'http://127.0.0.1:8811';
const pages=['index','trilhas','aula','aulas-pranchas','pranchas','oficina','acervo-revisado','creditos','studio','auditoria-imagens','homologacao-artes','revisao-candidatos'];
const ALLOWED_FONTS=new Set(['Hanken Grotesk','Shippori Mincho']);
// matizes permitidos para texto: neutro, carimbo (vermelho ~0-20) e verde de "concluído" (~140-170)
const okHue=h=>h==='neutro'||(h>=0&&h<=22)||(h>=345)||(h>=130&&h<=175);
const hue=c=>{const m=c.match(/[\d.]+/g);if(!m)return null;const [r,g,b,a]=m.map(Number);if(a===0)return null;const mx=Math.max(r,g,b),mn=Math.min(r,g,b),d=mx-mn;if(d<26||d/mx<0.28)return 'neutro'; /* cinzas quentes fazem parte da paleta */let h=mx===r?((g-b)/d)%6:mx===g?(b-r)/d+2:(r-g)/d+4;h=Math.round(h*60);return h<0?h+360:h};
(async()=>{const b=await chromium.launch();let fail=0;
for(const f of pages){const p=await b.newPage({viewport:{width:1360,height:900}});
 await p.goto(`${base}/${f}.html${f==='aula'?'?lesson=gato-sentado':''}`,{waitUntil:'networkidle'});await p.waitForTimeout(300);
 const d=await p.evaluate(()=>{const fonts={},colors={};for(const e of document.querySelectorAll('body *')){const t=[...e.childNodes].some(n=>n.nodeType===3&&n.textContent.trim());if(!t)continue;const c=getComputedStyle(e);if(c.display==='none'||c.visibility==='hidden')continue;const fam=c.fontFamily.split(',')[0].replace(/["']/g,'').trim();fonts[fam]=1;colors[c.color]=1}return {fonts:Object.keys(fonts),colors:Object.keys(colors),ox:document.documentElement.scrollWidth>innerWidth+1}});
 const badFonts=d.fonts.filter(x=>!ALLOWED_FONTS.has(x));
 const badColors=d.colors.filter(c=>!okHue(hue(c)));
 const ok=!badFonts.length&&!badColors.length&&!d.ox;if(!ok)fail++;
 console.log((ok?'ok    ':'FALHA ')+f.padEnd(20),ok?'':JSON.stringify({fontesForaDoSistema:badFonts,coresForaDaPaleta:badColors,rolagemHorizontal:d.ox}));
 await p.close();}
await b.close();console.log(fail?`${fail} página(s) fora do sistema`:'todas as páginas dentro do sistema');process.exit(fail?1:0);})();
