# Conteúdo que ranqueia (e converte)

O Google quer conteúdo "útil, confiável, feito para pessoas". Para negócio local, isso é concreto:

## O que cada página de serviço precisa ter
1. **O que é** o serviço, em linguagem do paciente/cliente, em 2-3 frases. Primeiro parágrafo já responde a busca.
2. **Para quem é / quando procurar.**
3. **Como funciona** aqui: etapas, tempo, o que a pessoa leva, se atende convênio, se tem estacionamento.
4. **Prova**: anos de experiência, registro profissional, fotos reais, casos (respeitando o conselho), número de clientes/obras, clientes conhecidos (B2B).
5. **Perguntas frequentes** visíveis (as do WhatsApp do cliente). Responda direto na primeira frase. Isso alimenta "As pessoas também perguntam" e AI Overviews, mesmo sem FAQ rich result.
6. **Local**: cidade/bairro de forma natural ("no Centro de Sorocaba, a 2 quadras da Praça..."), área atendida.
7. **Chamada para ação** clara: WhatsApp com mensagem pré-preenchida citando o serviço, telefone, formulário.
8. **Links** para serviços relacionados e para contato.

Tamanho: o necessário para responder bem. Word count não é fator. Uma página de serviço boa costuma ficar entre 300 e 900 palavras porque tem muita coisa para responder, não por regra.

## E-E-A-T (experiência, especialização, autoridade, confiança)
Pesa mais em saúde, direito e dinheiro ("YMYL"). Para nossos clientes:
- Página "Sobre" com nome, foto real, formação, registro (CRM/CRO/OAB/CREA/CRECI), anos de atuação.
- Conteúdo de saúde/direito assinado ou revisado pelo profissional, com data.
- Endereço, telefone, CNPJ no rodapé. Política de privacidade (LGPD) se tem formulário.
- Avaliações reais: mostrar trechos de avaliações do Google na página (com nome e link para o GBP) é bom para conversão. Só não marcar com `aggregateRating` no schema do negócio.

## Texto feito com IA
Pode usar IA para rascunhar, desde que o resultado tenha informação real do cliente (preços, processo, diferenciais, fotos) e seja revisado. O Google pune conteúdo em escala sem valor ("scaled content abuse"), não o uso de IA em si. Texto genérico que serviria para qualquer dentista do Brasil não ranqueia e não converte.

## Visibilidade em IA (AI Overviews, AI Mode, ChatGPT, Perplexity, Gemini)
Segundo o guia oficial do Google (mai/2026), AI Overviews e AI Mode usam o mesmo índice e ranking da busca. Na prática, o que ajuda:
- Fatos claros e consistentes em todo lugar (site, GBP, Instagram, diretórios): nome, endereço, serviços, horário, preço quando existe.
- Respostas diretas a perguntas, em texto no HTML.
- Avaliações e menções em sites de terceiros (imprensa local, diretórios do setor, Doctoralia, Reclame Aqui para lojas).
- Não precisa: `llms.txt`, "chunking" de conteúdo, reescrever para IA, schema especial para IA.
- Teste: perguntar ao ChatGPT/Gemini/Perplexity "melhor [serviço] em [cidade]" e "o que é [marca]" antes e depois. Registrar no relatório.

## Regras de publicidade dos conselhos (afetam o texto e as fotos)
Conferir a versão vigente antes de publicar; resumo:
- **Médicos (CFM, Resolução 2.336/2023)**: permite antes/depois com fins educativos e consentimento, mostrar preços e equipamentos. Proíbe prometer resultado, sensacionalismo, "o melhor", autopromoção enganosa. Obrigatório: nome, CRM e RQE (se citar especialidade).
- **Dentistas (CFO, Código de Ética + Resolução CFO-196/2019 e atualizações)**: obrigatório nome e CRO. Antes/depois e selfies com regras (consentimento, sem garantia de resultado). Evitar preço como chamariz e "promoção".
- **Advogados (OAB, Provimento 205/2021)**: publicidade informativa e sóbria. Pode site, conteúdo educativo, anúncios impulsionados. Proíbe mencionar preços/honorários como atrativo, captação de clientela, prometer resultado, citar casos de clientes sem autorização. Obrigatório nome e número da OAB.
- **Corretores (CRECI)**: CRECI do corretor/imobiliária visível em anúncios e no site.
- **Engenharia (CREA)**: responsável técnico com registro.
Texto que fere o conselho pode gerar processo ético para o cliente. Na dúvida, texto informativo e sóbrio.
