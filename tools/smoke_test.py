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
index=(ROOT/'index.html').read_text('utf-8')   # home (landing)
aula=(ROOT/'aula.html').read_text('utf-8')     # aplicativo de aulas
studio=(ROOT/'studio.html').read_text('utf-8')
catalog=json.loads((ROOT/'catalog.generated.json').read_text('utf-8'))
assert catalog['lessons']==88 and catalog['stages']==141, catalog
published = {p.parent.name: json.loads(p.read_text('utf-8')) for p in ROOT.glob('lessons/*/lesson.json')}
expected = {'gato-sentado':10, 'gato-em-pe':6, 'leao':10, 'lobo-correndo':10, 'mao':6,
            'observacao-vetorial':4, 'silhuetas-criaturas':4, 'rosto-feminino':6, 'cabelos-ondulados':6}
boards=json.loads((ROOT/'pranchas.json').read_text('utf-8'))
for board in boards:
    if board['category']=='História visual do projeto' or 'practice' in board:continue
    number=board['image'].split('prancha-')[1].split('.')[0]
    key='estudo-prancha-'+number
    expected[key]=1
    lesson=published[key]
    assert lesson['lessonType']=='board-study' and lesson['images']==[board['image']]
    assert lesson['sourceDimensions']==[board['width'],board['height']]
assert len([lesson for lesson in published.values() if lesson.get('lessonType')=='board-study'])==79
assert {key:len(value['images']) for key,value in published.items()} == expected
archive=ROOT/'drafts/retired-lessons'
assert len(list(archive.glob('*.json')))==25
assert all(path.startswith('assets/mao-aberta-r2-') for path in published['mao']['images'])
assert all(x.startswith('assets/review-pending/') for name in ('rosto-feminino','cabelos-ondulados') for x in published[name]['images'])
assert all(published[name]['reviewStatus']=='experimental' for name in ('rosto-feminino','cabelos-ondulados'))
assert 'Em avaliação' in aula
with tempfile.TemporaryDirectory() as temp:
    public=Path(temp)/'public'
    subprocess.run([sys.executable, str(ROOT/'tools/package_pages.py'), str(public)], check=True)
    assert not (public/'drafts').exists()
    assert not (public/'assets/shojo-1.webp').exists()
    assert len(list((public/'assets').glob('*.webp')))==42
    assert len(list((public/'assets/review-pending').glob('*.webp')))==12
    assert (public/'oficina.html').exists()
    assert (public/'revisao-candidatos.html').exists()
    boards = json.loads((public/'pranchas.json').read_text('utf-8'))
    paths = {board['image'] for board in boards}
    assert len(boards) == len(paths) == 106
    practice = [board for board in boards if 'practice' in board]
    assert len(practice) == 20
    assert len({board['practiceId'] for board in practice}) == len(practice)
    assert all(board['smudgeTool'] in {'line', 'reticle', 'pencil', 'brush'} for board in practice)
    for board in practice:
        assert set(board['practice']) == {'level', 'tool', 'exercise', 'review'}
        assert all(isinstance(text, str) and text.strip() for text in board['practice'].values())
        assert (public/board['image']).read_bytes()[8:12] == b'WEBP'
    assert len({board['category'] for board in boards}) == 7
    assert all(board['width'] > 0 and board['height'] > 0 for board in boards)
    assert all((public/path).is_file() for path in paths)
    assert (public/'pranchas.html').exists()
    # Integridade do pacote: todo href/src local de cada página publicada deve existir no artefato.
    import re as _re
    from urllib.parse import urlparse as _urlparse
    for page in sorted(public.glob('*.html')):
        text=_re.sub(r'<script(?:\s[^>]*)?>[\s\S]*?</script>','',page.read_text('utf-8'))  # só HTML estático
        for ref in _re.findall(r'(?:href|src)="([^"#?]+)(?:[?#][^"]*)?"',text):
            if ref.startswith(('http:','https:','data:','mailto:','javascript:','//')) or ref in ('./','') or any(c in ref for c in "+'{$"):
                continue
            assert (public/ref).exists(), f'{page.name}: referência quebrada no pacote: {ref}'
    for css in sorted((public/'styles').glob('*.css')):
        for ref in _re.findall(r'url\("?([^)"?#]+)',css.read_text('utf-8')):
            if ref.startswith(('data:','http')):continue
            assert (css.parent/ref).resolve().exists(), f'{css.name}: url() quebrada no pacote: {ref}'
        for ref in _re.findall(r'@import url\("([^"]+)"\)',css.read_text('utf-8')):
            assert (css.parent/ref).exists(), f'{css.name}: @import quebrado: {ref}'

    for f in ('aula.html','curso.generated.js','scripts/curso.js','scripts/home.js','styles/site.css','styles/curso.css','styles/home.css','styles/aula.css','assets/academia/hero-curso.webp','assets/academia/hero-anime.webp','assets/academia/smudge-produto.webp','assets/fonts/shippori-mincho-latin-700-normal.woff2','assets/fonts/hanken-grotesk-latin-400-normal.woff2'):assert (public/f).exists(),f
    assert (public/'aulas-pranchas.html').exists()
    assert not (public/'styles/atelier.css').exists() and not (public/'styles/dojo-identity.css').exists(), 'CSS legado não deve ir ao Pages'
    assert 'pranchas.html' in aula
    assert 'aulas-pranchas.html' in aula
    assert 'pranchas.html' in (public/'acervo-revisado.html').read_text('utf-8')
