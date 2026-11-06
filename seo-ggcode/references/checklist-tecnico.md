# Checklist técnico (on-page)

Marque cada item. Em cada um, o motivo vem junto para você decidir bem quando o caso fugir da regra.

## Sumário
1. Indexação e rastreio
2. Head de cada página
3. Estrutura do conteúdo
4. Imagens e mídia
5. Velocidade (Core Web Vitals)
6. Mobile e acessibilidade
7. Links e navegação
8. Sites com animação, 3D e JS pesado
9. Next.js
10. Medição

---

## 1. Indexação e rastreio
- [ ] HTTPS com redirecionamento 301 de http para https. Um único host canônico (www ou sem www), o outro redireciona 301.
- [ ] `robots.txt` na raiz, sem `Disallow: /`, com a linha `Sitemap:`. Modelo em `arquivos-raiz.md`.
- [ ] `sitemap.xml` na raiz com **só** URLs canônicas, indexáveis, status 200. `lastmod` real (não a data do build em toda página). `priority` e `changefreq` são ignorados pelo Google; não precisa.
- [ ] Nenhuma página que deve aparecer tem `noindex`. Páginas de obrigado, política e testes podem ter `noindex`.
- [ ] Página 404 de verdade (status 404), com links para home e contato. Nada de redirecionar todo erro para a home (o Google trata como soft 404).
- [ ] URLs curtas, minúsculas, com hífen, sem acento: `/implante-dentario`, não `/Implante_Dentário.html`. Mudou URL de site antigo do cliente? 301 de cada URL antiga para a nova equivalente (perder isso derruba o ranking que ele já tinha).
- [ ] Ambiente de teste/beta (Vercel preview, subdomínio) com `noindex` ou senha, para não competir com o site oficial.

## 2. Head de cada página
- [ ] `<html lang="pt-BR">`
- [ ] `<meta charset="utf-8">` e `<meta name="viewport" content="width=device-width, initial-scale=1">`
- [ ] `<title>` único por página, 30 a 60 caracteres. Padrão: `Serviço principal em Cidade | Marca`. Home de negócio local: `Marca: serviço principal em Cidade - UF`. O Google reescreve title ruim ou muito longo.
- [ ] `<meta name="description">` única, 120 a 155 caracteres, com serviço, cidade e um motivo para clicar (anos, diferencial, "agende pelo WhatsApp"). Não ranqueia, mas aumenta clique.
- [ ] `<link rel="canonical" href="https://www.dominio.com.br/pagina">` absoluto, autorreferente.
- [ ] Open Graph: `og:title`, `og:description`, `og:image` (absoluta, 1200x630, JPG/PNG/WebP < 300 KB), `og:url`, `og:type` (`website`), `og:locale` (`pt_BR`), `og:site_name`. Mais `twitter:card` = `summary_large_image`. Isso é o que aparece quando o cliente manda o link no WhatsApp; para a gente vale tanto quanto SEO.
- [ ] Favicon: `<link rel="icon" href="/favicon.svg">` + PNG 48x48 ou maior + `apple-touch-icon` 180x180. O Google mostra o favicon no resultado mobile; precisa ser quadrado e no múltiplo de 48 px.
- [ ] JSON-LD do negócio (modelos em `schema-jsonld.md`). Na home: o tipo de negócio local completo + `WebSite`. Em páginas de serviço: `Service` ligado ao negócio por `@id` + `BreadcrumbList`.
- [ ] `<meta name="theme-color">` (opcional, cosmético).
- [ ] Não usar: `meta keywords`, `meta revisit-after`, `meta author` como "SEO". São inúteis.

## 3. Estrutura do conteúdo
- [ ] Um `<h1>` por página, com o serviço e, se local, a cidade. Pode ser criativo, mas tem que dizer o que é. Se o título de design for poético ("O site se constrói"), coloque o descritivo em `<h1>` e o poético como frase de destaque, ou junte os dois no mesmo H1.
- [ ] H2 para cada seção, na ordem. H3 dentro de H2. Heading é estrutura, não tamanho de fonte.
- [ ] HTML semântico: `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<footer>`, `<address>`. Ajuda leitor de tela e máquinas a entender a página.
- [ ] NAP no rodapé, em texto (não imagem), igual ao GBP e ao JSON-LD, caractere por caractere.
- [ ] Telefone como `<a href="tel:+5515999999999">`, WhatsApp como `<a href="https://wa.me/5515999999999?text=...">`, e-mail como `mailto:`.
- [ ] Mapa do Google incorporado na página de contato (iframe com `loading="lazy"`) e link "Como chegar" para o perfil no Maps.
- [ ] Texto visível de verdade: serviços explicados, para quem é, como funciona, perguntas frequentes. Ver `conteudo.md`.

