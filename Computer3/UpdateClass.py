import  tkinter as  tk
import  tkinter.ttk as ttk
import  SqlDB as sql
import  datetime
from  dateutil.relativedelta import  relativedelta
import  tkinter.messagebox as messagebox
import  User
import  UpdateClassSqlDB as UpdateSql

class Update(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.yongtu=[]
        self.guishu=[]


        #初始化綁定變量
        self.pc_no=tk.StringVar()
        self.pc_nm=tk.StringVar()
        self.pf_date=tk.StringVar()
        self.spec=tk.StringVar()
        self.gb_date=tk.StringVar()

        #修改前變量
        self.yt_before=tk.StringVar()
        self.gs_before=tk.StringVar()
        self.add_before=tk.StringVar()
        self.master_emp_before=tk.StringVar()
        self.master_dpt_before=tk.StringVar()


        #修改後變量
        self.yt_after = tk.StringVar()
        self.gs_after = tk.StringVar()
        self.add_after = tk.StringVar()
        self.master_emp_after = tk.StringVar()
        self.master_dpt_after = tk.StringVar()

        self.upddate = tk.StringVar()
        #self.upddate.set(str(datetime.datetime.now().strftime("%Y%m%d%H%M%S")))

        self.pc_no_after=tk.StringVar()#更改后编号


        self.initPage()
        self.createPage()



    def initPage(self):

        dict = sql.CONDB().getyongtu()
        for item in dict:
            self.yongtu.append(str(item["type_seq"]) + "-" + str(item["type_info_name"]))

        dict = sql.CONDB().getguishu()
        for item in dict:
            self.guishu.append(str(item["type_seq"]) + "-" + str(item["type_info_name"]))


    def checknull(self):
            if not self.yt_after.get():
                messagebox.showinfo("","用途不允许为空")
            if not self.gs_after.get():
                messagebox.showinfo("", "归属不允许为空")
            if not self.add_after.get():
                messagebox.showinfo("", "地址不允许为空")
            if not self.master_emp_after.get():
                messagebox.showinfo("", "保管主管不允许为空")
            if not self.master_dpt_after.get():
                messagebox.showinfo("", "保管部门不允许为空")
            dict = sql.CONDB().getEmpInfo(self.master_emp_after.get()[0:5])
            if (len(dict) <= 0):
                messagebox.showinfo("", "保管主管职号不正确")
                return False
            return True


    def createPage(self):


        def search():
            dict=UpdateSql.UpdateSql().search(self.pc_no.get().strip())
            if(len(dict)>0):
                self.pc_nm.set(dict["pc_name"])
                self.pf_date.set( dict["peifa_date"])
                self.spec.set(dict["p_spec"])
                self.gb_date.set( dict["guobao_date"])
                self.yt_before.set( dict["use_type"])
                self.gs_before.set(dict["own_type"])
                self.add_before.set(dict["address"])
                self.master_emp_before.set(dict["master_empno"])
                self.master_dpt_before.set(dict["master_deptno"])

                self.yt_after.set(dict["use_type"])
                self.gs_after.set(dict["own_type"])
                self.add_after.set(dict["address"])
                self.master_emp_after.set(dict["master_empno"])
                self.master_dpt_after.set(dict["master_deptno"])


                tk.Label(frm1,text="修改為").grid(row=1,column=3)

                tk.Entry(frm1,textvariable=self.pc_no_after).grid(row=1, column=4)
                self.pc_no_after.set(self.pc_no.get())

                btn_save.config(state="normal")
                txt_machine_no.config(state="disable")


            else:
                messagebox.showinfo("","沒有此設備編號")


        def reset():
            # 初始化綁定變量
            self.pc_no.set("")
            self.pc_nm.set("")
            self.pf_date.set("")
            self.spec.set("")
            self.gb_date.set("")
            # 修改前變量
            self.yt_before.set("")
            self.gs_before.set("")
            self.add_before.set("")
            self.master_emp_before.set("")
            self.master_dpt_before.set("")
            # 修改後變量
            self.yt_after.set("")
            self.gs_after.set("")
            self.add_after.set("")
            self.master_emp_after.set("")
            self.master_dpt_after.set("")
            self.upddate.set("")
            self.pc_no_after.set("")
            txt_machine_no.config(state="normal")



        frm1 = tk.Frame(self)

        frm3 = tk.Frame(self)


        btn_reset=tk.Button(frm3,text="重置",command=reset)
        btn_reset.grid(row=0,column=0,padx=15)



        btn_search=tk.Button(frm3,text="查詢",command=search)
        btn_search.grid(row=0,column=2,padx=15)


        def save():

            self.upddate.set(str(datetime.datetime.now().strftime("%Y%m%d%H%M%S")))
            dict = UpdateSql.UpdateSql().updat(self)
            reset()


        btn_save = tk.Button(frm3, text="保存",command=save)
        btn_save.config(state="disable")
        btn_save.grid(row=0, column=4,padx=15)







        tk.Label(frm1,text="設備編號").grid(row=1,column=0)
        tk.Label(frm1, text="設備名稱").grid(row=2, column=0)
        tk.Label(frm1, text="配發日期").grid(row=3, column=0)

        def searchpc(event):
            dict = UpdateSql.UpdateSql().search(self.pc_no.get().strip())
            if (len(dict) > 0):
                self.pc_nm.set(dict["pc_name"])
                self.pf_date.set(dict["peifa_date"])
                self.spec.set(dict["p_spec"])
                self.gb_date.set(dict["guobao_date"])
                self.yt_before.set(dict["use_type"])
                self.gs_before.set(dict["own_type"])
                self.add_before.set(dict["address"])
                self.master_emp_before.set(dict["master_empno"])
                self.master_dpt_before.set(dict["master_deptno"])

                self.yt_after.set(dict["use_type"])
                self.gs_after.set(dict["own_type"])
                self.add_after.set(dict["address"])
                self.master_emp_after.set(dict["master_empno"])
                self.master_dpt_after.set(dict["master_deptno"])

                tk.Label(frm1, text="修改為").grid(row=1, column=3)

                tk.Entry(frm1, textvariable=self.pc_no_after).grid(row=1, column=4)
                self.pc_no_after.set(self.pc_no.get())

                btn_save.config(state="normal")
                txt_machine_no.config(state="disable")


            else:
                messagebox.showinfo("", "沒有此設備編號")


        txt_machine_no=tk.Entry(frm1,textvariable=self.pc_no)
        txt_machine_no.grid(row=1,column=1)
        txt_machine_no.bind("<Return>", searchpc)


        txt_machine_nm = tk.Entry(frm1,textvariable=self.pc_nm)
        txt_machine_nm.config(state="disable")  # 不可编辑
        txt_machine_nm.grid(row=2, column=1)

        txt_pf_date = tk.Entry(frm1,textvariable=self.pf_date)
        txt_pf_date.config(state="disable")  # 不可编辑
        txt_pf_date.grid(row=3, column=1)







        tk.Label(frm1, text="規格").grid(row=2, column=3)
        tk.Label(frm1, text="過保日期").grid(row=3, column=3)






        txt_spec = tk.Entry(frm1,textvariable=self.spec)
        txt_spec.config(state="disable")#不可编辑
        txt_spec.grid(row=2, column=4)
        txt_gb_date = tk.Entry(frm1,textvariable=self.gb_date)
        txt_gb_date.config(state="disable")#不可编辑
        txt_gb_date.grid(row=3, column=4)



        frm2=tk.Frame(self)
        tk.Label(frm2, text="修改前").grid(row=4, column=0)
        tk.Label(frm2, text="修改後").grid(row=4, column=2)
        tk.Label(frm2, text="用途").grid(row=5, column=0,sticky=tk.W)
        tk.Label(frm2, text="歸屬分類").grid(row=6, column=0,sticky=tk.W)
        tk.Label(frm2, text="地點").grid(row=7, column=0,sticky=tk.W)
        tk.Label(frm2, text="保管主管").grid(row=8, column=0,sticky=tk.W)
        tk.Label(frm2, text="單位代號").grid(row=9, column=0,sticky=tk.W)



        cmb_yt_before= ttk.Combobox(frm2,values=self.yongtu,textvariable=self.yt_before,      width=18)
        cmb_yt_before.config(state="disable")
        cmb_yt_before.grid(row=5, column=1)

        cmb_gs_before=ttk.Combobox(frm2,values=self.guishu, textvariable=self.gs_before,     width=18)
        cmb_gs_before.config(state="disable")
        cmb_gs_before.grid(row=6, column=1)


        ttk.Combobox(frm2, values=self.yongtu,textvariable=self.yt_after,      width=18).grid(row=5, column=2)
        ttk.Combobox(frm2, values=self.guishu,textvariable=self.gs_after,       width=18).grid(row=6, column=2)



        txt_add_before=tk.Entry(frm2,textvariable=self.add_before)
        txt_add_before.config(state="disable")
        txt_add_before.grid(row=7, column=1)

        txt_emp_before=tk.Entry(frm2,textvariable=self.master_emp_before)
        txt_emp_before.config(state="disable")
        txt_emp_before.grid(row=8, column=1)



        txt_dpt_before=tk.Entry(frm2,textvariable=self.master_dpt_before)
        txt_dpt_before.config(state="disable")
        txt_dpt_before.grid(row=9, column=1)

        def masterinfo(event):
            dict = sql.CONDB().getEmpInfo(self.master_emp_after.get())
            if (len(dict) > 0):
                self.master_emp_after.set(dict["emp"])
                self.master_dpt_after.set(dict["dept"])
            else:
                messagebox.showinfo("","沒有改職號或已經離職")


        tk.Entry(frm2,textvariable=self.add_after).grid(row=7, column=2)

        txt_emp_afetr=tk.Entry(frm2,textvariable=self.master_emp_after)
        txt_emp_afetr.bind("<Return>",masterinfo)
        txt_emp_afetr.grid(row=8, column=2)




        tk.Entry(frm2,textvariable=self.master_dpt_after).grid(row=9, column=2)

        frm3.pack(side=tk.TOP)
        frm1.pack(side=tk.TOP)
        frm2.pack(side=tk.TOP)
