# Revisão de artes 12.6 — Pacote limpo e acervo local

Data: 2026-11-21.

## Execução realizada
- Corrigida a cadeia de processamento: agora os arquivos de geração já montados em /mnt/data são processados diretamente, sem depender da transferência para Adobe que falhava.
- Extraídas **36 etapas individuais** com enquadramento branco e sem textos/molduras das quatro pranchas: gato sentado (10), gato de pé (6), leão (10), lobo correndo (10).
- Correção manual da região inferior do leão: a primeira extração cortava as patas, então o limite de recorte foi ampliado e revalidado visualmente.
- O pacote final contém 36 WebP, quatro descritores JSON, manifesto e visualizador offline. O ZIP está disponível como anexo no chat; **os bytes do ZIP não foram inseridos neste repositório**, pois o conector de escrita GitHub desta sessão permite gravar texto mas não importar diretamente os arquivos binários do container.
- Nova página pública `acervo-revisado.html` permite selecionar o ZIP e importar localmente sem servidor usando `DecompressionStream('deflate-raw')`, com alternativa de importação WebP individual.
- Imagens importadas ficam em IndexedDB (`mangadojo-artwork`, store `images`) e podem ser abertas no Smudge pelo parâmetro `?localArt=` sem distorção.
- O site não aplica bordas extras no visualizador; imagens são exibidas em `contain`.

## Validação
- Arquivos WebP com dimensões mínimas de 800×800 px e borda branca intencional.
- ZIP validado com o parser do navegador reproduzido no Node v22: 36 arquivos RIFF/WEBP descompactados e íntegros.
- Sintaxe JavaScript dos componentes de importação verificada.
- Workflow GitHub Actions da versão 12.6 passou com sucesso.
- Página pública foi acessada e retornou HTTP 200.
- **Não foi possível confirmar a interação real de importação do ZIP em Android/iOS** usando o navegador conectado; ainda deve ser testada no aparelho.

## Limitações honestas
- As 158 telas anteriores continuam no catálogo. Apenas remover a moldura do visualizador não recupera elementos que já faltam no WebP original.
- O pacote de 36 itens é o primeiro lote curado, não todas as imagens geradas no histórico.
- Foram examinados mais 12 quadros candidatos (rosto feminino e cabelo ondulado); alguns ainda terminam em corte de cabelo/pescoço dentro da composição original e **não foram aprovados como substitutos integrais**.
- O acervo local é pessoal, por dispositivo e navegador. Para tornar as 36 imagens disponíveis a todos os visitantes, é necessário adicionar os arquivos WebP ao repositório (por upload GitHub) e recompilar o catálogo após aprovação visual.
- Anatomia de mãos, rostos e outras artes antigas continua exigindo revisão humana.
