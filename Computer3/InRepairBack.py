import  tkinter as  tk
import  tkinter.ttk as ttk
import  InWeiXiuClassSqlDB as sql
import  datetime
from  dateutil.relativedelta import  relativedelta
import  tkinter.messagebox as messagebox
import  User
import  SqlDB as  sqlbase

class InRepairBack(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)

        self.root = master  # 定义内部变量root

        self.pc_no = tk.StringVar()  #
        self.pc_nm = tk.StringVar()  #
        self.spec = tk.StringVar()  # 規格


        self.question = tk.StringVar()#問題
        self.back_date = tk.StringVar()#回廠時間
        self.ask = tk.StringVar()#處理結果

        self.upddate= tk.StringVar()

        self.b_status=tk.StringVar()
        self.b_status.set("10")

        self.createPage()

        # 檢查日期格式是否正確

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

        if not self.back_date.get():
            messagebox.showinfo("", "回廠日期不允許為空")
            return False
        if not self.checkdate(self.back_date.get()):
            messagebox.showinfo("", "回廠日期應為八位有效數字")
            return False
        return True




    def createPage(self):
        def reset():
            self.pc_no.set("")
            self.pc_nm.set("")
            self.spec.set("")
            self.question.set("")
            txt_pc_no.config(state="normal")
            # txt_question.delete("1.0", tk.END)


        def search():
            flag = sql.INWeiXiuSql().searchITcom_Inrepair(self)
            if flag:
                self.back_date.set(str(datetime.datetime.now().strftime("%Y%m%d")))
                btn_save.config(state="normal")
                txt_question.config(state="normal")
                txt_question.insert(tk.END, self.question.get())
                txt_question.config(state="disable")
                txt_pc_no.config(state="disable")
                # self.sx_date.set(str(datetime.datetime.now().strftime("%Y%m%d")))
            else:
                btn_save.config(state="disable")

        def save():
            flag = self.checknull()
            if flag:
                self.upddate.set(str(datetime.datetime.now().strftime("%Y%m%d%H%M%S")))
                self.ask.set(txt_ask.get('1.0', tk.END))
                sql.INWeiXiuSql().updateback(self)
            pass
            # flag = self.checknull()
            # if flag:
            #     self.upddate.set(str(datetime.datetime.now().strftime("%Y%m%d%H%M%S")))
            #     self.question.set(txt_question.get('1.0', tk.END))
            #     sql.INWeiXiuSql().insertINReapir(self)

        frm1=tk.Frame(self)

        btn_reset = tk.Button(frm1, text="重置", command=reset)
        btn_reset.pack(side=tk.LEFT, padx=10)

        btn_search = tk.Button(frm1, text="查询", command=search)
        btn_search.pack(side=tk.LEFT, padx=10)

        btn_save = tk.Button(frm1, text="保存", command=save)
        btn_save.config(state="disable")  # 不可编辑
        btn_save.pack(side=tk.LEFT, padx=10)




        frm2 = tk.Frame(self)

        def searchpc(event):
            flag = sql.INWeiXiuSql().searchITcom_Inrepair(self)
            if flag:
                self.back_date.set(str(datetime.datetime.now().strftime("%Y%m%d")))
                btn_save.config(state="normal")
                txt_question.config(state="normal")
                txt_question.insert(tk.END, self.question.get())
                txt_question.config(state="disable")
                txt_pc_no.config(state="disable")
                # self.sx_date.set(str(datetime.datetime.now().strftime("%Y%m%d")))
            else:
                btn_save.config(state="disable")

        tk.Label(frm2, text="設備編號").grid(row=0, column=0)
        txt_pc_no = tk.Entry(frm2, textvariable=self.pc_no)
        txt_pc_no.grid(row=0, column=1)
        txt_pc_no.bind("<Return>", searchpc)





        tk.Label(frm2, text="設備名稱").grid(row=1, column=0)
        txt_pc_nm = tk.Entry(frm2, textvariable=self.pc_nm)
        txt_pc_nm.grid(row=1, column=1)
        txt_pc_nm.config(state="disable")  # 不可编辑

        tk.Label(frm2, text="規格").grid(row=1, column=2)
        txt_spec = tk.Entry(frm2, textvariable=self.spec)
        txt_spec.grid(row=1, column=3)
        txt_spec.config(state="disable")  # 不可编辑



        tk.Label(frm2, text="故障問題").grid(row=2, column=0)
        txt_question=tk.Text(frm2,width=46,height=3)
        txt_question.grid(row=2, column=1,columnspan=3)




        frm3 = tk.Frame(self)


        tk.Label(frm3, text="回廠日期").grid(row=0, column=0)
        txt_back_date = tk.Entry(frm3, textvariable=self.back_date)
        txt_back_date.grid(row=0, column=1,sticky=tk.W)

        tk.Label(frm3, text="處理結果").grid(row=1, column=0)


        txt_ask = tk.Text(frm3,width=48,height=3)
        txt_ask.grid(row=1, column=1,columnspan=3)














        frm1.pack(side=tk.TOP)
        frm2.pack(side=tk.TOP)
        frm3.pack(side=tk.TOP,pady=20)




        pass