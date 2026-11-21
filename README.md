# MangaDojo Atelier 13.0 · Smudge Studio

Academia gratuita de desenho mangá com biblioteca de aulas, prática e um editor de desenho independente.

- Academia: https://siriuscraft704.github.io/mangadojo/
- Smudge: https://siriuscraft704.github.io/mangadojo/studio.html
- Acervo: https://siriuscraft704.github.io/mangadojo/acervo-revisado.html
- Oficina criativa: https://siriuscraft704.github.io/mangadojo/oficina.html

## Catálogo

Sete aulas e 50 telas, sendo quatro sequências de animais (36 etapas), a Mão Aberta em revisão 2 (6 etapas) e duas oficinas com oito referências de Vijay Verma sob licença MIT. O Acervo oferece as 42 imagens novas por acesso direto e conserva a importação local do pacote de animais.

A revisão visual retirada da publicação está em `drafts/retired-lessons/`. Os WebP legados permanecem no Git para recuperação e comparação. O artefato do Pages leva apenas os arquivos estáticos do site e as imagens apontadas pelas aulas vigentes.

## Prática e editor

- Trilhas, comparação de etapas, ampliação, checklists e auditoria por imagem.
- Oficina criativa com exercícios em três faixas de estudo, ficha de personagem e roteiro de quadrinhos.
- Smudge raster com estabilização, pressão de caneta, seleção por laço, deslocamento, rotação e escala da seleção e máscaras reversíveis por camada.
- Projetos de desenho usam IndexedDB com fallback, importam projetos anteriores e exportam PNG e JSON. Os dados são locais ao navegador.

## Desenvolvimento e publicação

```sh
python tools/build_catalog.py
python tools/smoke_test.py
python tools/verify_mit_assets.py
node tools/test_visual_geometry.cjs
python tools/media_audit.py
```

O workflow publica a branch `main` no GitHub Pages. A nova pasta do artefato é preparada com `python tools/package_pages.py CAMINHO`. Rodar um servidor local na pasta do artefato permite testar o mesmo conjunto de arquivos que o Pages publica.

## Trabalho em aberto

Recriar as referências retiradas, ampliar as oficinas de criação, revisar o conteúdo pedagógico com um professor de desenho e testar todo o fluxo em aparelhos Android/iOS e canetas físicas. A oficina de quadrinhos salva um roteiro textual e o Smudge continua sendo um editor raster. Atribuição de recursos externos em `THIRD_PARTY_NOTICES.md`.
