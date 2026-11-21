# MangaDojo Atelier 13.2.0 · Smudge Studio

Academia gratuita de desenho mangá com biblioteca de aulas, prática e um editor de desenho independente.

- Academia: https://siriuscraft704.github.io/mangadojo/
- Smudge: https://siriuscraft704.github.io/mangadojo/studio.html
- Galeria de pranchas: https://siriuscraft704.github.io/mangadojo/pranchas.html
- Acervo: https://siriuscraft704.github.io/mangadojo/acervo-revisado.html
- Oficina criativa: https://siriuscraft704.github.io/mangadojo/oficina.html

## Catálogo

Sete aulas e 50 telas, sendo quatro sequências de animais (36 etapas), a Mão Aberta em revisão 2 (6 etapas) e duas oficinas com oito referências de Vijay Verma sob licença MIT. O Acervo oferece as 42 imagens novas por acesso direto e conserva a importação local do pacote de animais.

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

## Revisão 13.2 — Imagens de rosto e cabelo

- O catálogo oficial permanece com **7 aulas / 50 etapas**; 42 imagens WebP novas já estão na pasta `assets/`.
- O pacote original de 48 etapas contém **12 imagens adicionais de rosto feminino e cabelos ondulados**, catalogadas como **candidatas**, nunca como aulas aprovadas automaticamente.
- `acervo-revisado.html` importa 48 imagens em ZIP ou WebP para armazenamento local (IndexedDB). Mostra as 12 candidatas em uma seção distinta, com abertura no Smudge.
- `revisao-candidatos.html` apresenta comparador entre etapas, checklist anatômico de quatro critérios e exportação JSON da avaliação.
- `art-review-manifest.json` fixa os hashes SHA-256 das candidatas; a automação `.github/workflows/importar-artes.yml` recebe o ZIP anexado à **issue #2** e coloca as imagens apenas em `assets/review-pending/`.
- O workflow do Pages não incorpora `assets/review-pending/`; estas imagens só serão publicadas quando aprovadas por revisão humana e vinculadas a aulas.
- Nenhum arquivo legado foi apagado nesta versão. O acervo histórico permanece em `drafts/retired-lessons/` para eventual reconstrução artística.
- Conteúdo criado nesta conversa não foi apresentado como MIT: a licença MIT das oito imagens de Vijay Verma é separada e continua preservada em `THIRD_PARTY_NOTICES.md`.

### Como inserir os 12 WebP no repositório

Baixe o pacote `MangaDojo_12_Artes_Revisao_GitHub.zip` desta conversa e anexe-o em um comentário na [issue #2](https://github.com/siriuscraft704/mangadojo/issues/2) usando a conta proprietária. O upload é executado no ambiente do GitHub, sem digitar token no site do MangaDojo. Os arquivos serão armazenados como candidatos, sem publicação automática nas aulas.
