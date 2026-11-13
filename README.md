# Selos para AIOStreams

Em **Configurações → Reprodução → Versões → Selos**, vincule o [endereço do pacote](https://raw.githubusercontent.com/Prokyro/aiostreams-selos/main/badges.json). O AIOStreams atualiza o pacote periodicamente e sincroniza a configuração entre dispositivos da mesma conta, inclusive TVs. [Documentação do AIOStreams](https://aiostreams.org/reference/version-badges/)

- Bandeira e alto-falante em verde indicam áudio em português do Brasil.
- Bandeira e balão com linhas em azul indicam legendas em português do Brasil.

Os 78 selos são SVGs autônomos, desenhados para a altura de 16 px usada pelo aplicativo. Os caracteres técnicos são contornos vetoriais e dispensam fontes instaladas no aparelho.

## Regenerar os SVGs

Com `fonttools` instalado, execute `python make_badges.py --font BarlowSemiCondensed-Bold.ttf --flag flag.svg`. Use a [Barlow Semi Condensed Bold](https://github.com/google/fonts/tree/main/ofl/barlowsemicondensed), de Jeremy Tribby, sob SIL Open Font License, e o [SVG da bandeira do Brasil em domínio público](https://commons.wikimedia.org/wiki/File:Flag_of_Brazil.svg). A geometria da bandeira foi adaptada com cores e brilho para leitura em escala pequena.
