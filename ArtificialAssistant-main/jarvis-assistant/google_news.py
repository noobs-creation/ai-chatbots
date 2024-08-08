import gnewsclient
from gnewsclient import gnewsclient

def getting_news(topic = 'COVID-19', location = 'India'):
    client_b = gnewsclient.NewsClient(language='english',
                                location=location,
                                topic=topic,
                                max_results=10)
    # print(len(client_b.get_news()))

    return client_b.get_news()


# getting_news(topic='sports')
# client_b = gnewsclient.NewsClient(language='english',
#                                 location='India',
#                                 topic='Business',
#                                 max_results=10)

# client_n = gnewsclient.NewsClient(language='english',
#                                 location='India',
#                                 topic='Nation',
#                                 max_results=10)

# client_t = gnewsclient.NewsClient(language='english',
#                                 location='India',
#                                 topic='Technology',
#                                 max_results=10)

# client_s = gnewsclient.NewsClient(language='english',
#                                 location='India',
#                                 topic='Sports',
#                                 max_results=10)
# # print(client.get_news())

# for news in client_b.get_news():
#     print(news['title'])
#     # print(news['link'])
#     print()

# for news in client_n.get_news():
#     print(news['title'])
#     # print(news['link'])
#     print()

# for news in client_t.get_news():
#     print(news['title'])
#     # print(news['link'])
#     print()

# for news in client_s.get_news():
#     print(news['title'])
#     # print(news['link'])
#     print()