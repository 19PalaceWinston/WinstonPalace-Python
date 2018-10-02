from tkinter import *

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Window")
        self.pack(fill=BOTH, expand=1)
        #quitButton = Button(self, text="Quit",command=self.client_exit)
        #quitButton.place(x=0, y=0)
        playButton = Button(self, text="Play", command=self.play())
        playButton.place(x=0, y=0)

    def client_exit(self):
        exit()

    def play(self):
        print("")

root = Tk()
root.geometry("700x500")
app = Window(root)
root.mainloop()
