import  tkinter as  tk
import  tkinter.ttk as ttk
import  InWeiXiuClassSqlDB as sql
import  datetime
from  dateutil.relativedelta import  relativedelta
import  tkinter.messagebox as messagebox
import  User
import  SqlDB as  sqlbase

class InRepairTZ(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.root = master  # 定义内部变量root

        self.pc_no = tk.StringVar()  #
        self.pc_nm = tk.StringVar()  #
        self.spec = tk.StringVar()  # 規格


        
        self.zhuban_part_no = tk.StringVar()  # 主板编号
        self.zhuban_nm = tk.StringVar()  # 主板名称
        self.zhuban_spec = tk.StringVar()  # 主板规格
        self.zhuban_qty = tk.StringVar()  # 主板数量

        self.cpu_part_no = tk.StringVar()  # cpu编号
        self.cpu_nm = tk.StringVar()  # cpu名称
        self.cpu_spec = tk.StringVar()  # cpu规格
        self.cpu_qty = tk.StringVar()  # cpu数量

        self.yingpan_part_no = tk.StringVar()  # 硬盘编号
        self.yingpan_nm = tk.StringVar()  # 硬盘名称
        self.yingpan_spec = tk.StringVar()  # 硬盘规格
        self.yingpan_qty = tk.StringVar()  # 硬盘数量

        self.neicun_part_no = tk.StringVar()  # 内存编号
        self.neicun_nm = tk.StringVar()  # 内存名称
        self.neicun_spec = tk.StringVar()  # 内存规格
        self.neicun_qty = tk.StringVar()  # 内存数量



        self.con_person=tk.StringVar()
        self.con_phone = tk.StringVar()
        self.sx_date = tk.StringVar()
        self.question = tk.StringVar()



        self.upddate=tk.StringVar()

        self.createPage()


    # 檢查日期格式是否正確
    def checkdate(self,date_time):
        try:
            datetime.datetime.strptime(date_time, '%Y%m%d')
            return True
        except:
            return False

    def checknull(self):
        if not self.pc_no.get():
            messagebox.showinfo("", "設備編號不允許為空")
            return False

        if not self.con_person.get():
            messagebox.showinfo("", "聯絡人不允許為空")
            return False
        if not self.con_phone.get():
            messagebox.showinfo("", "聯絡電話不允許為空")
            return False
        if not self.sx_date.get():
            messagebox.showinfo("", "送修日期不允許為空")
            return False
        if not self.checkdate(self.sx_date.get()):
            messagebox.showinfo("", "送修日期應為八位有效數字")
            return False
        return True






    def createPage(self):
        
        def reset():
            self.pc_no.set("")
            self.pc_nm.set("")
            self.spec.set("")
            self.zhuban_part_no.set("") # 主板编号
            self.zhuban_nm.set("")  # 主板名称
            self.zhuban_spec.set("") # 主板规格
            self.zhuban_qty.set("")  # 主板数量
            self.cpu_part_no.set("")# cpu编号
            self.cpu_nm.set("")# cpu名称
            self.cpu_spec.set("")# cpu规格
            self.cpu_qty.set("")# cpu数量
            self.yingpan_part_no.set("") # 硬盘编号
            self.yingpan_nm.set("") # 硬盘名称
            self.yingpan_spec.set("")  # 硬盘规格
            self.yingpan_qty.set("") # 硬盘数量
            self.neicun_part_no.set("")  # 内存编号
            self.neicun_nm.set("") # 内存名称
            self.neicun_spec.set("")  # 内存规格
            self.neicun_qty.set("") # 内存数量
            self.con_person.set("")
            self.con_phone.set("")
            self.sx_date.set("")
            txt_question.delete("1.0", tk.END)
            txt_pc_no.config(state="normal")


        def search():
            flag=sql.INWeiXiuSql().search(self.pc_no.get().strip(),self)
            if flag:
                btn_save.config(state="normal")
                self.sx_date.set(str(datetime.datetime.now().strftime("%Y%m%d")))
                txt_pc_no.config(state="disable")
            else:
                btn_save.config(state="disable")
            sql.INWeiXiuSql().search_eqm_zhuban(self)
            sql.INWeiXiuSql().search_eqm_cpu(self)
            sql.INWeiXiuSql().search_eqm_neicun(self)
            sql.INWeiXiuSql().search_eqm_yingpan(self)



        def save():
            flag=self.checknull()
            if flag:
                self.upddate.set(str(datetime.datetime.now().strftime("%Y%m%d%H%M%S")))
                self.question.set(txt_question.get('1.0', tk.END))
                sql.INWeiXiuSql().insertINReapir(self)




        frm1 = tk.Frame(self)
        btn_reset = tk.Button(frm1, text="重置",command=reset)
        btn_reset.pack(side=tk.LEFT, padx=10)

        btn_search = tk.Button(frm1, text="查询",command=search)
        btn_search.pack(side=tk.LEFT, padx=10)

        btn_save = tk.Button(frm1, text="保存",command=save)
        btn_save.config(state="disable")  # 不可编辑
        btn_save.pack(side=tk.LEFT, padx=10)

        def searchpc(event):
            flag=sql.INWeiXiuSql().search(self.pc_no.get().strip(),self)
            if flag:
                btn_save.config(state="normal")
                self.sx_date.set(str(datetime.datetime.now().strftime("%Y%m%d")))
                txt_pc_no.config(state="disable")
            else:
                btn_save.config(state="disable")
            sql.INWeiXiuSql().search_eqm_zhuban(self)
            sql.INWeiXiuSql().search_eqm_cpu(self)
            sql.INWeiXiuSql().search_eqm_neicun(self)
            sql.INWeiXiuSql().search_eqm_yingpan(self)




        frm2 = tk.Frame(self)
        tk.Label(frm2,text="设备编号").grid(row=0,column=0)
        txt_pc_no=tk.Entry(frm2,textvariable=self.pc_no)
        txt_pc_no.grid(row=0,column=1)
        txt_pc_no.bind("<Return>", searchpc)

        
        
        tk.Label(frm2, text="设备名称").grid(row=0, column=2)
        txt_pc_nm=tk.Entry(frm2,textvariable=self.pc_nm)
        txt_pc_nm.grid(row=0,column=3)
        txt_pc_nm.config(state="disable")  # 不可编辑






        frm3 = tk.Frame(self)
        lbl_zhuban = tk.Label(frm3, text="主板/型號")
        lbl_zhuban.grid(row=1, column=1)
        lbl_zhuban = tk.Label(frm3, text="CPU")
        lbl_zhuban.grid(row=2, column=1)
        lbl_neicun = tk.Label(frm3, text="內存")
        lbl_neicun.grid(row=3, column=1)
        lbl_yingpan = tk.Label(frm3, text="硬盤")
        lbl_yingpan.grid(row=4, column=1)
        tk.Label(frm3, text="料編").grid(row=0, column=2, padx=15)
        tk.Label(frm3, text="名稱").grid(row=0, column=3, padx=15)
        tk.Label(frm3, text="規格").grid(row=0, column=4, padx=15)
        tk.Label(frm3, text="數量").grid(row=0, column=5, padx=15)

        # 主板
        txt_zhubanpartno = tk.Entry(frm3, width=10, textvariable=self.zhuban_part_no)
        txt_zhubanpartno.config(state="disable")
        txt_zhubanpartno.grid(row=1, column=2)
        # txt_zhubanpartno.bind('<Return>', zhubaninfo)
        # txt_zhubanpartno.bind('<FocusOut>', zhubaninfo)

        txt_zhubanpartnm = tk.Entry(frm3, width=25, textvariable=self.zhuban_nm)
        txt_zhubanpartnm.grid(row=1, column=3)
        txt_zhubanpartnm.config(state="disable")

        txt_zhubanguige = tk.Entry(frm3, width=25, textvariable=self.zhuban_spec)
        txt_zhubanguige.grid(row=1, column=4)
        txt_zhubanguige.config(state="disable")

        txt_zhubanqty = tk.Entry(frm3, width=2, textvariable=self.zhuban_qty)
        txt_zhubanqty.grid(row=1, column=5)
        txt_zhubanqty.config(state="disable")

        # CPU
        txt_cpunpartno = tk.Entry(frm3, width=10, textvariable=self.cpu_part_no)
        txt_cpunpartno.grid(row=2, column=2)
        txt_cpunpartno.config(state="disable")
        # txt_cpunpartno.bind('<Return>', cpuinfo)
        # txt_cpunpartno.bind('<FocusOut>', cpuinfo)

        txt_cpubanpartnm = tk.Entry(frm3, width=25, textvariable=self.cpu_nm)
        txt_cpubanpartnm.grid(row=2, column=3)
        txt_cpubanpartnm.config(state="disable")

        txt_cpuguige = tk.Entry(frm3, width=25, textvariable=self.cpu_spec)
        txt_cpuguige.grid(row=2, column=4)
        txt_cpuguige.config(state="disable")

        txt_cpuqty = tk.Entry(frm3, width=2, textvariable=self.cpu_qty)
        txt_cpuqty.grid(row=2, column=5)
        txt_cpuqty.config(state="disable")

        # 內存
        txt_neicunnpartno = tk.Entry(frm3, width=10, textvariable=self.neicun_part_no)
        txt_neicunnpartno.grid(row=3, column=2)
        txt_neicunnpartno.config(state="disable")
        # txt_neicunnpartno.bind('<Return>', neicuninfo)
        # txt_neicunnpartno.bind('<FocusOut>', neicuninfo)

        txt_neicunbanpartnm = tk.Entry(frm3, width=25, textvariable=self.neicun_nm)
        txt_neicunbanpartnm.grid(row=3, column=3)
        txt_neicunbanpartnm.config(state="disable")

        txt_neicunguige = tk.Entry(frm3, width=25, textvariable=self.neicun_spec)
        txt_neicunguige.grid(row=3, column=4)
        txt_neicunguige.config(state="disable")

        txt_neicunqty = tk.Entry(frm3, width=2, textvariable=self.neicun_qty)
        txt_neicunqty.grid(row=3, column=5)
        txt_neicunqty.config(state="disable")

        # 硬盤
        txt_yingpannpartno = tk.Entry(frm3, width=10, textvariable=self.yingpan_part_no)
        txt_yingpannpartno.grid(row=4, column=2)
        txt_yingpannpartno.config(state="disable")
        # txt_yingpannpartno.bind('<Return>', yingpaninfo)
        # txt_yingpannpartno.bind('<FocusOut>', yingpaninfo)

        txt_yingpanbanpartnm = tk.Entry(frm3, width=25, textvariable=self.yingpan_nm)
        txt_yingpanbanpartnm.grid(row=4, column=3)
        txt_yingpanbanpartnm.config(state="disable")

        txt_yingpanguige = tk.Entry(frm3, width=25, textvariable=self.yingpan_spec)
        txt_yingpanguige.grid(row=4, column=4)
        txt_yingpanguige.config(state="disable")

        txt_yingpanqty = tk.Entry(frm3, width=2, textvariable=self.yingpan_qty)
        txt_yingpanqty.grid(row=4, column=5)
        txt_yingpanqty.config(state="disable")




        def masterinfo(event):
            dict=sql.CONDB().getEmpInfo(self.con_person.get()[0:5])
            if(len(dict)>0):
                self.con_person.set(dict["emp"])
            else:
                if self.con_person.get():
                    messagebox.showinfo("", "沒有改職號或已經離職")
                    self.con_person.set("")

        frm4=tk.Frame(self)
        tk.Label(frm4,text="聯絡人").grid(row=0,column=0)

        txt_con_person=tk.Entry(frm4,textvariable=self.con_person)
        txt_con_person.grid(row=0, column=1)
        txt_con_person.bind('<Return>', masterinfo)
        txt_con_person.bind('<FocusOut>', masterinfo)




        tk.Label(frm4, text="電話").grid(row=0, column=2)
        tk.Entry(frm4,textvariable=self.con_phone).grid(row=0,column=3)



        tk.Label(frm4, text="送修日期").grid(row=1, column=0)
        tk.Entry(frm4,textvariable=self.sx_date).grid(row=1,column=1)
        #
        tk.Label(frm4, text="故障問題").grid(row=2, column=0)

        txt_question=tk.Text(frm4,width=45,height=3)
        txt_question.grid(row=2,column=1,columnspan=3)


        
        frm1.pack(side=tk.TOP)
        frm2.pack(side=tk.TOP)
        frm3.pack(side=tk.TOP)
        frm4.pack(side=tk.TOP,pady=20)
        
        
        
        
        
        
        
        
        # frm2.pack(side=tk.TOP)
        # frm3.pack(side=tk.TOP, pady=10)
        # 
        