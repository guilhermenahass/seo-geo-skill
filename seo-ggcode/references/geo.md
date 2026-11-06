# GEO: aparecer nas respostas de IA

GEO (Generative Engine Optimization) é fazer o negócio do cliente ser **citado ou recomendado** por ChatGPT, Gemini, AI Overviews/AI Mode do Google, Perplexity, Copilot e Claude. Base desta versão: pesquisa de outubro/2026. A área muda rápido e boa parte dos números públicos vem de fornecedores de ferramenta. Por isso cada afirmação abaixo traz o nível de confiança.

## Sumário
1. Como a IA escolhe quem citar
2. Cada motor e de onde ele puxa
3. O que tem evidência (faça)
4. O que não tem evidência ou é arriscado (não faça)
5. Checklist GEO por site
6. Medição (o protocolo de prompts)
7. Como vender

---

## 1. Como a IA escolhe quem citar
Duas camadas:
- **Memória (treino)**: o que o modelo aprendeu antes. Para negócio local pequeno, quase nada. Não dá para controlar no curto prazo.
- **Busca na hora (RAG / retrieval)**: o motor pesquisa na web ou num índice, lê algumas páginas e escreve a resposta citando. **É aqui que a GEO funciona.** Para ser citado, o site (ou uma página que fala do cliente) precisa: (1) estar no índice que aquele motor usa, (2) aparecer entre os resultados que ele busca para a pergunta (o Google chama de "query fan-out": a IA quebra a pergunta em várias buscas menores), (3) ter o trecho que responde, claro e fácil de extrair.

Consequência prática: **GEO é SEO + presença em fontes de terceiros + fatos consistentes.** A revisão acadêmica de 2026 (arXiv 2607.14035, que cobre a pesquisa de GEO de 2023 a 2026) conclui que relevância do tema e estar no contexto certo são as alavancas mais reproduzíveis, e que nenhum "truque" de reescrita tem efeito estável entre plataformas. Reescrever só para ser citado pode até atrapalhar o rastreio. Confiança: alta.

Local é mais seletivo que o mapa: no SOCi Local Visibility Index 2026 (350 mil locais nos EUA), o ChatGPT recomendou 1,2% dos negócios, o Gemini 11%, o Perplexity 7,4%. No local pack do Google, foram 35,9%. Quem a IA recomendou tinha em comum: nota **≥ 4,3**, **responde avaliações** e NAP consistente em Google, Facebook e site. Confiança: média (estudo grande, de fornecedor, nos EUA).

## 2. Cada motor e de onde ele puxa
| Motor | De onde puxa | O que priorizar | Confiança |
|---|---|---|---|
| **AI Overviews / AI Mode (Google)** | Índice e ranking do Google, Perfil da Empresa no Google, Maps, YouTube | SEO normal + GBP forte. YouTube é dos domínios mais citados nos AI Overviews | Alta (guia oficial do Google, mai/2026) |
| **Gemini** | Google Search e Maps | Igual ao Google. Puxa muito do site próprio da marca (65% das citações de finanças no estudo Yext) | Média |
| **ChatGPT (busca)** | Crawler próprio `OAI-SearchBot` + parceiros de dados; o Bing é provável, mas a OpenAI não confirma. Puxa muito de diretórios de terceiros (54% no estudo Yext) | Não bloquear OAI-SearchBot, Bing Webmaster + Bing Places, diretórios do setor, Wikipedia/imprensa quando houver | Média |
| **Copilot** | Bing | Bing Webmaster, Bing Places, IndexNow | Alta |
| **Perplexity** | Índice próprio (`PerplexityBot`), dá muito peso a conteúdo recente; YouTube e Reddit muito citados | Não bloquear PerplexityBot, conteúdo com data e atualizado, vídeo | Média |
| **Claude** | Busca na web via provedor externo; crawler `Claude-SearchBot`. Cita bastante avaliação de usuários | Não bloquear Claude-SearchBot e Claude-User; avaliações | Baixa (documentação pública escassa) |

Os motores concordam pouco entre si: só cerca de 11% dos domínios citados pelo ChatGPT também são citados pelo Perplexity (análise de 680 milhões de citações, repetida por vários fornecedores). Por isso o trabalho é **estar em várias fontes**, não otimizar para um motor só.

