api_key = '2FpmxLePkWTs4BHJ8UQld5vubd5kldyKiQocy-pe6ujafQ_U'

import requests
# url = ('https://api.currentsapi.services/v1/latest-news?'
#         'language=en&'
#         'country=in&'
#         'apiKey=2FpmxLePkWTs4BHJ8UQld5vubd5kldyKiQocy-pe6ujafQ_U')
# response = requests.get(url)
# data = response.json()

# print(data['news'])

# for d in data['news']:
#     print(d['title'])
#     print(d['description'])
#     print()


url = ('https://api.currentsapi.services/v1/search?'
        'keywords=Bitcoin&language=en&'
        'apiKey=2FpmxLePkWTs4BHJ8UQld5vubd5kldyKiQocy-pe6ujafQ_U')
response = requests.get(url)
data = response.json()
# print(data)

for d in data['news']:
    print(d['title'])
    print(d['description'])
    print()