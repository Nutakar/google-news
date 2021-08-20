import feedparser
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

query = 'Russia'

def parse_data(query = query):
    url = 'https://news.google.com/rss/search?q={}+when:1y&hl=en-US&gl=US&ceid=US:en'.format(query)
    news = feedparser.parse(url)
    news_count = len(news.entries)
    news_titles = []
    for i in range(news_count):
        entry = news.entries[i]
        news_titles.append(entry.title)
    separate_words = []
    for title in news_titles:
        words_in_title  = str(title).split()
        for word in words_in_title:
            separate_words.append(word)
    return separate_words

def get_top_50(separate_words):
    for word in separate_words:
        if len(word)<=2:
            separate_words.remove(word)
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

def top50_dict_to_str(top_50):
    top_50 = list(top_50)
    top50_str = ''
    for word in top_50:
        top50_str += word + " "
    return top50_str

def plot_cloud(wordcloud):
    plt.figure(figsize=(40, 30))
    plt.imshow(wordcloud)
    plt.axis("off")



list_of_words = parse_data()
top50 = get_top_50(list_of_words)
top50_str = top50_dict_to_str(top50)

wordcloud = WordCloud ( width= 3000, 
                        height= 2000, 
                        random_state=1, 
                        background_color='black', 
                        colormap='Set2', 
                        collocations=False, 
                        stopwords=STOPWORDS).generate(top50_str)
plot_cloud(wordcloud)
wordcloud.to_file("wordcloud.png")
