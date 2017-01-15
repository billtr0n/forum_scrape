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
    for post in posts.find():
        paragraph = post['first_post']
        sentences = nltk.tokenize.sent_tokenize(paragraph)

        print(post['title'])
        for sentence in sentences:
            ss = sid.polarity_scores(sentence)
            print(sentence)
            print(ss)
        print()
    
    # output results


        

if __name__ == "__main__":
    main()
