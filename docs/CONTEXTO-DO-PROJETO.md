# MangaDojo · Contexto para uma nova conversa

Gerado em 27/11/2026. Leia este arquivo e `docs/REPAGINACAO.md` primeiro.

**Stack:** site estático (HTML, CSS, JS), dados em `lessons/*/lesson.json`, build em Python (`tools/build_catalog.py`), publicação no GitHub Pages. **Branch de trabalho:** `claude/claude-code-capabilities-l75ppk` (sem PR; a `main` não foi alterada).

## Estado verificado
- `python3 tools/smoke_test.py` e `node tools/test_visual_geometry.cjs` passam.
- 88 aulas (79 pranchas de estudo e 9 aulas), 141 etapas, 7 categorias, 7 módulos de curso.
- Pacote do Pages: 220 arquivos. As 12 páginas foram percorridas no pacote real em 1360 e 390 px: 0 requisições quebradas, 0 chamadas externas, 0 erros de JavaScript e 0 rolagem horizontal.

## Comandos
- `python3 tools/build_catalog.py` (valida aulas e currículo, gera `catalog.generated.*` e `curso.generated.js`)
- `python3 tools/stamp_shell.py [--check]` (cabeçalho e rodapé únicos)
- `python3 tools/package_pages.py PASTA` e servir a pasta para conferir o que o Pages publica

## Decisões já tomadas
- `trilhas.html` é o **Curso** (endereço mantido). `index.html` é a **home** nova; o aplicativo de aulas está em `aula.html`.
- Menu principal com 4 itens (Curso, Pranchas, Oficina, Smudge); Auditoria e telas de revisão ficam no rodapé.
- Identidade **"Tinta e papel"** (ver `DESIGN.md`): variáveis e fontes em `styles/tokens.css`. Fontes hospedadas, sem Google Fonts.
- Cabeçalho e rodapé têm fonte única: edite `tools/stamp_shell.py` e rode `python3 tools/stamp_shell.py`.

## Pendências, em ordem
1. Fase 3 (página própria da aula; consolidar o CSS histórico por baixo de `aula-tinta.css`).
2. Escolher a licença do código (não há `LICENSE`).
3. Fase 4 (nível Avançado, SEO, acessibilidade, teste em iOS e Android).
4. Fase 5 (revisão pedagógica e conteúdo).

## Regras de trabalho
- Não substituir imagens por protótipos inferiores; mudanças de arte passam pela homologação (`art-review-manifest.json`).
- Autoria e licença de cada asset ficam registradas em `THIRD_PARTY_NOTICES.md`.
- Um objetivo por conversa; ao terminar, commit e push.

## Ecossistema
Projetos irmãos do mesmo dono, todos no GitHub: `crazydale-tcg`, `HGW-Idle`, `crazydale-rpg`, `drax-hgw`, `hgwcore`, `hgw-rpg-minecraft`, `veloryansongs`. O MangaDojo é o único público.
