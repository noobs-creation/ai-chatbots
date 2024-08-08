import requests

url = 'https://api.binance.com/api/v1/ticker/24hr'
bnn_df = requests.get(url).json()

print(bnn_df)