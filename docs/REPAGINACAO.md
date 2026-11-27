# Repaginação do MangaDojo · plano por fases

Objetivo: um site de curso profissional, mas fácil de entender. Princípio: **um sistema visual único** (`styles/site.css`), **dados padronizados** e **uma estrutura de curso clara**. Este documento é a fonte para conversas dedicadas ao projeto.

## Fase 1 · feita
- **Dados padronizados:** 11 categorias viraram 7 (`tools/normalize_categories.py`). O `build_catalog.py` agora falha se alguma categoria ficar sem módulo ou algum módulo apontar para categoria inexistente.
- **Currículo como dado:** `curso.json` define 7 módulos (Fundamentos, Rostos, Cabelos, Mãos e pés, Corpo, Animais, Quadrinhos) com resumo e resultado esperado. O build gera `curso.generated.js`.
- **Sistema visual:** `styles/site.css` (tokens, cabeçalho, rodapé, botões, selos, cartões, progresso) e `styles/curso.css`.
- **Página do Curso** (`trilhas.html`, mesmo endereço de antes): cobre as **88 aulas** (a versão anterior cobria 9), com "continue de onde parou", progresso por módulo, tempo estimado e três passos de "como funciona".
- **Menu enxuto:** Academia, Curso, Pranchas, Smudge. "Auditoria" saiu do menu e foi para o rodapé ("Equipe e revisão").
- **Offline e publicação:** Service Worker (cache v35) e empacotador do Pages incluem os arquivos novos.
- **Verificado:** `smoke_test.py` e `test_visual_geometry.cjs` passam; o pacote do Pages (205 arquivos) carrega sem requisições quebradas nem erros de JavaScript.

## Fase 2 · padronização e nova identidade · feita
- **Identidade "Tinta e papel"** (ver `DESIGN.md`): papel quente, tinta quase preta e um único vermelho de carimbo; réguas finas no lugar de sombras; cantos quase retos; sem degradês decorativos, sem pílulas e sem emojis como ícones. Fontes **Shippori Mincho** e **Hanken Grotesk**, hospedadas no site (OFL-1.1). Nenhuma página chama o Google Fonts.
- **Home nova** (`index.html`): capa editorial com ilustração real, o método em seis passos (aula do gato, 10 etapas), índice dos sete módulos preenchido pelos dados, pranchas, Smudge e perguntas frequentes. Os números vêm do catálogo.
- **Cabeçalho e rodapé únicos:** `tools/stamp_shell.py` carimba o mesmo cabeçalho e rodapé em 13 páginas; o teste de fumaça falha se alguma sair de sincronia.
- **Aplicativo de aulas** movido para `aula.html` (a home ficou livre para ser vitrine). Mesmo sistema visual; emojis removidos dos títulos (só na exibição).
- **Smudge Studio** no mesmo sistema (tema escuro de tinta, vermelho de carimbo nas ferramentas ativas), sem emojis nos botões. Verificado desenhando um traço de verdade.
- **Páginas secundárias** (pranchas, oficina, acervo, créditos, auditoria, homologação, candidatos) em `styles/subpagina.css`.
- **Teste de integridade do pacote:** toda referência local de cada página, todo `url()` e `@import` de CSS devem existir no artefato do Pages. Foi esse teste que pegou três CSS ausentes do pacote, que deixariam o site publicado sem estilo.

## Fase 3 · correções de comportamento encontradas na revisão · parte feita
- **Feito:** a barra de progresso dos cartões da biblioteca contava a etapa 1 como já feita, então toda prancha de uma etapa aparecia 100% sem ter sido iniciada. Agora conta só etapas concluídas.
- **Feito:** os botões "− Zoom" e "＋ Zoom" do Smudge ficaram "Reduzir zoom" e "Ampliar zoom"; a visibilidade de camada ganhou `aria-pressed`.
- **Pendente:** página da aula separada do aplicativo da biblioteca (hoje `aula.html` ainda reúne biblioteca e estudo), com "próxima aula do módulo" e "marcar como concluída".

## Fase 4 · profissionalização
- Nível **Avançado** (hoje só há Iniciante e Intermediário) e uma sequência de revisão.
- SEO e compartilhamento: títulos e descrições por página, imagem de pré-visualização, `sitemap.xml`, `robots.txt`.
- Acessibilidade e desempenho: Lighthouse nas principais páginas, contraste, teclado, teste em iOS Safari e Android.
- Certificado simples de conclusão de módulo (opcional).

## Fase 5 · conteúdo e monetização
- Revisão pedagógica com um professor de desenho, como já indica o README.
- Recriar as referências retiradas (`drafts/retired-lessons/`).
- Monetização sugerida: doações, material complementar pago ou curso presencial. Qualquer asset externo exige autoria e licença registradas.

## Limites conhecidos
- A **ordem dos módulos e os textos de resumo são uma proposta**; o conteúdo pedagógico das aulas não foi alterado nem revisado.
- "44 h de prática" é a soma dos minutos declarados em cada aula, não uma medição.
- O hero usa um recorte de `assets/academia/referencia.webp` (`hero-curso.webp`), que tem resolução modesta; vale substituir por arte original em alta resolução.
- O `aula.html` mantém o HTML e o CSS históricos por baixo da nova camada (`aula-tinta.css`, com `!important`); consolidar isso é trabalho da Fase 3.
- O Smudge e as páginas internas receberam só a camada visual; a lógica não mudou.
- Não há `LICENSE` na raiz do repositório. Decisão do dono: escolher a licença do código (as imagens têm licenças próprias, listadas em `creditos.html`).
- Sem teste em aparelhos reais (iOS e Android) nem em Lighthouse; as verificações foram com Chromium em 1360 e 390 px.
