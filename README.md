# MangaDojo Atelier 13.6.0 · Smudge Studio

Academia gratuita de desenho mangá com biblioteca de aulas, prática e um editor de desenho independente.

- Academia: https://siriuscraft704.github.io/mangadojo/
- Smudge: https://siriuscraft704.github.io/mangadojo/studio.html
- Galeria de pranchas: https://siriuscraft704.github.io/mangadojo/pranchas.html
- Acervo: https://siriuscraft704.github.io/mangadojo/acervo-revisado.html
- Oficina criativa: https://siriuscraft704.github.io/mangadojo/oficina.html

## Catálogo

Nove aulas e 62 telas de estudo: quatro sequências de animais (36), Mão Aberta (6), duas oficinas de observação com oito imagens de Vijay Verma sob MIT e duas novas aulas experimentais (12 imagens originais de rosto feminino e cabelos ondulados). O Acervo mostra 54 WebP diretamente e permite importação local opcional.

A galeria reúne 79 pranchas ligadas às aulas, 20 pranchas de prática guiada e 7 painéis históricos em tamanho integral. A [coleção de prática](https://siriuscraft704.github.io/mangadojo/pranchas.html?colecao=pratica) inclui dicas de ferramentas, exercícios e critérios de revisão. As atividades complementares ficam na galeria.

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

## Novidade 13.4 — 79 aulas de pranchas inteiras

- A [biblioteca de 79 aulas](https://siriuscraft704.github.io/mangadojo/aulas-pranchas.html) transforma cada prancha ilustrada de estudo já hospedada no projeto em uma **aula individual**, com ID `estudo-prancha-NN`, sua própria definição em `lessons/`, atividades de construção e checklist.
- As 7 imagens de história visual não foram convertidas em aulas de desenho.
- O catálogo contém agora **88 aulas e 141 telas**: 9 aulas anteriores (62 telas) mais 79 aulas de prancha integral (uma tela cada).
- Nenhum arquivo foi recortado ou esticado para construir as novas aulas; as imagens WebP de `assets/pranchas/` são reaproveitadas diretamente na resolução integral do repositório (de 1024×1536 a 1774×887, conforme o arquivo).
- O visualizador da aula utiliza layout de largura inteira, proporção específica de cada prancha, zoom e download do **arquivo WebP original**, evitando redução forçada para 900×1000 na exportação destas aulas.
- As pranchas internas não foram divididas em passos falsos. Os exercícios de leitura, construção e acabamento fazem referência à **mesma imagem completa**.
- O teste `tools/media_audit.py` verifica individualmente dimensões reais e resolução mínima das 79 fontes; `tools/smoke_test.py` confere IDs, correspondência com o atlas, integridade de paths e empacotamento.
- **Limite de validação:** integridade e enquadramento na interface foram testados automaticamente, mas a anatomia e possíveis cortes que já existiam na ilustração original ainda exigem aprovação artística individual. Não declarar todas as 79 pranchas anatomicamente corretas.

## 13.5 — identidade editorial MangaDojo + Smudge

- Identidade original: ameixa escura `#4B1E3D`, tinta `#171418`, papel marfim `#F7EFDF`, rosa antigo `#C8798C` e dourado suave `#C9A86A`.
- Logotipos vetoriais autorais para MangaDojo (portal e pincel) e Smudge (S em pincelada), fontes Playfair Display e Inter com fallbacks offline.
- Texturas e ornamentos SVG locais; cabeçalho hero apresenta a prancha original 29 sem corte.
- Arquivos de identidade isolados em `styles/dojo-identity.css`, `styles/smudge-identity.css` e `styles/dojo-subpages.css`; reversão simples sem reescrever a estrutura.
- Layout e ordem das 88 aulas, 141 telas, identificadores e dados de progresso permanecem inalterados. O Smudge mantém todas as ferramentas e geometria.

## 13.6 — entrada da Academia

- A página inicial segue a referência aprovada, com navegação superior, panorama ilustrado, acesso às 79 pranchas completas, seis categorias, aulas em destaque e acesso ao Smudge.
- Os destaques são atalhos para aulas do catálogo. A ordem das 88 aulas, suas fontes de imagem e os registros de progresso usam os mesmos dados e identificadores.
