import tkinter
class App(object):
    def __init__(self):
        # 创建主窗口,用于容纳其它组件
        self.root = tkinter.Tk()
        # 给主窗口设置标题内容
        self.root.title("app")

def main():
    # 初始化对象
    app = App()
    # 主程序执行
    tkinter.mainloop()
    pass

if __name__ == "__main__":
    main()
