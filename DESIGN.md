# DESIGN.md — MangaDojo Atelier / Smudge
Última revisão: 2026-11-27 (identidade "Tinta e papel").

## Identidade atual (27/11/2026)
Substitui o tema vinho e rosa com degradês. Princípios: **papel quente, tinta quase preta e um único vermelho de carimbo**; réguas finas em vez de sombras; cantos quase retos; sem pílulas, sem degradês decorativos e sem emojis como ícones; títulos em mincho e texto em grotesca.
- Cores: papel `#F3EEE3`, giz `#FBF8F1`, tinta `#16130F`, grafite `#4A443B`, carimbo `#B83A26`. Contrastes verificados (WCAG AA): tinta/papel 16:1, vermelho/papel 4,9:1.
- Fontes hospedadas no site (OFL-1.1): **Shippori Mincho** (títulos) e **Hanken Grotesk** (texto). Definidas em `styles/tokens.css`. Nenhuma fonte externa é carregada.
- Sistema: `styles/tokens.css` (variáveis e fontes), `styles/site.css` (cabeçalho, rodapé, botões, réguas, etiquetas), `styles/home.css`, `styles/curso.css`, `styles/subpagina.css`, `styles/aula.css` (aplicativo de aulas, reescrito do zero) e `styles/studio-tinta.css` (editor, tema escuro). O CSS histórico (`atelier`, `dojo-identity`, `dojo-home`) foi removido.
- **Auditoria do que é renderizado:** `node tools/audit_visual.cjs` (precisa do Playwright) falha se uma página usar fonte fora do sistema, texto com matiz fora da paleta ou rolagem horizontal. As 12 páginas passam.
- **Capa da home:** composição de página de mangá (grade preta com calhas inclinadas), com a ilustração de anime em `assets/academia/hero-anime.webp` (recorte e ampliação de `referencia.webp`, de resolução modesta; trocar por arte original em alta resolução).
- Cabeçalho e rodapé têm **fonte única** em `tools/stamp_shell.py`; o teste de fumaça falha se uma página sair de sincronia.

---
## Registro anterior (21/11/2026), mantido para referência
Última revisão: 2026-11-21. Fonte observada: https://siriuscraft704.github.io/mangadojo/ (captura móvel 390×844 pelo Firecrawl), código `index.html`, `studio.html`, `styles/atelier.css` e `styles/smudge.css`.

## Identidade existente (observada, não proposta)
- **MangaDojo:** academia de desenho, fundo claro e painéis brancos; marca escura com cor coral.
- **Smudge:** estúdio de desenho com fundo escuro e área central branca.
- Cores observadas: primária `#C65F56`, secundária `#353945`, fundo `#FBF9F5`, texto `#20222C`, link `#9C4D43`. Valores recolhidos de branding da página publicada; tokens efetivos variam por componente.
- Hierarquia: Georgia nos títulos editoriais e system-ui em controles/legendas. Isso é proposital; manter **duas famílias principais**, sem misturar fontes decorativas em conteúdo.
- Controles primários arredondados em torno de 13px; componentes de navegação e cartões em 12px-18px.

## Componentes e comportamento verificados
1. Menu lateral no desktop e cabeçalho compacto no mobile.
2. Catálogo com filtros por categoria, nível e conclusão, cards com imagem preservada via `contain`.
3. Visualizador de aula: modo Ler e Rolar por padrão; Desenhar opcional, imagem sem ampliação de recorte; zoom independente.
4. Comparador: etapas lado a lado, inclusive em largura ~390 px; legendas e proporções preservadas.
5. Link da aula para auditoria de ilustrações com busca filtrada; registro local de defeitos e exportação JSON.
6. Smudge: controles de pincéis, camadas, estabilizador, modo de rolagem/desenho, exportação; importação de imagens via desenho proporcional.

## Diretrizes editoriais para novas artes (propostas)
- Retratos: reservar margem visual de 8%–12% em torno da área essencial para evitar cortes na origem.
- Mãos: mostrar cinco dedos corretos, articulações proporcionais, sobreposições coerentes e pose idêntica entre etapas.
- Etapas: construção → proporção → volumes → detalhes → line art → acabamento; sem mudança de identidade entre painéis.
- Priorizar uma **prancha por desenho com seis quadros separados** apenas quando a divisão e o enquadramento forem validados na resolução nativa.
- Guardar autoria/licença/fonte de cada asset; um repositório MIT não torna suas imagens automaticamente reutilizáveis.
- Não substituir imagens existentes por protótipos geométricos inferiores. Aprovação visual antes de merge.

## Evolução técnica proposta
- Consolidar os vários CSS históricos de `index.html` somente em uma branch de refatoração com comparação visual automatizada.
- Revisar cabeçalho, tipografia de cards e tamanhos no mobile como componentes de um sistema, não como exceções CSS sucessivas.
- Pincéis com pressão em estudo: Perfect Freehand (MIT), condicionado a benchmark mobile.
- Persistência Smudge em IndexedDB já existe; próximos passos: versionamento de projetos, armazenamento por nome, recuperação e quota.
- Migração futura da área educativa: avaliar Astro Starlight (MIT) em protótipo isolado, sem substituir o site atual.

## Lacunas de validação
- Captura de 390 px observada; outras resoluções e iOS Safari não comprovados.
- Os WebP legados incluem cortes dentro da própria imagem. `object-fit:contain` preserva o que existe; não desenha informação perdida.
- A aprovação de anatomia requer inspeção humana de cada imagem e comparação entre etapas.
- Testes de sintaxe e CI não são equivalentes a revisão pedagógica nem visual integral.
