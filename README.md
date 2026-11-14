# Selos para AIOStreams

Em **Configurações → Reprodução → Versões → Selos**, vincule o [endereço do pacote](https://raw.githubusercontent.com/Prokyro/aiostreams-selos/main/badges.json). O AIOStreams atualiza o pacote periodicamente e sincroniza a configuração entre dispositivos da mesma conta, inclusive TVs. [Documentação do AIOStreams](https://aiostreams.org/reference/version-badges/)

- O microfone cromado com fones verdes aparece quando a versão entra em `Dublado PT - em cache` ou `Dublado PT - sem cache`.
- Os balões verde e dourado aparecem quando a versão entra em `Legendado PT - em cache` ou `Legendado PT - sem cache`.

Os dois selos leem a preferência selecionada (`seMatched`). A classificação pode vir da faixa ou de uma indicação aceita pelas regras da configuração. Português do Brasil, de Portugal e sem região usam os mesmos ícones.

## Prioridade de HDR e Dolby Vision

O pacote mostra **no máximo um selo de faixa dinâmica por versão**, com a prioridade `Dolby Vision → HDR10+ → HDR10 → HLG → HDR → SDR`. `HDR+DV`, `DV Only`, `DV`, `DoVi` e `Dolby Vision` são representados por **apenas Dolby Vision**; o selo combinado antigo não é mais uma regra ativa. Os arquivos de imagens anteriores permanecem preservados.

Os formatos são reconhecidos somente em `visualTags`; os selos não alteram o HDR do vídeo, a ordem dos streams nem as pontuações. Essa exclusividade vale **dentro deste pacote**: outros pacotes ou selos personalizados de HDR podem apresentar ícones adicionais.

### Selo 10BIT sem redundância com HDR

O selo `10BIT` usa o mesmo grupo `hdr` e fica depois de Dolby Vision, HDR10+, HDR10, HLG e HDR. Isso faz o aplicativo esconder **10BIT quando qualquer desses formatos HDR for reconhecido**. O selo SDR não participa desse grupo, permitindo exibir **SDR + 10BIT** juntos quando ambos são identificados.

Se um arquivo trouxer `10bit` sem nenhuma tag HDR identificada, o selo 10BIT também aparece; **não é necessário existir uma tag SDR explícita**. A regra remove redundância visual, mas não confirma a profundidade de cor por FFprobe, não muda a classificação dos streams e não exige qualquer alteração nas Ranked Stream Expressions.

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

## Integração por faixa de áudio (14/11/2026)

O formato de áudio (Atmos, DTS:X, TrueHD, DTS-HD MA e DD+) e os canais (7.1 / 5.1) agora usam `rseMatched` da configuração **AIO PT Qualidade** atualizada, e não os `audioTags` / `audioChannels` agregados do arquivo. Dessa forma, áudio português DD+ 5.1 + áudio inglês Atmos mostra DD+ e 5.1, e não o Atmos inglês.

As novas expressões de pontuação zero são `Faixa PT <formato>`, `Canais PT <canais>`, `Áudio geral <formato>` e `Canais gerais <canais>`. A detecção usa a mesma faixa que possui idioma português (independente da variante PT-BR/PT-PT); faixas sem idioma podem ser consideradas quando o título da faixa declara português. Sem faixa portuguesa detectada, o selo de áudio geral é usado **somente quando o stream não foi classificado como áudio PT**. Quando o português é apenas indicado por nome/indexador e o formato da faixa não está disponível, os selos de formato/canais são omitidos em vez de exibir o codec da trilha estrangeira.

**Importante:** é necessário importar a configuração AIOStreams correspondente, com as 14 regras classificadas adicionadas; o pacote de badges, por si só, não enxerga as faixas de áudio. Todas essas regras têm score 0 e não alteram a pontuação. Os símbolos, imagens, URLs dos arquivos e demais regras do pacote foram preservados.
