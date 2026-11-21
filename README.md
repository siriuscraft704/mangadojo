# MangaDojo — Academia de Desenho

Projeto gratuito de ensino de desenho mangá e anime, criado para crescer continuamente com novas aulas.

## Publicação

- Endereço esperado: https://siriuscraft704.github.io/mangadojo/
- GitHub Actions: `.github/workflows/deploy.yml` publica o conteúdo automaticamente.
- GitHub > Settings > Pages > Build and deployment > Source: **GitHub Actions** (caso seja necessário selecionar).
- A estrutura original de 9 aulas / 54 imagens encontra-se no pacote local `MangaDojo_Pages_v5.zip`; os arquivos binários ainda precisam ser transferidos ao repositório. O site inicial disponível aqui será uma versão de demonstração e **não** substitui as ilustrações originais.
- Para adicionar aula: pasta `lessons/<slug>/lesson.json` e artes em `assets/`, reexecutar `tools/build_catalog.py` e publicar. A automatização de catálogo será incluída com o pacote completo.

## Direitos autorais
Aplicativo original; não copiar material protegido de mangás comerciais nem imagens de repositórios sem licença compatível. Bibliotecas técnicas MIT planejadas: React Konva, React Sketch Canvas, Perfect Freehand, Panzoom. Licença MIT dessas bibliotecas **não** se estende automaticamente às artes.
