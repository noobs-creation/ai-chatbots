import requests

def reading_crypto_news():

    url = 'https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,TRX,SHIB,ETH&tsyms=INR&api_key=95735d5f67b07c7707cba3f13f9868cb373206cf5a75de46a2a6c50a651d3a38'
    r = requests.get(url)

    data = r.json()

    print(data)


    url = 'https://min-api.cryptocompare.com/data/v2/news/?lang=EN'

    r = requests.get(url)

    data = r.json()

    return data