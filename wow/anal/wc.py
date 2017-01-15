from __future__ import print_function
import pymongo
from wordcloud import WordCloud
import nltk
import nltk.sentiment.vader as vader

import matplotlib.pyplot as plt

def main():
    # connect on localhost:default_port
    client = pymongo.MongoClient()
    db = client.test
    posts = db['wow-ptr-items']
    words = []
    for post in posts.find():
        words.append(post['first_post'])
    
    with open('stopwords.txt') as fin:
        stop = fin.readlines()
    
    # filter out stopwords
    filtered = [word for word in words if word not in stop]

    # build wordcloud
    wordcloud = WordCloud(max_font_size=72).generate( ' '.join(filtered) )

# lower max_font_size
    plt.figure()
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.savefig('title_cloud_stop.png')


if __name__ == "__main__":
    main()