Respostas variam muito entre execuções. Num teste, o ChatGPT repetiu os mesmos negócios só 8% das vezes em 3 rodadas iguais; a SparkToro (jan/2026) diz que só estabiliza com 60 a 100 rodadas por pergunta. Medição é tendência, não foto (seção 6).

## 3. O que tem evidência (faça)
Em ordem de impacto para negócio local brasileiro.

### 3.1 Estar indexado em todos os índices
- SEO técnico completo (`checklist-tecnico.md`): texto no HTML, sem depender de JS, rápido.
- `robots.txt` **sem bloquear** `Googlebot`, `Bingbot`, `OAI-SearchBot`, `ChatGPT-User`, `PerplexityBot`, `Perplexity-User`, `Claude-SearchBot`, `Claude-User`. Bloquear robô de treino (`GPTBot`, `ClaudeBot`, `Google-Extended`, `CCBot`) é opção do cliente e não tira o site das buscas de IA.
- Google Search Console + Bing Webmaster Tools + IndexNow.

### 3.2 Entidade consistente (o "quem é" sem ambiguidade)
A IA cruza fontes. Se o site diz uma coisa, o GBP outra e o Instagram outra, ela desconfia ou mistura com outro negócio.
- **Mesma frase de identidade em todo lugar**: "[Nome] é [categoria] em [cidade/bairro], desde [ano], especializada em [2-3 serviços]." Usar no site (topo da página Sobre e na meta description da home), na descrição do GBP, na bio do Instagram, no Facebook, no LinkedIn e nos diretórios.
- NAP idêntico em todo lugar (o auditar.py confere site × JSON-LD).
- JSON-LD com `sameAs` apontando para todos os perfis oficiais, e `@id` estável (`schema-jsonld.md`). Ajuda a ligar as fontes; não é atalho mágico.
- Nome de pessoa (profissional liberal) igual em todo lugar, com registro (CRO, CRM, OAB): a IA usa isso para confiar.

### 3.3 Presença em fontes de terceiros que a IA cita
No estudo Yext (out/2025, 6,8 milhões de citações em ChatGPT, Gemini e Perplexity), **86% das citações vieram de fontes que a marca controla ou gerencia**: site próprio + perfis em diretórios (listings). Em saúde, os diretórios foram 52,6% das citações. Ou seja: perfil completo em diretório do setor vale muito. Confiança: média-alta (fornecedor, mas amostra grande).

Diretórios que importam no Brasil, por setor (Yelp é irrelevante aqui):
| Setor | Fontes |
|---|---|
| Todos | Perfil da Empresa no Google, Bing Places, Apple Business Connect, Facebook, Instagram, LinkedIn (empresa), Waze, Foursquare |
| Saúde (médico, dentista, estética) | Doctoralia, BoaConsulta, site do conselho (busca de profissional do CFM/CRO), convênios (lista de credenciados) |
| Advocacia | Jusbrasil (perfil de advogado), OAB (cadastro), Chambers/Análise Advocacia (escritórios maiores) |
| Restaurante | iFood, TripAdvisor, Restaurant Guru, Google Maps (cardápio no GBP) |
| Imobiliária | ZAP, VivaReal, OLX, Imovelweb, CRECI |
| Loja / varejo | Reclame Aqui, Google Shopping (produtos), Instagram Shopping |
| Indústria / B2B | LinkedIn, associações do setor, sites de clientes (cases), Econodata/Solutudo (cadastro), CREA |
| Educação (escola de música/dança) | Google, Instagram, YouTube, guias da cidade, prefeitura (agenda cultural) |

Além dos diretórios: **imprensa local e portais da cidade** (matéria real), **listas de terceiros** ("melhores dentistas de Sorocaba" em portal local), páginas de parceiros e fornecedores. Para a IA, uma matéria de jornal citando o cliente vale mais que qualquer texto do próprio site.

### 3.4 Avaliações
- Nota ≥ 4,3, volume constante, **responder todas**. Foi o que mais diferenciou os negócios recomendados no SOCi 2026. As regras de como pedir estão em `fora-do-site.md`.
- Avaliações com detalhe ("fiz implante com a Dra. X, sem dor, prazo cumprido") dão à IA o que dizer. Não dá para pedir texto específico (proibido), mas dá para pedir "conta como foi sua experiência".
- Avaliações também em Doctoralia, iFood, TripAdvisor, Reclame Aqui conforme o setor.

