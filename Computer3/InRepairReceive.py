import  tkinter as  tk
import  tkinter.ttk as ttk
import  InWeiXiuClassSqlDB as sql
import  datetime
from  dateutil.relativedelta import  relativedelta
import  tkinter.messagebox as messagebox
import  User
import  SqlDB as  sqlbase

class InRepairReceive(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)

        self.root = master  # 定义内部变量root

        self.pc_no = tk.StringVar()  #
        self.pc_nm = tk.StringVar()  #
        self.spec=tk.StringVar()
        self.question = tk.StringVar()


        self.receive_person=tk.StringVar()
        self.receive_date = tk.StringVar()

        self.upddate = tk.StringVar()

        self.b_status = tk.StringVar()
        self.b_status.set("15")
        self.createPage()


    def checkdate(self, date_time):
        try:
            datetime.datetime.strptime(date_time, '%Y%m%d')
            return True
        except:
            return False

    def checknull(self):
        if not self.pc_no.get():
            messagebox.showinfo("", "設備編號不允許為空")
            return False

        if not self.receive_date.get():
            messagebox.showinfo("", "領取日期不允許為空")
            return False
        if not self.receive_person.get():
            messagebox.showinfo("", "領取人不允許為空")
            return False

        if not self.checkdate(self.receive_date.get()):
            messagebox.showinfo("", "回廠日期應為八位有效數字")
            return False
        return True




    def createPage(self):
        def reset():
            self.pc_no.set("")
            self.pc_nm.set("")
            self.receive_person.set("")
            self.receive_date.set("")

            self.upddate.set("")

            btn_save.config(state="disable")
            txt_pc_no.config(state="normal")


            # txt_question.delete("1.0", tk.END)

        def search():
            flag = sql.INWeiXiuSql().searchITcom_Inrepair(self)
            if flag:
                self.receive_date.set(str(datetime.datetime.now().strftime("%Y%m%d")))
                btn_save.config(state="normal")
                txt_pc_no.config(state="disable")
                # self.sx_date.set(str(datetime.datetime.now().strftime("%Y%m%d")))
            else:
                btn_save.config(state="disable")

        def save():
            flag = self.checknull()
            if flag:
                self.upddate.set(str(datetime.datetime.now().strftime("%Y%m%d%H%M%S")))
                sql.INWeiXiuSql().updatereceive(self)
            pass


        frm1 = tk.Frame(self)

        btn_reset = tk.Button(frm1, text="重置", command=reset)
        btn_reset.pack(side=tk.LEFT, padx=10)

        btn_search = tk.Button(frm1, text="查询", command=search)
        btn_search.pack(side=tk.LEFT, padx=10)

        btn_save = tk.Button(frm1, text="保存", command=save)
        btn_save.config(state="disable")  # 不可编辑
        btn_save.pack(side=tk.LEFT, padx=10)




        frm2=tk.Frame(self)

        def searchpc(event):
            flag = sql.INWeiXiuSql().searchITcom_Inrepair(self)
            if flag:
                self.receive_date.set(str(datetime.datetime.now().strftime("%Y%m%d")))
                btn_save.config(state="normal")
                txt_pc_no.config(state="disable")
                # self.sx_date.set(str(datetime.datetime.now().strftime("%Y%m%d")))
            else:
                btn_save.config(state="disable")


        tk.Label(frm2,text="設備編號").grid(row=0,column=0)
        txt_pc_no=tk.Entry(frm2,textvariable=self.pc_no)
        txt_pc_no.grid(row=0,column=1)
        txt_pc_no.bind("<Return>", searchpc)



        tk.Label(frm2, text="設備名稱").grid(row=1, column=0)
        txt_pc_nm = tk.Entry(frm2,textvariable=self.pc_nm)
        txt_pc_nm.config(state="disable")  # 不可编辑
        txt_pc_nm.grid(row=1, column=1)




        def masterinfo(event):
            dict=sql.CONDB().getEmpInfo(self.receive_person.get()[0:5])
            if(len(dict)>0):
                self.receive_person.set(dict["emp"])
            else:
                if self.receive_person.get():
                    messagebox.showinfo("", "沒有改職號或已經離職")
                    self.receive_person.set("")

        tk.Label(frm2, text="領取人").grid(row=2, column=0)
        txt_receive_person= tk.Entry(frm2,textvariable=self.receive_person)
        txt_receive_person.grid(row=2, column=1)
        txt_receive_person.bind('<Return>', masterinfo)
        txt_receive_person.bind('<FocusOut>', masterinfo)






        tk.Label(frm2, text="領取日期").grid(row=3, column=0)
        txt_receive_person = tk.Entry(frm2,textvariable=self.receive_date)
        txt_receive_person.grid(row=3, column=1)





        frm1.pack(side=tk.TOP)
        frm2.pack(side=tk.TOP)