from tkinter import *
from PIL import Image, ImageTk

class App():
    def __init__(self):

        self.number = 0

    def widget(self):
        self.root = Tk()
        self.root.title("app")
        self.im=Image.open("python.jpg")
        self.img=ImageTk.PhotoImage(self.im)
        self.img_label=Label(self.root,image=self.img)
        self.button = Button(self.root, text="Hello, world!",command = self.click,width=50,height=5)

    def pack(self):
        self.button.pack()
        self.img_label.pack()
        #self.label.place(x=0,y=0)


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
