# MangaDojo Atelier 12.5 · Smudge Studio

Academia de desenho mangá gratuita com biblioteca de aulas progressivas, ferramentas de prática e editor independente **Smudge**.

## Estado atual
- 27 aulas e 158 telas de estudo após compilar o catálogo, incluindo duas oficinas novas com oito SVG MIT atribuídos.
- Protótipos vetoriais provisórios foram retirados do catálogo e arquivados em `drafts/` por baixa qualidade artística.
- Identidade própria MangaDojo e Smudge; estilos em `styles/atelier.css` e `styles/smudge.css`.
- Smudge mantém pincéis, preenchimento, camadas, exportação PNG/JSON e referência da aula; até 16 camadas e 24 pontos de histórico.
- Projetos locais agora usam IndexedDB com fallback e migração dos dados anteriores do localStorage.
- PWA e deploy automatizado pelo GitHub Actions.

## Desenvolvimento / publicação
```sh
python tools/build_catalog.py
python tools/smoke_test.py
```

O workflow `.github/workflows/deploy.yml` compila, testa e publica na branch `main`.
Site: https://siriuscraft704.github.io/mangadojo/
Editor: https://siriuscraft704.github.io/mangadojo/studio.html

## Referências open-source pesquisadas
- Konva.js — MIT: https://github.com/konvajs/konva
- Drawora — MIT: https://github.com/pradipNP/drawora

Outras referências e licenças estão documentadas em `OPEN_SOURCE_RESEARCH_2026.md`. O projeto incluiu oito SVGs da biblioteca de Vijay Verma, com aviso MIT preservado em `THIRD_PARTY_NOTICES.md`; **não foram usados como substitutos para aulas de anatomia defeituosas**. Futuras integrações devem preservar as licenças e avisos dos projetos utilizados.

## Limitações honestas
- As 96 imagens de antigas pranchas continuam sendo recortes provisórios e exigem substituição por desenhos nativos.
- Não houve teste em aparelhos iOS/Android reais; os smoke tests são estáticos.
- Sem sincronização em nuvem; o usuário deve exportar JSON para backup.
- Ferramentas avançadas (laço, transformação, pressão da caneta, máscaras) permanecem futuras.
- SVGs originais desta versão são estudos técnicos esquemáticos, não substituem avaliação humana de desenho/anatomia.

## Correção 12.3 (2026-11-21)
A avaliação visual identificou que os desenhos SVG de mãos e os dois protótipos adicionais tinham qualidade inferior às ilustrações originais. Foram removidos da navegação; a aula `maos-gestos` volta aos WebP anteriores. O visualizador segue com `object-fit:contain` para não aplicar cortes extras. As artes antigas com cortes internos continuam aguardando reconstrução profissional. Não afirmar que foram corrigidas por completo.

## Atualização 12.5 (2026-11-21)
- Novas oficinas de **Observação e Composição** e **Silhuetas e Personagens Animais** (quatro exercícios independentes por oficina). Fonte e licença: `THIRD_PARTY_NOTICES.md`.
- Checklists de prática agora são interativos, com progresso salvo no dispositivo.
- Página `trilhas.html` agrupa quatro percursos de estudo e identifica referências em revisão.
- Abrir uma aula específica: `index.html?lesson=observacao-vetorial#workspace`.
- Imagens novas são disponíveis offline via Service Worker v17.
- O Smudge continua preservando proporção das referências e salvamento de projetos, sem substituir artes de baixa qualidade por desenhos genéricos.
- Pendente: recriação e validação humana de rostos, cabelos e mãos já cortados ou anatomicamente incoerentes no WebP original.
