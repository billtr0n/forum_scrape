import os
from string import Template

import nltk
import nltk.sentiment.vader as vader

import pandas

""" decorators... maybe more into different file at some point. """
def bind_static(**kwargs):
    def decorate(func):
        for k in kwargs:
            setattr(func, k, kwargs[k])
        return func
    return decorate


""" pipeline tasks """
def vader_polarity_scores( paragraph ):
    sid = vader.SentimentIntensityAnalyzer()
    sentences = nltk.tokenize.sent_tokenize(paragraph)
    scores = []
    for sentence in sentences:
        s = sid.polarity_scores(sentence)
        scores.append( s )
    d = pandas.DataFrame( scores )
    return d['compound'].mean()


@bind_static(count=0)
def write_positive( data ):
    cwd = os.getcwd()

    # read string template
    fin = open( os.path.join( cwd, 'template.txt' ) )
    temp = Template( fin.read() )
    out = temp.substitute( data )

    # write output file
    fname = os.path.join( cwd, "data_cleaned/positive/%07i.txt" % write_positive.count )
    with open( fname, 'w') as fout:
        fout.write( out )

    # update count
    write_positive.count += 1


@bind_static(count=0)
def write_negative( data ):
    cwd = os.getcwd()

    # read string templates
    fin = open( os.path.join( cwd, 'template.txt' ) )
    temp = Template( fin.read() )
    out = temp.substitute( data )

    # write output file
    fname = os.path.join( cwd, "data_cleaned/negative/%07i.txt" % write_negative.count )
    with open( fname, 'w' ) as fout:
        fout.write( out )

    # update count
    write_negative.count += 1

