

# from GoogleNews import GoogleNews
# googlenews = GoogleNews()

# googlenews = GoogleNews(lang='en', region='IN')

# googlenews.search('CORONAVIRUS')


import gnewsclient
from gnewsclient import gnewsclient
 
client_b = gnewsclient.NewsClient(language='english',
                                location='India',
                                topic='Business',
                                max_results=10)

client_n = gnewsclient.NewsClient(language='english',
                                location='India',
                                topic='Nation',
                                max_results=10)

client_t = gnewsclient.NewsClient(language='english',
                                location='India',
                                topic='Technology',
                                max_results=10)

client_s = gnewsclient.NewsClient(language='english',
                                location='India',
                                topic='Sports',
                                max_results=10)
# print(client.get_news())

for news in client_b.get_news():
    print(news['title'])
    # print(news['link'])
    print()

for news in client_n.get_news():
    print(news['title'])
    # print(news['link'])
    print()

for news in client_t.get_news():
    print(news['title'])
    # print(news['link'])
    print()

for news in client_s.get_news():
    print(news['title'])
    # print(news['link'])
    print()

# prints location
# print("Location: \n",client.locations)
# print()
 
# prints languages
# print("Language \n",client.languages)
# print()
 
# prints topics
# print("Topic \n",client.topics)