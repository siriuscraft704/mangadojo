# MangaDojo · Pesquisa de bases open source e plano técnico
Data da análise: 2026-11-21. Critérios: GitHub Pages ou build estático, código reutilizável mediante licença, experiência mobile, modularidade, acessibilidade e ferramentas de desenho/ensino. Os projetos abaixo são **referências técnicas**, não fontes automaticamente licenciadas de ilustrações.

## 13 repositórios examinados

| Projeto | Licença / evidência | Aplicabilidade | Decisão |
|---|---|---|---|
| [Konva](https://github.com/konvajs/konva) | MIT declarada pelo projeto | Canvas, transformações e seleção | Investigar para futura versão estruturada do Smudge |
| [Fabric.js](https://github.com/fabricjs/fabric.js) | MIT (GitHub) | Camadas, seleção e transformações | Referência principal do editor |
| [Excalidraw](https://github.com/excalidraw/excalidraw) | MIT (GitHub) | UI de canvas, atalhos e exportação | Referência de UX e acessibilidade |
| [Perfect Freehand](https://github.com/steveruizok/perfect-freehand) | MIT (GitHub) | Pincel com pressão e curva suave | Proposta de integração de pincéis |
| [Free Drawing](https://github.com/fabienwnklr/free-drawing) | MIT (GitHub) | Canvas infinito, ferramentas e colaboração | Estudo de arquitetura |
| [TUI Image Editor](https://github.com/nhn/tui.image-editor) | MIT (GitHub) | Filtros, recorte e edições raster | Inspiração para ajustes não destrutivos |
| [VitePress](https://github.com/vuejs/vitepress) | MIT (GitHub) | Conteúdo de aulas, navegação e busca | Alternativa futura ao HTML monolítico |
| [Astro Starlight](https://github.com/withastro/starlight) | MIT (GitHub) | Trilhas, documentação, acessibilidade | Melhor candidata para áreas didáticas |
| [Docsify Open Course Starter](https://github.com/hibbitts-design/docsify-open-course-starter-kit) | MIT (GitHub) | Curso em Markdown, navegação | Inspiração para conteúdos escaláveis |
| [Knowledge Core](https://github.com/casoon/knowledge-core) | MIT (GitHub) | Cursos e exercícios em Astro/MDX | Referência de organização curricular |
| [Educenter Hugo](https://github.com/spcorg/pilot-website-template) | MIT (GitHub) | Catálogo educacional | Inspiração de hierarquia de curso |
| [Astro Template](https://github.com/lonestone/astro-template) | MIT (GitHub) | Base estática responsiva | Referência de estrutura |
| [ScrewFast](https://github.com/mearashadowfax/ScrewFast) | MIT (GitHub) | Componentes, seções e estilo refinado | Referência visual e tokens |

### Restrições importantes
- [tldraw](https://github.com/tldraw/tldraw): NÃO presumir que o SDK seja MIT; há licença própria para o SDK, apesar de componentes MIT no repositório.
- [Anime2Sketch](https://github.com/Mukosame/Anime2Sketch): MIT no código, mas isso **não concede direitos** sobre ilustrações usadas como entrada ou dados de treinamento.
- [ProAnatomy](https://github.com/IsaacBh1/ProAnatomy): código MIT e ativos anatômicos com licenças independentes, como CC BY/CC BY-SA; requer atribuição e conferência de cada material.
- Tutoriais de sites especializados como AnimeOutline ou Clip Studio TIPS podem inspirar a metodologia, mas **não autorizam copiar desenhos** sem licença específica.
- Licenças de código não cobrem automaticamente fontes, imagens e materiais de demonstração.

## Decisões técnicas (sem migração destrutiva)
1. **Agora:** preservar HTML estático, JSON por aula, GitHub Actions e IndexedDB do Smudge, realizando correções pontuais com testes.
2. **Curto prazo:** permitir comparador de etapas, sinalização de problemas de fonte, exportação sem distorção, carregamento com aspecto preservado.
3. **Médio prazo:** testar Perfect Freehand isoladamente em um protótipo de brush; não incorporar sem medir desempenho mobile e confirmar licença em NOTICE.
4. **Longo prazo:** avaliar Astro Starlight ou VitePress em branch de protótipo, com migração incremental do catálogo e testes de regressão; não reconstruir o site inteiro sem prova de melhoria.
5. **Qualidade artística:** toda nova arte deve preservar pose/identidade, anatomia plausível e bordas completas. Ausência das partes no arquivo de origem exige ilustração nova, não CSS.
6. **Imagens externas:** somente incorporar com evidência do autor, URL, licença específica, atribuição e registros de transformações; não usar datasets com licença ambígua.

## Skills e ferramentas disponíveis/recomendadas
- **GitHub**: versionamento, documentação, revisão de código, branch de homologação e Actions.
- **Firecrawl deep-research**: investigar repositórios, permissões de uso e referências educativas.
- **Design (website design extraction)**: transformar referências visuais verificadas em DESIGN.md sem copiar artes.
- **Context7**: consultar APIs atualizadas das bibliotecas antes de integrar no editor.
- **Figma**: protótipo visual editável de componentes/layout antes de substituir a UI.
- **Adobe/Photoshop e Canva**: trabalhar composição, margens e acabamento de ativos que tenham direitos adequados; não corrige automaticamente anatomia incorreta.
- **Testes com Node/Python no GitHub Actions**: barreiras automáticas antes da publicação.

## Critérios de aceite para release
- Testes de catálogo, HTML/JS, integridade de imagens e dimensões passam.
- Nenhum SVG provisório com qualidade inferior substitui WebP original.
- Proporção de referências preservada na aula, importação do Smudge e exportação.
- Comparação entre etapas funcional, inclusive em viewport móvel.
- Deploy GitHub Pages concluído com sucesso no commit mais recente.
- Revisão visual humana de anatomia e arte final permanece distinta dos testes automáticos.
