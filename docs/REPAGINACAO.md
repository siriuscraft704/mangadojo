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

## Fase 2 · padronização das páginas (próxima)
1. Migrar o cabeçalho e o rodapé de **todas** as páginas para `site.css` (hoje cada uma tem o seu: `index`, `pranchas`, `aulas-pranchas`, `oficina`, `acervo-revisado`, `creditos`, `studio`).
2. Consolidar os CSS históricos (`atelier.css`, `dojo-identity.css`, `dojo-home.css`, `dojo-subpages.css`) e o CSS inline do `index.html` (50 KB), com comparação visual automatizada antes e depois, como já indica o `DESIGN.md`.
3. Renomear "Biblioteca de aulas" e "Aula atual" na home para os mesmos termos do Curso.

## Fase 3 · página da aula
Reorganizar a aula (hoje dentro do `index.html`) em uma página própria: título, objetivo, etapas numeradas, checklist, botão "Próxima aula do módulo" e "Marcar como concluída". Mesmo layout no celular.

## Fase 4 · profissionalização
- Nível **Avançado** (hoje só há Iniciante e Intermediário) e uma sequência de revisão.
- SEO e compartilhamento: títulos e descrições por página, imagem de pré-visualização, `sitemap.xml`, `robots.txt`.
- Acessibilidade e desempenho: Lighthouse nas principais páginas, contraste, teclado, teste em iOS Safari e Android.
- Certificado simples de conclusão de módulo (opcional).

## Fase 5 · conteúdo e monetização
- Revisão pedagógica com um professor de desenho, como já indica o README.
- Recriar as referências retiradas (`drafts/retired-lessons/`).
- Monetização sugerida: doações, material complementar pago ou curso presencial. Qualquer asset externo exige autoria e licença registradas.

## Limites conhecidos desta fase
- A **ordem dos módulos e os textos de resumo são uma proposta**; o conteúdo pedagógico das aulas não foi alterado nem revisado.
- "44 h de prática" é a soma dos minutos declarados em cada aula, não uma medição.
- O hero usa um recorte de `assets/academia/referencia.webp` (`hero-curso.webp`), que tem resolução modesta; vale substituir por arte original em alta resolução.
- Páginas além do Curso ainda têm seus cabeçalhos próprios até a Fase 2.
