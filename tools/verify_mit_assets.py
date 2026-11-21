#!/usr/bin/env python3
"""Verify every third-party MIT asset against its verified Git blob checksum.

Do not infer that arbitrary GitHub image files inherit the repository's code license.
"""
from pathlib import Path
import hashlib
import json
import xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
manifest=json.loads((ROOT/'assets/mit-asset-manifest.json').read_text('utf-8'))
assert manifest['schema']==1 and len(manifest['assets'])==8
notices=(ROOT/'THIRD_PARTY_NOTICES.md').read_text('utf-8')
assert 'Copyright (c) 2015 vijay verma' in notices
assert 'Permission is hereby granted' in notices
paths=set()
for entry in manifest['assets']:
    path=ROOT/entry['path']
    assert path.is_file(),entry['path']
    assert entry['path'].startswith('assets/mit-')
    assert entry['path'] not in paths,'Repetido: '+entry['path']
    paths.add(entry['path'])
    assert entry['license']=='MIT' and entry['author']=='Vijay Verma'
    assert entry['source'].startswith('https://github.com/realvjy/illlustrations/blob/develop/')
    assert entry['path'].split('/')[-1] in notices
    content=path.read_bytes()
    blob=hashlib.sha1(b'blob '+str(len(content)).encode()+b'\0'+content).hexdigest()
    assert blob==entry['git_blob_sha1'],f"Arte modificada sem revisão: {entry['path']}"
    node=ET.fromstring(content)
    assert node.tag.endswith('svg')
    forbidden=(b'<script',b'<foreignObject',b'onload=',b'onerror=')
    assert not any(t in content for t in forbidden),entry['path']
print(f"PASS: {len(paths)} arquivos MIT íntegros, com origem e licença verificadas")
