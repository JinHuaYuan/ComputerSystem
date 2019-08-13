import  tkinter as  tk
import  tkinter.messagebox as  messagebox
import  MainClass
import  SqlDB as sql
import  User


class Login:
    def __init__(self,maseter=None):
        self.root=maseter
        self.emp_no=tk.StringVar()
        self.password=tk.StringVar()
        self.photo = tk.PhotoImage(file="d12.png")
        self.page=tk.Frame(self.root)
        self.user_code = tk.StringVar()
        self.user_pwd = tk.StringVar()
        self.cretePage()

    def cretePage(self):
        self.page.pack()

        tx = tk.Text(self.page, width=45, height=10)
        tx.image_create(index="end", image=self.photo, padx=80)
        tx.config(state="disable")#不可编辑
        tx.grid(row=0, column=0, columnspan=3)


        lbl_emp = tk.Label(self.page,text="职号")
        txt_emp = tk.Entry(self.page,textvariable=self.user_code)
        lbl_emp.grid(row=2, column=0)
        txt_emp.grid(row=2, column=1)

        def enterchecklogin(event):
            emp = sql.CONDB().getdbcon()
            if emp:
                cur = emp.cursor()
                # value=(self.user_code,self.user_pwd)
                cur.execute(
                    "select user_code,user_pwd from zuser_info_ITeqm where user_code='%s' and user_pwd='%s' " % (
                        self.user_code.get(), self.user_pwd.get()))
                c1 = cur.fetchall()
                print(c1)
                if (len(c1) == 0):
                    messagebox.showwarning("账号或密码错误", "账号密码不存在，兄弟")
                else:
                    MainClass.MainClass(self.root)
                    User.uer_code = self.user_code.get()
                    User.user_pwd = self.user_pwd.get()
                    self.page.destroy()


        lbl_pwd = tk.Label(self.page,text="密碼")
        txt_pwd = tk.Entry(self.page, show='*',textvariable=self.user_pwd)
        txt_pwd.bind("<Return>",enterchecklogin)



        lbl_pwd.grid(row=3, column=0)
        txt_pwd.grid(row=3, column=1)
        btn_login = tk.Button(self.page,text="登錄", width=10,command=self.checklogin)
        btn_login.grid(row=4, column=0, columnspan=3)

        # btn_login = tk.Button(self.page,text="幫助", width=10, command=lambda: messagebox.showinfo("About us", "有疑問撥打2270"))
        # btn_login.grid(row=5, column=0, columnspan=3)

        self.root.title("電腦管理系統")
        self.root.geometry(newGeometry="300x220")


        self.root.resizable(width=False, height=False)
        self.root.mainloop()







    def checklogin(self):

        emp = sql.CONDB().getdbcon()
        if emp:
            cur=emp.cursor()
           # value=(self.user_code,self.user_pwd)
            cur.execute("select user_code,user_pwd from zuser_info_ITeqm where user_code='%s' and user_pwd='%s' "%(self.user_code.get(),self.user_pwd.get()))
            c1=cur.fetchall()
            print(c1)
            if(len(c1)==0):
                messagebox.showwarning("账号或密码错误","账号密码不存在，兄弟")
            else:
                User.uer_code=self.user_code.get()
                User.user_pwd=self.user_pwd.get()
                MainClass.MainClass(self.root)
                self.page.destroy()


