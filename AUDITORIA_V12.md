# Auditoria de entrega — MangaDojo Atelier 12 / Smudge

Data: 2026-11-21. Escopo: revisão dos arquivos do repositório e alterações realizadas na branch `main`.

## Evidência de implementação
- Marca própria em `assets/mangadojo-mark.svg` e `assets/smudge-mark.svg`.
- Design system complementar em `styles/atelier.css` e `styles/smudge.css`.
- Navegação do site renomeia Paint Pro para Smudge e dá acesso ao estúdio.
- Interface do editor `studio.html` renomeada Smudge e estilos atualizados.
- Persistência dos projetos muda para IndexedDB (`smudge-projects`), com tentativa de migração de projetos anteriores em localStorage e fallback em caso de indisponibilidade.
- Limite aumentado de oito para 16 camadas e histórico de doze para 24 snapshots.
- Duas lições novas, cada uma com seis imagens SVG originais: `rosto-tres-quartos` e `olhos-expressivos`.
- Integração da aula com o estúdio agora usa o caminho real da imagem (`.svg`, `.png` e `.webp`).
- `sw.js` atualizado com cache v12 e estilos/marcas no núcleo offline.
- `tools/smoke_test.py` integrado ao workflow de GitHub Pages depois da compilação.

## Auditoria estática
- 27 lições e 162 etapas esperadas após gerar o catálogo.
- Testes estáticos devem comprovar existência dos arquivos, XML dos SVGs, estrutura das aulas e marcas/links.
- O workflow foi modificado para falhar antes de publicar quando o smoke test não passar.
- O GitHub confirma os commits no repositório; o status de execução do workflow não foi verificado nesta sessão.

## Pendências críticas
1. **Artes legadas:** os 96 recortes continuam provisórios. Recriar imagens nativas em alta resolução de modo incremental e consistente em cada aula.
2. **Teste em navegador real:** smoke tests estáticos não simulam o canvas; realizar teste manual ou E2E em Android, iOS, Chrome desktop e Firefox.
3. **Fluxo de publicação:** confirmar no GitHub Actions que o workflow terminou com sucesso e validar os URLs publicados.
4. **Retenção de projetos:** testar migração, quotas, erros de IndexedDB e exportação/importação JSON com projetos grandes.
5. **Novos recursos de edição:** seleção/lasso, transformação, estabilização, máscaras, pressão de caneta e grades de perspectiva não foram incluídos nesta versão.
6. **Refatoração:** o CSS antigo acumulado persiste no HTML e deve ser migrado para arquivos modulares depois de testes de regressão.
7. **Anatomia e pedagogia:** estudos SVG novos são esquemáticos, não têm validação de especialista e não substituem uma coleção artística de alta fidelidade.
8. **PWA:** verificar instalação, ícones SVG por navegador e comportamento offline após atualizar o cache.

## Política de licenças
Projetos pesquisados: Konva.js e Drawora, ambos MIT na origem. Nenhum código ou imagem externa foi incorporado nesta entrega; todos os novos SVGs são autorais. Antes de reutilizar bibliotecas, preservar avisos de copyright e licença e confirmar direitos de cada asset.

## Próxima fase recomendada
Priorizar recriação de imagens legadas, auditoria visual com screenshots e arquitetura modular, depois instrumentos avançados do Smudge e trilhas de aprendizado.

## Complemento — Smudge 12.1 (2026-11-21)
- Adicionado controle de estabilização de traço (0% a 85%) com suavização progressiva e finalização na posição real do ponteiro.
- Referências de aulas deixam de ser duplicadas ao reabrir o mesmo projeto com a mesma URL.
- Importação de arquivos JSON passa a validar quantidade máxima de camadas, presença de PNG base64 e tamanho máximo individual.
- O catálogo compilado no próprio repositório foi atualizado de 25/150 para 27 aulas e 162 etapas.
- Smoke test ganhou verificações específicas do estabilizador e análise sintática dos scripts com Node, disponível no runner GitHub.
- Scripts inline do `index.html` e `studio.html` passaram em verificação de sintaxe JavaScript pela ferramenta da sessão.
- Não houve validação de execução do deploy GitHub Pages nem teste de interface em dispositivos reais; ambos seguem pendentes.
