# O que não funciona (ou deixou de funcionar)

Lista para não perder tempo e para responder cliente que "ouviu falar". Datas indicam quando a informação foi confirmada.

| Mito / prática | Realidade | Fonte / data |
|---|---|---|
| `meta keywords` | O Google ignora desde 2009. | Google SEO office hours, jan/2023 |
| Densidade de palavra-chave (ex.: 2%) | Não existe. Ser explícito importa; repetir não. | Google SEO office hours, jan/2023 |
| Mínimo de X palavras | Word count não é fator. Página precisa responder bem. | Google (Mueller/Illyes), 2023 |
| `llms.txt` para aparecer em IA | Google Search ignora; não ajuda nem atrapalha. 97% dos llms.txt não recebem nenhuma requisição (Ahrefs, mai/2026). | Guia de IA do Google, atualizado 15/jun/2026; Mueller, Search Off the Record ep. 111 |
| "Otimizar para IA" separado (chunking, reescrever para LLM, schema especial) | AI Overviews/AI Mode usam o mesmo índice e ranking. SEO normal bem feito. | Guia oficial do Google, 15/mai/2026 |
| FAQ schema para ganhar espaço no Google | FAQ rich result deixou de aparecer em 7/mai/2026. | Google Search Central, mai/2026 |
| HowTo schema | Removido em 2023. | Google, ago-set/2023 |
| `aggregateRating` no schema do próprio negócio | Proibido ("self-serving"); não aparece e pode gerar ação manual. | Diretrizes de review snippet do Google |
| `priority`/`changefreq` no sitemap | Ignorados. Só `lastmod` (real). | Google Search Central |
| Enviar o site a "1000 buscadores" / submissão paga | Inútil. Search Console + Bing Webmaster bastam. | — |
| Comprar backlinks / PBN / troca de links em massa | Contra as diretrizes; risco de penalidade; para negócio local quase nunca compensa. | Políticas de spam do Google |
| Páginas por cidade com texto trocado | Doorway pages = spam. Só com conteúdo único de verdade. | Políticas de spam do Google (doorway, scaled content abuse) |
| Gerar 50 páginas com IA para "cobrir todas as buscas" | Scaled content abuse, alvo de updates de spam (ex.: jun/2026). | Políticas de spam do Google, rev. ago/2026 |
| Palavra-chave no nome do GBP que não é o nome real | Funciona até ser denunciado; suspensão. | Diretrizes do Perfil da Empresa |
| Avaliações em massa, incentivadas ou filtradas | Proibido; remoção e bloqueio de avaliações. Regras endurecidas em abr/2026 (sem meta por funcionário, sem pedir nome de funcionário/texto). | Política de conteúdo do GBP, abr/2026 |
| Postar no GBP todo dia para subir no mapa | Efeito no ranking pequeno; vale pela conversão e por mostrar perfil ativo. | Whitespark 2026 |
| Core Web Vitals perfeitos = 1º lugar | É desempate. Conteúdo e relevância vêm primeiro. Mas site lento perde cliente. | Google |
| Domínio com palavra-chave (dentistasorocaba.com.br) | Sem vantagem relevante hoje; prefira a marca. | Google |
| `.com.br` vs `.com` | Para negócio no Brasil, `.com.br` é natural e passa confiança; o Google não penaliza `.com`. | — |
| Google Analytics instalado ajuda a ranquear | Não. Serve para medir. | Google |
| Redes sociais ranqueiam o site | Sinais sociais não são fator direto. Perfis ajudam marca, citações e IA. | Google |
| Bloquear GPTBot tira o site do ChatGPT | GPTBot é treino. A busca do ChatGPT usa OAI-SearchBot. | Documentação OpenAI |
| `Google-Extended` controla AI Overviews | Não. Controla uso para treino/Gemini; AI Overviews segue o Googlebot. | Google |
| Duplicar o conteúdo do site no Instagram/blog dá penalidade | Não há penalidade por duplicação comum; o Google escolhe uma versão. Use canonical. | Google |