for path in ['styles/aula.css','styles/smudge.css','assets/mangadojo-mark.svg','assets/smudge-mark.svg']:
    assert (ROOT/path).is_file(),path
assert 'styles/aula.css' in aula
assert 'atelier.css' not in aula and 'dojo-identity.css' not in aula and 'dojo-home.css' not in aula, 'aula.html não deve mais carregar o CSS legado'
assert 'styles/smudge-identity.css' in studio
assert 'MangaDojo Atelier 13.6.0' in aula
for path in ['styles/smudge-identity.css']:
    assert (ROOT/path).is_file(), path
for path in ['assets/mangadojo-mark.svg','assets/smudge-mark.svg']:
    ET.parse(ROOT/path)
assert 'board-layout' in aula and 'boardOriginal' in aula
assert "const move=n<0?-1:n>0?1:0" in aula and 'Próxima aula →' in aula
assert 'aspect-ratio:var(--sheet-aspect)' in (ROOT/'styles/aula.css').read_text('utf-8')
assert 'styles/smudge.css' in studio
assert 'auditoria-imagens.html' in aula
assert (ROOT/'auditoria-imagens.html').exists()
review=(ROOT/'auditoria-imagens.html').read_text('utf-8')
assert 'catalog.generated.js' in review and 'object-fit:contain' in review
assert 'mangadojo-review-v1' in review
assert 'mangadojo-auditoria-imagens.json' in review
assert 'Anatomia incorreta' in review and 'Imagem cortada' in review
assert 'closeLightbox' in review
assert 'aspect-ratio:9/10' in (ROOT/'styles/aula.css').read_text('utf-8')
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
assert 'licenseNote' in aula and 'exercícios de observação' in aula
assert 'checksCount' in aula and 'checkIds' in aula
assert 'trilhas.html' in aula and 'requestedLesson' in aula
assert 'creditos.html' in aula
assert 'homologacao-artes.html' in aula
assert 'acervo-revisado.html' in aula
local_art=(ROOT/'acervo-revisado.html').read_text('utf-8')
assert 'mangadojo-artwork' in local_art and 'indexedDB' in local_art
assert 'localArt=' in local_art and 'imagens públicas' in local_art
assert "new DecompressionStream('deflate-raw')" in local_art
assert "extractZip(zip)" in local_art and "importZip" in local_art
assert 'function importLocalArt' in studio and "params.has('localArt')" in studio
assert 'cabelos-ondulados|rosto-feminino' in local_art or ('cabelos-ondulados' in local_art and 'rosto-feminino' in local_art)
assert 'cabelos-ondulados' in studio and 'rosto-feminino' in studio
candidate_page=(ROOT/'revisao-candidatos.html').read_text('utf-8')
assert 'mangadojo-art-review-v2' in candidate_page and 'Exportar avaliação' in candidate_page
assert "assets/review-pending/" in candidate_page
manifest=json.loads((ROOT/'art-review-manifest.json').read_text('utf-8'))
assert len(manifest['candidates'])==12
assert all(len(a['sha256'])==64 and a['dimensions']==[840,960] for a in manifest['candidates'])
assert 'import_art_pack.py' in [p.name for p in (ROOT/'tools').iterdir()]
assert 'issue_comment' in (ROOT/'.github/workflows/importar-artes.yml').read_text('utf-8')
assert "object-fit:contain" in (ROOT/'styles/aula.css').read_text('utf-8')

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
# Curso (trilhas.html): módulos vêm de curso.json; todas as aulas pertencem a exatamente um módulo
assert 'catalog.generated.js' in trails and 'curso.generated.js' in trails and 'scripts/curso.js' in trails
assert 'styles/site.css' in trails and 'styles/curso.css' in trails
course=json.loads((ROOT/'curso.json').read_text('utf-8'))
lesson_data=json.loads((ROOT/'catalog.generated.json').read_text('utf-8'))
assert len(course['modules'])==7 and len({m['category'] for m in course['modules']})==7
assert sorted(m['category'] for m in course['modules'])==lesson_data['categories']
assert len(lesson_data['categories'])==7, 'categorias duplicadas voltaram'
assert 'Curso' in aula and 'trilhas.html' in aula
assert 'Auditoria de imagens' in aula
assert (ROOT/'assets/academia/hero-curso.webp').exists()
# Home nova (index.html)
home_counts=json.loads((ROOT/'catalog.generated.json').read_text('utf-8'))
assert 'styles/home.css' in index and 'scripts/home.js' in index and 'styles/site.css' in index
assert f'data-n="aulas">{home_counts["lessons"]}<' in index, 'número de aulas da home desatualizado'
assert f'data-n="modulos">{len(course["modules"])}<' in index, 'número de módulos da home desatualizado'
assert 'assets/academia/hero-anime.webp' in index, 'a ilustração de anime deve estar na capa'
for link in ('trilhas.html','aulas-pranchas.html','studio.html','oficina.html','creditos.html','aula.html?lesson='):
    assert link in index, link
