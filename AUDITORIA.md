# Auditoria MangaDojo 8.0 — 20/11/2026

## Correções aplicadas

1. **Responsividade crítica**: declarações de `.app { grid-template-columns: 252px ... }` no fim da folha de estilos sobrescreviam as media queries anteriores para celulares. Corrigido com regras móveis finais e explícitas, sem coluna lateral em até 1000px.
2. **Largura**: `max-width: 100%` e `min-width: 0` aplicados aos containers, com proteção contra overflow horizontal e mudanças responsivas nos cartões, filtros e ferramentas.
3. **Usabilidade touch**: miniaturas com rolagem horizontal, controles maiores e cartões em duas colunas no celular.
4. **Paint Pro**: página independente `studio.html` com pincel, lápis, marcador, borracha, linha, retângulo, elipse, texto, paleta, espessura, opacidade, até oito camadas, visibilidade/ordem de camadas, simetria, grade, desfazer/refazer, importar imagem, exportar PNG, projeto JSON e salvamento automático local.
5. **PWA**: cache do shell atualizado para v8 e arquivo `studio.html` incluído na lista de pré-cache.

## Auditoria de qualidade restante — ordem de prioridade

### P0 — Altamente prioritário
- **Validação mobile real**: testar Android Chrome, iOS Safari, orientação horizontal/vertical e teclado virtual. Código passou no parser JS e no gerador de catálogo, mas a navegação local automatizada foi bloqueada por política do ambiente nesta execução.
- **Arte em aulas**: etapas recentes são recortes de infográficos, com textos sobrepostos às imagens. O desenho fica pequeno em telas de celular; ideal separar cada ilustração sem textos e exibir instruções em painel HTML acessível.
- **Progresso**: "concluído" é marcado manualmente, sem exercícios corrigidos nem rubricas de avaliação.

### P1 — Evoluções próximas
- **Pedagogia**: trilhas por fundamentos, objetivos, pré-requisitos, avaliação de proporção, rubricas simples, cronograma gradual, exemplos comuns de erros e comparações antes/depois.
- **Revisão artística**: algumas sequências de imagens são lindas, mas nem sempre a etapa é reproduzível como processo técnico isolado. Necessário revisão humana de anatomia, alinhamento, proporções e consistência entre etapas.
- **Capas do catálogo**: cards usam imagens finais de lição com muito texto e cortes. Criar thumbs autorais 4:3 com foco na arte e ícones de categoria.
- **Design system**: CSS atual acumula camadas de versões antigas, com cores, media queries e tokens repetidos. Separar `styles.css`, tokens, componentes e breakpoints consistentes.
- **Editor**: autosave atual usa localStorage, com limite de armazenamento variável, normalmente baixo para várias camadas em PNG. Migrar projetos para IndexedDB com limites, backup e recuperação em caso de falha.
- **Editor**: falta pincel sensível à pressão, preenchimento bucket, ferramenta laço/seleção, transformações, zoom e pan, régua, perspectiva e modelos de simetria além da vertical.

### P2 — Academia completa
- **Biblioteca**: filtros por tempo, traço, perspectiva e tema; busca com sinônimos e tags; páginas de curso, coleções e desafios.
- **Continuidade**: exercícios de criações originais e exportação de portfólio; inspiração sem copiar franquias e personagens licenciados.
- **Offline**: download seletivo de pacotes e lista do que está disponível offline, sincronização entre dispositivos só com login/serviço futuro, backup manual gratuito.
- **Performance**: thumbs menores, formatos modernos com fallback, lazy loading e redução da memória usada no paint.
- **Acessibilidade**: contraste, tamanhos de toque, leitores de tela, rótulos do canvas, tutoriais com alternativa para impressão.

## Nota de produto
- A versão 8 mantém 19 aulas e 114 imagens/etapas de construção. Não confundir quantidade de aulas com número de artes independentes.
- Os recursos do Paint Pro foram criados sem serviços pagos nem dependências externas. É uma primeira ferramenta funcional, não substitui Clip Studio Paint, Krita ou similares.
