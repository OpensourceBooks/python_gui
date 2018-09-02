from tkinter import *

class App():
    def __init__(self):

        self.number = 0

    def widget(self):
        self.root = Tk()
        self.root.title("app")

        self.button = Button(self.root, text="Hello, world!",command = self.click,width=50,height=5)

    def pack(self):
        self.button.pack()

    #events
    def click(self):
        self.number += 1
        self.button["text"] = self.number

    #run
    def run(self):
        self.widget()
        self.pack()
        self.root.mainloop()

App().run()
