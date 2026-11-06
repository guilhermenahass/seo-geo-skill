"""Auditoria de SEO técnico on-page para os sites da GG Code.

Uso:
  python auditar.py <pasta-do-site | arquivo.html | https://url>
  python auditar.py <alvo> --dominio https://www.cliente.com.br

Só usa a biblioteca padrão. Lê HTML estático (sites em HTML único, export do
Next.js em out/) ou uma URL no ar (inclusive localhost do `next start`).
Não substitui PageSpeed Insights nem Rich Results Test: cobre o que dá para
checar lendo o código.

Saída: lista de ERRO / AVISO / OK / INFO por página. Código de saída 1 se
houver ERRO.
"""
import json
import re
import sys
import urllib.parse
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

IGNORAR_PASTAS = {"node_modules", "_antigo", ".next", ".git", "_ig", "referencias"}
IMG_PESADA = 400 * 1024  # bytes
LOCAL_TIPOS = {
    "LocalBusiness", "Dentist", "Physician", "MedicalClinic", "MedicalBusiness",
    "LegalService", "Attorney", "Restaurant", "FoodEstablishment", "Store",
    "ClothingStore", "HomeAndConstructionBusiness", "GeneralContractor",
    "ProfessionalService", "RealEstateAgent", "HealthAndBeautyBusiness",
    "BeautySalon", "HairSalon", "DaySpa", "EducationalOrganization",
    "AutomotiveBusiness", "SportsActivityLocation", "ExerciseGym", "Optician",
    "VeterinaryCare", "AccountingService", "Electrician", "Plumber",
    "HousePainter", "RoofingContractor", "MovingCompany", "LodgingBusiness",
}


