import requests
from datetime import datetime
import json
import random
import time


def DataHoraAtual():
    data_hora_atual = datetime.now()
    formato_desejado = "%Y-%m-%dT%H:%M:%S"
    data_hora_formatada = data_hora_atual.strftime(formato_desejado)
    return data_hora_formatada


def RealizarPost() -> dict:
    url = "https://cliente.apdata.com.br/dicon/.net/index.ashx/SaveTimmingEvent"

    usuario = '2600506'
    senha = 'G@el170382'

    payload = {'deviceID': '8001',
               'eventType': '1',
               'userName': usuario,
               'password': senha,
               'cracha': '',
               'costCenter': '',
               'leave': '',
               'func': '0',
               'captcha': '',
               'tenantName': '',
               'tsc': '',
               'sessionID': '0',
               'selectedEmployee': '0',
               'selectedCandidate': '0',
               'selectedVacancy': '0',
               'dtFmt': 'd/m/Y',
               'tmFmt': 'H:i:s',
               'shTmFmt': 'H:i',
               'dtTmFmt': 'd/m/Y H:i:s',
               'language': '0',
               'idEmployeeLogged': '0',
               'rnd': DataHoraAtual()}
    files = [

    ]
    headers = {
        'Origin': 'https://cliente.apdata.com.br',
        'Referer': 'https://cliente.apdata.com.br/dicon/',
        'Cookie': 'X-Oracle-BMC-LBS-Route=bb089166a4d059141e589f5733aa94f02d71e92b; dashPublicImg=dpi; __z_a=2899977914199555886319955; clockDeviceToken8001=/hvmmdjtCMNQzYclwDbwfWoXjZeQljjudvHKcjFufA==; acceptedRequiredCookies=COOKIEACCEPTED; acceptedOptionalCookies=COOKIEACCEPTED; X-Oracle-BMC-LBS-Route=bb089166a4d059141e589f5733aa94f02d71e92b'
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    return json.loads(response.text)


print(f'{datetime.now()} - Processo iniciado')

atraso = random.randint(0, 5) * 60
hora = datetime.now().hour

print(f'{datetime.now()} - Adicionando um atrado de {atraso / 60} minutos')

if hora != 19:
    time.sleep(atraso)

ret = RealizarPost()
mensagem = ''
if ret["success"]:
    mensagem = 'Operacao realizada com sucesso'
else:
    mensagem = 'Erro no registro do ponto'

print(f'{datetime.now()} - {mensagem}')
print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ \n')
