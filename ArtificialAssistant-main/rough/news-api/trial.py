API_KEY = '726dda269ab74bb4b77c39b8983fa33d'

import requests
  
# api-endpoint
# URL = "https://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey="+API_KEY
URL = 'https://newsapi.org/v2/top-headlines?q=Bitcoin&category=business&language=en&apiKey=726dda269ab74bb4b77c39b8983fa33d'
  
  
# sending get request and saving the response as response object
r = requests.get(url = URL)
  
# extracting data in json format
data = r.json()

print(data['articles'])

for d in data['articles']:
    print(d['title'])
    print(d['description'])
    print()