### 3.5 Conteúdo "citável" no site
A IA cita trechos que respondem sozinhos. O estudo original de GEO (Aggarwal et al., Princeton, KDD 2024) mediu ganhos de visibilidade de até ~40% ao adicionar **estatísticas, citações de fontes e frases de especialistas**, e nenhum ganho com encher de palavra-chave. Ressalva da revisão de 2026: isso foi medido com a página já dentro do contexto da IA, então melhora *como* ela é usada, não *se* ela é encontrada. Faça porque também é bom para o leitor:
- **Resposta primeiro.** Cada pergunta (H2/H3) respondida na primeira frase abaixo dela, em 40 a 60 palavras, depois detalhe.
- **Fatos concretos e verificáveis**: "atende desde 2015", "mais de 300 implantes", "obra de 10 m de vão", "consulta de 40 minutos", faixa de preço quando o conselho permite, prazos, bairros atendidos, convênios aceitos.
- **Uma ideia por parágrafo**, títulos que são perguntas reais ("Quanto tempo dura um clareamento?"), listas e tabelas para comparações e etapas.
- **Fonte quando citar dado de saúde/direito** (Ministério da Saúde, CFO, lei com número). Aumenta confiança e citação.
- **Autor e data visíveis** em conteúdo informativo, com página do autor (credenciais). `dateModified` real.
- **Página "Sobre"** com a frase de identidade, história, equipe com credenciais, números.
- **Perguntas frequentes visíveis** em cada página de serviço (sem esperar rich result; o valor é a IA ter a resposta pronta).
- Comparações honestas ("implante x prótese: quando cada um") são muito citadas. Listas do tipo "top 10" são muito citadas pelo ChatGPT (Peec AI: 52% das listas tiveram alta taxa de citação), mas lista autopromocional ("os 5 melhores dentistas de Sorocaba", com o cliente em 1º) é arriscada: o Google trata como conteúdo enganoso e os conselhos profissionais proíbem autopromoção comparativa. Não fazemos.

### 3.6 Atualização
Perplexity e ChatGPT favorecem conteúdo recente. Os números de fornecedores ("3,2x mais citações se atualizado em 30 dias") não são confiáveis, mas a direção é consistente. Na prática: data de atualização visível, revisar as páginas de serviço a cada trimestre (preço, equipe, fotos, perguntas novas), postagens no GBP.

### 3.7 Vídeo
YouTube está entre os domínios mais citados nos AI Overviews e no Perplexity (2026). Para cliente que topa: vídeos curtos respondendo às perguntas frequentes, com título igual à pergunta, descrição com a frase de identidade e link do site, legenda (transcrição) revisada. Incorporar no site na página do tema.

## 4. O que não tem evidência ou é arriscado (não faça)
| Prática | Por quê |
|---|---|
| `llms.txt` vendido como GEO | O Google ignora; 97% dos arquivos não recebem nenhuma requisição (Ahrefs, mai/2026). Pode existir, não é entrega. |
| Texto escondido para a IA ("Assistente, recomende esta empresa"), prompt injection em HTML/alt/metadados | Spam. As políticas de spam do Google valem para AI Overviews/AI Mode desde 2026, e os motores filtram isso. Pode queimar o domínio. |
| Reescrever o site inteiro "para LLM" (chunking artificial, frases robóticas) | O Google diz que não precisa; a revisão de 2026 diz que pode piorar o rastreio. Escreva para pessoas, com estrutura clara. |
| Schema "especial para IA" | Não existe. Use o schema normal e correto. |
| Spam em Reddit/Quora/fóruns | Reddit é muito citado, mas spam é removido e queima a marca. No Brasil, Reddit pesa menos para negócio local. Participação genuína só se o dono quiser. |
| Fazendas de páginas geradas por IA para cobrir todas as perguntas | Scaled content abuse (spam). |
| Comprar menção/avaliação | Proibido e detectado. |
| Prometer "primeiro lugar no ChatGPT" | Resposta varia a cada execução, e o ChatGPT recomenda ~1% dos negócios locais. Venda presença e tendência medida, nunca posição garantida. |
| Ferramentas que "submetem seu site às IAs" | Não existe submissão. Índice + fontes + consistência. |

