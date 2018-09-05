from PIL import Image,ImageTk
import tkinter as tk

# 简单插入显示
def show_jpg():
    root = tk.Tk()
    im=Image.open("python.jpg")
    img=ImageTk.PhotoImage(im)
    imLabel=tk.Label(root,image=img)
    imLabel.pack()
    root.mainloop()

if __name__ == '__main__':
    show_jpg()