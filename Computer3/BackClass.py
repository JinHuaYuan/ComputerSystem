import  tkinter as  tk
import  tkinter.messagebox as messagebox
import  datetime
import  BorrowClassSqlDB as Borrowsql
class Back(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.root = master  # 定义内部变量root

        self.pc_no = tk.StringVar()
        self.pc_nm = tk.StringVar()
        self.gb_date = tk.StringVar()
        self.address = tk.StringVar()
        self.tem_noYN = tk.StringVar()  # 臨時編號
        self.tem_noYN.set("F")
        self.spec = tk.StringVar()
        self.master_emp = tk.StringVar()
        self.con_person = tk.StringVar()
        self.con_phone = tk.StringVar()
        self.len_date=tk.StringVar()#借出日期
        self.back_date = tk.StringVar() # 計劃歸還日期
        self.ex_back_date = tk.StringVar() # 實際歸還日期

        self.upddate=tk.StringVar()
        #self.upddate.set(str(datetime.datetime.now().strftime("%Y%m%d%H%M%S")))

        # self.zhuban_part_no = tk.StringVar()  # 主板编号
        # self.zhuban_nm = tk.StringVar()  # 主板名称
        # self.zhuban_spec = tk.StringVar()  # 主板规格
        # self.zhuban_qty = tk.StringVar()  # 主板数量
        #
        # self.cpu_part_no = tk.StringVar()  # cpu编号
        # self.cpu_nm = tk.StringVar()  # cpu名称
        # self.cpu_spec = tk.StringVar()  # cpu规格
        # self.cpu_qty = tk.StringVar()  # cpu数量
        #
        # self.yingpan_part_no = tk.StringVar()  # 硬盘编号
        # self.yingpan_nm = tk.StringVar()  # 硬盘名称
        # self.yingpan_spec = tk.StringVar()  # 硬盘规格
        # self.yingpan_qty = tk.StringVar()  # 硬盘数量
        #
        # self.neicun_part_no = tk.StringVar()  # 内存编号
        # self.neicun_nm = tk.StringVar()  # 内存名称
        # self.neicun_spec = tk.StringVar()  # 内存规格
        # self.neicun_qty = tk.StringVar()  # 内存数量
        self.createPage()

    # 檢查日期格式是否正確
    def checkdate(self,date_time):
        try:
            datetime.datetime.strptime(date_time, '%Y%m%d')
            return True
        except:
            return False

    def checknull(self):
        if not self.ex_back_date.get():
            messagebox.showinfo("", "實際歸還日期不允許為空")
            return False
        if not self.checkdate(self.ex_back_date.get()):
            messagebox.showinfo("", "實際歸還日期應為八位有效數字")
            return False

        return True


    def createPage(self):

        def reset():
            self.pc_nm.set("")
            self.gb_date.set("")
            self.address.set("")
            self.tem_noYN.set("")
            self.spec.set("")
            self.master_emp.set("")
            self.con_person.set("")
            self.len_date.set("")
            self.con_phone.set("")
            self.back_date.set("")
            self.ex_back_date.set("")
            self.tem_noYN.set("F")
            txt_pc_no.config(state="normal")  # 不可编辑


        def search():
            dict=Borrowsql.BorrowSql().search_borrow(self.pc_no.get().strip())
            if (len(dict) > 0):
                self.pc_nm.set(dict["pc_name"])
                self.gb_date.set(dict["guobao_date"])
                self.address.set(dict["address"])
                self.tem_noYN.set(dict["temp_noYN"])
                self.spec.set(dict["p_spec"])
                self.master_emp.set(dict["master_empno"] )

                self.con_person.set(dict["con_person"])
                self.len_date.set(dict["len_date"])
                self.con_phone.set(dict["con_phone"])
                self.back_date.set(dict["ds_back_date"])
                txt_pc_no.config(state="disable")  # 不可编辑
                btn_save.config(state="normal")  # 不可编辑
                self.ex_back_date.set(str(datetime.datetime.now().strftime("%Y%m%d")))
            else:
                messagebox.showinfo("", "沒有此設備編號")


        def save():
            flag=self.checknull()
            if flag:
                self.upddate.set(str(datetime.datetime.now().strftime("%Y%m%d%H%M%S")))
                Borrowsql.BorrowSql().comfirm_borrow(self)

        frm1 = tk.Frame(self)

        btn_reset = tk.Button(frm1, text="重置",command=reset)
        btn_reset.pack(side=tk.LEFT, padx=10)

        btn_search = tk.Button(frm1, text="查询",command=search)
        btn_search.pack(side=tk.LEFT, padx=10)


        btn_save = tk.Button(frm1, text="保存",command=save)
        btn_save.config(state="disable")  # 不可编辑
        btn_save.pack(side=tk.LEFT, padx=10)


        frm2 = tk.Frame(self)
        tk.Label(frm2,text="設備編號").grid(row=0,column=0,sticky=tk.W)
        tk.Label(frm2, text="設備名稱").grid(row=1, column=0, sticky=tk.W)
        tk.Label(frm2, text="過保日期").grid(row=2, column=0, sticky=tk.W)
        tk.Label(frm2, text="地點").grid(row=3, column=0, sticky=tk.W)

        tk.Label(frm2, text="臨時編號").grid(row=0, column=2, sticky=tk.W)
        tk.Label(frm2, text="規格").grid(row=1, column=2, sticky=tk.W)
        tk.Label(frm2, text="保管主管").grid(row=3, column=2, sticky=tk.W)

        def searchpc(event):
            dict=Borrowsql.BorrowSql().search_borrow(self.pc_no.get().strip())
            if (len(dict) > 0):
                self.pc_nm.set(dict["pc_name"])
                self.gb_date.set(dict["guobao_date"])
                self.address.set(dict["address"])
                self.tem_noYN.set(dict["temp_noYN"])
                self.spec.set(dict["p_spec"])
                self.master_emp.set(dict["master_empno"] )

                self.con_person.set(dict["con_person"])
                self.len_date.set(dict["len_date"])
                self.con_phone.set(dict["con_phone"])
                self.back_date.set(dict["ds_back_date"])
                txt_pc_no.config(state="disable")  # 不可编辑
                btn_save.config(state="normal")  # 不可编辑
                self.ex_back_date.set(str(datetime.datetime.now().strftime("%Y%m%d")))
            else:
                messagebox.showinfo("", "沒有此設備編號")
        txt_pc_no=tk.Entry(frm2,textvariable=self.pc_no)
        #txt_pc_no.config(state="disable")  # 不可编辑
        txt_pc_no.grid(row=0,column=1)
        txt_pc_no.bind("<Return>",searchpc)


        txt_pc_nm = tk.Entry(frm2,textvariable=self.pc_nm)
        txt_pc_nm.config(state="disable")  # 不可编辑
        txt_pc_nm.grid(row=1, column=1)


        txt_gb_date = tk.Entry(frm2,textvariable=self.gb_date)
        txt_gb_date.config(state="disable")  # 不可编辑
        txt_gb_date.grid(row=2, column=1)

        txt_address = tk.Entry(frm2,textvariable=self.address)
        txt_address.config(state="disable")  # 不可编辑
        txt_address.grid(row=3, column=1)


        ckb_ls = tk.Checkbutton(frm2,onvalue="T", offvalue="F", variable=self.tem_noYN)
        ckb_ls.config(state="disable")  # 不可编辑
        ckb_ls.grid(row=0, column=3)

        txt_spec = tk.Entry(frm2,textvariable=self.spec)
        txt_spec.config(state="disable")  # 不可编辑
        txt_spec.grid(row=1, column=3)

        txt_master_emp = tk.Entry(frm2,textvariable=self.master_emp)
        txt_master_emp.config(state="disable")  # 不可编辑
        txt_master_emp.grid(row=3, column=3)

        frm3 = tk.Frame(self)

        tk.Label(frm3,text="聯絡人").grid(row=0,column=0,sticky=tk.W)
        tk.Label(frm3, text="借出日期").grid(row=1, column=0, sticky=tk.W)

        tk.Label(frm3, text="實際歸還日期").grid(row=2, column=0, sticky=tk.W,pady=10)

        tk.Label(frm3, text="聯絡電話").grid(row=0, column=2, sticky=tk.W)
        tk.Label(frm3, text="計劃歸還日期").grid(row=1, column=2, sticky=tk.W)

        txt_con_emp = tk.Entry(frm3,textvariable=self.con_person)
        txt_con_emp.config(state="disable")  # 不可编辑
        txt_con_emp.grid(row=0, column=1,sticky=tk.W)

        txt_len_date = tk.Entry(frm3,textvariable=self.len_date)
        txt_len_date.config(state="disable")  # 不可编辑
        txt_len_date.grid(row=1, column=1,sticky=tk.W)

        txt_ex_back_date = tk.Entry(frm3, textvariable=self.ex_back_date)
        txt_ex_back_date.grid(row=2, column=1, sticky=tk.W,pady=10)

        txt_con_phone = tk.Entry(frm3,textvariable=self.con_phone)
        txt_con_phone.config(state="disable")  # 不可编辑
        txt_con_phone.grid(row=0, column=3,sticky=tk.W)

        txt_back_date = tk.Entry(frm3,textvariable=self.back_date)
        txt_back_date.config(state="disable")  # 不可编辑
        txt_back_date.grid(row=1, column=3,sticky=tk.W)


        # tk.Label(frm3, text="料編").grid(row=0, column=1, sticky=tk.W)
        # tk.Label(frm3, text="名稱").grid(row=0, column=2, sticky=tk.W)
        # tk.Label(frm3, text="規格").grid(row=0, column=3, sticky=tk.W)
        # tk.Label(frm3, text="數量").grid(row=0, column=4, sticky=tk.W)
        #
        # tk.Label(frm3, text="主板/型號").grid(row=1, column=0, sticky=tk.W)
        # tk.Label(frm3, text="CPU").grid(row=2, column=0, sticky=tk.W)
        # tk.Label(frm3, text="內存").grid(row=3, column=0, sticky=tk.W)
        # tk.Label(frm3, text="硬盤").grid(row=4, column=0, sticky=tk.W)
        #
        #
        # tk.Entry(frm3, text="主板/型號",width=12).grid(row=1, column=1, sticky=tk.W)
        # tk.Entry(frm3, text="CPU",width=12).grid(row=1, column=2, sticky=tk.W)
        # tk.Entry(frm3, text="內存",width=12).grid(row=1, column=3, sticky=tk.W)
        # tk.Entry(frm3, text="硬盤",width=12).grid(row=1, column=4, sticky=tk.W)
        #
        # tk.Entry(frm3, text="主板/型號", width=12).grid(row=2, column=1, sticky=tk.W)
        # tk.Entry(frm3, text="CPU", width=12).grid(row=2, column=2, sticky=tk.W)
        # tk.Entry(frm3, text="內存", width=12).grid(row=2, column=3, sticky=tk.W)
        # tk.Entry(frm3, text="硬盤", width=12).grid(row=2, column=4, sticky=tk.W)
        #
        # tk.Entry(frm3, text="主板/型號", width=12).grid(row=3, column=1, sticky=tk.W)
        # tk.Entry(frm3, text="CPU", width=12).grid(row=3, column=2, sticky=tk.W)
        # tk.Entry(frm3, text="內存", width=12).grid(row=3, column=3, sticky=tk.W)
        # tk.Entry(frm3, text="硬盤", width=12).grid(row=3, column=4, sticky=tk.W)
        #
        # tk.Entry(frm3, text="主板/型號", width=12).grid(row=4, column=1, sticky=tk.W)
        # tk.Entry(frm3, text="CPU", width=12).grid(row=4, column=2, sticky=tk.W)
        # tk.Entry(frm3, text="內存", width=12).grid(row=4, column=3, sticky=tk.W)
        # tk.Entry(frm3, text="硬盤", width=12).grid(row=4, column=4, sticky=tk.W)

        frm1.pack(side=tk.TOP)
        frm2.pack(side=tk.TOP)
        frm3.pack(side=tk.TOP,pady=10)