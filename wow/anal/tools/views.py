import Tkinter

class View(Tkinter.Toplevel):
    def __init__( self, master ):
        Tkinter.Toplevel.__init__(self, master)
        self.protocol('WM_DELETE_WINDOW', self.master.destroy)
        self.geometry("575x510")
        self.resizable(width=False, height=False)

        # add text area for viewing title
        self.title = Tkinter.Entry(self, width=8)
        self.title.grid(row=0, column=0, columnspan=10, rowspan=1, sticky='nsew', padx=(5,5))

        # add text area for viewing post
        self.text = Tkinter.Text(self, wrap=Tkinter.WORD)
        self.text.grid(row=1, column=0, columnspan=10, rowspan=7, padx=(5,5))

        # add classification stuff
        self.var = Tkinter.StringVar(self)
        self.var.set("positive")
        self.entry = Tkinter.OptionMenu(self, self.var, "positive", "negative")
        self.entry.grid(row=9, column=4, columnspan=2, sticky='nesw')

        # add label for vader scores on each post
        self.vader_label = Tkinter.Label(self, text="")
        self.vader_label.grid(row=8, column=3, columnspan=4, sticky='nesw')

        # add padding
        self.blank_space = Tkinter.Label(self)
        self.blank_space.grid(row=10, column=0, columnspan=10, pady=(15,15))

        # add buttons
        self.next = Tkinter.Button(self, text='Next', width=8)
        self.next.grid(row=11, column=5, sticky='nesw')

        self.discard = Tkinter.Button(self, text="Discard", width=8)
        self.discard.grid(row=11, column=4, sticky='nesw')

    # getters and setters
    def set_vader( self, score ):
        self.vader_label.config(text="vader: %.2f" % score)

    def set_post( self, post ):
        self.text.delete(1.0, Tkinter.END)
        self.text.insert(Tkinter.INSERT, post)

    def get_input( self ):
        return self.var.get()

    def get_text( self ):
        return self.text.get(1.0, Tkinter.END)

    def get_title( self ):
        return self.title.get()

    def set_title( self, text ):
        self.title.delete(0, Tkinter.END)
        self.title.insert(Tkinter.INSERT, text)