## 4. Imagens e mídia
- [ ] Formato AVIF ou WebP, no tamanho de exibição (não 4000 px exibida em 600 px). `srcset`/`sizes` quando a imagem muda muito entre mobile e desktop.
- [ ] `width` e `height` em toda `<img>` (evita CLS). CSS pode redimensionar depois.
- [ ] `alt` descritivo em imagem com conteúdo ("Dra. Tatiane atendendo paciente no consultório em Sorocaba"). `alt=""` em imagem decorativa. Sem encher de palavra-chave.
- [ ] Imagem principal do topo (LCP): **sem** `loading="lazy"`, com `fetchpriority="high"`, e `<link rel="preload">` se for background CSS. Demais imagens: `loading="lazy"`.
- [ ] Nome de arquivo descritivo: `consultorio-odontologico-sorocaba.webp`, não `IMG_2034.webp`.
- [ ] Fotos reais do cliente (fachada, equipe, trabalho) valem mais que banco de imagem, para usuário, para o Google Imagens e para o GBP.
- [ ] Vídeo de fundo: `muted playsinline`, `poster` leve, `preload="none"` ou carregado depois do LCP. Vídeo com conteúdo útil (apresentação, tour): hospedar também no YouTube e incorporar com fachada leve (lite-youtube).

## 5. Velocidade (Core Web Vitals)
Medidos no percentil 75 de usuários reais, separado por mobile e desktop. Limites (inalterados desde 2024):
| Métrica | Bom | Ruim |
|---|---|---|
| LCP (maior elemento visível carregar) | ≤ 2,5 s | > 4 s |
| INP (resposta a clique/toque) | ≤ 200 ms | > 500 ms |
| CLS (layout pular) | ≤ 0,1 | > 0,25 |

É critério de desempate, não de ranking principal. Mas site lento perde cliente antes de perder posição: priorize.
- [ ] HTML e CSS críticos pequenos; CSS inline só do necessário para a primeira tela.
- [ ] JS com `defer` ou `type="module"`. Bibliotecas pesadas (three.js, GSAP, Lenis, vídeo de rolagem) carregam depois da primeira pintura ou por `IntersectionObserver`.
- [ ] Fontes: no máximo 2 famílias, `font-display: swap`, `preconnect` para fonts.gstatic.com ou, melhor, fonte hospedada no próprio site com `preload` do arquivo principal.
- [ ] Nada que mude o layout depois de carregar: reservar espaço de imagens, embeds, banners de cookie.
- [ ] INP: handlers de clique/scroll leves, nada de trabalho pesado no main thread a cada evento de scroll. Use `requestAnimationFrame`, `passive: true`.
- [ ] Compressão (gzip/brotli) e cache longo para estáticos (`.htaccess` em `arquivos-raiz.md`).
- [ ] Testar em celular médio com 4G (DevTools: Moto G Power, Slow 4G), não só no PC.

## 6. Mobile e acessibilidade
- [ ] Mesmo conteúdo no mobile e no desktop. O Google indexa a versão mobile; texto escondido no mobile não conta.
- [ ] Alvos de toque ≥ 44 px, texto ≥ 16 px, sem rolagem horizontal.
- [ ] Contraste suficiente, foco visível, `prefers-reduced-motion` respeitado. Acessibilidade não é fator direto, mas sobrepõe quase tudo do que o Google mede.
- [ ] Sem pop-up intersticial cobrindo o conteúdo no mobile (penalidade antiga, ainda vale).

## 7. Links e navegação
- [ ] Menu com `<a href>` reais para as páginas (não `onclick`). O Google segue `href`, não JS.
- [ ] Toda página a no máximo 3 cliques da home; páginas de serviço linkadas da home e entre si com texto descritivo ("implante dentário", não "clique aqui").
- [ ] Breadcrumb visível em páginas internas (+ `BreadcrumbList` no JSON-LD).
- [ ] Links externos para Instagram/GBP com `rel="noopener"`. Não precisa `nofollow` neles.
- [ ] Nenhum link interno quebrado (o script confere em site estático).

