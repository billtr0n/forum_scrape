import pymongo
import utils


class Observable:
    """ general use case for any value that is changing.  callback functions activated
        when the data variable is set.  if initial data is provided, callbacks are not
        preformed until data is updated.
    """
    def __init__(self, initial_value = None):
        self.data = initial_value
        self.callbacks = {}

    def add_callback(self, func):
        self.callbacks[func] = 1

    def _exec_callbacks(self):
        for func in self.callbacks:
            func( self.data ) 
            
    def set(self, data):
        self.data = data
        self._exec_callbacks()

    def get(self):
        return self.data

    def remove(self):
        self.data = None

class Model:
    """ model for initial forum post data """
    def __init__(self):
        # if this becomes big abstract away database access
        client = pymongo.MongoClient()
        db = client.test
        collection = db['wow-ptr-items']

        # store all posts as iterator
        self.posts = collection.find()
        
        # set initial posts
        self.title = Observable()
        self.post = Observable()
        self.author = Observable()

        # other model values
        self.word_count = Observable()
        self.vader_compound_scores = Observable()

    def get_next_from_db(self):
        return next(self.posts)
    
    def get_random_from_db(self, n=40):
        pass

    def set_vader_score( self, scores ):
        self.vader_compound_scores.set( scores )
        
    def set_title( self, val ):
        self.title.set( val )

    def set_post( self, val ):
        self.post.set( val )

    def get_title( self ): return self.title.get()

    def get_post( self ):
        return self.post.get()

    def vader_polarity_scores( self, data ):
        scores = utils.vader_polarity_scores( data )
        self.set_vader_score( scores )
        return scores

    def get_word_count( self ):
        pass

    def get_author( self ):
        return self.author.get()