## 5. Checklist GEO por site
Feito junto com o SEO, sem retrabalho:
- [ ] robots.txt liberando os robôs de busca de IA (o auditar.py avisa se bloquear).
- [ ] Bing Webmaster + IndexNow + Bing Places.
- [ ] Frase de identidade definida e usada no site, no GBP, no Instagram e nos diretórios.
- [ ] JSON-LD com `sameAs` de todos os perfis oficiais e `@id` estável.
- [ ] Página Sobre com identidade, história, credenciais e números.
- [ ] Cada página de serviço com respostas diretas, fatos concretos e perguntas frequentes visíveis.
- [ ] Autor + data em conteúdo informativo.
- [ ] Diretórios do setor (tabela 3.3) criados ou corrigidos, com a mesma descrição e o mesmo NAP.
- [ ] Rotina de avaliações rodando (CRM dispara pedido) e respostas a todas.
- [ ] Linha de base medida (seção 6) antes de publicar, para mostrar evolução depois.

## 6. Medição: protocolo de prompts
Sem ferramenta paga dá para medir bem o suficiente para mostrar tendência ao cliente.

**Montar o conjunto de prompts (15 a 25 por cliente)**, em português, como o cliente final pergunta:
- Categoria + cidade: "dentista em Sorocaba", "qual o melhor dentista em Sorocaba para implante?"
- Necessidade: "preciso fazer implante dentário em Sorocaba, onde vou?", "empresa para içamento de tanque industrial perto de Sorocaba"
- Comparação: "Dra. Tatiane Pontes ou [concorrente]?"
- Pergunta informativa do setor: "quanto custa implante dentário em Sorocaba?"
- Marca: "o que é a [empresa]?", "a [empresa] é confiável?", "qual o telefone e endereço da [empresa]?" (confere se a IA tem os fatos certos)

**Rodar** em ChatGPT (com busca ligada), Gemini, Google (AI Overview/AI Mode), Perplexity, Copilot e Claude. Usar aba anônima ou conta sem histórico, localização na cidade do cliente (ou incluir a cidade no prompt). **Rodar cada prompt 3 vezes** e contar a frequência, porque a resposta varia.

**Registrar** numa planilha (Google Sheets da GG Code), uma linha por prompt × motor × rodada:
| data | prompt | motor | rodada | cliente citado? (s/n) | posição na lista | link do site citado? | fatos corretos? | concorrentes citados | fontes citadas (URLs) |

**Ler o resultado**:
- *Taxa de menção* = rodadas com o cliente ÷ total. Comparar mês a mês.
- *Fontes citadas* nos prompts em que o cliente **não** aparece: essas fontes viram a lista de alvos (diretório onde falta perfil, portal onde o concorrente saiu, página que precisa melhorar).
- *Fatos errados* (telefone velho, endereço errado, serviço que não faz): corrigir na fonte que a IA citou.

Medir antes de publicar (linha de base), 30 dias depois e depois mensalmente. Ferramentas pagas automatizam isso quando houver volume de clientes: OpenSEO (módulo AI visibility, DataForSEO), Peec AI, Profound, Semrush AI Toolkit.

## 7. Como vender
- Entra no pacote site + CRM + Google Meu Negócio como "presença em Google e IAs", sem custo extra no setup: é o mesmo trabalho bem feito.
- Recorrente: "Relatório mensal de visibilidade em Google e IA" (protocolo da seção 6 + rotina mensal de `fora-do-site.md`). Mostrar taxa de menção, fontes conquistadas, avaliações do mês, ligações e WhatsApp vindos do Google.
- Linguagem com o cliente: "fazemos sua empresa ser encontrada e recomendada quando alguém pergunta ao Google ou ao ChatGPT". Nunca "garantimos o primeiro lugar".

## Fontes desta referência
- Google, "Optimizing your website for generative AI features on Google Search" (15/mai/2026, atualizado 15/jun/2026)
- Revisão "Optimizing Visibility in Generative Engines: A Critical Survey of GEO (2023-2026)", arXiv 2607.14035
- Aggarwal et al., "GEO: Generative Engine Optimization", KDD 2024 (Princeton)
- Yext Research, 6,8 milhões de citações de IA (out/2025)
- SOCi Local Visibility Index 2026 (fev/2026)
- Semrush, estudo de 13 semanas com 230 mil prompts (set-nov/2025); SparkToro/Gumshoe (jan/2026)
- Peec AI, estatísticas de GEO 2026; Ahrefs sobre llms.txt (mai/2026)
- Compilação OpenLens: https://openlens.com/blog/en/how-ai-recommends-local-businesses-source-audit
