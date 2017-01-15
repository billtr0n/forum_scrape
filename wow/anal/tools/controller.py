from models import Model
from views import View
import utils

class Controller:
    def __init__(self, root):
        # initialize model and add callback functions to observables
        self.model = Model()
        self.model.post.add_callback( self.update_post )
        self.model.vader_compound_scores.add_callback( self.update_vader )
        self.model.title.add_callback( self.update_title )

        # initialize the view
        self.view = View(root)
        post = self.model.get_next_from_db()
        self.model.post.set( post['first_post'] )
        self.model.title.set( post['title'] )
        self.model.author.set( post['author'] )
        self.model.vader_polarity_scores( post['first_post'] )

        # add event handlers
        self.view.next.config(command=self.next)
        self.view.discard.config(command=self.discard)

    # functions to handle interaction with view
    def next(self):

        # user is supposed to clean using tool
        cleaned = {
            'title':  self.view.get_title(),
            'post':   self.view.get_text(),
            'author': self.model.get_author() # not being modified in gui
        }
        
        # write to training data.
        try:
            if self.view.get_input() == "positive":
                utils.write_positive( cleaned )

            elif self.view.get_input() == "negative":
                utils.write_negative( cleaned )
        except:
            print('error writing to file discarding.')

        # update the model
        self.update_model()



    def update_model( self ):
        post = self.model.get_next_from_db()
        self.model.post.set( post['first_post'] )
        self.model.title.set( post['title'] )
        self.model.vader_polarity_scores( post['first_post'] )
        self.model.author.set( post['author'] )

    def discard( self ):
        self.update_model()


    def update_vader(self, scores):
        self.view.set_vader( scores )

    def update_post(self, text ):
        self.view.set_post( text )

    def update_title(self, text ):
        self.view.set_title( text )


