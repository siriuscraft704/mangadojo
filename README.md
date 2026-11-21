# MangaDojo Atelier 12 · Smudge Studio

Academia de desenho mangá gratuita com biblioteca de aulas progressivas, ferramentas de prática e editor independente **Smudge**.

## Estado atual
- 25 aulas e 150 etapas esperadas após compilar o catálogo.
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

Essas referências inspiram organização e ferramentas; **nenhum código ou arte foi copiado dessas bibliotecas nesta entrega**. Futuras integrações devem preservar as licenças e avisos dos projetos utilizados.

## Limitações honestas
- As 96 imagens de antigas pranchas continuam sendo recortes provisórios e exigem substituição por desenhos nativos.
- Não houve teste em aparelhos iOS/Android reais; os smoke tests são estáticos.
- Sem sincronização em nuvem; o usuário deve exportar JSON para backup.
- Ferramentas avançadas (laço, transformação, pressão da caneta, máscaras) permanecem futuras.
- SVGs originais desta versão são estudos técnicos esquemáticos, não substituem avaliação humana de desenho/anatomia.

## Correção 12.3 (2026-11-21)
A avaliação visual identificou que os desenhos SVG de mãos e os dois protótipos adicionais tinham qualidade inferior às ilustrações originais. Foram removidos da navegação; a aula `maos-gestos` volta aos WebP anteriores. O visualizador segue com `object-fit:contain` para não aplicar cortes extras. As artes antigas com cortes internos continuam aguardando reconstrução profissional. Não afirmar que foram corrigidas por completo.
