import feedparser
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

query = 'Russia'

def parse_data(query = query):
    url = 'https://news.google.com/rss/search?q={}+when:1y&hl=en-US&gl=US&ceid=US:en'.format(query)
    news = feedparser.parse(url)
    news_titles = [i.title for i in news.entries]
    separate_words_titles = [str(title).split() for title in news_titles]
    separate_words = []
    for title in separate_words_titles:
        for word in title:
            separate_words.append(word)
    return separate_words

def get_top_50(separate_words):
    separate_words = [word for word in separate_words if len(word)>2]
    dict_of_words = {}
    for word in separate_words:
        if word in dict_of_words:
            dict_of_words[word] +=1
        else:
            dict_of_words[word] = 1
    sorted_dict = dict(sorted(dict_of_words.items(), key = lambda item: item[1], reverse = True))
    sorted_dict_items = sorted_dict.items()
    top_50 = dict(list(sorted_dict_items)[:50])
    print(top_50)
    return top_50