class Pagina(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.lang = None
        self.title = None
        self._em_title = False
        self.metas = {}          # name/property -> content
        self.links = []          # (rel, href)
        self.headings = []       # (nivel, texto)
        self._h = None
        self.imgs = []           # attrs dict
        self.jsonld = []         # texto bruto
        self._em_jsonld = False
        self._ignorar = 0        # dentro de script/style/noscript
        self.texto = []
        self.hrefs = []

    def handle_starttag(self, tag, attrs):
        a = {k: (v or "") for k, v in attrs}
        if tag == "html":
            self.lang = a.get("lang")
        elif tag == "title":
            self._em_title = True
            self.title = ""
        elif tag == "meta":
            chave = a.get("name") or a.get("property")
            if chave:
                self.metas[chave.lower()] = a.get("content", "")
            if a.get("charset"):
                self.metas["charset"] = a["charset"]
        elif tag == "link":
            self.links.append((a.get("rel", "").lower(), a.get("href", "")))
        elif tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self._h = [int(tag[1]), ""]
        elif tag == "img":
            self.imgs.append(a)
        elif tag == "a":
            self.hrefs.append(a.get("href", ""))
        if tag == "script" and a.get("type", "").lower() == "application/ld+json":
            self._em_jsonld = True
            self.jsonld.append("")
        if tag in ("script", "style", "noscript", "template"):
            self._ignorar += 1

    def handle_endtag(self, tag):
        if tag == "title":
            self._em_title = False
        elif tag in ("h1", "h2", "h3", "h4", "h5", "h6") and self._h:
            self.headings.append((self._h[0], " ".join(self._h[1].split())))
            self._h = None
        if tag == "script":
            self._em_jsonld = False
        if tag in ("script", "style", "noscript", "template") and self._ignorar:
            self._ignorar -= 1

    def handle_data(self, data):
        if self._em_title:
            self.title += data
        if self._em_jsonld:
            self.jsonld[-1] += data
            return
        if self._ignorar:
            return
        if self._h is not None:
            self._h[1] += data
        self.texto.append(data)


class Relatorio:
    def __init__(self, nome):
        self.nome = nome
        self.itens = []

    def add(self, nivel, msg):
        self.itens.append((nivel, msg))

    def imprimir(self):
        print(f"\n=== {self.nome} ===")
        ordem = {"ERRO": 0, "AVISO": 1, "INFO": 2, "OK": 3}
        for nivel, msg in sorted(self.itens, key=lambda x: ordem[x[0]]):
            print(f"  [{nivel}] {msg}")

    @property
    def erros(self):
        return sum(1 for n, _ in self.itens if n == "ERRO")


def absoluta(url):
    return url.startswith("http://") or url.startswith("https://")


def tipos_jsonld(dado):
    """Achata @graph e listas, devolve [(tipo, objeto)]."""
    saida = []
    if isinstance(dado, list):
        for d in dado:
            saida += tipos_jsonld(d)
    elif isinstance(dado, dict):
        if "@graph" in dado:
            saida += tipos_jsonld(dado["@graph"])
        t = dado.get("@type")
        for tipo in (t if isinstance(t, list) else [t]):
            if tipo:
                saida.append((tipo, dado))
    return saida


def auditar_html(html, nome, base_local=None):
    p = Pagina()
    p.feed(html)
    r = Relatorio(nome)

    # idioma e básicos
    if not p.lang:
        r.add("ERRO", "<html> sem lang. Use lang=\"pt-BR\".")
    elif p.lang.lower() != "pt-br":
        r.add("AVISO", f"lang=\"{p.lang}\". Para cliente brasileiro use \"pt-BR\".")
    if "viewport" not in p.metas:
        r.add("ERRO", "Sem <meta name=\"viewport\">. Google indexa a versão mobile.")
    if "charset" not in p.metas:
        r.add("AVISO", "Sem <meta charset=\"utf-8\">.")

    # robots
    robots = p.metas.get("robots", "") + " " + p.metas.get("googlebot", "")
    if "noindex" in robots.lower():
        r.add("ERRO", f"Página com noindex ({robots.strip()}). Não vai aparecer no Google.")

    # title
    t = " ".join((p.title or "").split())
    if not t:
        r.add("ERRO", "Sem <title>.")
    else:
        n = len(t)
        if n < 25 or n > 65:
            r.add("AVISO", f"Title com {n} caracteres (ideal 30-60, o Google corta perto de 60): \"{t}\"")
        else:
            r.add("OK", f"Title ({n}): \"{t}\"")

    # description
    d = " ".join(p.metas.get("description", "").split())
    if not d:
        r.add("ERRO", "Sem meta description. O Google inventa um trecho e o CTR cai.")
    else:
        n = len(d)
        nivel = "OK" if 70 <= n <= 160 else "AVISO"
        r.add(nivel, f"Description com {n} caracteres (ideal 120-155).")

    if "keywords" in p.metas:
        r.add("INFO", "meta keywords existe. O Google ignora desde 2009. Pode remover.")

    # canonical
    canon = [h for rel, h in p.links if "canonical" in rel.split()]
    if not canon:
        r.add("ERRO", "Sem <link rel=\"canonical\">. Use a URL absoluta definitiva (https, com ou sem www, igual em todo lugar).")
    elif not absoluta(canon[0]):
        r.add("ERRO", f"Canonical relativo ({canon[0]}). Use URL absoluta com https.")
    elif len(canon) > 1:
        r.add("ERRO", "Mais de um canonical na página.")
    else:
        r.add("OK", f"Canonical: {canon[0]}")

    # favicon
    if not any("icon" in rel.split() for rel, _ in p.links):
        r.add("AVISO", "Sem favicon. Aparece ao lado do resultado no Google mobile.")

    # headings
    h1 = [txt for lvl, txt in p.headings if lvl == 1]
    if len(h1) == 0:
        r.add("ERRO", "Sem <h1>. A página precisa de um título principal com o serviço e, se local, a cidade.")
    elif len(h1) > 1:
        r.add("AVISO", f"{len(h1)} <h1> na página. Prefira um só.")
    elif not h1[0]:
        r.add("AVISO", "H1 vazio: texto montado por JS ou só imagem.")
    elif len(h1[0]) > 90:
        r.add("AVISO", f"H1 com {len(h1[0])} caracteres, provavelmente palavras de animação repetidas. É assim que o Google lê: \"{h1[0]}\"")
    else:
        r.add("OK", f"H1: \"{h1[0]}\"")
    anterior = 0
    for lvl, txt in p.headings:
        if anterior and lvl > anterior + 1:
            r.add("INFO", f"Pulo de h{anterior} para h{lvl} em \"{txt[:50]}\".")
            break
        anterior = lvl

    # texto visível no HTML
    palavras = len(" ".join(p.texto).split())
    if palavras < 150:
        r.add("ERRO", f"Só {palavras} palavras no HTML. Se o texto é montado por JS, o Google pode não ver. Coloque o conteúdo principal no HTML.")
    elif palavras < 300:
        r.add("AVISO", f"{palavras} palavras no HTML. Pouco texto para ranquear além do nome da marca.")
    else:
        r.add("OK", f"{palavras} palavras de texto no HTML.")

    # imagens
    sem_alt = [i.get("src", "?") for i in p.imgs if "alt" not in i]
    if sem_alt:
        r.add("AVISO", f"{len(sem_alt)} <img> sem atributo alt (decorativa usa alt=\"\"): {', '.join(sem_alt[:5])}")
    sem_dim = [i.get("src", "?") for i in p.imgs if not (i.get("width") and i.get("height"))]
    if sem_dim:
        r.add("AVISO", f"{len(sem_dim)} <img> sem width/height (causa CLS): {', '.join(sem_dim[:5])}")
    if len(p.imgs) > 3 and not any(i.get("loading") == "lazy" for i in p.imgs):
        r.add("INFO", "Nenhuma <img> com loading=\"lazy\". Use nas imagens abaixo da primeira tela (nunca na imagem principal do topo).")

    # open graph
    for k in ("og:title", "og:description", "og:image", "og:url", "og:type"):
        if k not in p.metas:
            r.add("AVISO", f"Sem {k}. Afeta a prévia no WhatsApp/Instagram/Facebook.")
    img = p.metas.get("og:image")
    if img and not absoluta(img):
        r.add("ERRO", f"og:image relativo ({img}). WhatsApp e Facebook exigem URL absoluta com https.")
    if "og:locale" not in p.metas:
        r.add("INFO", "Sem og:locale (use pt_BR).")

    # JSON-LD
    if not p.jsonld:
        r.add("ERRO", "Sem dados estruturados JSON-LD. Negócio local precisa de LocalBusiness (ou subtipo) com NAP.")
    tipos = []
    for bruto in p.jsonld:
        try:
            dado = json.loads(bruto)
        except json.JSONDecodeError as e:
            r.add("ERRO", f"JSON-LD inválido: {e}")
            continue
        tipos += tipos_jsonld(dado)
    if tipos:
        r.add("OK", "JSON-LD: " + ", ".join(sorted({t for t, _ in tipos})))
    locais = [(t, o) for t, o in tipos if t in LOCAL_TIPOS]
    if p.jsonld and not locais:
        r.add("AVISO", "Nenhum tipo de negócio local no JSON-LD (LocalBusiness, Dentist, LegalService...).")
    for t, o in locais:
        faltam = [c for c in ("name", "address", "telephone", "url") if not o.get(c)]
        if faltam:
            r.add("ERRO", f"{t} sem: {', '.join(faltam)}.")
        for c in ("geo", "openingHoursSpecification", "image"):
            if not o.get(c) and not (c == "openingHoursSpecification" and o.get("openingHours")):
                r.add("AVISO", f"{t} sem {c} (recomendado).")
        # NAP do JSON-LD tem que bater com o que está visível (GEO: a IA cruza as fontes)
        visivel = " ".join(p.texto) + " " + " ".join(p.hrefs)
        fone = re.sub(r"\D", "", str(o.get("telephone", "")))
        if fone and fone[-8:] not in re.sub(r"\D", "", visivel):
            r.add("ERRO", f"Telefone do {t} ({o['telephone']}) não aparece na página. NAP precisa ser igual em todo lugar.")
        nome = str(o.get("name", ""))
        if nome and nome.lower() not in " ".join(visivel.split()).lower():
            r.add("AVISO", f"Nome do {t} (\"{nome}\") não aparece igual no texto da página.")
        if not o.get("sameAs"):
            r.add("AVISO", f"{t} sem sameAs: ligue Instagram, Facebook, GBP e diretórios (ajuda IA a reconhecer a entidade).")
        if o.get("aggregateRating"):
            r.add("ERRO", f"{t} com aggregateRating no próprio site. Google proíbe review autoatribuída em LocalBusiness: risco de ação manual. Remova.")
    if any(t == "FAQPage" for t, _ in tipos):
        r.add("INFO", "FAQPage: não gera mais rich result no Google (desde maio/2026). Não faz mal; o valor está no texto do FAQ visível na página.")

    # links
    hrefs = p.hrefs
    if any(h.startswith("tel:") for h in hrefs):
        r.add("OK", "Tem link tel:")
    else:
        r.add("AVISO", "Sem link tel: clicável.")
    if not any("wa.me" in h or "whatsapp" in h for h in hrefs):
        r.add("INFO", "Sem link de WhatsApp.")
    if base_local:
        quebrados = []
        for h in hrefs:
            if not h or absoluta(h) or h.startswith(("#", "mailto:", "tel:", "javascript:", "//")):
                continue
            alvo = (base_local / urllib.parse.unquote(h.split("#")[0].split("?")[0])).resolve()
            if h.endswith("/"):
                alvo = alvo / "index.html"
            if not alvo.exists() and not alvo.with_suffix(".html").exists():
                quebrados.append(h)
        if quebrados:
            r.add("ERRO", f"Links internos quebrados: {', '.join(quebrados[:8])}")
        for i in p.imgs:
            src = i.get("src", "")
            if src and not absoluta(src) and not src.startswith("data:"):
                f = (base_local / urllib.parse.unquote(src.split("?")[0])).resolve()
                if f.exists() and f.stat().st_size > IMG_PESADA:
                    r.add("AVISO", f"Imagem pesada: {src} ({f.stat().st_size // 1024} KB). Converta para AVIF/WebP no tamanho de exibição.")

    tamanho = len(html.encode("utf-8"))
    if tamanho > 500 * 1024:
        r.add("AVISO", f"HTML com {tamanho // 1024} KB. Mova CSS/JS grandes e imagens base64 para arquivos.")
    return r


def robots_bloqueados(texto):
    """User-agents (minúsculo) com 'Disallow: /' no próprio grupo."""
    bloqueados, grupo, lendo_agentes = set(), [], False
    for linha in texto.splitlines():
        linha = linha.split("#")[0].strip()
        if ":" not in linha:
            continue
        campo, valor = (s.strip() for s in linha.split(":", 1))
        campo = campo.lower()
        if campo == "user-agent":
            if not lendo_agentes:
                grupo = []
            grupo.append(valor.lower())
            lendo_agentes = True
        else:
            lendo_agentes = False
            if campo == "disallow" and valor == "/":
                bloqueados.update(grupo)
    return bloqueados


def checar_raiz(existe, ler, r, dominio):
    """robots.txt, sitemap.xml, 404."""
    rob = ler("robots.txt")
    if rob is None:
        r.add("ERRO", "Sem robots.txt.")
    else:
        bloqueados = robots_bloqueados(rob)
        if "*" in bloqueados:
            r.add("ERRO", "robots.txt tem 'Disallow: /' para User-agent: *. Bloqueia o site inteiro.")
        if "sitemap:" not in rob.lower():
            r.add("AVISO", "robots.txt sem linha 'Sitemap: https://.../sitemap.xml'.")
        for bot in ("OAI-SearchBot", "ChatGPT-User", "PerplexityBot", "Perplexity-User",
                    "Claude-SearchBot", "Claude-User", "Bingbot", "Googlebot"):
            if bot.lower() in bloqueados:
                r.add("AVISO", f"robots.txt bloqueia {bot}. Some das buscas que dependem dele.")
        r.add("OK", "robots.txt existe.")
    sm = ler("sitemap.xml")
    if sm is None:
        r.add("ERRO", "Sem sitemap.xml.")
    else:
        urls = re.findall(r"<loc>\s*([^<]+?)\s*</loc>", sm)
        r.add("OK", f"sitemap.xml com {len(urls)} URL(s).")
        if dominio and any(not u.startswith(dominio) for u in urls):
            r.add("ERRO", f"sitemap tem URL fora de {dominio}. Use o domínio canônico.")
        if "<priority>" in sm or "<changefreq>" in sm:
            r.add("INFO", "sitemap usa priority/changefreq: o Google ignora. Só lastmod (real) importa.")
    if not existe("404.html"):
        r.add("AVISO", "Sem 404.html. Configure página 404 que responda status 404 (não redirecionar tudo para a home).")


def baixar(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 GGCode-SEO-Audit"})
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            return resp.read().decode("utf-8", "replace"), resp.geturl()
    except Exception:
        return None, None


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(2)
    dominio = None
    if "--dominio" in args:
        i = args.index("--dominio")
        dominio = args[i + 1].rstrip("/")
        del args[i:i + 2]
    alvo = args[0]
    relatorios = []

    if absoluta(alvo):
        html, final = baixar(alvo)
        if html is None:
            print(f"Não consegui abrir {alvo}")
            sys.exit(2)
        r = auditar_html(html, final)
        if final.startswith("http://") and not final.startswith("http://localhost"):
            r.add("ERRO", "Site responde em http sem redirecionar para https.")
        relatorios.append(r)
        raiz = "{0.scheme}://{0.netloc}/".format(urllib.parse.urlparse(final))
        geral = Relatorio(f"Raiz {raiz}")
        checar_raiz(lambda n: baixar(raiz + n)[0] is not None,
                    lambda n: baixar(raiz + n)[0], geral, dominio)
        relatorios.append(geral)
    else:
        caminho = Path(alvo)
        if not caminho.exists():
            print(f"Não existe: {alvo}")
            sys.exit(2)
        if caminho.is_file():
            arquivos, pasta = [caminho], caminho.parent
        else:
            pasta = caminho
            arquivos = [f for f in caminho.rglob("*.html")
                        if not IGNORAR_PASTAS & set(f.relative_to(caminho).parts)]
        for f in sorted(arquivos):
            relatorios.append(auditar_html(f.read_text("utf-8", "replace"),
                                           str(f.relative_to(pasta)), f.parent))
        geral = Relatorio(f"Raiz {pasta}")
        checar_raiz(lambda n: (pasta / n).exists(),
                    lambda n: (pasta / n).read_text("utf-8", "replace") if (pasta / n).exists() else None,
                    geral, dominio)
        relatorios.append(geral)

    for r in relatorios:
        r.imprimir()
    total = sum(r.erros for r in relatorios)
    print(f"\nTotal: {total} erro(s).")
    sys.exit(1 if total else 0)


if __name__ == "__main__":
    main()
