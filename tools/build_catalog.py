#!/usr/bin/env python3
"""Valida aulas, fotos e compila um catálogo para acesso local e GitHub Pages."""
from pathlib import Path
import json, sys
ROOT=Path(__file__).resolve().parents[1]
LESSONS=ROOT/'lessons'
items=[]
errors=[]
for path in sorted(LESSONS.glob('*/lesson.json')):
    try:
        data=json.loads(path.read_text('utf-8'))
        required=['id','name','category','style','level','min','emoji','steps','images']
        missing=[x for x in required if x not in data]
        if missing: raise ValueError('Campos ausentes: '+', '.join(missing))
        if data['id']!=path.parent.name: raise ValueError('id difere da pasta')
        if not isinstance(data['steps'],list) or not (3<=len(data['steps'])<=60):raise ValueError('Aula deve ter entre 3 e 60 etapas')
        if len(data['steps'])!=len(data['images']):raise ValueError('Quantidade de imagens diferente das etapas')
        if any(not isinstance(s,list) or len(s)!=3 or not isinstance(s[2],list) for s in data['steps']):raise ValueError('Etapa deve ser [título, instrução, [checklist]]')
        for img in data['images']:
            src=(ROOT/img).resolve()
            if not src.is_relative_to(ROOT) or not src.is_file():raise ValueError('Imagem inválida ou ausente: '+img)
            if src.suffix.lower() not in ('.webp','.png','.jpg','.jpeg','.svg'):raise ValueError('Formato não permitido: '+img)
        items.append(data)
    except Exception as exc: errors.append(str(path.relative_to(ROOT))+': '+str(exc))
ids=[x['id'] for x in items]
if len(ids)!=len(set(ids)):errors.append('IDs de aulas duplicados')
if errors:
    print('\n'.join('ERRO: '+x for x in errors),file=sys.stderr)
    sys.exit(1)
text=json.dumps(items,ensure_ascii=False,separators=(',',':'))
(ROOT/'catalog.generated.js').write_text('/* Arquivo compilado: edite lessons/ e não este arquivo. */\nwindow.MANGADOJO_LESSONS='+text+';\n',encoding='utf-8')
(ROOT/'catalog.generated.json').write_text(json.dumps({'lessons':len(items),'stages':sum(len(x['steps']) for x in items),'categories':sorted(set(x['category'] for x in items))},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(f'MangaDojo: {len(items)} aulas e {sum(len(x["steps"]) for x in items)} etapas validadas.')
