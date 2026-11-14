# Selos para AIOStreams

Em **Configurações → Reprodução → Versões → Selos**, vincule o [endereço do pacote](https://raw.githubusercontent.com/Prokyro/aiostreams-selos/main/badges.json). O AIOStreams atualiza o pacote periodicamente e sincroniza a configuração entre dispositivos da mesma conta, inclusive TVs. [Documentação do AIOStreams](https://aiostreams.org/reference/version-badges/)

- O microfone cromado com fones verdes aparece quando a versão entra em `Dublado PT - em cache` ou `Dublado PT - sem cache`.
- Os balões verde e dourado aparecem quando a versão entra em `Legendado PT - em cache` ou `Legendado PT - sem cache`.

Os dois selos leem a preferência selecionada (`seMatched`). A classificação pode vir da faixa ou de uma indicação aceita pelas regras da configuração. Português do Brasil, de Portugal e sem região usam os mesmos ícones.

## Prioridade de HDR e Dolby Vision

O pacote mostra **no máximo um selo de faixa dinâmica por versão**, com a prioridade `Dolby Vision → HDR10+ → HDR10 → HLG → HDR → SDR`. `HDR+DV`, `DV Only`, `DV`, `DoVi` e `Dolby Vision` são representados por **apenas Dolby Vision**; o selo combinado antigo não é mais uma regra ativa. Os arquivos de imagens anteriores permanecem preservados.

Os formatos são reconhecidos somente em `visualTags`; os selos não alteram o HDR do vídeo, a ordem dos streams nem as pontuações. Essa exclusividade vale **dentro deste pacote**: outros pacotes ou selos personalizados de HDR podem apresentar ícones adicionais.

## Integração com a configuração AIO PT Qualidade (14/11/2026)

Os selos de português permanecem vinculados ao campo **`seMatched`** e às quatro preferências `Dublado PT - em cache`, `Dublado PT - sem cache`, `Legendado PT - em cache` e `Legendado PT - sem cache`. Isso acompanha tanto as regras `Audio PT confirmado/indicado` quanto `Legenda PT confirmada/indicada` da configuração, sem exigir nenhuma alteração nela.

Quando a mesma versão for classificada como dublada e legendada, a preferência `Dublado` e a prioridade do grupo `aiostreams-selos-pt` exibem apenas o selo de áudio. **Importante:** um ícone de português reflete a classificação aceita pela configuração; ele não prova, por si só, que a faixa foi verificada por FFprobe.

O pacote tem 78 selos. Os 18 serviços usam as imagens da [aba Serviços do AIOStreams](https://github.com/Viren070/AIOStreams/blob/302f93c3908f239f84faf28c94b357bc0583b03d/packages/frontend/src/lib/services.ts).

## Ajustar o tamanho na lista de versões

Em **Configurações → Tema → CSS personalizado**, use o conteúdo de [selos-grandes.css](selos-grandes.css) e selecione **Aplicar CSS → Manter**. Se o tema já contém o bloco Selos AIOStreams, substitua esse bloco pela versão atual. A altura padrão fica em 20 px, ou 22 px em janelas com pelo menos 1440 px de largura. Os selos de português e o logo Full HD da Sony ganham 4 px de altura para melhorar a leitura. O aplicativo salva o tema na conta. [Documentação do tema](https://aiostreams.org/reference/web-app-css/)

## Origem das marcas

- REMUX, WEB-DL verde, HEVC, H.264 (AVC), 7.1, 5.1, THEATRICAL (THTR) e 10bit usam as imagens de [Kingsize Fusion Badges](https://github.com/kingsizew/badges/tree/fdd3479bacf2232e431acda4b59b2858b509d2df). EXTENDED usa a imagem de [IaemTary/nuvio-badges](https://github.com/IaemTary/nuvio-badges/tree/fb17a15cd292783326d72b0f38a8b373a2b1bf30). 1080p usa o [SVG Full HD 1080 da Sony](https://commons.wikimedia.org/wiki/File:Full_HD_1080_logo_(Sony).svg).
- 4K Ultra HD, Blu-ray Disc, HDR, DTS:X, DTS-HD Master Audio, Dolby Atmos e Dolby TrueHD vêm da [coleção TaranVH/LOGOS](https://github.com/TaranVH/LOGOS/tree/c5b46e82c87d8ab731112835957aca3000d08da4). As imagens foram recortadas e algumas receberam tinta clara para o fundo escuro.
- HDR10 usa a imagem de [Kingsize Fusion Badges](https://github.com/kingsizew/badges/tree/fdd3479bacf2232e431acda4b59b2858b509d2df/badge-images/visual), com revisão fixa.
- [AV1](https://aomedia.org/resources/logo/), [HDR10+](https://hdr10plus.org/), [Dolby Vision](https://commons.wikimedia.org/wiki/File:Dolby_Vision_2021_logo.svg), [Dolby Digital Plus](https://professional.dolby.com/globalassets/dolby-digital-plus/dolby-digital-plus-audio-coding-tech-paper.pdf), [IMAX](https://commons.wikimedia.org/wiki/File:IMAX_blue_logo.svg) e [The Criterion Collection](https://commons.wikimedia.org/wiki/File:The_Criterion_Collection_logo_and_wordmark.svg).

As marcas identificam os serviços, formatos e coleções que o aplicativo detecta.

## Regenerar as etiquetas tipográficas

Com `fonttools` instalado, execute `python make_badges.py --font BarlowSemiCondensed-Bold.ttf`. Use a [Barlow Semi Condensed Bold](https://github.com/google/fonts/tree/main/ofl/barlowsemicondensed), de Jeremy Tribby, sob SIL Open Font License.
