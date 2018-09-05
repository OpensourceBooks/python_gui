from tkinter import *

class App():
    def __init__(self):

        self.number = 0
        

    def widget(self):
        self.root = Tk()
        self.root.title("app")
        self.label=Label(self.root)


    def pack(self):
        
        self.label.pack()


    #events
    def click(self):
        self.number += 1
        self.label["text"] = self.number

    def update_clock(self):
        self.click()
        self.root.after(1000, self.update_clock)

    #run
    def run(self):
        self.widget()
        self.pack()
        self.update_clock()
        self.root.mainloop()

App().run()
