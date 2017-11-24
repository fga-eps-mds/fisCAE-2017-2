import requests
import json
from .models import Profile


def postUser(cep, email, name, username, password):
    url = 'http://mobile-aceite.tcu.gov.br:80/appCivicoRS/rest/pessoas/'
    cep = str(cep)
    """if len(cep) is not 8:
        raise ValueError('CEP deve conter 8 dígitos\n')"""
    email = str(email)
    name = str(name)
    username = str(username)
    password = str(password)
    data = {
        "CEP": cep,
        "email": email,
        "nomeCompleto": name,
        "nomeUsuario": username,
        "senha": password,
        "sexo": "F",
        "tokenFacebook": "",
        "tokenGoogle": "",
        "tokenInstagram": "",
        "tokenTwitter": ""
    }

    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    response = requests.post(url, data=json.dumps(data), headers=headers)

    return response


def authenticateUser(email, password):
    email = str(email)
    password = str(password)

    url_base = 'http://mobile-aceite.tcu.gov.br:80/appCivicoRS'
    rest = '/rest/pessoas/autenticar?'
    url = url_base + rest

    headers = {'email': email, 'senha': password}
    request = requests.get(url, headers=headers)

    text = json.loads(request.text)
    header = request.headers
    dictionary = {'request': request, 'text': text, 'header': header}

    return dictionary


def registerProfile(description, codAplicativo, email, password):
    authenticate = authenticateUser(email, password)
    codAplicativo = str(codAplicativo)
    app_token = authenticate.get('header').get('appToken')

    description = str(description)

    data = {
        "descricao": description
    }

    url_base = 'http://mobile-aceite.tcu.gov.br:80/appCivicoRS'
    rest = '/rest/aplicativos/' + codAplicativo + '/tipos-perfil'
    url = url_base + rest
    headers = {
        'Content-type': 'application/json',
        'Accept': 'text/plain',
        'appToken': str(app_token)
    }
    response = requests.post(url, data=json.dumps(data), headers=headers)

    return response


def associateProfile(perfil, codPessoa, email, password):
    authenticate = authenticateUser(email, password)
    codPessoa = str(codPessoa)
    app_token = authenticate.get('header').get('appToken')
    profile = Profile.objects.get(description=perfil)
    codTipoPerfil = profile.code

    url_base = 'http://mobile-aceite.tcu.gov.br:80/appCivicoRS'
    rest = '/rest/pessoas/' + codPessoa + '/perfil'
    url = url_base + rest

    data = {
        "camposAdicionais": "",
        "tipoPerfil": {
            "codTipoPerfil": codTipoPerfil
        }
    }

    headers = {
        'Content-type': 'application/json',
        'appToken': str(app_token)
    }
    response = requests.post(url, data=json.dumps(data), headers=headers)
    print(response.text)
    return response
