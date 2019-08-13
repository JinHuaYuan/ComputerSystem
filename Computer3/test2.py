import  tkinter as tk

class  A:
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.geometry('%dx%d' % (300, 180))  # 设置窗口大小
        self.username = tk.StringVar()
        self.username.set("ddd")
        self.password = tk.StringVar()
        self.password.set("T")
        self.createPage()



    def createPage(self):
        tk.Entry(self.root,textvariable=self.username).pack()
        ck1=tk.Checkbutton(self.root, variable=self.password,onvalue="T",offvalue="F")

        def chang(event):
            print(self.password.get())

        ck1.bind("<Button-1>",chang)

        ck1.pack()


wk=tk.Tk()
a=A(wk)
wk.mainloop()
