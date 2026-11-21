const fs=require('node:fs'),assert=require('node:assert/strict');
const studio=fs.readFileSync('studio.html','utf8');
const index=fs.readFileSync('index.html','utf8');
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
