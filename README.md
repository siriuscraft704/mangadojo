# MangaDojo v8.0 — Academia de desenho mangá

Site estático gratuito com catálogo de 19 aulas/114 etapas. Interface responsiva e `studio.html`, o Paint Pro independente.

## URL
https://siriuscraft704.github.io/mangadojo/

## Como publicar
Enviar arquivos ao repositório, `main`. O GitHub Actions em `.github/workflows/deploy.yml` valida as aulas e publica automaticamente. Adicione novas aulas em `lessons/<slug>/lesson.json` e imagens em `assets/`, depois execute `python tools/build_catalog.py`.

## Estúdio
`studio.html` usa armazenamento local do navegador para o autosave. Exporte um projeto JSON regularmente para backup, especialmente antes de limpar dados do navegador ou trocar de dispositivo.

## Limitações
Ver `AUDITORIA.md` para próximos trabalhos e testes pendentes. Artes são conteúdo original assistido por IA; as aulas ilustradas devem passar por revisão pedagógica humana antes de serem consideradas material de ensino profissional.
