from newsapi import NewsApiClient

api = NewsApiClient(api_key='726dda269ab74bb4b77c39b8983fa33d')

headlines = api.get_top_headlines(sources='google-news-in')

print(headlines['articles'])

for h in headlines['articles']:
    print(h['title'])
    print(h['description'])
    print(h['content'])
    print()

# bitcoin = api.get_everything(q='bitcoin')

# print(bitcoin)