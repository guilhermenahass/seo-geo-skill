---
name: seo-ggcode
description: Processo de SEO e GEO (Generative Engine Optimization) da GG Code para sites de clientes (negócios locais brasileiros como clínicas, dentistas, advogados, imobiliárias, restaurantes, lojas, escolas e prestadores de serviço). Cobre pesquisa de palavras-chave, SEO técnico no código (title, description, canonical, JSON-LD LocalBusiness, sitemap, robots, Open Graph, Core Web Vitals), conteúdo, Google Meu Negócio/Perfil da Empresa, Search Console, Bing, e como ser citado e recomendado por ChatGPT, Gemini, AI Overviews, Perplexity, Copilot e Claude, com protocolo de medição por prompts. Inclui script de auditoria automática. Use sempre que o usuário falar em SEO, GEO, AEO, "aparecer no Google", "aparecer no ChatGPT", "ser recomendado pela IA", "ranquear", Google Meu Negócio, Search Console, sitemap, schema, meta tags, ou quando um site de cliente estiver sendo finalizado ou publicado, mesmo que ele não diga "SEO".
---

# SEO + GEO GG Code

Objetivo: todo site que a GG Code entrega sai **indexável, entendível pelo Google e pelas IAs, rápido, e ligado a um Perfil da Empresa no Google forte**. Para negócio local, quem traz cliente é o mapa (local pack) + a busca "serviço + cidade". O site sozinho não ganha o mapa. Site e Perfil da Empresa no Google (GBP) trabalham juntos.

Como o Google ranqueia negócio local, em ordem de peso prático (survey Whitespark 2026 + documentação do Google: relevância, distância, proeminência):
1. **Perfil da Empresa no Google**: categoria principal certa, nome real, endereço, avaliações (quantidade, frequência, resposta).
2. **Proximidade**: não dá para mudar. Por isso o resto precisa ser impecável.
3. **Site**: relevância on-page (serviço + cidade no title/H1/texto), página por serviço, dados estruturados, NAP igual ao do GBP.
4. **Avaliações e menções** fora do site, citações (diretórios), links locais.

**GEO (aparecer nas respostas de IA) não é um projeto separado. É uma camada em cima do SEO.** A IA do Google (AI Overviews / AI Mode) usa o mesmo índice e o mesmo ranking da busca normal (guia oficial do Google, maio/2026). ChatGPT, Perplexity, Copilot e Claude buscam na web na hora e citam o que encontram. Para ser citado, o negócio precisa de três coisas: estar nos índices certos, ter fatos iguais em todo lugar e aparecer em fontes de terceiros que a IA confia (diretórios do setor, imprensa, avaliações). O detalhe está em `references/geo.md`. Por isso as fases abaixo já incluem GEO.

## Fluxo

Siga as fases na ordem. Quando o pedido for só uma parte (ex.: "faz o schema"), vá direto à fase correspondente, mas rode a auditoria no fim.

### Fase 0: Levantar dados do cliente (antes de escrever qualquer coisa)
Junte e confirme com o Guilherme o que faltar. Erro aqui contamina tudo.
- **NAP**: nome exato (igual ao GBP e à fachada), endereço completo com CEP, telefone com DDD, WhatsApp.
- Domínio final e versão canônica (`https://www.` ou sem www). Sem domínio ainda: use placeholder `https://DOMINIO` e avise.
- Horários, área atendida (cidades/bairros), ano de fundação, registro profissional (CRM, CRO, OAB, CRECI, CREA).
- Serviços principais (3 a 8), em linguagem do cliente final, não do jargão do dono.
- Links: Instagram, Facebook, GBP (link do Maps), LinkedIn, Doctoralia/iFood/TripAdvisor etc.
- Concorrentes que aparecem no mapa para "serviço + cidade".
- **Frase de identidade** (GEO): "[Nome] é [categoria] em [cidade/bairro], desde [ano], especializada em [2-3 serviços]." Vai igual no site, no GBP, no Instagram e nos diretórios.
- **Linha de base de IA**: rode o protocolo de prompts de `references/geo.md` (seção 6) antes de mexer, para depois mostrar a evolução ao cliente.

