# Auditoria técnica — MangaDojo 11.0

## Evidência na versão 10.0
- Catálogo: 25 aulas e 150 referências; 9 lições originais com imagens autônomas e 16 lições importadas de infográficos.
- 96 imagens das 16 lições importadas tinham textos, barras ou títulos incorporados à arte.
- CSS continha múltiplas camadas de regras herdadas (incluindo media queries conflitantes e `!important`).
- A interface exibia textos estáticos de versões antigas (v5, 9 aulas, 54 imagens), embora o catálogo fosse maior.
- A prancheta captura eventos de toque e impede rolagem mesmo quando o usuário só queria ler.
- Pintura salva em localStorage; o estúdio tem limite de 8 camadas e 12 snapshots, não há IndexedDB nem sincronização.
- Os recortes da fonte 2×3 impõem perda parcial das artes, sobretudo nas bordas; recuperação integral exige **regenerar artes sem texto desde a origem**.

## Implementado e validado no pacote v11
- 96 imagens substituídas por recortes exclusivamente da zona de desenho, compostas em tela branca padronizada 720×800 sem coluna textual.
- Modos explícitos de leitura e desenho na aula, leitura como padrão; ampliação de arte em diálogo acessível.
- Modo seguro de rolagem para toque no Paint Pro, com botão de ativação do desenho; mouse continua habilitado.
- Correções de textos e contadores estáticos; imagens de cartões exibidas com `object-fit: contain`.
- Cache de imagens atualizado para v11, para invalidar os recursos antigos.

## Pendências reais (não confundir com recursos implementados)
1. Refazer cada uma das 96 artes sem texto nativamente em resolução alta, com composição adequada por etapa; recorte atual é melhoria transitória, pode perder detalhes no limite direito.
2. Testar iOS Safari e Android Chrome em aparelhos reais (rolagem, Pointer Events, PWA, importação e salvamento).
3. Substituir armazenamento local dos projetos grandes por IndexedDB com recuperação e versões.
4. Ferramentas avançadas de seleção, estabilização e transformação; atualmente não foram implementadas.
5. Navegação curricular por trilhas, exercícios, criador de personagens e criador de quadrinhos — novas frentes, ainda não implementadas.
6. Refatorar CSS acumulado e realizar testes de regressão automatizados.
7. Revisão de geometria, anatomia e progressão didática por professor de desenho.
