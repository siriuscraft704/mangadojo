#!/usr/bin/env python3
"""Non-destructive inventory of all lesson images. Flags are review hints, never automatic anatomical verdicts."""
from pathlib import Path
import json, re, hashlib, struct, statistics
import xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
courses=[]
for p in sorted((ROOT/'lessons').glob('*/lesson.json')):
    courses.append(json.loads(p.read_text('utf-8')))
records=[]
seen={}
def dimensions(path):
    b=path.read_bytes()
    if b[:8]==b'\x89PNG\r\n\x1a\n':
        return struct.unpack('>II',b[16:24])
    if b[:4]==b'RIFF' and b[8:12]==b'WEBP':
        kind=b[12:16]
        if kind==b'VP8X':
            return (1+int.from_bytes(b[24:27],'little'),1+int.from_bytes(b[27:30],'little'))
        if kind==b'VP8 ' and b[23:26]==b'\x9d\x01\x2a':
            return (int.from_bytes(b[26:28],'little')&0x3fff,int.from_bytes(b[28:30],'little')&0x3fff)
        if kind==b'VP8L':
            v=int.from_bytes(b[21:25],'little')
            return ((v&0x3fff)+1,((v>>14)&0x3fff)+1)
    if path.suffix.lower()=='.svg':
        root=ET.fromstring(b)
        box=root.attrib.get('viewBox','').replace(',',' ').split()
        if len(box)==4: return (float(box[2]),float(box[3]))
    return (None,None)
for lesson in courses:
    for i,relative in enumerate(lesson['images'],start=1):
        path=ROOT/relative
        if not path.is_file():raise SystemExit('Asset ausente: '+relative)
        w,h=dimensions(path)
        if lesson.get('lessonType')=='board-study':
            expected=tuple(lesson['sourceDimensions'])
            if (w,h)!=expected:
                raise SystemExit(f"Prancha {relative}: dimensões reais {(w,h)} diferentes do catálogo {expected}")
            if min(w,h)<800:
                raise SystemExit(f"Prancha {relative}: resolução inferior a 800 px")
        sha=hashlib.sha256(path.read_bytes()).hexdigest()
        r={'lesson':lesson['id'],'step':i,'path':relative,'width':w,'height':h,
           'bytes':path.stat().st_size,'format':path.suffix.lower()[1:],
           'generation':'new-vector' if '-original-' in relative and relative.endswith('.svg') else 'existing',
           'manual_art_review':True,'source_sheet_preserved':lesson.get('lessonType')=='board-study','risk_flags':[]}
        if w is None:r['risk_flags'].append('unknown-dimensions')
        if w and h and min(w,h)<480:r['risk_flags'].append('low-source-resolution')
        if w and h and (max(w,h)/min(w,h)>2.0):r['risk_flags'].append('extreme-aspect-ratio')
        if sha in seen:r['risk_flags'].append('duplicate-binary:'+seen[sha])
        seen[sha]=relative
        if relative.endswith('.webp') and lesson['id'] in {
            'bob-curto','cabelo-fem-liso','cabelo-fem-ondas','cabelo-masc-longo',
            'cabelos-cacheados','maos-gestos','olhos-femininos','pes-34','pes-perfil',
            'rosto-fem-frontal','rosto-fem-perfil','rosto-masc-34',
            'rosto-masc-frontal','rosto-masc-perfil','sakura','shonen'
        }:r['risk_flags'].append('legacy-composite-review')
        records.append(r)
# Cross-step consistency is only a review heuristic. Aspect variations can be intentional.
by_lesson={}
for row in records:
    if row['width'] and row['height']:
        by_lesson.setdefault(row['lesson'],[]).append(row)
for lesson,images in by_lesson.items():
    aspects=[r['width']/r['height'] for r in images]
    if len(aspects)<2: continue
    typical=statistics.median(aspects)
    for row in images:
        aspect=row['width']/row['height']
        if abs(aspect/typical-1)>0.10:
            row['risk_flags'].append('stage-aspect-inconsistency')
# Source-to-lesson mismatch confirmed in manual browser inspection.
for row in records:
    if row['path']=='assets/cabelo-fem-ondas-1.webp':
        row['risk_flags'].append('source-content-mismatch-review')
summary={'lessons':len(courses),'images':len(records),
         'new_vector':sum(r['generation']=='new-vector' for r in records),
         'legacy_or_unreviewed':sum(r['generation']!='new-vector' for r in records),
         'broken':0,'board_lessons_verified':sum(r['source_sheet_preserved'] for r in records),'flagged':sum(bool(r['risk_flags']) for r in records),
         'aspect_inconsistent':sum('stage-aspect-inconsistency' in r['risk_flags'] for r in records)}
(ROOT/'media_audit.generated.json').write_text(json.dumps({'summary':summary,'assets':records},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('MEDIA AUDIT:',summary)
