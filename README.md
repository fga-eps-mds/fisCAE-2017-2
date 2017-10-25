<br><p align="center"> <img src="https://i.imgur.com/PTkqmJC.png" width="325"></p></br>

# Projeto FisCAE
Esse projeto tem por objetivo criar um canal de comunicação eficiente entre os conselheiros alimentares escolares (CAEs) e os fiscais do Tribunal de Contas da União (TCU) a fim de otimizar o processo de fiscalização do uso de verbas destinadas à merenda escolar evitando fraudes e a má qualidade do serviço prestado. O Programa Nacional de alimentação Escolar (PNAE) responsável por repassar as verbas destinadas a merenda das escolas públicas brasileiras e regulamentar esse processo, enfrenta problemas tais como a logística de fiscalizar o uso correto do valor repassado tendo em vista que moramos em um país de dimensões continentais. Para tanto, fora criado um grupo de conselheiros em cada município (CAEs) a fim de tentar amenizar esses problemas. Atualmente a fiscalização é realizada através de ações que estão contidas nas cartilhas e denúncias regulares, por telefone e etc. A solução requisitada e proposta no nosso software a ser implementado é coletar os dados provenientes das ações realizadas pelos conselhos e disponibilizá-los na nuvem cívica.

## Guia de Uso do Docker

### Instalação
Primeiramente é necessário ter o docker instalado, caso não tenha acesse o [Intalação docker](https://docs.docker.com/engine/installation/linux/docker-ce/). Após feito isso, instale o [Docker-compose](https://docs.docker.com/compose/install/).

### Utilizando o ambiente

Para a utilização do ambiente, basta dar o comando `docker-compose up -d` e ele ira ligar o container.

Para a visualização dos logs use o comando `docker-compose logs -f`.

Para acessar o container use o comando `docker exec -it NOME-CONTAINER bash`.

Para parar o container use o comando `docker-compose stop` , e para religar um container parado use o comando `docker-compose start`.

Caso deseje remover um container `docker-compose down`.

## Principais funcionalidades até o momento

* Login de usuário
* Acessar Cartilha
* Manter checklist
* Home page

## Licença
FisCAE é distribuído sob a licença do MIT. Consulte [LICENSE](https://github.com/fga-gpp-mds/fisCAE-2017-2/blob/master/LICENSE) para obter detalhes.

## Documentaço
Toda a documentação pode ser acessada através da wiki do projeto [aqui](https://github.com/fga-gpp-mds/fisCAE-2017-2/wiki).