assert 'googleapis' not in index and 'googleapis' not in aula and 'googleapis' not in trails, 'fontes devem ser hospedadas no site'
for f in ('shippori-mincho-latin-500-normal','shippori-mincho-latin-700-normal','hanken-grotesk-latin-400-normal','hanken-grotesk-latin-600-normal'):
    assert (ROOT/'assets/fonts'/(f+'.woff2')).exists(), f
assert (ROOT/'assets/fonts/OFL-Shippori-Mincho.txt').exists() and (ROOT/'assets/fonts/OFL-Hanken-Grotesk.txt').exists()
# Cabeçalho e rodapé únicos em sincronia em todas as páginas migradas
r=subprocess.run(['python3',str(ROOT/'tools/stamp_shell.py'),'--check'],capture_output=True,text=True)
assert r.returncode==0, r.stderr
# O aplicativo de aulas mantém o botão oculto que o script referencia e não exibe emoji nos títulos
assert 'id="navhome"' in aula and "c.emoji" not in aula
assert "Number(state.step[c.id]||0)/c.steps.length" in aula, 'barra de progresso de cartas deve contar só etapas concluídas'
assert 'state.checks[checkIds[i]]' in aula
assert '.check-row.done' in (ROOT/'styles/aula.css').read_text('utf-8')
for img in workshop['images']: ET.parse(ROOT/img)
assert 'Smudge' in aula and 'Smudge' in studio
assert 'smudge-projects' in studio and 'dbRead' in studio
assert "courseImg(current,step+1).replace(/^assets\\//,'')" in aula
assert 'webp|svg|png' in studio
assert 'review-pending' in studio and "path.replace(/^assets\\//,'')" in (ROOT/'acervo-revisado.html').read_text('utf-8')
assert 'stabilizer' in studio and 'smoothPoint' in studio
assert 'Referência: ' in studio
assert 'Projeto incompatível' in studio
assert 'function drawContained' in studio
assert 'drawContained(c,im,size,size)' in studio
assert 'Math.min(width/sw,height/sh)' in studio
assert "img.naturalWidth*scale" in aula
assert 'compareArt' in aula and 'compareDialog' in aula
assert 'reportArt' in aula
assert 'category.includes(\'mãos\')' in aula
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
    for name, html in [('index', index), ('aula', aula), ('studio', studio), ('trilhas', trails), ('acervo', local_art), ('oficina', (ROOT/'oficina.html').read_text('utf-8')), ('pranchas', (ROOT/'pranchas.html').read_text('utf-8')), ('aulas-pranchas',(ROOT/'aulas-pranchas.html').read_text('utf-8')), ('revisao', candidate_page)]:
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
