# imports
import nltk
import nltk.sentiment.vader as vader

import pymongo

import matplotlib
import matplotlib.pyplot as plt

import numpy as np

from pandas import Series

# global settings
matplotlib.rcParams['xtick.direction'] = 'out'
matplotlib.rcParams['ytick.direction'] = 'out'

def main():
    # connect to db
    client = pymongo.MongoClient()
    db = client.test
    posts = db['wow-ptr-items']

    # vader sentiment analysis
    sid = vader.SentimentIntensityAnalyzer()
    post_scores = []
    for post in posts.find():
        paragraph = post['first_post']
        sentences = nltk.tokenize.sent_tokenize(paragraph)

        sentence_scores = []
        for sentence in sentences:
            ss = sid.polarity_scores(sentence)
            sentence_scores.append( ss['compound'] )
        post_scores.append( sum(sentence_scores) / len(sentence_scores) )

    # visualize results
    s = Series(post_scores)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    s.hist(ax=ax)
    ax.set_xlabel('VADER compound score')
    ax.set_ylabel('Count')
    fig.savefig('vader_hist.png')
    


        

if __name__ == "__main__":
    main()
