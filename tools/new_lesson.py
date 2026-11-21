#!/usr/bin/env python3
"""Gera modelo de nova aula; substitua as imagens antes de publicar."""
from pathlib import Path
import json, re, sys
slug=sys.argv[1] if len(sys.argv)>1 else 'nova-aula'
if not re.fullmatch(r'[a-z0-9-]+',slug):sys.exit('Use apenas letras minúsculas, números e hífens.')
p=Path(__file__).resolve().parents[1]/'lessons'/slug
p.mkdir(parents=True,exist_ok=False)
obj={'id':slug,'name':'Título da nova aula','category':'Personagens','style':'Mangá','level':'Iniciante','min':20,'emoji':'✏️','author':'MangaDojo','contentLicense':'Original','steps':[['Construção','Desenhe as formas básicas.',['Faça as guias']],['Refinamento','Refine volumes e proporções.',['Adicione detalhes']],['Arte-final','Finalize com contornos limpos.',['Faça o acabamento']]],'images':[f'assets/{slug}-{i}.webp' for i in range(1,4)]}
(p/'lesson.json').write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Criado',p,'; acrescente as 3 imagens e execute python tools/build_catalog.py')
