import requests
import json


def postUser(cep, email, name, username, password):
    url = 'http://mobile-aceite.tcu.gov.br:80/appCivicoRS/rest/pessoas/'
    cep = str(cep)
    if len(cep) is not 8:
        raise ValueError('CEP deve conter 8 dígitos\n')
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
