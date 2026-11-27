#!/usr/bin/env python3
"""Carimba o cabeçalho e o rodapé únicos do MangaDojo nas páginas.

Cada página marca as regiões com comentários:
    <!--cab-->  ... <!--/cab-->
    <!--rodape--> ... <!--/rodape-->
O conteúdo entre as marcas vem daqui. Uso:
    python3 tools/stamp_shell.py          # reescreve as páginas
    python3 tools/stamp_shell.py --check  # só confere (sai com 1 se algo estiver fora de sincronia)
"""
from pathlib import Path
import re, sys

ROOT = Path(__file__).resolve().parents[1]

# página -> item do menu marcado como atual (None = nenhum)
PAGES = {
    'index.html': None,
    'trilhas.html': 'Curso',
    'aulas-pranchas.html': 'Pranchas',
    'pranchas.html': 'Pranchas',
    'oficina.html': 'Oficina',
    'acervo-revisado.html': None,
    'creditos.html': None,
    'aula.html': 'Curso',
    'auditoria-imagens.html': None,
    'homologacao-artes.html': None,
    'revisao-candidatos.html': None,
}

MENU = [('Curso', 'trilhas.html'), ('Pranchas', 'aulas-pranchas.html'), ('Oficina', 'oficina.html'), ('Smudge', 'studio.html')]


def cab(current):
    links = '\n'.join(
        f'    <a href="{href}"' + (' aria-current="page"' if name == current else '') + f'>{name}</a>'
        for name, href in MENU)
    return f'''<header class="cab"><div class="cab__in">
  <a class="marca" href="./" aria-label="MangaDojo, página inicial"><img src="assets/mangadojo-mark.svg" alt=""><span><b>MangaDojo</b><small>Academia de desenho de mangá</small></span></a>
  <nav class="menu" aria-label="Menu principal">
{links}
  </nav>
  <a class="btn" href="trilhas.html">Começar<span class="seta" aria-hidden="true"></span></a>
</div></header>'''


RODAPE = '''<footer class="rodape"><div class="largura">
  <div class="rodape__grade">
    <div><a class="marca" href="./"><img src="assets/mangadojo-mark.svg" alt=""><span><b>MangaDojo</b></span></a><p>Academia gratuita de desenho de mangá, com aulas em etapas, pranchas completas e um editor no navegador.</p></div>
    <div><h2>Estudar</h2><ul><li><a href="trilhas.html">Curso</a></li><li><a href="aulas-pranchas.html">Pranchas</a></li><li><a href="oficina.html">Oficina criativa</a></li><li><a href="studio.html">Smudge</a></li></ul></div>
    <div><h2>Sobre</h2><ul><li><a href="acervo-revisado.html">Acervo</a></li><li><a href="creditos.html">Créditos e licenças</a></li></ul></div>
    <div><h2>Equipe e revisão</h2><ul><li><a href="auditoria-imagens.html">Auditoria de imagens</a></li><li><a href="homologacao-artes.html?lesson=mao">Homologação das artes</a></li><li><a href="revisao-candidatos.html">Candidatos em revisão</a></li></ul></div>
  </div>
  <div class="rodape__fim"><span>MangaDojo · projeto público</span><span>Origem e licença de cada imagem estão nos <a href="creditos.html">créditos</a>.</span></div>
</div></footer>'''


def render(text, current):
    for tag, body in (('cab', cab(current)), ('rodape', RODAPE)):
        pattern = re.compile(rf'<!--{tag}-->.*?<!--/{tag}-->', re.S)
        if not pattern.search(text):
            raise SystemExit(f'marcas <!--{tag}--> ausentes')
        text = pattern.sub(lambda m: f'<!--{tag}-->{body}<!--/{tag}-->', text, count=1)
    return text


def main():
    check = '--check' in sys.argv
    bad = []
    for name, current in PAGES.items():
        path = ROOT / name
        if not path.exists():
            continue
        old = path.read_text('utf-8')
        if '<!--cab-->' not in old:
            continue  # página ainda não migrada
        new = render(old, current)
        if new != old:
            if check:
                bad.append(name)
            else:
                path.write_text(new, 'utf-8')
                print('atualizado:', name)
    if bad:
        print('Fora de sincronia (rode python3 tools/stamp_shell.py):', ', '.join(bad), file=sys.stderr)
        sys.exit(1)
    if check:
        print('cabeçalho e rodapé em sincronia')


if __name__ == '__main__':
    main()
