# Dados estruturados (JSON-LD)

Para que serve: o Google, o Bing e as IAs entendem sem ambiguidade quem é o negócio, onde fica, o que faz e como contatar. Reforça o painel de conhecimento e a ligação site ↔ Perfil da Empresa no Google. Não garante rich result e não é fator de ranking direto, mas é barato e reduz erro de interpretação.

Regras:
- Todo dado no JSON-LD tem que estar **visível na página** e ser verdade. Marcação de algo que não aparece é violação de diretriz.
- NAP idêntico ao rodapé e ao GBP.
- Use o **subtipo mais específico** do schema.org (tabela abaixo), não `LocalBusiness` genérico.
- Um `@id` estável para o negócio (`https://www.dominio.com.br/#negocio`) e reutilize nas outras páginas.
- Telefone no formato internacional `+55-15-99999-9999`. País `BR`. Estado com sigla (`SP`).
- `aggregateRating`/`review` do próprio negócio, escritos por você ou puxados do próprio site: **não** usar em LocalBusiness/Organization. O Google chama de "self-serving reviews" e não mostra; em casos abusivos dá ação manual.
- `FAQPage`: o Google parou de mostrar FAQ rich result em 7/maio/2026 (já era restrito a sites de governo e saúde desde 2023). Pode manter se já existe (não faz mal), mas não é motivo para criar. `HowTo` também morreu (2023).
- Validar: https://validator.schema.org (sintaxe) e https://search.google.com/test/rich-results (o que o Google aproveita).

## Subtipo por cliente
| Cliente | @type |
|---|---|
| Dentista | `Dentist` |
| Médico / clínica médica | `Physician` (profissional) ou `MedicalClinic` (clínica) |
| Clínica de estética | `MedicalClinic` se procedimento médico; `BeautySalon` / `HealthAndBeautyBusiness` se não |
| Advogado / escritório | `LegalService` (o tipo `Attorney` é antigo) |
| Imobiliária / corretor | `RealEstateAgent` |
| Restaurante / lanchonete | `Restaurant` (+ `servesCuisine`, `menu`, `acceptsReservations`) |
| Loja de roupa / aluguel de vestido | `ClothingStore` (aluguel: `Store` com `description` clara) |
| Brechó / loja virtual com retirada | `Store` ou `ClothingStore` |
| Escola de música / dança | schema.org não tem tipo próprio: use `["EducationalOrganization", "LocalBusiness"]` (array) com `description` clara |
| Barbearia / salão | `HairSalon` / `BeautySalon` |
| Construção, manutenção industrial | `GeneralContractor` ou `HomeAndConstructionBusiness` |
| Prestador sem endereço aberto ao público | Tipo específico + `areaServed`, e não exibir rua se o GBP oculta o endereço |

## Modelo: home de negócio local
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Dentist",
      "@id": "https://www.dominio.com.br/#negocio",
      "name": "Dra. Tatiane Pontes Odontologia",
      "url": "https://www.dominio.com.br/",
      "image": "https://www.dominio.com.br/img/consultorio.jpg",
      "logo": "https://www.dominio.com.br/img/logo.png",
      "description": "Consultório odontológico em Sorocaba: implantes, clareamento, ortodontia e clínica geral.",
      "telephone": "+55-15-99999-9999",
      "email": "contato@dominio.com.br",
      "priceRange": "$$",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "Rua Exemplo, 123, sala 4",
        "addressLocality": "Sorocaba",
        "addressRegion": "SP",
        "postalCode": "18000-000",
        "addressCountry": "BR"
      },
      "geo": { "@type": "GeoCoordinates", "latitude": -23.5015, "longitude": -47.4526 },
      "openingHoursSpecification": [
        { "@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"], "opens": "08:00", "closes": "18:00" },
        { "@type": "OpeningHoursSpecification", "dayOfWeek": "Saturday", "opens": "08:00", "closes": "12:00" }
      ],
      "areaServed": [
        { "@type": "City", "name": "Sorocaba" },
        { "@type": "City", "name": "Votorantim" }
      ],
      "hasMap": "https://maps.google.com/?cid=000000000000",
      "sameAs": [
        "https://www.instagram.com/perfil",
        "https://www.facebook.com/perfil",
        "https://maps.google.com/?cid=000000000000"
      ],
      "founder": { "@type": "Person", "name": "Tatiane Pontes", "identifier": "CRO-SP 125743" },
      "knowsAbout": ["Implante dentário", "Clareamento dental", "Ortodontia"]
    },
    {
      "@type": "WebSite",
      "@id": "https://www.dominio.com.br/#site",
      "url": "https://www.dominio.com.br/",
      "name": "Dra. Tatiane Pontes Odontologia",
      "inLanguage": "pt-BR",
      "publisher": { "@id": "https://www.dominio.com.br/#negocio" }
    }
  ]
}
</script>
```
Como achar `geo`: no Google Maps, clicar com o botão direito no pin do negócio, as coordenadas aparecem no topo do menu. Como achar o link `cid`: no GBP, "Compartilhar perfil", ou no Maps o link do lugar.

## Modelo: página de serviço
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Service",
      "@id": "https://www.dominio.com.br/implante-dentario#servico",
      "name": "Implante dentário",
      "serviceType": "Implante dentário",
      "description": "Implante dentário com planejamento digital em Sorocaba.",
      "provider": { "@id": "https://www.dominio.com.br/#negocio" },
      "areaServed": { "@type": "City", "name": "Sorocaba" },
      "url": "https://www.dominio.com.br/implante-dentario"
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": "Início", "item": "https://www.dominio.com.br/" },
        { "@type": "ListItem", "position": 2, "name": "Implante dentário", "item": "https://www.dominio.com.br/implante-dentario" }
      ]
    }
  ]
}
</script>
```

## Extras por segmento
- **Restaurante**: `servesCuisine`, `menu` (URL do cardápio digital), `acceptsReservations`. Cardápio em HTML (texto), não PDF/imagem: o Google lê pratos e preços.
- **Imobiliária**: imóveis podem ter `RealEstateListing` / `Offer` nas páginas de imóvel. Sem rich result garantido; útil para entendimento.
- **Evento / espetáculo** (ex.: PEC Studio): `Event` com `startDate`, `location` (`Place` com endereço), `offers` (preço, `availability`, `url` de compra), `eventStatus`, `image`. Este ainda gera rich result de evento no Google.
- **Produto com preço** (loja): `Product` + `Offer` (`price`, `priceCurrency: "BRL"`, `availability`). Avaliações de produto reais de clientes podem usar `aggregateRating` (só em Product, não no negócio).
- **Profissional liberal com página "Sobre"**: `Person` com `jobTitle`, `identifier` (CRM/CRO/OAB), `alumniOf`, `worksFor` → `@id` do negócio, `sameAs` (Lattes, LinkedIn, Doctoralia). Reforça E-E-A-T (experiência, autoridade), que pesa em saúde e direito.
- **Artigo de blog**: `Article`/`BlogPosting` com `author` (`Person` com URL de página de autor), `datePublished`, `dateModified`.
