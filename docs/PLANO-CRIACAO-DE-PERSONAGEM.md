# Plano · Criação de personagem

Documento para aprovação. Nada aqui foi implementado ainda. Gerado em 27/11/2026.

## 1. Onde estamos

- A criação de personagem existe hoje só como uma **"Ficha de personagem"** dentro da Oficina criativa (campos soltos, salvos no navegador) e como exercícios avulsos. Não há trilha guiada, não há módulo no Curso e a ficha não conversa com o Smudge.
- O Curso tem 7 módulos de técnica (fundamentos, rostos, cabelos, mãos e pés, corpo, animais, quadrinhos). **Falta o módulo que junta tudo**: pegar essas técnicas e criar um personagem próprio, do zero ao resultado final.
- O Smudge já tem o que o plano precisa: camadas, referência carregada por `?ref=`, régua de perspectiva, retículas e exportação em PNG.

## 2. Objetivo

Em oito etapas, o aluno sai com uma **folha de personagem pronta para exportar**: três vistas (frente, perfil e costas), seis expressões, paleta de cores e uma pose de ação. Cada etapa produz um resultado visível, não só leitura.

## 3. Módulo 8 do Curso: "Criação de personagem" (projeto final)

| Etapa | O aluno decide | Entrega da etapa | Liga com o módulo |
|---|---|---|---|
| 1. Briefing | Quem é, o que quer, onde vive, três palavras de personalidade | Ficha preenchida | n/a |
| 2. Silhuetas | Forma geral do corpo | Seis silhuetas pretas; escolhe uma. Teste: se a silhueta for reconhecível, o design funciona | Fundamentos |
| 3. Proporção | Altura em cabeças (de 5 a 8) e tipo de corpo | Boneco de proporção sobre uma grade | Corpo |
| 4. Rosto e identidade | Forma do rosto, olhos e **um traço marcante** | Rosto de frente e de três quartos | Rostos |
| 5. Cabelo | Volume, direção e silhueta do cabelo | Cabelo aplicado ao rosto | Cabelos |
| 6. Figurino | Três peças que contam a história | Figurino por formas simples | Corpo |
| 7. Paleta | De 3 a 5 cores, regra 60/30/10 | Paleta e **versão em preto e branco** (teste de valor) | n/a |
| 8. Folha final | Montagem | Folha com vistas, expressões, paleta e pose | Quadrinhos |

Regra de ouro do módulo: o aluno cria **um personagem original**. As aulas pedem referências de estilo, não a cópia de personagens existentes.

## 4. Ferramentas novas

1. **Ficha de personagem v2** (na Oficina): um passo a passo com as oito etapas, que lembra onde o aluno parou. Salva no navegador, como o resto do site. Cada etapa tem um botão **"Abrir no Smudge"** já com o gabarito certo carregado.
2. **Gabaritos vetoriais próprios** (SVG, originais, sem problema de direitos): grades de proporção de 5 a 8 cabeças, guia de vistas (frente, perfil e costas), grade de seis expressões, faixa de silhuetas e faixa de paleta. Os nomes seguem o padrão que o Smudge já aceita em `?ref=`, então entram como camada de referência sem mudar o editor.
3. **Paleta com checagem de valor:** o aluno escolhe as cores e a ferramenta mostra a versão em tons de cinza lado a lado, para o personagem ler bem em preto e branco.
4. **Exportar a folha:** PNG (e PDF, se aprovado), com o nome do personagem e as etapas escolhidas.

## 5. O que reaproveitar do GitHub

Dados da busca do GitHub em 27/11/2026 (estrelas e licença conforme a API). Não li o código de terceiros; a análise é de descrição, licença e conhecimento prévio das técnicas.

| Projeto | ★ | Licença | Para que serve aqui |
|---|---|---|---|
| excalidraw/excalidraw | 136 mil | MIT | Referência de **biblioteca de elementos reutilizáveis**, exportação PNG e persistência local primeiro. Ideia para a faixa de gabaritos. |
| fabricjs/fabric.js | 31,5 mil | MIT | Se a montagem da folha precisar de mover, girar e escalar elementos com alças, é uma base sólida (MIT permite reuso). |
| steveruizok/perfect-freehand | 5,8 mil | MIT | Traço com pressão. Já citado no `DESIGN.md`; condicionado a teste de desempenho no celular. |
| dicebear/dicebear | 10 mil | MIT (biblioteca) | Ideia de **personagem montado por partes**. Atenção: cada estilo de avatar tem licença própria (alguns CC BY); não usar arte deles. |
| KDE/krita | 10,8 mil | GPL-3.0 | Referência de ferramentas de artista (assistentes de perspectiva, estabilizador). **Só ideias**; GPL não permite copiar código para um site sem aceitar a mesma licença. |
| tldraw/tldraw | 51,6 mil | licença própria (a API não identifica) | **Evitar** sem ler os termos comerciais. |
| konvajs/konva | 15 mil | a API não identifica | Verificar a licença no repositório antes de qualquer uso. |

Nota: a busca por "character creator" no GitHub devolve quase só ferramentas 3D (Blender, Unity, iClone), que não servem para um curso de desenho 2D. Por isso o plano é próprio, e não adaptado de um projeto existente.

## 6. Plano de trabalho (3 semanas)

| Semana | Entrega | Como saber que ficou pronto |
|---|---|---|
| 1 | Gabaritos SVG e a Ficha v2 (etapas 1 a 3), com persistência | O aluno abre o gabarito no Smudge em um clique e volta à ficha sem perder dados |
| 2 | Etapas 4 a 7 e a checagem de valor da paleta | A versão em tons de cinza aparece ao lado da paleta escolhida |
| 3 | Etapa 8 (folha final), exportação e o módulo 8 no Curso | Folha exportada em PNG com as três vistas e seis expressões; teste automático da persistência |

## 7. Riscos e como tratar

- **Conteúdo pedagógico:** as lições precisam de exemplos desenhados. Opções: ilustrador, ou arte gerada por IA com retoque. Em qualquer caso, **registrar origem e licença** de cada imagem em `THIRD_PARTY_NOTICES.md`. Arte gerada por IA tem proteção autoral incerta.
- **Direitos de personagens:** o módulo deve orientar a criar personagens originais e a usar referências só como estudo de estilo.
- **Peso no celular:** a folha com várias camadas pode pesar. Medir em aparelho real antes de liberar.
- **Escopo:** começar pelas etapas 1 a 3 e validar com alunos antes de produzir o restante.

## 8. Decisões que preciso de você

1. Aprova o **Módulo 8 como projeto final** do Curso, com estas oito etapas?
2. Os exemplos desenhados virão de **ilustrador** ou de **IA com retoque**?
3. Quer exportação em **PDF** além de PNG?
4. Posso começar pelos **gabaritos SVG e pela Ficha v2** em uma branch separada?
