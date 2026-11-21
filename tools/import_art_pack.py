#!/usr/bin/env python3
"""Stage only SHA256-pinned WebP candidates from a GitHub issue attachment ZIP."""
from __future__ import annotations
import hashlib
import io
import json
from pathlib import Path
import sys
from urllib.parse import urlparse
from urllib.request import Request,urlopen
from zipfile import ZipFile,BadZipFile

ROOT=Path(__file__).resolve().parents[1]
MANIFEST=ROOT/'art-review-manifest.json'
DEST=ROOT/'assets'/'review-pending'

def main(source_url):
    parsed=urlparse(source_url)
    if parsed.scheme!='https' or parsed.hostname!='github.com' or not parsed.path.startswith('/user-attachments/'):
        raise ValueError('Apenas anexos ZIP do GitHub são aceitos')
    with urlopen(Request(source_url,headers={'User-Agent':'MangaDojo-ArtImporter/1.0'}),timeout=45) as response:
        data=response.read(10*1024*1024+1)
    if len(data)>10*1024*1024: raise ValueError('ZIP acima de 10 MB')
    expected=json.loads(MANIFEST.read_text('utf8'))['candidates']
    by_name={entry['name']:entry for entry in expected}
    if len(by_name)!=12: raise ValueError('Manifesto deve conter 12 candidatos')
    try: archive=ZipFile(io.BytesIO(data))
    except BadZipFile as exc: raise ValueError('Arquivo não é ZIP') from exc
    found={}
    with archive:
        entries=archive.infolist()
        if len(entries)>90 or sum(item.file_size for item in entries)>10*1024*1024:
            raise ValueError('ZIP contém dados demais')
        for item in entries:
            name=Path(item.filename).name
            if name not in by_name: continue
            if name in found or item.file_size>256*1024:
                raise ValueError('Arquivo repetido ou grande demais: '+name)
            content=archive.read(item)
            if content[:4]!=b'RIFF' or content[8:12]!=b'WEBP':
                raise ValueError('WebP inválido: '+name)
            if hashlib.sha256(content).hexdigest()!=by_name[name]['sha256']:
                raise ValueError('Hash divergente: '+name)
            found[name]=content
    missing=set(by_name)-set(found)
    if missing: raise ValueError('Faltam arquivos: '+', '.join(sorted(missing)))
    DEST.mkdir(parents=True,exist_ok=True)
    for name,content in sorted(found.items()):
        (DEST/name).write_bytes(content)
    print('STAGED',len(found),'verified candidate images.')
    print('No images enter active lessons or the Pages artifact automatically.')

if __name__=='__main__':
    if len(sys.argv)!=2: raise SystemExit('Uso: python tools/import_art_pack.py URL_DO_ANEXO_GITHUB')
    try: main(sys.argv[1])
    except Exception as exc: raise SystemExit('IMPORT FAILED: '+str(exc))
