# MangaDojo Atelier 13.3.0 · Smudge Studio

Academia gratuita de desenho mangá com biblioteca de aulas, prática e um editor de desenho independente.

- Academia: https://siriuscraft704.github.io/mangadojo/
- Smudge: https://siriuscraft704.github.io/mangadojo/studio.html
- Galeria de pranchas: https://siriuscraft704.github.io/mangadojo/pranchas.html
- Acervo: https://siriuscraft704.github.io/mangadojo/acervo-revisado.html
- Oficina criativa: https://siriuscraft704.github.io/mangadojo/oficina.html

## Catálogo

Nove aulas e 62 telas de estudo: quatro sequências de animais (36), Mão Aberta (6), duas oficinas de observação com oito imagens de Vijay Verma sob MIT e duas novas aulas experimentais (12 imagens originais de rosto feminino e cabelos ondulados). O Acervo mostra 54 WebP diretamente e permite importação local opcional.

A galeria reúne 79 pranchas de estudo e 7 painéis históricos em tamanho integral, com busca, categorias, ampliação e download. A contagem do catálogo computa apenas as aulas.

A revisão visual retirada da publicação está em `drafts/retired-lessons/`. Os WebP legados permanecem no Git para recuperação e comparação. O artefato do Pages leva apenas os arquivos estáticos do site e as imagens apontadas pelas aulas vigentes.

## Prática e editor

- Trilhas, comparação de etapas, ampliação, checklists e auditoria por imagem.
- Oficina criativa com exercícios em três faixas de estudo, ficha de personagem, roteiro e montagem de páginas de quadrinhos em PNG.
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

Recriar as referências retiradas, ampliar as oficinas de criação, revisar o conteúdo pedagógico com um professor de desenho e testar todo o fluxo em aparelhos Android/iOS e canetas físicas. O Smudge continua sendo um editor raster. Atribuição de recursos externos em `THIRD_PARTY_NOTICES.md`.

## Revisão 13.3 — Upload e publicação das 12 novas imagens

- As 12 imagens WebP de rosto feminino e cabelos ondulados foram **enviadas ao GitHub como blobs binários verificados**, em `assets/review-pending/`, com hashes documentados em `art-review-manifest.json`.
- Duas aulas novas (`lessons/rosto-feminino/` e `lessons/cabelos-ondulados/`) usam os arquivos públicos. As aulas são sinalizadas como **estudos experimentais**, para não esconder limitações anatômicas ou mudanças de perspectiva entre as etapas.
- O catálogo tem **9 aulas e 62 telas**, com **54 WebP** das aulas produzidas, além das 8 referências vetoriais MIT.
- `acervo-revisado.html` apresenta os arquivos públicos sem exigir ZIP; a importação local permanece como alternativa.
- `revisao-candidatos.html` carrega as 12 imagens diretamente do site e permite checklist humano por etapa, notas e exportação JSON.
- As pranchas históricas e lições arquivadas não foram sobrescritas; o fluxo de rollback permanece possível.
- As 12 imagens não foram erroneamente rotuladas como MIT: são criações do projeto; o acervo MIT de Vijay Verma permanece atribuído separadamente.
- O workflow do GitHub Pages executa compilação, verificações estáticas, geometria do Smudge, integridade MIT e auditoria de mídia antes de publicar.

### Revisão ainda necessária

A continuidade de ângulos dos cabelos ondulados e a anatomia final dos rostos devem ser avaliadas por um desenhista. As novas aulas estão acessíveis como estudos, não como referência anatômica certificada. A versão atual não afirma eliminar todos os problemas do acervo histórico.