## 8. Sites com animação, 3D e JS pesado (o nosso caso)
A GG Code faz sites com three.js, vídeo controlado por rolagem, texto que aparece palavra por palavra. Dá para manter tudo isso sem perder SEO:
- [ ] **Todo texto existe no HTML na carga.** Animação revela texto que já está no DOM (opacity/transform), nunca injeta texto via JS. Teste: desligue o JS no DevTools; o conteúdo todo tem que estar lá, legível.
- [ ] **Palavra girando no H1** (ex.: "Sua indústria [montada/construída/coberta]"): o HTML deve ler como frase normal. Coloque a frase completa e legível no H1 (ex.: `<h1>Sua indústria montada, construída, coberta e mantida, no prazo.</h1>`) e faça o efeito com elementos `aria-hidden="true"` por cima, ou marque as palavras extras do rotador com `aria-hidden="true"`. O auditar.py mostra o texto do H1 como o Google lê; se sair embaralhado, corrija.
- [ ] Texto dividido em `<span>` por letra/palavra para animação: manter o texto original em `aria-label` no elemento pai ou num elemento `sr-only`, e os spans com `aria-hidden="true"`.
- [ ] Canvas/WebGL é invisível para o Google. Tudo que o 3D "diz" precisa estar em texto ao lado ou embaixo.
- [ ] O que é pesado (modelos 3D, vídeo, sequência de quadros) começa a baixar **depois** do `load` ou quando chega perto da tela. A primeira tela tem que pintar com HTML + CSS + uma imagem.
- [ ] Rolagem suave (Lenis) e scroll-jacking não podem quebrar `#âncoras`, voltar do navegador nem a rolagem por teclado.
- [ ] Peso total razoável: a primeira visita no mobile não deve baixar dezenas de MB antes de o usuário pedir. Versão mobile do vídeo/filme menor.

## 9. Next.js (App Router)
- [ ] `export const metadata` ou `generateMetadata` em cada `page.tsx`, com `title`, `description`, `alternates.canonical`, `openGraph`, `twitter`. No `layout.tsx` raiz: `metadataBase: new URL('https://www.dominio.com.br')` (sem isso, og:image e canonical saem relativos) e `title.template: '%s | Marca'`.
- [ ] `app/sitemap.ts` e `app/robots.ts` gerando os arquivos (modelos em `arquivos-raiz.md`).
- [ ] `app/icon.png`/`app/apple-icon.png` e `app/opengraph-image.(png|tsx)`.
- [ ] JSON-LD com `<script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(dados) }} />` dentro do componente da página (Server Component).
- [ ] Páginas de conteúdo como Server Components / estáticas (SSG). Evitar `"use client"` no topo de página inteira só por causa de uma animação: isole a animação num componente cliente.
- [ ] `next/image` com `priority` na imagem do topo e `sizes` correto; `next/font` para fontes (sem CLS, sem request externo).
- [ ] `app/not-found.tsx` com links úteis.
- [ ] Preview da Vercel não deve indexar (a Vercel já manda `X-Robots-Tag: noindex` em domínios `*.vercel.app` de preview; confira o domínio de produção).
- [ ] Auditar com `npm run build && npm start` e `auditar.py http://localhost:3000`, ou com o export estático em `out/`.

## 10. Medição (depois de publicar)
- [ ] Google Search Console: propriedade de domínio (DNS TXT), sitemap enviado, inspeção da home e das páginas de serviço com "Solicitar indexação".
- [ ] Bing Webmaster Tools: importar do Search Console (1 clique). Alimenta Bing, Copilot, DuckDuckGo e muito do que o ChatGPT encontra.
- [ ] Google Analytics 4 ou alternativa leve (Plausible, Umami, Vercel Analytics) com eventos de clique em WhatsApp, telefone e formulário. Sem isso não dá para provar resultado ao cliente.
- [ ] No GBP, usar link com UTM no botão "Site" (`?utm_source=google&utm_medium=organic&utm_campaign=gbp`) para separar tráfego do mapa.
- [ ] PageSpeed Insights mobile da home e de uma página interna; anotar a nota no relatório.
