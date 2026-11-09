"""Testes da auditoria: um site certo passa, um site com erros conhecidos é pego.

Rodar: python tests/test_auditar.py
"""
import pathlib
import subprocess
import sys

RAIZ = pathlib.Path(__file__).resolve().parent.parent
SCRIPT = RAIZ / "seo-ggcode" / "scripts" / "auditar.py"
FIX = RAIZ / "tests" / "fixtures"


def auditar(pasta):
    r = subprocess.run([sys.executable, "-I", str(SCRIPT), str(FIX / pasta)],
                       capture_output=True, text=True, encoding="utf-8")
    return r.returncode, r.stdout


def test_site_bom_passa():
    codigo, saida = auditar("site-bom")
    assert codigo == 0, saida
    assert "Total: 0 erro(s)." in saida
    assert "JSON-LD: Dentist" in saida
    assert "404.html ===" not in saida, "a página 404 não deve ser auditada como página comum"


def test_site_ruim_e_pego():
    codigo, saida = auditar("site-ruim")
    assert codigo == 1, "auditoria deveria falhar"
    esperados = [
        "sem lang",
        "Sem <meta name=\"viewport\">",
        "Sem meta description",
        "Sem <link rel=\"canonical\">",
        "Sem <h1>",
        "og:image relativo",
        "Sem dados estruturados JSON-LD",
        "Sem robots.txt",
        "Sem sitemap.xml",
    ]
    faltando = [e for e in esperados if e not in saida]
    assert not faltando, f"erros não detectados: {faltando}"
    assert "Total: 10 erro(s)." in saida


if __name__ == "__main__":
    for nome, fn in list(globals().items()):
        if nome.startswith("test_"):
            fn()
            print(f"ok  {nome}")
