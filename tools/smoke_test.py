#!/usr/bin/env python3
"""Static smoke tests for the GitHub Pages build, dependencies and original lesson assets."""
from pathlib import Path
import json
import xml.etree.ElementTree as ET
import shutil
import subprocess
import tempfile
import re
import sys
ROOT=Path(__file__).resolve().parents[1]
index=(ROOT/'index.html').read_text('utf-8')
studio=(ROOT/'studio.html').read_text('utf-8')
catalog=json.loads((ROOT/'catalog.generated.json').read_text('utf-8'))
assert catalog['lessons']==7 and catalog['stages']==50, catalog
published = {p.parent.name: json.loads(p.read_text('utf-8')) for p in ROOT.glob('lessons/*/lesson.json')}
expected = {'gato-sentado':10, 'gato-em-pe':6, 'leao':10, 'lobo-correndo':10, 'mao':6,
            'observacao-vetorial':4, 'silhuetas-criaturas':4}
assert {key:len(value['images']) for key,value in published.items()} == expected
archive=ROOT/'drafts/retired-lessons'
assert len(list(archive.glob('*.json')))==25
assert all(path.startswith('assets/mao-aberta-r2-') for path in published['mao']['images'])
with tempfile.TemporaryDirectory() as temp:
    public=Path(temp)/'public'
    subprocess.run([sys.executable, str(ROOT/'tools/package_pages.py'), str(public)], check=True)
    assert not (public/'drafts').exists()
    assert not (public/'assets/shojo-1.webp').exists()
    assert len(list((public/'assets').glob('*.webp')))==42
    assert (public/'oficina.html').exists()
    assert (public/'revisao-candidatos.html').exists()
    boards = json.loads((public/'pranchas.json').read_text('utf-8'))
    paths = {board['image'] for board in boards}
    assert len(boards) == len(paths) == 86
    assert len({board['category'] for board in boards}) == 7
    assert all(board['width'] > 0 and board['height'] > 0 for board in boards)
    assert all((public/path).is_file() for path in paths)
    assert (public/'pranchas.html').exists()
    assert 'pranchas.html' in index
    assert 'pranchas.html' in (public/'acervo-revisado.html').read_text('utf-8')
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
assert 'checksCount' in index and 'checkIds' in index
assert 'trilhas.html' in index and 'requestedLesson' in index
assert 'creditos.html' in index
assert 'homologacao-artes.html' in index
assert 'acervo-revisado.html' in index
local_art=(ROOT/'acervo-revisado.html').read_text('utf-8')
assert 'mangadojo-artwork' in local_art and 'indexedDB' in local_art
assert 'localArt=' in local_art and 'referências públicas' in local_art
assert "new DecompressionStream('deflate-raw')" in local_art
assert "extractZip(zip)" in local_art and "importZip" in local_art
assert 'function importLocalArt' in studio and "params.has('localArt')" in studio
assert 'cabelos-ondulados|rosto-feminino' in local_art or ('cabelos-ondulados' in local_art and 'rosto-feminino' in local_art)
assert 'cabelos-ondulados' in studio and 'rosto-feminino' in studio
candidate_page=(ROOT/'revisao-candidatos.html').read_text('utf-8')
assert 'mangadojo-art-review-v2' in candidate_page and 'Exportar avaliação' in candidate_page
manifest=json.loads((ROOT/'art-review-manifest.json').read_text('utf-8'))
assert len(manifest['candidates'])==12
assert all(len(a['sha256'])==64 and a['dimensions']==[840,960] for a in manifest['candidates'])
assert 'import_art_pack.py' in [p.name for p in (ROOT/'tools').iterdir()]
assert 'issue_comment' in (ROOT/'.github/workflows/importar-artes.yml').read_text('utf-8')
assert "object-fit:contain!important" in (ROOT/'styles/atelier.css').read_text('utf-8')

homolog=(ROOT/'homologacao-artes.html').read_text('utf-8')
assert 'catalog.generated.js' in homolog
assert 'image/webp' in homolog and 'image/png' in homolog
assert 'object-fit:contain' in homolog
assert 'Exportar relatório JSON' in homolog
assert 'zoomImage' in homolog and 'closeZoom' in homolog
assert 'ART_REVIEW_HAND_OPEN.md' in [p.name for p in ROOT.iterdir()]
assert 'candidate' in homolog and 'decisions' in homolog

credits=(ROOT/'creditos.html').read_text('utf-8')
assert 'mit-asset-manifest.json' in credits and 'Vijay Verma' in credits
assert (ROOT/'assets/mit-asset-manifest.json').exists()
trails=(ROOT/'trilhas.html').read_text('utf-8')
assert 'catalog.generated.js' in trails and 'lobo-correndo' in trails
assert 'observacao-vetorial' in trails and 'silhuetas-criaturas' in trails
assert 'state.checks[checkIds[i]]' in index
assert '.check-row.done' in (ROOT/'styles/atelier.css').read_text('utf-8')
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
    for name, html in [('index', index), ('studio', studio), ('trilhas', trails), ('acervo', local_art), ('oficina', (ROOT/'oficina.html').read_text('utf-8')), ('pranchas', (ROOT/'pranchas.html').read_text('utf-8')), ('revisao', candidate_page)]:
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
