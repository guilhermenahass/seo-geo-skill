# SEO + GEO para negócios locais: skill para Claude Code

[![CI](https://github.com/guilhermenahass/seo-geo-skill/actions/workflows/ci.yml/badge.svg)](https://github.com/guilhermenahass/seo-geo-skill/actions/workflows/ci.yml)

**Um agente de IA que aplica SEO técnico e GEO (Generative Engine Optimization) nos sites da GG Code, para o cliente aparecer no Google e ser recomendado pelo ChatGPT, Gemini, Perplexity, Copilot e Claude.**

Escrevi esta skill para o [Claude Code](https://docs.anthropic.com/en/docs/claude-code) transformar o processo de SEO da minha agência em algo que o agente executa sozinho e sempre do mesmo jeito. Quando um site de cliente está sendo finalizado, o agente reconhece o contexto e segue as fases da skill: levanta os dados do negócio, ajusta o código, gera os dados estruturados, roda a auditoria e entrega o checklist do que precisa ser feito fora do site.

## Por que GEO

Para negócios locais, a busca está migrando para respostas de IA. Num levantamento de 2026 com 350 mil locais, o ChatGPT recomendou só 1,2% dos negócios, contra 35,9% que aparecem no mapa do Google. Para estar nesses poucos, o negócio precisa de três coisas:

1. Estar nos índices que cada motor usa.
2. Ter os mesmos fatos em todo lugar: site, Google, Instagram e diretórios.
3. Ser citado por fontes de terceiros em que a IA confia.

A skill trata GEO como uma camada sobre o SEO, e não como truque. Cada recomendação traz a fonte e o nível de confiança (alta, média ou baixa), porque boa parte dos números públicos vem de fornecedores de ferramenta.

## O que tem dentro

```
seo-ggcode/
  SKILL.md                     fluxo em fases que o agente segue (e quando ativar)
  scripts/auditar.py           auditoria automática de SEO técnico (só biblioteca padrão)
  references/
    geo.md                     como cada IA escolhe quem citar + protocolo de medição por prompts
    checklist-tecnico.md       title, description, canonical, Core Web Vitals, robots, 404
    schema-jsonld.md           JSON-LD LocalBusiness e subtipos (Dentist, Physician, LegalService...)
    palavras-chave.md          pesquisa "serviço + cidade" para negócio local brasileiro
    conteudo.md                páginas por serviço, FAQ, texto que a IA consegue extrair
    fora-do-site.md            Perfil da Empresa no Google, Bing Places, diretórios por setor
    arquivos-raiz.md           robots.txt (quais robôs de IA liberar) e sitemap
    mitos.md                   o que não funciona ou é arriscado
```

## Auditoria automática

O `auditar.py` lê uma pasta, um arquivo HTML ou uma URL no ar e aponta o que está errado. Ele confere:
- title, description, canonical e H1;
- texto no HTML (sem depender de JavaScript);
- JSON-LD do negócio local e a consistência do NAP (nome, endereço e telefone);
- Open Graph, imagens pesadas ou sem dimensão (que causam CLS);
- robots.txt, sitemap e página 404.

O script sai com código 1 quando há erro, então dá para usar como trava antes de publicar.

**Testes:** a auditoria é testada a cada commit no GitHub Actions com dois sites de exemplo em `tests/fixtures/`. O site certo precisa passar com zero erros, e o site com 10 erros conhecidos precisa ter todos detectados. O teste já pegou um bug: a página 404 era auditada como página comum e acusava `noindex`, que numa 404 é o correto.

```
$ python seo-ggcode/scripts/auditar.py https://ibanhezservicosind.com

=== https://ibanhezservicosind.com ===
  [AVISO] H1 com 98 caracteres, provavelmente palavras de animação repetidas. É assim que o Google lê: "Manutenção, montagem industrial e construção civil Da base à manutenção, excelência em cada etapa."
  [AVISO] GeneralContractor sem geo (recomendado).
  [OK] Title (58): "Ibanhez: manutenção industrial e obras civis – Sorocaba/SP"
  [OK] Description com 146 caracteres (ideal 120-155).
  [OK] Canonical: https://ibanhezservicosind.com/
  [OK] 1038 palavras de texto no HTML.
  [OK] JSON-LD: GeneralContractor, WebSite
  ...
Total: 0 erro(s).
```

<sub>Saída real em um site de cliente da GG Code.</sub>

**Resultado na prática:** na primeira rodada, em novembro de 2026, a auditoria achou erros em 3 dos sites no ar (canonical ausente, falta de JSON-LD, endereço faltando nos dados estruturados). Depois das correções, **5 de 6 sites passam com zero erros**. O sexto é o da própria agência, que não tem endereço físico para declarar.

## Medição de GEO

As respostas das IAs variam muito entre execuções, então a skill define um protocolo:
1. Montar um conjunto fixo de perguntas reais de cliente (por exemplo, "urologista bom na Barra da Tijuca").
2. Rodar as mesmas perguntas em cada motor, várias vezes.
3. Registrar se o negócio foi citado e de qual fonte a IA tirou a informação.

O resultado é lido como tendência ao longo das semanas, não como foto de um dia.

## Como usar

1. Copie a pasta `seo-ggcode/` para `~/.claude/skills/`.
2. No Claude Code, peça algo como "o site da clínica está pronto, faz o SEO" ou "quero que ela apareça no ChatGPT". A skill ativa sozinha.
3. Para usar só a auditoria: `python seo-ggcode/scripts/auditar.py <pasta | arquivo.html | https://url>`.

## Stack

Claude Code (Agent Skills) · Python (biblioteca padrão) · schema.org / JSON-LD · Google Search Console · Bing Webmaster Tools · IndexNow

---

<sub>© 2026 Guilherme Reis Nahass, GG Code. Licença MIT.</sub>
