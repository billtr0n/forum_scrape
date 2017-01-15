import Tkinter
from controller import Controller


if __name__ == '__main__':
    root = Tkinter.Tk()
    root.withdraw()
    app = Controller(root)
    root.mainloop()
