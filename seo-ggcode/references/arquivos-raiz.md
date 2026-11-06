# Arquivos da raiz: robots.txt, sitemap.xml, 404, .htaccess

## robots.txt
```
User-agent: *
Allow: /

Sitemap: https://www.dominio.com.br/sitemap.xml
```
- Não bloquear CSS, JS nem imagens: o Google precisa deles para renderizar.
- Não bloquear `Googlebot`, `Bingbot`, `OAI-SearchBot` (busca do ChatGPT), `ChatGPT-User`, `PerplexityBot`, `Perplexity-User`, `Claude-SearchBot`, `Claude-User`. Para negócio local, aparecer em IA é bom (ver `geo.md`).
- Bloquear robôs de treino (`GPTBot`, `ClaudeBot`, `Google-Extended`, `CCBot`) é decisão do cliente. Não afeta Google Search nem AI Overviews (`Google-Extended` não controla AI Overviews). Padrão GG Code: não bloquear nada.
- `robots.txt` não tira página do índice. Para isso use `noindex` (e deixe a página rastreável para o Google ver o noindex).

## sitemap.xml
```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://www.dominio.com.br/</loc>
    <lastmod>2026-10-24</lastmod>
  </url>
  <url>
    <loc>https://www.dominio.com.br/implante-dentario</loc>
    <lastmod>2026-10-24</lastmod>
  </url>
</urlset>
```
- Só URLs canônicas, com status 200, sem noindex, com o mesmo host/protocolo do canonical.
- `lastmod` só muda quando o conteúdo muda de verdade. O Google confia no lastmod se ele for consistente.
- Site de uma página: o sitemap tem uma URL. Ainda assim vale ter (Search Console e Bing usam).

## 404
- `404.html` com a identidade do site, frase curta, links para home, serviços e WhatsApp.
- Servidor tem que responder **status 404** (Apache: `ErrorDocument 404 /404.html`). Página "não encontrada" com status 200 é soft 404.

## .htaccess (Hostinger / Apache)
```apache
# HTTPS e host único (troque para a versão sem www se for o canônico)
RewriteEngine On
RewriteCond %{HTTPS} !=on [OR]
RewriteCond %{HTTP_HOST} !^www\. [NC]
RewriteRule ^ https://www.dominio.com.br%{REQUEST_URI} [L,R=301]

# URLs sem .html: /servicos serve servicos.html
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteCond %{REQUEST_FILENAME}.html -f
RewriteRule ^(.+?)/?$ $1.html [L]
# e /servicos.html redireciona para /servicos
RewriteCond %{THE_REQUEST} \s/+(.+?)\.html[\s?] [NC]
RewriteRule ^ /%1 [R=301,L]

ErrorDocument 404 /404.html

AddType image/avif .avif
AddType image/webp .webp

<IfModule mod_deflate.c>
  AddOutputFilterByType DEFLATE text/html text/css application/javascript application/json image/svg+xml text/xml application/xml
</IfModule>

<IfModule mod_expires.c>
  ExpiresActive On
  ExpiresByType text/html "access plus 0 seconds"
  ExpiresByType text/css "access plus 1 month"
  ExpiresByType application/javascript "access plus 1 month"
  ExpiresByType image/avif "access plus 1 year"
  ExpiresByType image/webp "access plus 1 year"
  ExpiresByType image/jpeg "access plus 1 year"
  ExpiresByType image/png "access plus 1 year"
  ExpiresByType image/svg+xml "access plus 1 year"
  ExpiresByType video/mp4 "access plus 1 year"
  ExpiresByType font/woff2 "access plus 1 year"
</IfModule>
```
Se o CSS/JS não tem hash no nome, cache de 1 mês pode segurar versão antiga depois de atualização: use `?v=2` no link ao publicar mudança.

## Next.js
`app/robots.ts`:
```ts
import type { MetadataRoute } from 'next'

export default function robots(): MetadataRoute.Robots {
  return {
    rules: { userAgent: '*', allow: '/' },
    sitemap: 'https://www.dominio.com.br/sitemap.xml',
  }
}
```
`app/sitemap.ts`:
```ts
import type { MetadataRoute } from 'next'

const base = 'https://www.dominio.com.br'
const paginas = ['', '/implante-dentario', '/clareamento', '/contato']

export default function sitemap(): MetadataRoute.Sitemap {
  return paginas.map((p) => ({ url: `${base}${p}`, lastModified: new Date('2026-10-24') }))
}
```
Na Vercel, redirecionar o host não canônico nas configurações de domínio (Domains: redirect `dominio.com.br` → `www.dominio.com.br`, 308).
