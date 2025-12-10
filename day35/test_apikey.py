import os
from sms_ir import SmsIr
import requests
import json
from dotenv import load_dotenv
load_dotenv()
URL = "https://api.sms.ir/v1/send/verify"
header = {
        'Content-Type': 'application/json',
        'Accept': 'text/plain',
        'x-api-key': os.getenv("X-API-KEY")
}
body = {
    "mobile": "9912005828",
    "templateId": 123456,
    "parameters": [
      {
        "name": "Code",
        "value": "12345"
      }
    ]
}
r = requests.post(url=URL, json=body, headers=header)
r.raise_for_status()
print(r.status_code)
print(r.json())
print(r.text)
print(r.url)
print(r.headers)
print(r.connection)
print(r.content)
print(r.cookies)
print(r.history)





