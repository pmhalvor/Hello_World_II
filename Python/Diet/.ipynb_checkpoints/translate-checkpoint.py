import requests, json, uuid
from config import *


url = "https://api.cognitive.microsofttranslator.com"
path = '/translate'
constructed_url = url + path

params = {
    'api-version': '3.0',
    'from': 'no',
    'to':   'en'
}

headers = {
    'Ocp-Apim-Subscription-Key': key,
    'Ocp-Apim-Subscription-Region': location,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}


def translate(input):
    body = ''
    if type(input)==type(''):
        body = [{
            'text': input
        }]
    elif type(input)==type([]):
        body = input
    
    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    return request.json()


