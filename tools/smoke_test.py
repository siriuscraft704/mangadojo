#!/usr/bin/env python3
"""Static smoke tests for the GitHub Pages build, dependencies and original lesson assets."""
from pathlib import Path
import json
import xml.etree.ElementTree as ET
import shutil
import subprocess
import tempfile
import re
ROOT=Path(__file__).resolve().parents[1]
index=(ROOT/'index.html').read_text('utf-8')
studio=(ROOT/'studio.html').read_text('utf-8')
catalog=json.loads((ROOT/'catalog.generated.json').read_text('utf-8'))
assert catalog['lessons']==27 and catalog['stages']==158, catalog
for path in ['styles/atelier.css','styles/smudge.css','assets/mangadojo-mark.svg','assets/smudge-mark.svg']:
    assert (ROOT/path).is_file(),path
assert 'styles/atelier.css' in index
assert 'styles/smudge.css' in studio
assert 'auditoria-imagens.html' in index
assert (ROOT/'auditoria-imagens.html').exists()
review=(ROOT/'auditoria-imagens.html').read_text('utf-8')
assert 'catalog.generated.js' in review and 'object-fit:contain' in review
assert 'mangadojo-review-v1' in review
assert 'mangadojo-auditoria-imagens.json' in review
assert 'Anatomia incorreta' in review and 'Imagem cortada' in review
assert 'closeLightbox' in review
gesture=json.loads((ROOT/'lessons/maos-gestos/lesson.json').read_text('utf-8'))
assert len(gesture['images'])==6 and all(p==f'assets/maos-gestos-{i}.webp' for i,p in enumerate(gesture['images'],start=1))
assert 'aspect-ratio:9/10!important' in (ROOT/'styles/atelier.css').read_text('utf-8')
assert not (ROOT/'lessons/olhos-expressivos/lesson.json').exists()
assert not (ROOT/'lessons/rosto-tres-quartos/lesson.json').exists()
workshop=json.loads((ROOT/'lessons/observacao-vetorial/lesson.json').read_text('utf-8'))
assert workshop['lessonType']=='reference-studies' and len(workshop['images'])==4
animals=json.loads((ROOT/'lessons/silhuetas-criaturas/lesson.json').read_text('utf-8'))
assert animals['lessonType']=='reference-studies' and len(animals['images'])==4
assert all((ROOT/img).exists() for img in animals['images'])
for img in animals['images']: ET.parse(ROOT/img)
assert all((ROOT/img).exists() for img in workshop['images'])
assert 'THIRD_PARTY_NOTICES.md' in [p.name for p in ROOT.iterdir()]
assert 'licenseNote' in index and 'exercícios de observação' in index
for img in workshop['images']: ET.parse(ROOT/img)
assert 'Smudge' in index and 'Smudge' in studio
assert 'smudge-projects' in studio and 'dbRead' in studio
assert 'courseImg(current,step+1).split' in index
assert 'webp|svg|png' in studio
assert 'stabilizer' in studio and 'smoothPoint' in studio
assert 'Referência: ' in studio
assert 'Projeto incompatível' in studio
assert 'function drawContained' in studio
assert 'drawContained(c,im,size,size)' in studio
assert 'Math.min(width/sw,height/sh)' in studio
assert "img.naturalWidth*scale" in index
assert 'compareArt' in index and 'compareDialog' in index
assert 'reportArt' in index
assert 'category.includes(\'mãos\')' in index
assert 'OPEN_SOURCE_RESEARCH_2026.md' in [p.name for p in ROOT.iterdir()]
review_scripts=re.findall(r'<script(?:\s[^>]*)?>([\s\S]*?)</script>', review)
if shutil.which('node'):
    for number, code in enumerate(review_scripts):
        if not code.strip(): continue
        with tempfile.NamedTemporaryFile('w',suffix='.js',encoding='utf-8',delete=False) as script:
            script.write(code)
        path=Path(script.name)
        try: subprocess.run(['node','--check',str(path)],check=True,capture_output=True,text=True)
        finally: path.unlink(missing_ok=True)
# Validate inline browser JavaScript with Node when present on the runner.
if shutil.which('node'):
    for name, html in [('index', index), ('studio', studio)]:
        for number, code in enumerate(re.findall(r'<script(?:\s[^>]*)?>([\s\S]*?)</script>', html)):
            if not code.strip():
                continue
            with tempfile.NamedTemporaryFile('w', suffix='.js', encoding='utf-8', delete=False) as script:
                script.write(code)
            path=Path(script.name)
            try:
                subprocess.run(['node', '--check', str(path)], check=True, capture_output=True, text=True)
            finally:
                path.unlink(missing_ok=True)
for path in [*ROOT.glob('assets/*-original-*.svg'),ROOT/'assets/smudge-mark.svg',ROOT/'assets/mangadojo-mark.svg']:
    ET.parse(path)
for path in ROOT.glob('lessons/*/lesson.json'):
    lesson=json.loads(path.read_text('utf-8'))
    assert len(lesson['images'])==len(lesson['steps']),path
    for asset in lesson['images']:
        assert (ROOT/asset).exists(),asset
print(f"PASS: {catalog['lessons']} aulas, {catalog['stages']} etapas; Smudge e imagens originais preservadas")
