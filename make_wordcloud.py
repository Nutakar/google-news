import parse
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

def top50_dict_to_str(top_50):

    '''turn top-50 dict to string in order to hand over to wordcloud's lib'''

    top_50 = list(top_50)
    top50_str = ''
    for word in top_50:
        top50_str += word + " "
    return top50_str

def plot_cloud(wordcloud):

    '''set parameters to wordcloud image'''

    plt.figure(figsize=(40, 30))
    plt.imshow(wordcloud)
    plt.axis("off")



list_of_words = parse.parse_data()
top50 = parse.get_top_50(list_of_words)
top50_str = top50_dict_to_str(top50)

wordcloud = WordCloud  (width=3000,
                        height=2000,
                        random_state=1,
                        background_color='black',
                        colormap='Set2',
                        collocations=False,
                        stopwords=STOPWORDS).generate(top50_str)
plot_cloud(wordcloud)
wordcloud.to_file("wordcloud.png")
