<b><p align="center">
<img src="https://github.com/fga-gpp-mds/fisCAE-2017-2/blob/Mateusas3s-patch-1/photo5001714833711802342.jpg">
</p></br>

# Projeto fisCAE
<p align="justify">Esse projeto tem por objetivo criar um canal de comunicação eficiente entre os conselheiros alimentares escolares (CAEs) e os fiscais do Tribunal de Contas da União (TCU) a fim de otimizar o processo de fiscalização do uso de verbas destinadas à merenda escolar evitando fraudes e a má qualidade do serviço prestado. O Programa Nacional de alimentação Escolar (PNAE) responsável por repassar as verbas destinadas a merenda das escolas públicas brasileiras e regulamentar esse processo, enfrenta problemas tais como a logística de fiscalizar o uso correto do valor repassado tendo em vista que moramos em um país de dimensões continentais. Para tanto, fora criado um grupo de conselheiros em cada município (CAEs) a fim de tentar amenizar esses problemas. Atualmente a fiscalização é realizada através de ações que estão contidas nas cartilhas e denúncias regulares, por telefone e etc. A solução requisitada e proposta no nosso software a ser implementado é coletar os dados provenientes das ações realizadas pelos conselhos e disponibilizá-los na nuvem cívica.</p>

## Equipe de Desenvolvimento
|Nome | Email | Git|
|----------|-------|-------------|  
|Amanda Bezerra da Silva|emaildaamandasilva@gmail.com |[amandabezerra](https://github.com/amandabezerra)
|Eduardo Júnio Veloso Rodrigues|eduardojvr10@gmail.com |[Eduardojvr](https://github.com/Eduardojvr)
|José Aquiles Guedes Rezende|mksgalvao@gmail.com |[aquiles23](https://github.com/aquiles23)           
|Luís Bruno Fidelis |l_brunofidelis@yahoo.com.br |[lbrunofidelis](https://github.com/lbrunofidelis)          
|Mateus Augusto Sousa e Silva|eduardojvr10@gmail.com |[Mateusas3s](https://github.com/Mateusas3s)        
|Miguel Siqueira Santos|miguelisdemir@gmail.com |[miguelisdemir](https://github.com/miguelisdemir)      
|Mônica Karoline Silva Galvão|mksgalvao@gmail.com |[mksgalvao](https://github.com/mksgalvao)      

## Equipe de Gerência
|Nome | Email | Git|
|----------|-------|-------------|       
|Henrique Lopes Dutra| hlopes1331@gmail.com |[henriquedutra](https://github.com/henriquedutra)
|Hugo da Silva de Freitas Catarino|hugocatarino1@gmail.com |[hugocatarino](https://github.com/hugocatarino)     
|Marcelo Martins de Oliveira|martins.oliveira.mo@gmail.com |[oliveiraMarcelo](https://github.com/oliveiraMarcelo)
|Matheus Henrique Sousa Costa|matheus.bionicle@gmail.com |[matheusherique](https://github.com/matheusherique)     
|Ramon Silva Sales|ramon.silvasales@gmail.com |[ramonsales](https://github.com/ramonsales)     


## Guia de Uso do Docker

### Instalação
Primeiramente é necessário ter o docker instalado, caso não tenha acesse o [Intalação docker](https://docs.docker.com/engine/installation/linux/docker-ce/). Após feito isso, instale o [Docker-compose](https://docs.docker.com/compose/install/).

### Utilizando o ambiente

Para a utilização do ambiente, basta dar o comando `docker-compose up -d` e ele ira ligar o container.

Para a visualização dos logs use o comando `docker-compose logs -f`.

Para acessar o container use o comando `docker exec -it NOME-CONTAINER bash`.

Para parar o container use o comando `docker-compose stop` , e para religar um container parado use o comando `docker-compose start`.

Caso deseje remover um container `docker-compose down`.
