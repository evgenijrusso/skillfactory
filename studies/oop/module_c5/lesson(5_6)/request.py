import requests
import json
from config import LAYER_API_KEY


payload = {}
headers = {"apikey": LAYER_API_KEY}

# -------------  1 - вариант (оригинал) -------------------------

# url = "https://api.apilayer.com/exchangerates_data/latest?symbols=RUB,USD,EUR&base=USD"
# response = requests.request("GET", url, headers=headers,  data=payload)

# -------------  2 - вариант (удобный) -------------------------
#
params = {
    'symbols': 'USD, EUR, RUB',
    'base': 'USD'
}

dots = ['/latest', '/convert']

url = "https://api.apilayer.com/exchangerates_data"
url = url + dots[0]
r = requests.request("GET", url,  headers=headers, params=params, data=payload)


status_code = r.status_code
print('status_code:', status_code)
result = r.text
print('result: ', result)
d = json.loads(r.content)
print('d:', d)
print('base:', d['base'])
print('date:', d['date'])
