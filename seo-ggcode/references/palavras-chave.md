# Palavras-chave e arquitetura do site

## Como o cliente final procura
Negócio local tem três tipos de busca:
1. **Serviço + cidade/bairro**: "dentista em Sorocaba", "advogado trabalhista zona sul SP". O Google mostra o mapa (3 empresas) e depois os sites. É a busca que mais vira cliente.
2. **"Perto de mim" / sem cidade**: "dentista perto de mim", "implante dentário". O Google usa a localização da pessoa. Ganha quem tem GBP forte e site relevante para o serviço.
3. **Marca**: "Ibanhez", "Casa Maestro imobiliária". Tem que ser o primeiro resultado com o painel do GBP ao lado. Se não for, há problema técnico ou de consistência.

Mais o tipo **pergunta**: "quanto custa implante dentário", "quanto tempo dura clareamento". Bom para página de serviço (seção de perguntas) e para aparecer em AI Overviews.

## Como pesquisar sem ferramenta paga
1. **Autocompletar do Google** em aba anônima, com a localização certa: digitar "serviço + cidade", "serviço + a", "serviço + b"... e "quanto custa serviço".
2. **"As pessoas também perguntam"** e **"Pesquisas relacionadas"** no fim da página.
3. **Mapa**: quais categorias e quais palavras os 3 primeiros usam no nome, nos serviços e nas avaliações.
4. **Concorrentes que aparecem na 1ª página**: quais páginas eles têm (`site:concorrente.com.br`), como titulam.
5. **Google Search Console** do cliente (depois de 4 a 8 semanas no ar): consultas reais com impressões. É a melhor fonte que existe; revise mensalmente.
6. **Google Keyword Planner** (grátis com conta Google Ads, sem anunciar): volume aproximado por cidade.
7. **Google Trends** para sazonalidade (ex.: vestido de festa em formatura e casamento).
8. **WhatsApp do cliente**: as perguntas que os clientes fazem são as buscas que eles fazem. Peça ao dono as 10 perguntas mais comuns.

Com ferramenta: OpenSEO (avaliado em 2026-10-24, DataForSEO pago por uso) dá volume, dificuldade e grade de ranking local no mapa. Usar quando a GG Code oferecer relatório mensal de SEO.

## Mapeamento palavra → página
- **Uma intenção principal por página.** Home = marca + serviço principal + cidade. Cada serviço com busca própria = uma página.
- Duas páginas competindo pela mesma palavra (canibalização) enfraquecem as duas. Junte.
- Variações e sinônimos ("implante" / "implante dentário" / "dente fixo") ficam na mesma página, no texto natural. Não precisa de página por variação.
- Palavra principal entra: no title, no H1, na URL, na description, no primeiro parágrafo, em um H2, no alt de uma imagem relevante e no texto do link interno que aponta para a página. Sem forçar repetição.

## Uma página ou várias?
| Situação | Arquitetura |
|---|---|
| Profissional com 1 serviço principal, pouca busca (ex.: indústria B2B regional) | One-page bem feito resolve. Foco em marca, GBP e 1 palavra principal. |
| 3+ serviços que as pessoas buscam separadamente (dentista, advogado, clínica, estética) | Home + uma página por serviço principal + Sobre (com credenciais) + Contato. |
| Atende várias cidades com endereço só em uma | Página da cidade-sede forte. Outras cidades citadas em "Área atendida". Página por cidade só se houver conteúdo único (obras feitas lá, depoimentos de lá, logística real). |
| Restaurante | Home + cardápio em HTML + reservas/delivery + contato. |
| Imobiliária | Home + página por tipo/bairro com imóveis reais + página de cada imóvel. |
| Quer captar busca de pergunta | Blog/artigos com resposta real, escritos ou revisados pelo profissional, com autor identificado. Só se o cliente vai manter. Blog abandonado com 3 posts não ajuda. |

Site one-page que a GG Code já entregou e o cliente quer crescer: transformar as seções de serviço em páginas próprias, mantendo a home como resumo com links.

## Nome do arquivo de saída
Ao terminar a fase 1, deixe registrado no relatório a tabela `Página | Palavra principal | Secundárias`.
