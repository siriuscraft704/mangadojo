# Auditoria final de engenharia — MangaDojo Atelier / Smudge 12.4
Data: 2026-11-21 · Repositório: https://github.com/siriuscraft704/mangadojo

## Escopo
Revisão da apresentação, geometria de referências, navegação pedagógica, editor e base open source. Os problemas de anatomia e recortes na **fonte das imagens** ainda exigem substituição artística de qualidade.

## Alterações técnicas verificáveis
- `studio.html`: `drawContained` importa referências sem distorção para o canvas quadrado e preserva proporções; projetos salvos são mantidos.
- `index.html`: exportação de etapa em 900×1000 sem esticar a imagem; compara a etapa anterior com a atual; direciona para revisão visual da aula; dicas específicas para mãos, rostos e cabelos.
- `styles/atelier.css`: comparação responsiva e registro de defeitos sem sobrepor botões.
- `auditoria-imagens.html`: busca filtrada por `?q=`, classificação de problemas, visualização ampliada e exportação JSON local.
- `tools/test_visual_geometry.cjs`: três casos numéricos de contain (vertical, horizontal, quadrado) + verificações de exportação/comparação.
- `tools/smoke_test.py`: validações do catálogo, CSS, JS, conteúdos e estado de publicação do acervo preservado.
- `tools/media_audit.py`: dimensões, formatos, duplicatas, risco de recorte legado, inconsistência de proporção entre etapas e caso conhecido de divergência na fonte.
- `.github/workflows/deploy.yml`: testes antes do GitHub Pages.
- `OPEN_SOURCE_RESEARCH_2026.md`: 13 repositórios estudados, licenças e prioridades.
- `DESIGN.md`: tokens e padrões observados na página pública.

## Pesquisa e decisão de arquitetura
Fabric.js, Konva, Excalidraw, Perfect Freehand, TUI Image Editor, VitePress, Starlight, Docsify Starter, Knowledge Core, Educenter, Free Drawing, Astro Template e ScrewFast foram avaliados como referências. **Não houve importação de assets artísticos de terceiros nesta versão**, porque não foi confirmada licença específica de desenhos passo a passo compatíveis com as aulas. A licença MIT de código não se estende automaticamente a imagens e fontes.

## Verificação de navegador
- Firecrawl: página inicial pública respondeu HTTP 200, identificada como MangaDojo Atelier 12.4; inspeção da marca e tokens.
- Auditoria mobile real via navegação automatizada (~390 px): catálogo com 25 aulas; aula Cabelos Femininos Ondulados abriu; navegação 1→2; comparação dupla completa sem overflow horizontal; auditoria filtrada com seis imagens; visualização ampliada funcional.
- Smudge via navegador: referência importada em camada separada, proporção preservada, alternância Rolar/Desenhar, controles de camadas e salvamento local visíveis.
- Limitação dos testes: o navegador automatizado não gerou efetivamente um traço no canvas; por isso Undo/Redo e exportação PNG não foram verificados ponta a ponta.
- Falha artística confirmada: `cabelo-fem-ondas-1.webp` já aparece cortado à esquerda e não representa claramente a aula anunciada. Marcar como fonte em revisão. **Não substituído** por imagem aleatória.

## Lacunas abertas (PENDENTES)
- 96 imagens WebP de origem recortada/infográfico, relatadas na V11: não regeneradas.
- Anatomia das quatro aulas de mãos requer curadoria e desenhos novos; não declarar corrigida.
- Rostos e cabelos cortados no arquivo original precisam de nova arte adequada; conter imagem no CSS não restaura partes ausentes.
- Testes reais em iOS Safari e Android de todos os recursos de desenho.
- Regressão visual completa nas 150 etapas e revisão pedagógica por desenhista.
- Refatoração dos múltiplos estilos CSS históricos; só após comparação visual automatizada.

## Resultado
A versão técnica é incremental e preserva a qualidade original existente. **Não declarar finalização artística de todo o acervo.** A publicação deve ser considerada tecnicamente validada somente após o workflow concluir com sucesso no commit final.
