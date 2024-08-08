import requests

url = "https://bing-news-search1.p.rapidapi.com/news/search"

querystring = {"q":"Bitcoin","freshness":"Day","textFormat":"Raw","safeSearch":"Off"}

headers = {
    'x-bingapis-sdk': "true",
    'x-rapidapi-host': "bing-news-search1.p.rapidapi.com",
    'x-rapidapi-key': "62c2b7fb91msh963773aad27380ep1f324ejsnaea42d3980c0"
    }

r = requests.request("GET", url, headers=headers, params=querystring)

data = r.json()

print(data)