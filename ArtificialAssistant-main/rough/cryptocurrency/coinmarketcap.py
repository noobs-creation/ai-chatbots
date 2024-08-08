from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'50',
  'convert':'INR'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'f295cc65-eb67-4760-8934-fd214c80fd8f',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
#   print(data['data'])
  for d in data['data']:
      print(d['name'])
      print(d['symbol'])
      print(d['quote']['INR']['price'])
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)