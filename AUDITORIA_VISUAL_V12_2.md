# Auditoria visual — MangaDojo 12.2

Data: 2026-11-21. Escopo: capturas do usuário, inspeção direta de ativos originais no GitHub e mudanças no repositório.

## Problema confirmado

- A prévia de aula herdava `aspect-ratio:1/1` e media queries conflitantes, embora as referências recortadas tivessem orientação diferente.
- O catálogo usava tamanho fixo de imagem no cartão e classes CSS acumuladas em várias versões.
- Inspeção direta dos arquivos `assets/cabelo-fem-liso-6.webp` e `assets/cabelos-cacheados-6.webp`: ambos contêm conteúdo que já termina na borda superior/lateral da imagem, de modo que CSS não recupera a parte ausente.
- A inspeção dos arquivos `assets/mao-6.webp` e `assets/maos-gestos-6.webp` confirma que a geometria das mãos deve ser verificada manualmente, independentemente do layout.
- Relatório anterior V11 identifica 96 ilustrações recuperadas por recorte de infográficos. Não considerar esses recortes artes nativas validadas.

## Alterações entregues neste ciclo

1. `styles/atelier.css`: novo enquadramento da prévia em proporção 9:10, imagem inteira visível via `contain`, com prancheta e canvas alinhados.
2. Cartões do catálogo e miniaturas exibem toda a área disponível da imagem sem zoom de recorte.
3. `lessons/maos-gestos/lesson.json`: seis novas imagens SVG originais e progressão pedagógica reescrita para gesto de paz com cinco dedos identificáveis.
4. `catalog.generated.js` sincronizado com os novos caminhos da aula.
5. `auditoria-imagens.html`: inspeção visual das 162 referências agrupadas por aula, com busca e filtro de ativos nativos.
6. `tools/media_audit.py`: inventário de resolução, formato, arquivos duplicados e marcações de risco em JSON gerado durante publicação.
7. `tools/smoke_test.py`: verificações adicionais de interface, auditoria e caminhos de imagem.
8. `sw.js`: cache incrementado para v13 para atualizar os arquivos estáticos.

## Estado editorial

- Total atual: 27 aulas e 162 etapas.
- 18 etapas SVG nativas novas identificadas: 12 de aulas adicionadas anteriormente e 6 da mão em gestos.
- 144 imagens WebP existentes: **não confundir a quantidade com 144 imagens comprovadamente cortadas**.
- 96 recortes anteriormente documentados precisam de reconstrução artística em resolução adequada; o restante também pede revisão de enquadramento, anatomia e progressão.
- A primeira sequência vetorial das mãos é um material transitório. O lote artístico de alta fidelidade existe como pacote produzido nesta sessão, porém não foi incorporado automaticamente ao GitHub; não declarar que foi publicado.

## Critérios para validar cada substituição

- Nenhuma região importante do desenho encosta involuntariamente no limite superior, inferior ou lateral.
- Mãos com cinco dedos anatomicamente plausíveis, sem dedos duplicados ou articulações extras.
- Cada etapa conserva a identidade e a pose entre quadros.
- Sem textos/indicadores herdados da composição original dentro da arte didática.
- Arte com proporções coerentes e resolução adequada ao viewport mobile e desktop.
- Teste de leitura, desenho e exportação PNG/JSON no Smudge após importar a nova referência.

## O que ainda não foi confirmado

- A conclusão com sucesso do workflow GitHub Actions e a disponibilidade desta revisão no GitHub Pages.
- Testes reais em dispositivos móveis e captura de screenshots do site publicado.
- Qualidade artística final e validação anatômica humana do conjunto.
- Substituição integral das 96 artes legadas: segue pendente e não deve ser afirmada como concluída.
