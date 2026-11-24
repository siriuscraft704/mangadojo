# MangaDojo — estado do acervo

A versão pública consultada já contém o histórico V11 e auditorias V12 a V12.4. O pacote V11 Auditado foi recuperado como referência histórica. O código público atual é a fonte primária do site, das nove aulas e dos 62 passos. As 12 artes de rosto feminino e cabelos ondulados estão em `assets/review-pending/`, com status e revisão em `art-review-manifest.json` e `AUDITORIA_ARTES_12_6.md`.

Validação do checkout em 24/11/2026: `python3 tools/smoke_test.py` passou, incluindo montagem de 172 arquivos para Pages. `node tools/test_visual_geometry.cjs` também passou nos três casos de importação proporcional, na exportação de retrato e na comparação do tutorial. Para consultar o processo editorial, comece por [README](../README.md) e [auditoria visual](../AUDITORIA_VISUAL_V12_2.md).
