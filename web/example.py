import hashlib
import hmac
import json
import requests
from config import api_creds

API_URL = 'https://api.changelly.com'
API_KEY = api_creds['key']
API_SECRET = api_creds['secret']

message = {
    'jsonrpc': '2.0',
    'id': 1,
    'method': 'getCurrencies',
    'params': []
}

serialized_data = json.dumps(message)

sign = hmac.new(API_SECRET.encode('utf-8'), serialized_data.encode('utf-8'), hashlib.sha512).hexdigest()

headers = {'api-key': API_KEY, 'sign': sign, 'Content-type': 'application/json'}
response = requests.post(API_URL, headers=headers, data=serialized_data)

print(response.json())
