ACCESS_KEY = '4ed30b52073578793dc9eb0880522609'

# url = 'http://api.mediastack.com/news?access_key=4ed30b52073578793dc9eb0880522609&country=in'

# import requests
# # sending get request and saving the response as response object
# r = requests.get(url)
# print(r.json())


import http.client, urllib.parse

conn = http.client.HTTPConnection('api.mediastack.com')

# Available News Categories:

# general - Uncategorized News
# business - Business News
# entertainment - Entertainment News
# health - Health News
# science - Science News
# sports - Sports News
# technology - Technology News

# -general - general excluded
# -business - business excluded

# general, business - both included

params = urllib.parse.urlencode({
    'access_key': ACCESS_KEY,
    'categories': 'general, business',
    'countries': 'in',
    'languages': 'en',
    'sort': 'published_desc',
    'limit': 100,
    })

conn.request('GET', '/v1/news?{}'.format(params))

res = conn.getresponse()
data = res.read()

str_data = data.decode("utf-8")
import json

json_data = json.loads(str_data)

# print(json_data['data'])
for j in json_data['data']:
    print(j['title'])
    print(j['description'])
    print()
