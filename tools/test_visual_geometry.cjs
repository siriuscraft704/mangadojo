const fs=require('node:fs'),assert=require('node:assert/strict');
const studio=fs.readFileSync('studio.html','utf8');
const index=fs.readFileSync('aula.html','utf8');
const start=studio.indexOf('function drawContained(');
const end=studio.indexOf('function imageInto(',start);
assert.ok(start>0&&end>start,'No Smudge contain helper');
const drawContained=new Function(studio.slice(start,end)+';return drawContained;')();
function check(w,h,expected){
 let call=null;const ctx={drawImage:(...args)=>call=args};
 drawContained(ctx,{naturalWidth:w,naturalHeight:h},900,900);
 assert.ok(call,'No drawImage');
 const actual=call.slice(1);assert.equal(actual.length,4);
 actual.forEach((v,i)=>assert.ok(Math.abs(v-expected[i])<.01,JSON.stringify({w,h,actual,expected})));
}
check(800,1200,[150,0,600,900]);
check(1200,800,[0,150,900,600]);
check(900,900,[0,0,900,900]);
assert.ok(index.includes('out.width=900;out.height=1000'),'Portrait lesson export missing');
assert.ok(index.includes('const scale=Math.min(out.width/img.naturalWidth,out.height/img.naturalHeight)'),'Reference export must preserve aspect');
assert.ok(index.includes('compareArt')&&index.includes('compareDialog'),'Comparison tool missing');
assert.ok(index.includes('reportArt'),'Report link missing');
console.log('PASS: 3 proportional-import cases + portrait export + tutorial comparison');

// Exercise the same geometry the editor uses for snapping and for its repeating dot tile.
const vm=require('node:vm');
const sandbox={window:{}};
vm.runInNewContext(fs.readFileSync('scripts/smudge-editing.js','utf8'),sandbox);
const editing=sandbox.window.SmudgeEditing;
const startPoint={x:30,y:30}, cursor={x:60,y:30}, vanishingPoint={x:0,y:0};
const snapped=editing.perspectiveEndpoint(startPoint,cursor,vanishingPoint);
assert.equal(snapped.x,45);
assert.equal(snapped.y,45);
assert.equal(editing.perspectiveEndpoint(vanishingPoint,cursor,vanishingPoint),cursor);
const offCenter=editing.perspectiveEndpoint({x:125,y:50},{x:245,y:170},{x:225,y:50});
assert.equal(offCenter.x,245);
assert.equal(offCenter.y,50);
assert.equal(editing.hasReticleArea([{x:0,y:0},{x:1,y:8},{x:0,y:10}]),false);
assert.equal(editing.hasReticleArea([{x:0,y:0},{x:12,y:0},{x:12,y:12}]),true);
for(const density of [5,25,70]){
 const radius=editing.reticleRadius(density,12);
 assert.ok(radius>0&&radius<6,'Reticle dots must fit inside the tile');
 assert.ok(Math.abs(Math.PI*radius*radius/144-density/100)<.0001,'Reticle density must match dot coverage');
}
assert.ok(fs.readFileSync('sw.js','utf8').includes('./scripts/smudge-editing.js?v=2'),'Offline shell must cache the current editor script');
console.log('PASS: perspective projection, reticle geometry and offline editor script');
