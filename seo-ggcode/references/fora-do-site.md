# Fora do site: Perfil da Empresa no Google, Search Console, Bing, citações, avaliações

Para negócio local, esta é a parte que mais traz cliente. O pacote GG Code (site + CRM + Google Meu Negócio) se apoia aqui.

## 1. Perfil da Empresa no Google (GBP, antigo Google Meu Negócio)
Fatores mais fortes do local pack (survey Whitespark 2026): **categoria principal**, proximidade, palavra-chave no nome (só se for o nome real), avaliações.

Checklist:
- [ ] Perfil reivindicado e verificado na conta do **cliente** (GG Code como gerente, nunca como único proprietário). Verificação pode ser por vídeo, telefone, e-mail ou cartão; vídeo costuma ser o mais rápido.
- [ ] **Nome** exatamente igual à fachada/registro. Nada de "Dentista Sorocaba Implantes | Dra X" se não for o nome real. Encher o nome dá ranking por um tempo e depois suspensão, e é uma das causas mais comuns de suspensão em 2026.
- [ ] **Categoria principal** = a mais específica que descreve o negócio ("Dentista", "Advogado trabalhista", "Imobiliária", "Empreiteiro industrial"). Pesquise a categoria dos 3 primeiros do mapa. Até 9 secundárias, só as reais.
- [ ] Endereço igual ao site. Prestador que atende no cliente (sem atendimento no local): ocultar endereço e definir área de atendimento (até 20 regiões, raio razoável). Endereço virtual/coworking sem atendimento é motivo de suspensão.
- [ ] Telefone local (DDD da cidade) igual ao site. Pode adicionar WhatsApp no botão de chat/link.
- [ ] Site com UTM: `https://www.dominio.com.br/?utm_source=google&utm_medium=organic&utm_campaign=gbp`.
- [ ] Horários, inclusive feriados (atualizar antes de cada feriado).
- [ ] **Serviços** cadastrados um a um com descrição curta, e produtos se fizer sentido.
- [ ] **Descrição** (750 caracteres): o que faz, para quem, onde, diferencial, desde quando. Sem link, sem promoção. Escreva e entregue pronta.
- [ ] **Atributos** (acessibilidade, Wi-Fi, estacionamento, "atende online", "de propriedade de mulheres" etc.).
- [ ] **Fotos reais**: logo, capa, fachada (ajuda a achar o lugar), interior, equipe, trabalhos. Pelo menos 10 no início e novas todo mês. Sem foto de banco.
- [ ] **Postagens** (novidades, ofertas, eventos) pelo menos a cada 2 semanas. Efeito pequeno no ranking, bom para conversão e sinal de perfil ativo.
- [ ] Perguntas e respostas: se a seção ainda existir no perfil, cadastrar as perguntas comuns e responder.
- [ ] Ativar mensagens/agendamento se o segmento permitir (link do CRM ou WhatsApp).
- [ ] Monitorar edições sugeridas por terceiros (o Google avisa por e-mail; aceitar ou rejeitar).

### Avaliações (o fator que mais cresceu)
- Quantidade, **frequência constante** e recência importam mais que um pico. Meta prática: algumas por semana, para sempre.
- Pedir para **todo** cliente satisfeito, no momento certo (fim do atendimento), com link direto (`https://g.page/r/.../review` do painel do GBP) e QR code no balcão. O CRM da GG Code pode disparar a mensagem pelo WhatsApp automaticamente depois do atendimento.
- Proibido (política do Google, endurecida em abr/2026): comprar avaliação, oferecer desconto/brinde em troca, pedir só para quem gostou (filtrar antes, "review gating"), meta de número de avaliações por funcionário, pedir que citem nome de funcionário ou texto específico, avaliação de familiares/funcionários. Pico artificial faz o Google remover avaliações e travar novas.
- **Responder todas**, inclusive as negativas, em até 48 h, com educação e sem expor dado do paciente/cliente (saúde e advocacia: nunca confirmar que a pessoa é paciente/cliente).
- Mensagem modelo para o cliente pedir (ajustar ao tom):
  > Oi, [nome]! Obrigado por escolher a [empresa]. Se puder, conta como foi sua experiência no Google, leva 1 minuto e ajuda muito: [link]. Obrigado!

