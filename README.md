
<p align="center"><a href="https://fiscae.herokuapp.com/" target="_blank"><img width="300"src="https://i.imgur.com/PTkqmJC.png"></a></p>

<p align="center">
  <a href="https://travis-ci.org/fga-gpp-mds/fisCAE-2017-2"><img src="https://travis-ci.org/fga-gpp-mds/fisCAE-2017-2.svg?branch=development" alt="Build"></a>
  <a href="https://landscape.io/github/fga-gpp-mds/fisCAE-2017-2/development"><img src="https://landscape.io/github/fga-gpp-mds/fisCAE-2017-2/development/landscape.svg?style=flat" alt="Code Health"></a>
  <a href="https://coveralls.io/github/fga-gpp-mds/fisCAE-2017-2?branch=development"><img src="https://coveralls.io/repos/github/fga-gpp-mds/fisCAE-2017-2/badge.svg?branch=development" alt="Coverage Status"></a>
  <a href="https://codeclimate.com/github/fga-gpp-mds/fisCAE-2017-2"><img src="https://codeclimate.com/github/fga-gpp-mds/fisCAE-2017-2/badges/issue_count.svg" alt="Issue Count"></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>
  <a href="https://codeclimate.com/github/fga-gpp-mds/fisCAE-2017-2/maintainability"><img src="https://api.codeclimate.com/v1/badges/2ab2048e44f5f93eaba2/maintainability" /></a>
</p>

<h1 align="center">FisCAE</h1>

## Sobre o projeto
<p align="justify"> &emsp;&emsp; Este projeto tem como objetivo criar um canal de comunicação eficiente entre os conselheiros alimentares escolares (CAEs) e os fiscais do Tribunal de Contas da União (TCU) a fim de otimizar o processo de fiscalização do uso de verbas destinadas à merenda escolar evitando fraudes e a má qualidade do serviço prestado. O Programa Nacional de alimentação Escolar (PNAE) responsável por repassar as verbas destinadas a merenda das escolas públicas brasileiras e regulamentar esse processo, enfrenta problemas tais como a logística de fiscalizar o uso correto do valor repassado tendo em vista que moramos em um país de dimensões continentais. Para tanto, fora criado um grupo de conselheiros em cada município (CAEs) a fim de tentar amenizar esses problemas. Atualmente a fiscalização é realizada através de ações que estão contidas nas cartilhas e denúncias regulares, por telefone e etc. A solução requisitada e proposta no nosso software a ser implementado é coletar os dados provenientes das ações realizadas pelos conselhos e disponibilizá-los na nuvem cívica.</p>

## Guia de Uso do Docker

### Instalação
Primeiramente é necessário ter o docker instalado, caso não tenha acesse o [Instalação docker](https://docs.docker.com/engine/installation/linux/docker-ce/). Após feito isso, instale o [Docker-compose](https://docs.docker.com/compose/install/).

### Utilizando o ambiente

 &emsp;&emsp; Para a utilização do ambiente, basta dar o comando abaixo e ele irá ligar o container:
 
 ```terminal
  docker-compose up -d
 ```

 &emsp;&emsp; Para a visualização dos logs use o comando abaixo:
 ```terminal
  docker-compose logs -f
 ```

 &emsp;&emsp; Para acessar o container use o comando abaixo:
 ```terminal
  docker exec -it NOME-CONTAINER bash
 ```

 &emsp;&emsp; Para parar o container use o comando abaixo:
 
  ```terminal
  docker-compose stop
 ```
 &emsp;&emsp; E para religar um container parado use o comando: 
 
 ```terminal
  docker-compose start
 ```

 &emsp;&emsp; Caso deseje remover um container:
 ```terminal
  docker-compose down
 ```
## Principais funcionalidades até o momento

* Login de usuário
* Acessar Cartilha
* Manter checklist
* Home page

## Licença

 &emsp;&emsp; FisCAE é distribuído sob a licença do MIT. Consulte [LICENSE](https://github.com/fga-gpp-mds/fisCAE-2017-2/blob/master/LICENSE) para obter detalhes.

## Documentação
 &emsp;&emsp; Toda a documentação pode ser acessada através da wiki do projeto [aqui](https://github.com/fga-gpp-mds/fisCAE-2017-2/wiki).

## Criação de administrador
 Acesse a pasta `src` que está localizada dentro da pasta do projeto, abra o shell digitando: 
 ```terminal
 python manage.py shell.
 ```
 No shell, digite os camandos listados abaixo na mesma ordem apresentada:
 
```python

from django.contrib.auth.models import User    
from user.models import Person, Administrator     
user = User.objects.create_user(username='admin', password='admin', is_superuser=True)      
admin = Administrator()    
admin.user = user   
admin.name = 'Administrator'   
admin.email = 'admin@email.com'  
admin.save()   

```
