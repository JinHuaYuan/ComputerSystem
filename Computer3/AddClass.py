import  tkinter as  tk
import  tkinter.ttk as ttk
import  SqlDB as sql
import  datetime
from  dateutil.relativedelta import  relativedelta
import  tkinter.messagebox as messagebox
import  User

class Add(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        # self.password = tk.StringVar()
        # self.password.set("T")
        # self.aa=tk.StringVar()

        self.pnodf1=[]
        self.pnodf2=[]
        self.yongtu=[]
        self.guishu=[]


        #初始化页面属性
        self.machine_no=tk.StringVar()#设备编号
        self.machine_name=tk.StringVar()#設備名稱
        self.address=tk.StringVar()#地點


        self.warranty_date=tk.StringVar()#过保日期
        self.pf_date=tk.StringVar()#配發日期

        self.tem_noYN = tk.StringVar()# 臨時編號
        self.tem_noYN.set("F")

        self.p_spec=tk.StringVar()#規格
        self.pr_no = tk.StringVar()  # 請購單號

        self.master_emp=tk.StringVar()#保存主管
        self.master_dept=tk.StringVar()#保存主管部門

        self.yongtutxt=tk.StringVar()#用途
        self.guishutxt=tk.StringVar()#歸屬
        self.bz = tk.StringVar()  # 備註

        self.p_btype = tk.StringVar()  # 大分类
        self.p_mtype = tk.StringVar()  # 中分类



        self.zhuban_part_no=tk.StringVar()#主板编号
        self.zhuban_nm = tk.StringVar()  # 主板名称
        self.zhuban_spec= tk.StringVar()  # 主板规格
        self.zhuban_qty = tk.StringVar()  # 主板数量


        self.cpu_part_no=tk.StringVar()#cpu编号
        self.cpu_nm = tk.StringVar()  # cpu名称
        self.cpu_spec = tk.StringVar()  # cpu规格
        self.cpu_qty = tk.StringVar()  # cpu数量


        self.yingpan_part_no=tk.StringVar()#硬盘编号
        self.yingpan_nm = tk.StringVar()  # 硬盘名称
        self.yingpan_spec = tk.StringVar()  # 硬盘规格
        self.yingpan_qty = tk.StringVar()  # 硬盘数量


        self.neicun_part_no=tk.StringVar()#内存编号
        self.neicun_nm = tk.StringVar()  # 内存名称
        self.neicun_spec = tk.StringVar()  # 内存规格
        self.neicun_qty = tk.StringVar()  # 内存数量

        self.upddate=tk.StringVar()#更新時間




        self.initpnodf1()
        #self.initpnodf2()
        self.createPage()

    #初始化
    def reset(self):
        # 初始化页面属性
        self.machine_no.set("")
        self.machine_name.set("")
        self.address.set("")

        self.warranty_date.set("")
        self.pf_date.set("")

        self.tem_noYN.set("F")

        self.p_spec.set("")
        self.pr_no.set("")

        self.master_emp.set("")
        self.master_dept.set("")

        self.yongtutxt.set("")
        self.guishutxt.set("")
        self.bz.set("")

        self.p_btype.set("")
        self.p_mtype.set("")

        self.zhuban_part_no.set("")
        self.zhuban_nm.set("")
        self.zhuban_spec.set("")
        self.zhuban_qty.set("")

        self.cpu_part_no.set("")
        self.cpu_nm.set("")
        self.cpu_spec.set("")
        self.cpu_qty.set("")

        self.yingpan_part_no.set("")
        self.yingpan_nm.set("")
        self.yingpan_spec.set("")
        self.yingpan_qty.set("")

        self.neicun_part_no.set("")
        self.neicun_nm.set("")
        self.neicun_spec.set("")
        self.neicun_qty.set("")

        self.upddate.set("")




    #格式化时间格式
    def gs_date(self,date):
        new_date=""
        date_arr=date.split('-')
        for item in date_arr:
            new_date+=str(item)
        return  new_date


    def checknull(self):
        if not self.p_btype.get():
            messagebox.showinfo("","請輸入大分類")
            return False
        elif not self.p_mtype.get():
            messagebox.showinfo("","請輸入中分類")
            return False
        elif not self.machine_no.get():
            messagebox.showinfo("","請輸入設備編號")
            return False
        elif not self.yongtutxt.get():
            messagebox.showinfo("", "請輸用途")
            return False
        elif not self.guishutxt.get():
            messagebox.showinfo("", "請輸入歸屬")
            return False
        elif not self.machine_name.get():
            messagebox.showinfo("", "請輸設備名稱")
            return False
        elif not self.address.get():
            messagebox.showinfo("", "請輸入地點")
            return False
        elif not self.master_emp.get():
            messagebox.showinfo("", "請輸入保管主管")
            return False
        elif not self.pf_date.get():
            messagebox.showinfo("", "請輸入配發日期")
            return False
        dict = sql.CONDB().getEmpInfo(self.master_emp.get()[0:5])
        if (len(dict)<=0):
            messagebox.showinfo("", "保管主管职号不正确")
            return False
        return True


    def reset(self):
        # 初始化页面属性
        # self.machine_no.set("")
        # self.machine_name.set("")  # 設備名稱
        # self.address.set("")  # 地點
        #
        # self.warranty_date.set("")  # 过保日期
        # self.pf_date.set("")  # 配發日期
        #
        # self.tem_noYN.set("F")
        #
        # self.p_spec.set("")  # 規格
        # self.pr_no.set("")  # 請購單號
        #
        # self.master_emp.set("")  # 保存主管
        # self.master_dept.set("")  # 保存主管部門
        #
        # self.yongtutxt.set("")  # 用途
        # self.guishutxt.set("")  # 歸屬
        # self.bz.set("")  # 備註
        #
        # self.p_btype.set("")  # 大分类
        # self.p_mtype.set("")  # 中分类

        self.zhuban_part_no.set("")  # 主板编号
        self.zhuban_nm.set("")  # 主板名称
        self.zhuban_spec.set("")  # 主板规格
        self.zhuban_qty.set("")  # 主板数量

        self.cpu_part_no.set("")  # cpu编号
        self.cpu_nm.set("")  # cpu名称
        self.cpu_spec.set("")  # cpu规格
        self.cpu_qty.set("")  # cpu数量

        self.yingpan_part_no.set("") # 硬盘编号
        self.yingpan_nm.set("") # 硬盘名称
        self.yingpan_spec.set("") # 硬盘规格
        self.yingpan_qty.set("")  # 硬盘数量

        self.neicun_part_no.set("") # 内存编号
        self.neicun_nm.set("")# 内存名称
        self.neicun_spec.set("")  # 内存规格
        self.neicun_qty.set("")  # 内存数量




    def initpnodf1(self):
        # dict1=sql.CONDB().getdbcon()
        # cur = dict1.cursor()
        # cur.execute("select * from ITeqm_pnodf1")
        # dict =cur.fetchall()


        dict=sql.CONDB().getpnodf1()
        for item in dict:
            self.pnodf1.append(str(item["p_btype"])+"-"+str(item["p_btype_nm"]))

        # dict = sql.CONDB().getpnodf2()
        # for item in dict:
        #     self.pnodf2.append(str(item["p_mtype"]) + "-" + str(item["p_mtype_nm"]))

        dict = sql.CONDB().getyongtu()
        for item in dict:
            self.yongtu.append(str(item["type_seq"]) + "-" + str(item["type_info_name"]))

        dict = sql.CONDB().getguishu()
        for item in dict:
            self.guishu.append(str(item["type_seq"]) + "-" + str(item["type_info_name"]))

    # def initpnodf2(self):
    #     # dict1=sql.CONDB().getdbcon()
    #     # cur = dict1.cursor()
    #     # cur.execute("select * from ITeqm_pnodf1")
    #     # dict =cur.fetchall()
    #
    #     dict=sql.CONDB().getpnodf2()
    #
    #     for item in dict:
    #         self.pnodf2.append(str(item["p_mtype"])+"-"+str(item["p_mtype_nm"]))

    def getpnoef2(self):
        dict = sql.CONDB().getpnodf2(self.p_btype.get()[0:2])
        if (len(dict) > 0):
            for item in dict:
                self.pnodf2.append(str(item["p_mtype"]) + "-" + str(item["p_mtype_nm"]))
                print(self.pnodf2)
        else:
            self.pnodf2.clear()


    def createPage(self):
        frm1 = tk.Frame(self)
        lbl_dafenlei = tk.Label(frm1, text="大分類")
        lbl_dafenlei.grid(row=1, column=1)


        txt_dafenlei = ttk.Combobox(frm1,values=self.pnodf1,textvariable=self.p_btype,width=18)
        txt_dafenlei.grid(row=1, column=2)


        def show(event):
            if(self.p_btype.get()[0:2]=='PC'):
               # frm4.grid(column=0, row=1, sticky=tk.N, padx=10, pady=20)
               frm4.pack(side=tk.TOP)
            else:
                frm4.pack_forget()
            self.getpnoef2()
            txt_zhongfenlei["value"]=self.pnodf2

        txt_dafenlei.bind("<<ComboboxSelected>>",show )


        lbl_zhongfenlei = tk.Label(frm1, text="中分類")
        lbl_zhongfenlei.grid(row=2, column=1)
        txt_zhongfenlei = ttk.Combobox(frm1,textvariable=self.p_mtype,width=18)
        txt_zhongfenlei.grid(row=2, column=2)
        #带出过保日期&配發日期
        def getguobaodate(event):
            date_year = sql.CONDB().getwarranty_date( str(self.p_btype.get())[0:2],str(self.p_mtype.get())[0:2]   )
            date=datetime.datetime.now()
            if date_year:
                date=date+relativedelta(years=date_year)#加上年份
                print(date.strftime("%F"))
                new_date=self.gs_date(date.strftime("%F"))
                self.warranty_date.set(new_date)
            else:
                self.warranty_date.set("")
            #配發日期
            pf_date = self.gs_date(datetime.datetime.now().strftime("%F"))
            self.pf_date.set(pf_date)



        txt_zhongfenlei.bind("<<ComboboxSelected>>", getguobaodate)



        #带出设备编号
        def show_machine_no(event):

            print(str(txt_machine_no.get()+event.char).upper())
            #self.pnodf2.append(11)
            #txt_zhongfenlei["value"]=self.pnodf2
            #self.pnodf2.append(11)

        lbl_machine_no = tk.Label(frm1, text="設備編號")
        lbl_machine_no.grid(row=3, column=1)
        txt_machine_no = tk.Entry(frm1,textvariable=self.machine_no)
        txt_machine_no.grid(row=3, column=2)
        txt_machine_no.bind("<Key>",show_machine_no)


        lbl_machine_nm = tk.Label(frm1, text="設備名稱")
        lbl_machine_nm.grid(row=4, column=1)
        txt_machine_nm = tk.Entry(frm1,textvariable=self.machine_name)
        txt_machine_nm.grid(row=4, column=2)

        lbl_machine_nm = tk.Label(frm1, text="過保日期")
        lbl_machine_nm.grid(row=5, column=1)
        txt_machine_nm = tk.Entry(frm1,textvariable=self.warranty_date)
        txt_machine_nm.grid(row=5, column=2)

        lbl_useway = tk.Label(frm1, text="用途")
        lbl_useway.grid(row=6, column=1)
        txt_useway = ttk.Combobox(frm1,values=self.yongtu,textvariable=self.yongtutxt,width=18)
        txt_useway.grid(row=6, column=2)

        lbl_address = tk.Label(frm1, text="地點")
        lbl_address.grid(row=7, column=1)
        txt_address = tk.Entry(frm1,textvariable=self.address)
        txt_address.grid(row=7, column=2)



        lbl_pefa_date = tk.Label(frm1, text="配發日期")
        lbl_pefa_date.grid(row=8, column=1)
        txt_pefa_date = tk.Entry(frm1,textvariable=self.pf_date)
        txt_pefa_date.grid(row=8, column=2)


        #備註
        lbl_bz = tk.Label(frm1, text="備註")
        lbl_bz.grid(row=9, column=1)
        txt_bz = tk.Text(frm1,width=50,height=2)
        txt_bz.grid(row=9, column=2,columnspan=3)
        ###

        #frm2 = tk.Frame(self)
        lbl_linshi_no = tk.Label(frm1, text="臨時編號")
        lbl_linshi_no.grid(row=1, column=3)
        chk_insi_no = tk.Checkbutton(frm1, onvalue="T", offvalue="F", variable=self.tem_noYN)
        chk_insi_no.grid(row=1, column=4, sticky=tk.W)



        lbl_psec = tk.Label(frm1, text="規格")
        lbl_psec.grid(row=2, column=3)
        txt_psec = tk.Entry(frm1,textvariable=self.p_spec)
        txt_psec.grid(row=2, column=4)



        lbl_pr_no = tk.Label(frm1, text="請購單號")
        lbl_pr_no.grid(row=3, column=3)
        txt_pr_no = tk.Entry(frm1,textvariable=self.pr_no)
        txt_pr_no.grid(row=3, column=4)


        lbl_gsfenlei = tk.Label(frm1, text="歸屬分類")
        lbl_gsfenlei.grid(row=4, column=3)
        txt_gsfenlei = ttk.Combobox(frm1,values=self.guishu,textvariable=self.guishutxt,width=18)
        txt_gsfenlei.grid(row=4, column=4)


        def masterinfo(event):
            dict=sql.CONDB().getEmpInfo(self.master_emp.get()[0:5])
            if(len(dict)>0):
                self.master_emp.set(dict["emp"])
                self.master_dept.set(dict["dept"])
            else:
                if self.master_emp.get():
                    messagebox.showinfo("", "沒有改職號或已經離職")

        lbl_bg_master = tk.Label(frm1, text="保管主管")
        lbl_bg_master.grid(row=5, column=3)

        txt_bg_master = tk.Entry(frm1,textvariable=self.master_emp)
        txt_bg_master.grid(row=5, column=4)
        txt_bg_master.bind('<Return>', masterinfo)
        txt_bg_master.bind('<FocusOut>', masterinfo)


        def create_machine_no():
            if not self.p_btype.get() or not self.p_mtype.get():
                messagebox.showinfo("waring","請先選擇大分類和中分類")

            else:
                self.machine_no.set(sql.CONDB().getMachine_no(self.p_btype.get()[0:2],self.p_mtype.get()[0:2]))

        btn_cs_machine_no = tk.Button(frm1, text="產生編號",command=create_machine_no)
        btn_cs_machine_no.grid(row=1, column=7)
       # btn_cs_machine_no.bind("<Button-1>",create_machine_no)


        def insert():
            flag=self.checknull()
            if flag:
                self.bz.set(txt_bz.get('1.0',tk.END))
                self.upddate.set(str(datetime.datetime.now().strftime("%Y%m%d%H%M%S")))
                sql.CONDB().insertPC(self)
                if(self.p_btype.get()[0:2]=='PC'):
                    sql.CONDB().insertPcEqm(self)
                self.reset()



        btn_save = tk.Button(frm1, text="保存", width=10,command=insert)
        btn_save.grid(row=3, column=7)

        btn_reset=tk.Button(frm1,text="清空",width=10,command=self.reset)
        btn_reset.grid(row=5, column=7)

        frm4 = tk.Frame(self)
        lbl_zhuban = tk.Label(frm4, text="主板/型號")
        lbl_zhuban.grid(row=1, column=1)
        lbl_zhuban = tk.Label(frm4, text="CPU")
        lbl_zhuban.grid(row=2, column=1)
        lbl_neicun = tk.Label(frm4, text="內存")
        lbl_neicun.grid(row=3, column=1)
        lbl_yingpan = tk.Label(frm4, text="硬盤")
        lbl_yingpan.grid(row=4, column=1)
        tk.Label(frm4, text="料編").grid(row=0, column=2, padx=15)
        tk.Label(frm4, text="名稱").grid(row=0, column=3, padx=15)
        tk.Label(frm4, text="規格").grid(row=0, column=4, padx=15)
        tk.Label(frm4, text="數量").grid(row=0, column=5, padx=15)
        # 主板

        def zhubaninfo(event):
            print(self.zhuban_part_no.get())
            print(txt_zhubanpartno.get())
            part_no=self.zhuban_part_no.get()
            type=part_no[0:4]
            dict=sql.CONDB().getEqm(part_no.strip(),'001')
            if(len(dict)>0):
                for item in dict:
                    self.zhuban_nm.set(item["p_stype_nm"])
                    self.zhuban_spec.set(item["pspec_basis"])
                    self.zhuban_qty.set("1")
            else:
                if  self.zhuban_part_no.get().strip():
                    messagebox.showwarning("no part_no","主板料編不存在")
                self.zhuban_nm.set("")
                self.zhuban_spec.set("")
                self.zhuban_qty.set("")



        txt_zhubanpartno = tk.Entry(frm4, width=10,textvariable=self.zhuban_part_no)
        txt_zhubanpartno.grid(row=1, column=2)
        txt_zhubanpartno.bind('<Return>',zhubaninfo)
        txt_zhubanpartno.bind('<FocusOut>', zhubaninfo)



        txt_zhubanpartnm = tk.Entry(frm4, width=25,textvariable=self.zhuban_nm)
        txt_zhubanpartnm.grid(row=1, column=3)
        txt_zhubanpartnm.config(state="disable")



        txt_zhubanguige = tk.Entry(frm4, width=25,textvariable=self.zhuban_spec)
        txt_zhubanguige.grid(row=1, column=4)
        txt_zhubanguige.config(state="disable")

        txt_zhubanqty = tk.Entry(frm4, width=2,textvariable=self.zhuban_qty)
        txt_zhubanqty.grid(row=1, column=5)


        # CPU
        def cpuinfo(event):
            part_no = self.cpu_part_no.get()
            type = part_no[0:4]
            dict = sql.CONDB().getEqm(part_no.strip(),'002')
            if (len(dict) > 0):
                for item in dict:
                    self.cpu_nm.set(item["p_stype_nm"])
                    self.cpu_spec.set(item["pspec_basis"])
                    self.cpu_qty.set("1")
            else:
                if self.cpu_part_no.get().strip():
                    messagebox.showwarning("no part_no", "CPU料編不存在")
                self.cpu_nm.set("")
                self.cpu_spec.set("")
                self.cpu_qty.set("")


        txt_cpunpartno = tk.Entry(frm4, width=10,textvariable=self.cpu_part_no)
        txt_cpunpartno.grid(row=2, column=2)
        txt_cpunpartno.bind('<Return>', cpuinfo)
        txt_cpunpartno.bind('<FocusOut>', cpuinfo)



        txt_cpubanpartnm = tk.Entry(frm4, width=25,textvariable=self.cpu_nm)
        txt_cpubanpartnm.grid(row=2, column=3)
        txt_cpubanpartnm.config(state="disable")

        txt_cpuguige = tk.Entry(frm4, width=25,textvariable=self.cpu_spec)
        txt_cpuguige.grid(row=2, column=4)
        txt_cpuguige.config(state="disable")

        txt_cpuqty = tk.Entry(frm4, width=2,textvariable=self.cpu_qty)
        txt_cpuqty.grid(row=2, column=5)






        # 內存
        def neicuninfo(event):
            part_no = self.neicun_part_no.get()
            type = part_no[0:4]
            dict = sql.CONDB().getEqm(part_no.strip(), '003')
            if (len(dict) > 0):
                for item in dict:
                    self.neicun_nm.set(item["p_stype_nm"])
                    self.neicun_spec.set(item["pspec_basis"])
                    self.neicun_qty.set("1")
            else:
                if self.neicun_part_no.get().strip():
                    messagebox.showwarning("no part_no", "内存料編不存在")
                self.neicun_nm.set("")
                self.neicun_spec.set("")
                self.neicun_qty.set("")


        txt_neicunnpartno = tk.Entry(frm4, width=10,textvariable=self.neicun_part_no)
        txt_neicunnpartno.grid(row=3, column=2)
        txt_neicunnpartno.bind('<Return>', neicuninfo)
        txt_neicunnpartno.bind('<FocusOut>', neicuninfo)

        txt_neicunbanpartnm = tk.Entry(frm4, width=25,textvariable=self.neicun_nm)
        txt_neicunbanpartnm.grid(row=3, column=3)
        txt_neicunbanpartnm.config(state="disable")


        txt_neicunguige = tk.Entry(frm4, width=25,textvariable=self.neicun_spec)
        txt_neicunguige.grid(row=3, column=4)
        txt_neicunguige.config(state="disable")

        txt_neicunqty = tk.Entry(frm4, width=2,textvariable=self.neicun_qty)
        txt_neicunqty.grid(row=3, column=5)
        # 硬盤
        def yingpaninfo(event):
            part_no = self.yingpan_part_no.get()
            type = part_no[0:4]
            dict = sql.CONDB().getEqm(part_no.strip(), '004')
            if (len(dict) > 0):
                for item in dict:
                    self.yingpan_nm.set(item["p_stype_nm"])
                    self.yingpan_spec.set(item["pspec_basis"])
                    self.yingpan_qty.set("1")
            else:
                if self.yingpan_part_no.get().strip():
                     messagebox.showwarning("no part_no", "硬盘料編不存在")
                self.yingpan_nm.set("")
                self.yingpan_spec.set("")
                self.yingpan_qty.set("")


        txt_yingpannpartno = tk.Entry(frm4, width=10,textvariable=self.yingpan_part_no)
        txt_yingpannpartno.grid(row=4, column=2)
        txt_yingpannpartno.bind('<Return>', yingpaninfo)
        txt_yingpannpartno.bind('<FocusOut>', yingpaninfo)

        txt_yingpanbanpartnm = tk.Entry(frm4, width=25,textvariable=self.yingpan_nm)
        txt_yingpanbanpartnm.grid(row=4, column=3)
        txt_yingpanbanpartnm.config(state="disable")

        txt_yingpanguige = tk.Entry(frm4, width=25,textvariable=self.yingpan_spec)
        txt_yingpanguige.grid(row=4, column=4)
        txt_yingpanguige.config(state="disable")

        txt_yingpanqty = tk.Entry(frm4, width=2,textvariable=self.yingpan_qty)
        txt_yingpanqty.grid(row=4, column=5)

        frm1.pack(side=tk.TOP)
        frm4.pack(side=tk.TOP)
