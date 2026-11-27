#!/usr/bin/env python3
"""Unifica categorias duplicadas em lessons/*/lesson.json (11 -> 7). Idempotente."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
MERGE={'Animais e criaturas':'Animais','Cabelos e penteados':'Cabelos','Mãos e anatomia':'Mãos e pés','Rostos e expressões':'Rostos e olhos'}
changed=0
for path in sorted((ROOT/'lessons').glob('*/lesson.json')):
    text=path.read_text('utf-8');data=json.loads(text)
    new=MERGE.get(data.get('category'))
    if not new:continue
    data['category']=new
    indent=2 if text.startswith('{\n  "') else None
    path.write_text(json.dumps(data,ensure_ascii=False,indent=indent,separators=(',',':') if indent is None else None)+('\n' if text.endswith('\n') else ''),'utf-8')
    changed+=1
print(f'{changed} aulas atualizadas')