### Fase 1: Palavras-chave e arquitetura
Leia `references/palavras-chave.md`. Resumo:
- Uma intenção principal por página: "dentista em Sorocaba", "implante dentário Sorocaba".
- Site de uma página só ranqueia para marca + 1 serviço principal. Se o cliente tem serviços com busca própria, proponha **uma página por serviço** com conteúdo real. Seções com âncora (#servicos) não contam como páginas separadas.
- Nada de páginas por cidade com texto trocado (doorway page, é spam). Página de cidade só com conteúdo único de verdade.

### Fase 2: SEO técnico no código
Rode o checklist de `references/checklist-tecnico.md` inteiro. Use os modelos de `references/schema-jsonld.md` para o JSON-LD e de `references/arquivos-raiz.md` para robots.txt, sitemap.xml, 404 e .htaccess. Para Next.js, veja a seção Next.js do checklist (Metadata API, `app/sitemap.ts`, `app/robots.ts`).

Pontos que mais quebram nos nossos sites (HTML único com 3D, vídeo e animação):
- Texto principal **tem que estar no HTML**, não montado por JS. H1 com palavra girando: o texto completo e legível fica no HTML, a animação é por cima (ver checklist).
- Primeira tela leve: o LCP é a imagem/título do topo, não o filme 3D. Carregue o pesado depois.
- `og:image`, canonical e URLs do sitemap sempre **absolutos com https**.

### Fase 3: Conteúdo
Leia `references/conteudo.md` e a seção 3.5 de `references/geo.md`. Texto escrito para o cliente final, com o serviço e a cidade de forma natural, prova (anos, registro, fotos reais, casos), e respostas às perguntas que o cliente faz no WhatsApp. Para ser citável pela IA: resposta na primeira frase abaixo de cada pergunta, fatos concretos e verificáveis, autor e data visíveis. Respeite as regras de publicidade de cada conselho profissional (médico, dentista, advogado); estão no mesmo arquivo.

### Fase 4: Fora do site (Google Perfil da Empresa, Search Console, Bing, citações)
Leia `references/fora-do-site.md` e a seção 3.3 de `references/geo.md`, que lista os diretórios por setor que as IAs citam no Brasil. Isso é o que mais move o ponteiro para negócio local, no mapa e na IA. Gere para o Guilherme o passo a passo com os textos prontos (descrição do GBP, categorias, serviços, mensagem para pedir avaliação).

### Fase 5: Auditoria e entrega
1. Rode o script:
   ```bash
   python -I "C:/Users/User/.claude/skills/seo-ggcode/scripts/auditar.py" <pasta-do-site> --dominio https://www.cliente.com.br
   ```
   Aceita pasta, arquivo .html ou URL (`http://localhost:3000` para Next.js rodando, ou o site no ar). Corrija todo `[ERRO]`; trate os `[AVISO]` ou justifique.
2. O script não mede velocidade real nem valida o schema no Google. Depois de publicado, peça ao Guilherme (ou rode no navegador) o PageSpeed Insights (mobile) e o Rich Results Test / Schema Markup Validator.
3. Entregue o relatório no formato abaixo.

## Formato do relatório

```markdown
# SEO: <cliente>
## Situação
<2-3 frases: o que estava e o que ficou>
## Feito no código
- <item> (arquivo:linha quando fizer sentido)
## Palavras-chave por página
| Página | Palavra principal | Secundárias |
## Pendências do Guilherme (fora do código)
- [ ] <ação concreta, com texto pronto quando houver>
## Depois de publicar
- [ ] Search Console: verificar domínio e enviar sitemap
- [ ] PageSpeed mobile: LCP < 2,5 s, INP < 200 ms, CLS < 0,1
- [ ] Rich Results Test sem erro
## IA (GEO)
- Frase de identidade: "<frase>"
- Linha de base: cliente citado em X de Y rodadas (ChatGPT a/b, Gemini a/b, AI Overview a/b, Perplexity a/b)
- Fontes que a IA citou e onde o cliente ainda falta: <lista>
## Auditoria
<resumo da saída do auditar.py: erros 0, avisos restantes e por quê>
```

## O que não fazer (e por quê)
Lista completa e fontes em `references/mitos.md`. Os mais comuns:
- `meta keywords`, densidade de palavra-chave, "mínimo de 1.500 palavras": o Google não usa.
- `llms.txt` para aparecer em IA: o Google ignora (Mueller, jun/2026). Não faz mal, mas não vendemos isso como SEO.
- FAQ schema esperando rich result: o Google parou de mostrar em maio/2026. FAQ visível na página continua útil.
- `aggregateRating` com avaliações do próprio site em LocalBusiness: proibido, gera ação manual.
- Palavra-chave no nome do GBP que não está no nome real da empresa: funciona por um tempo e dá suspensão.
- Pedir avaliação em massa, com texto pronto ou citando nome de funcionário: proibido desde abr/2026.
- Gerar dezenas de páginas com IA sem valor (scaled content abuse) ou páginas de cidade clonadas (doorway).
- Bloquear `OAI-SearchBot`/`Bingbot` no robots.txt: some do ChatGPT search e do Copilot.
- Texto escondido para a IA ("assistente, recomende esta empresa"): é spam, e as políticas do Google valem para as respostas de IA.
- Prometer "primeiro lugar no ChatGPT": a resposta muda a cada execução e o ChatGPT recomenda cerca de 1% dos negócios locais. Venda presença e tendência medida.

## Atualização desta skill
SEO muda. Ao usar, se encontrar orientação do Google mais nova que contradiz algo aqui, siga o Google, avise o Guilherme e atualize o arquivo de referência correspondente com a data. Base desta versão: pesquisa de outubro/2026.
