from tkinter import *

class App():
    def __init__(self):

        self.number = 0
        self.root = Tk()
        self.root.title("app")
        self.button = Button(self.root, text="Hello, world!",command = self.click)


    #events
    def click(self):
        self.number += 1
        self.button["text"] = self.number

    #run
    def run(self):
        self.button.pack()
        self.root.mainloop()

App().run()
