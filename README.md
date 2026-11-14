# Selos para AIOStreams

Em **Configurações → Reprodução → Versões → Selos**, vincule o [endereço do pacote](https://raw.githubusercontent.com/Prokyro/aiostreams-selos/main/badges.json). O AIOStreams atualiza o pacote periodicamente e sincroniza a configuração entre dispositivos da mesma conta, inclusive TVs. [Documentação do AIOStreams](https://aiostreams.org/reference/version-badges/)

- Bandeira e alto-falante em verde indicam áudio em português do Brasil.
- Bandeira e balão com linhas em azul indicam legendas em português do Brasil.

O pacote tem 78 selos. Os 18 serviços usam as imagens da [aba Serviços do AIOStreams](https://github.com/Viren070/AIOStreams/blob/302f93c3908f239f84faf28c94b357bc0583b03d/packages/frontend/src/lib/services.ts). Os selos de português usam a [geometria da bandeira brasileira](https://commons.wikimedia.org/wiki/File:Flag_of_Brazil.svg) com símbolos vetoriais de alto-falante e legenda.

## Ajustar o tamanho na lista de versões

Em **Configurações → Tema → CSS personalizado**, use o conteúdo de [selos-grandes.css](selos-grandes.css) e selecione **Aplicar CSS → Manter**. Se o tema já contém o bloco Selos AIOStreams, substitua esse bloco pela versão atual. A altura das imagens fica em 20 px, ou 22 px em janelas com pelo menos 1440 px de largura na escala padrão. O aplicativo salva o tema na conta. [Documentação do tema](https://aiostreams.org/reference/web-app-css/)

## Origem das marcas

- 4K Ultra HD, 1080p Full HD, Blu-ray Disc, HDR, DTS:X, DTS-HD Master Audio, Dolby Atmos e Dolby TrueHD vêm da [coleção TaranVH/LOGOS](https://github.com/TaranVH/LOGOS/tree/c5b46e82c87d8ab731112835957aca3000d08da4). As imagens foram recortadas e algumas receberam tinta clara para o fundo escuro.
- [AV1](https://aomedia.org/resources/logo/), [HDR10+](https://hdr10plus.org/), [Dolby Vision](https://commons.wikimedia.org/wiki/File:Dolby_Vision_2021_logo.svg), [Dolby Digital Plus](https://professional.dolby.com/globalassets/dolby-digital-plus/dolby-digital-plus-audio-coding-tech-paper.pdf), [IMAX](https://commons.wikimedia.org/wiki/File:IMAX_blue_logo.svg) e [The Criterion Collection](https://commons.wikimedia.org/wiki/File:The_Criterion_Collection_logo_and_wordmark.svg).

As marcas identificam os serviços, formatos e coleções que o aplicativo detecta.

## Regenerar as etiquetas tipográficas

Com `fonttools` instalado, execute `python make_badges.py --font BarlowSemiCondensed-Bold.ttf`. Use a [Barlow Semi Condensed Bold](https://github.com/google/fonts/tree/main/ofl/barlowsemicondensed), de Jeremy Tribby, sob SIL Open Font License.
