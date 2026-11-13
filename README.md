# Selos para AIOStreams

Em **Configurações → Reprodução → Versões → Selos**, vincule o [endereço do pacote](https://raw.githubusercontent.com/Prokyro/aiostreams-selos/main/badges.json). O AIOStreams atualiza o pacote periodicamente e sincroniza a configuração entre dispositivos da mesma conta, inclusive TVs. [Documentação do AIOStreams](https://aiostreams.org/reference/version-badges/)

- Bandeira e alto-falante em verde indicam áudio em português do Brasil.
- Bandeira e balão com linhas em azul indicam legendas em português do Brasil.

O pacote tem 78 selos. Os 18 serviços usam as imagens da [aba Serviços do AIOStreams](https://github.com/Viren070/AIOStreams/blob/302f93c3908f239f84faf28c94b357bc0583b03d/packages/frontend/src/lib/services.ts). Os indicadores de formatos e coleções usam as marcas correspondentes quando disponíveis. A arte dos dois selos de português foi gerada com a ferramenta de imagens da OpenAI, com uma bandeira em cetim e símbolos em metal.

## Aumentar os selos na lista de versões

Em **Configurações → Tema → CSS personalizado**, acrescente o conteúdo de [selos-grandes.css](selos-grandes.css) e selecione **Aplicar CSS → Manter**. O aplicativo salva o tema na conta. O CSS aumenta a altura das imagens de 16 px para 26 px, ou 32 px em janelas com pelo menos 1440 px de largura na escala padrão. [Documentação do tema](https://aiostreams.org/reference/web-app-css/)

## Origem das marcas

- [AV1](https://aomedia.org/resources/logo/), [HDR10+](https://hdr10plus.org/), [Blu-ray Disc](https://blu-raydisc.info/docs/BD_LogoGuide%20revised2008%20Mar.pdf) e [Ultra HD](https://commons.wikimedia.org/wiki/File:Ultra_HD_-_Logo.svg).
- Dolby [Vision](https://commons.wikimedia.org/wiki/File:Dolby_Vision_2021_logo.svg), [Atmos](https://commons.wikimedia.org/wiki/File:Dolby_Atmos_(logo).svg), [TrueHD](https://commons.wikimedia.org/wiki/File:Dolby_TrueHD.svg) e [Digital Plus](https://professional.dolby.com/globalassets/dolby-digital-plus/dolby-digital-plus-audio-coding-tech-paper.pdf).
- [DTS:X](https://tsdr.uspto.gov/#caseNumber=86643048&caseSearchType=US_APPLICATION&caseType=DEFAULT&searchType=statusSearch), [DTS-HD Master Audio](https://commons.wikimedia.org/wiki/File:Dts.png), [IMAX](https://commons.wikimedia.org/wiki/File:IMAX_blue_logo.svg) e [The Criterion Collection](https://commons.wikimedia.org/wiki/File:The_Criterion_Collection_logo_and_wordmark.svg).

As marcas identificam os serviços, formatos e coleções que o aplicativo detecta. A arte vetorial de Ultra HD é atribuída a [Depthfield](https://commons.wikimedia.org/wiki/File:Ultra_HD_-_Logo.svg), com licença [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Foi convertida para PNG e posicionada sobre fundo branco.

## Regenerar as etiquetas tipográficas

Com `fonttools` instalado, execute `python make_badges.py --font BarlowSemiCondensed-Bold.ttf`. Use a [Barlow Semi Condensed Bold](https://github.com/google/fonts/tree/main/ofl/barlowsemicondensed), de Jeremy Tribby, sob SIL Open Font License.
