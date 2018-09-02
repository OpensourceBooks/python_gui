import tkinter
class App(object):

    def __init__(self):
        # 创建主窗口,用于容纳其它组件
        self.root = tkinter.Tk()
        self.root['width']=500
        self.root['height']=300
        # 给主窗口设置标题内容
        self.root.title("app")

        self.num=0

        # 创建一个查询结果的按钮
        self.button = tkinter.Button(self.root, command = self.click, text = "click")

    def pack(self):
        self.button.pack()

    # events:

    def click(self):
        self.num+=1
        self.root.title(self.num)

def main():
    # 初始化对象
    app = App()
    # 布局生效
    app.pack()
    # 主程序执行
    tkinter.mainloop()
    pass

if __name__ == "__main__":
    main()