## 2. Google Search Console
- [ ] Propriedade de **domínio** (registro TXT no DNS: Hostinger/Registro.br). Cobre http/https/www.
- [ ] Enviar `sitemap.xml`.
- [ ] Inspecionar URL da home e das páginas de serviço, "Solicitar indexação".
- [ ] Adicionar o e-mail do cliente e o da GG Code (e-mail da agência) como usuários.
- [ ] Revisar mensalmente: Desempenho (consultas, cliques, posição), Páginas (não indexadas e por quê), Core Web Vitals, Ações manuais (tem que estar vazio).
- Site novo leva de dias a semanas para indexar e de 2 a 6 meses para ranquear bem para palavras disputadas. Alinhar essa expectativa com o cliente.

## 3. Bing (e ChatGPT, Copilot, DuckDuckGo)
- [ ] Bing Webmaster Tools: "Importar do Google Search Console" (2 minutos).
- [ ] IndexNow: avisa Bing/Yandex na hora quando uma página muda. Em site estático, opcional; em Next.js/WordPress com plugin, ligar.
- [ ] **Bing Places for Business**: importar do GBP. Mantém endereço e horário corretos no Bing, Copilot e mapas que usam dados da Microsoft.
- A busca do ChatGPT usa o crawler `OAI-SearchBot` (não bloquear). A dependência do índice do Bing é provável mas não confirmada pela OpenAI; Bing Webmaster é barato, então fazemos.

## 4. Citações e consistência de NAP (Brasil)
Mesmo nome, endereço e telefone em todo lugar. Prioridade:
- [ ] Apple Business Connect (Apple Maps, Siri, iPhone).
- [ ] Bing Places.
- [ ] Facebook (página com endereço) e Instagram (conta comercial com endereço e categoria).
- [ ] Waze (adicionar o lugar) e Foursquare.
- [ ] Setor: Doctoralia / BoaConsulta (saúde), Jusbrasil (advogados), iFood / TripAdvisor / Restaurant Guru (restaurantes), ZAP / VivaReal / OLX (imobiliárias), Reclame Aqui (lojas), Guia Mais / Apontador / TeleListas (genéricos BR, peso baixo hoje).
- [ ] Associação comercial da cidade (ACS em Sorocaba etc.), sindicato/conselho do setor, câmara de dirigentes lojistas: geralmente dão perfil com link.
- Não precisa de 100 diretórios. 10 a 20 relevantes e corretos valem mais. Corrigir dados antigos errados (endereço velho, telefone antigo) é mais importante que criar novos.

## 5. Links e menções locais (proeminência)
O que funciona para negócio local, sem comprar link (comprar link é contra as diretrizes e quase sempre desperdício):
- Fornecedores e parceiros com página de "onde comprar"/"parceiros" (ex.: marca de implante lista clínicas credenciadas).
- Imprensa e portais locais (jornal da cidade, blogs de bairro): pauta real (evento, prêmio, ação social, dado curioso do setor).
- Patrocínio de evento/time local com link no site do evento.
- Clientes B2B que citam o fornecedor (indústria: "obras realizadas para...").
- Entrevistas/podcasts locais, palestras em faculdade/associação.

## 6. Rotina mensal (para oferecer como serviço recorrente)
1. Search Console: consultas novas, páginas caindo, erros de indexação.
2. GBP: insights (buscas, ligações, rotas, cliques no site), novas avaliações respondidas, 1-2 postagens, fotos novas.
3. Grade de ranking local (OpenSEO ou similar) para 3-5 palavras.
4. 1 melhoria de conteúdo (nova pergunta respondida, página de serviço reforçada).
5. Relatório curto ao cliente: ligações + WhatsApp + rotas vindos do Google, posição no mapa, avaliações do mês.
