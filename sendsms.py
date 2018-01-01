#!/usr/bin/python3.4
from sys import argv
import requests
import json
smsurl= 'URL'
headers= {'Content-type': 'application/json', 'Accept': 'text/plain'}
script, sendto , text = argv
to = sendto
text = text
def singlesms():
        data = {
        "login":"LOGIN",
        "password":"PASSWORD",
        "MessageItems":[{
                "to":to,
                "body":text}]
        }
        jsondata=json.dumps(data)
        r = requests.post(url = smsurl, data = jsondata,headers=headers)


singlesms()
