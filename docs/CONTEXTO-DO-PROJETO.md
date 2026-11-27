# MangaDojo · Contexto para uma nova conversa

Gerado em 27/11/2026. Leia este arquivo e `docs/REPAGINACAO.md` primeiro.

**Stack:** site estático (HTML, CSS, JS), dados em `lessons/*/lesson.json`, build em Python (`tools/build_catalog.py`), publicação no GitHub Pages. **Branch de trabalho:** `claude/claude-code-capabilities-l75ppk` (sem PR; a `main` não foi alterada).

## Estado verificado
- `python3 tools/smoke_test.py` e `node tools/test_visual_geometry.cjs` passam.
- 88 aulas (79 pranchas de estudo e 9 aulas), 141 etapas, 7 categorias, 7 módulos de curso.
- Pacote do Pages: 205 arquivos, sem requisições quebradas.

## Comandos
- `python3 tools/build_catalog.py` (valida aulas e currículo, gera `catalog.generated.*` e `curso.generated.js`)
- `python3 tools/package_pages.py PASTA` e servir a pasta para conferir o que o Pages publica

## Decisões já tomadas
- `trilhas.html` virou o **Curso** e mantém o endereço antigo (testes e links dependem dele).
- Menu principal com 4 itens; Auditoria e telas de revisão ficam no rodapé.
- Identidade: vinho e rosa (`--md-plum`, `--md-rose`), Playfair Display e Inter, definidas em `styles/site.css`.

## Pendências, em ordem
1. Fase 2 (padronizar cabeçalho, rodapé e CSS das demais páginas).
2. Fase 3 (página própria da aula).
3. Fase 4 (nível Avançado, SEO, acessibilidade, teste em iOS e Android).
4. Fase 5 (revisão pedagógica e conteúdo).

## Regras de trabalho
- Não substituir imagens por protótipos inferiores; mudanças de arte passam pela homologação (`art-review-manifest.json`).
- Autoria e licença de cada asset ficam registradas em `THIRD_PARTY_NOTICES.md`.
- Um objetivo por conversa; ao terminar, commit e push.

## Ecossistema
Projetos irmãos do mesmo dono, todos no GitHub: `crazydale-tcg`, `HGW-Idle`, `crazydale-rpg`, `drax-hgw`, `hgwcore`, `hgw-rpg-minecraft`, `veloryansongs`. O MangaDojo é o único público.
