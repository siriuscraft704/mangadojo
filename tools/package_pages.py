#!/usr/bin/env python3
"""Build a GitHub Pages artifact containing only the active public site."""
import json
from pathlib import Path
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]
destination = Path(sys.argv[1]).resolve()
destination.mkdir(parents=True, exist_ok=False)

catalog = (ROOT / 'catalog.generated.js').read_text(encoding='utf-8')
lessons = json.loads(catalog.split('window.MANGADOJO_LESSONS=', 1)[1].strip().removesuffix(';'))
public_files = {
    '.nojekyll', 'index.html', 'studio.html', 'trilhas.html', 'oficina.html',
    'auditoria-imagens.html', 'homologacao-artes.html', 'acervo-revisado.html',
    'creditos.html', 'pranchas.html', 'pranchas.json', 'catalog.generated.js', 'catalog.generated.json',
    'manifest.webmanifest', 'sw.js', 'THIRD_PARTY_NOTICES.md',
    'assets/mangadojo-mark.svg', 'assets/smudge-mark.svg',
    'assets/mit-asset-manifest.json', 'styles/atelier.css', 'styles/smudge.css',
    'scripts/smudge-editing.js', 'scripts/oficina-art.js',
}
public_files.update(image for lesson in lessons for image in lesson['images'])

boards = json.loads((ROOT / 'pranchas.json').read_text(encoding='utf-8'))
public_files.update(board['image'] for board in boards)

for relative in sorted(public_files):
    source = ROOT / relative
    target = destination / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, target)
print(f'Pages artifact: {len(public_files)} files')
