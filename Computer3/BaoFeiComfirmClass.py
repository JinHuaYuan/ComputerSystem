import  tkinter as  tk
import  WeiXiuClassSqlDB as sql
import  SqlDB as  sqlBase
import  tkinter.messagebox as messagebox
import  tkinter.ttk as  ttk
import  datetime



# 這個目前不使用
# ''''
# 這個目前不使用
#
# '''


#寫錯了，應該是維修。。。。。。。
class BaoFeiComfirm(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.root = master  # 定义内部变量root

        self.pc_no = tk.StringVar()
        self.pc_nm = tk.StringVar()
        self.pf_date = tk.StringVar()
        self.address = tk.StringVar()
        self.yt = tk.StringVar()
        self.spec = tk.StringVar()
        self.gb_date = tk.StringVar()
        self.master_emp = tk.StringVar()
        self.gs_type = tk.StringVar()
        self.bz = tk.StringVar()

        self.con_person = tk.StringVar()
        self.con_phone = tk.StringVar()
        self.sx_date = tk.StringVar()
        self.sx_cust = tk.StringVar()

        self.question = tk.StringVar()

        self.back_date=tk.StringVar()#回厂日期
        self.receive_date=tk.StringVar()
        self.ask=tk.StringVar()


        # 保存時賦值

        self.status = tk.StringVar()
        self.upddate = tk.StringVar()

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



##########################################修改后
        self.zhuban_part_no_after = tk.StringVar()  # 主板编号
        self.zhuban_nm_after = tk.StringVar()  # 主板名称
        self.zhuban_spec_after = tk.StringVar()  # 主板规格
        self.zhuban_qty_after = tk.StringVar()  # 主板数量

        self.cpu_part_no_after = tk.StringVar()  # cpu编号
        self.cpu_nm_after = tk.StringVar()  # cpu名称
        self.cpu_spec_after = tk.StringVar()  # cpu规格
        self.cpu_qty_after = tk.StringVar()  # cpu数量

        self.yingpan_part_no_after = tk.StringVar()  # 硬盘编号
        self.yingpan_nm_after = tk.StringVar()  # 硬盘名称
        self.yingpan_spec_after = tk.StringVar()  # 硬盘规格
        self.yingpan_qty_after = tk.StringVar()  # 硬盘数量

        self.neicun_part_no_after = tk.StringVar()  # 内存编号
        self.neicun_nm_after = tk.StringVar()  # 内存名称
        self.neicun_spec_after = tk.StringVar()  # 内存规格
        self.neicun_qty_after = tk.StringVar()  # 内存数量




        self.repair_done=tk.StringVar()#維修完成
        self.repair_done.set("F")

        self.zhuban_reuse=tk.StringVar()#主板可以用
        self.zhuban_reuse.set("F")


        self.cpu_reuse=tk.StringVar()#cpu可以用
        self.cpu_reuse.set("F")

        self.neicun_reuse=tk.StringVar()#內存可以用
        self.neicun_reuse.set("F")

        self.yingpan_reuse=tk.StringVar()#硬盤可以用
        self.yingpan_reuse.set("F")






        self.createPage()

    def check_date(self):
        try:
            datetime.datetime.strptime(self.back_date.get(), '%Y%m%d')
            datetime.datetime.strptime(self.receive_date.get(), '%Y%m%d')
            nowdate=datetime.datetime.now().strftime("%Y%m%d")
            nowdate=datetime.datetime.strptime(nowdate,'%Y%m%d')
            back_date=datetime.datetime.strptime(self.back_date.get(),'%Y%m%d')
            days=(back_date-nowdate).days
            if(days<0):
                messagebox.showinfo("","回厂日期需大于等于今天")
                return False
            else:
                return True
        except:
            messagebox.showinfo("", "日期请输入八位有效日期")
            return False


    def checknull(self):
        if not self.pc_no.get():
            messagebox.showinfo("","请先查询出设备")
            return  False
        if not self.back_date.get():
            messagebox.showinfo("","回厂日期不允许为空")
            return False
        if not self.receive_date.get():
            messagebox.showinfo("","领取日期不允许为空")
            return False
        if not self.check_date():
            return False
        return True









    def createPage(self):
        def reset():
            self.pc_no.set("")
            self.pc_nm.set("")
            self.pf_date.set("")
            self.address.set("")
            self.yt.set("")
            self.con_person.set("")
            self.sx_date.set("")
            txt_question.config(state="normal")
            txt_question.delete("1.0",tk.END)
            self.spec.set("")
            self.gb_date.set("")
            self.master_emp.set("")
            self.gs_type.set("")
            self.con_phone.set("")
            self.sx_cust.set("")

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

            self.zhuban_part_no_after.set("")
            self.zhuban_nm_after.set("")
            self.zhuban_spec_after.set("")
            self.zhuban_qty_after.set("")

            self.cpu_part_no_after.set("")
            self.cpu_nm_after.set("")
            self.cpu_spec_after.set("")
            self.cpu_qty_after.set("")

            self.yingpan_part_no_after.set("")
            self.yingpan_nm_after.set("")
            self.yingpan_spec_after.set("")
            self.yingpan_qty_after.set("")

            self.neicun_part_no_after.set("")
            self.neicun_nm_after.set("")
            self.neicun_spec_after.set("")
            self.neicun_qty_after.set("")

            self.repair_done.set("F")
            self.zhuban_reuse.set("F")
            self.cpu_reuse.set("F")
            self.neicun_reuse.set("F")
            self.yingpan_reuse.set("F")

            txt_pc_no.config(state="normal")
            btn_save.config(state="disable")  # 不可编辑
            btn_search.config(state="normal")  # 不可编辑
        def search():
            dict=sql.WeiXiuSql().search_tz(self.pc_no.get())
            if (len(dict) > 0):
                self.pc_nm.set(dict["pc_name"])
                self.pf_date.set(dict["peifa_date"])
                self.address.set(dict["address"])
                self.yt.set(dict["use_type"])
                self.con_person.set(dict["con_person"])
                self.sx_date.set(dict["sx_date"])
                self.question.set(dict["question"])
                self.spec.set(dict["p_spec"])
                self.gb_date.set(dict["guobao_date"])
                self.master_emp.set(dict["master_empno"])
                self.gs_type.set(dict["own_type"])
                self.con_phone.set(dict["con_phone"])
                self.sx_cust.set(dict["sx_cust"])
                txt_question.insert(tk.END,self.question.get())
                txt_question.config(state="disable")
                txt_pc_no.config(state="disable")
                btn_save.config(state="normal")  # 不可编辑
            else:
                messagebox.showinfo("", "改設備未產生維修通知")

            sql.WeiXiuSql().search_eqm_zhuban(self)
            sql.WeiXiuSql().search_eqm_cpu(self)
            sql.WeiXiuSql().search_eqm_neicun(self)
            sql.WeiXiuSql().search_eqm_yingpan(self)



        def save():
            flag=self.checknull()
            if(flag):
                self.upddate.set(str(datetime.datetime.now().strftime("%Y%m%d%H%M%S")))
                sql.WeiXiuSql().comfirm_repair(self)
                sql.WeiXiuSql().upd_eqm(self)
                messagebox.showinfo("","保存成功！")
                reset()






        frm1=tk.Frame(self)

        btn_reset=tk.Button(frm1,text="重置",command=reset)
        btn_reset.grid(row=0,column=0,padx=10)

        btn_search=tk.Button(frm1,text="查詢",command=search)
        btn_search.grid(row=0,column=1,padx=10)

        btn_save=tk.Button(frm1,text="保存",command=save)
        btn_save.grid(row=0,column=2,padx=10)
        btn_save.config(state="disable")  # 不可编辑






        frm2 = tk.Frame(self)
        tk.Label(frm2, text="设备编号").grid(row=0, column=0)
        tk.Label(frm2, text="设备名称").grid(row=1, column=0)
        tk.Label(frm2, text="配发日期").grid(row=2, column=0)
        tk.Label(frm2, text="地点").grid(row=3, column=0)
        tk.Label(frm2, text="用途").grid(row=4, column=0)
        tk.Label(frm2, text="备注").grid(row=5, column=0)
        tk.Label(frm2, text="联络人").grid(row=6, column=0)
        tk.Label(frm2, text="送修日期").grid(row=7, column=0)
        tk.Label(frm2, text="故障问题描述").grid(row=8, column=0)

        def searchpc(event):
            dict = sql.WeiXiuSql().search_tz(self.pc_no.get())
            if (len(dict) > 0):
                self.pc_nm.set(dict["pc_name"])
                self.pf_date.set(dict["peifa_date"])
                self.address.set(dict["address"])
                self.yt.set(dict["use_type"])
                self.con_person.set(dict["con_person"])
                self.sx_date.set(dict["sx_date"])
                self.question.set(dict["question"])
                self.spec.set(dict["p_spec"])
                self.gb_date.set(dict["guobao_date"])
                self.master_emp.set(dict["master_empno"])
                self.gs_type.set(dict["own_type"])
                self.con_phone.set(dict["con_phone"])
                self.sx_cust.set(dict["sx_cust"])
                txt_question.insert(tk.END, self.question.get())
                txt_question.config(state="disable")
                txt_pc_no.config(state="disable")
                btn_save.config(state="normal")  # 不可编辑
            else:
                messagebox.showinfo("", "改設備未產生維修通知")

            sql.WeiXiuSql().search_eqm_zhuban(self)
            sql.WeiXiuSql().search_eqm_cpu(self)
            sql.WeiXiuSql().search_eqm_neicun(self)
            sql.WeiXiuSql().search_eqm_yingpan(self)


        txt_pc_no = tk.Entry(frm2, textvariable=self.pc_no)
        # txt_pc_no.config(state="disable")
        txt_pc_no.grid(row=0, column=1)
        txt_pc_no.bind("<Return>", searchpc)


        txt_pc_nm = tk.Entry(frm2, textvariable=self.pc_nm)
        txt_pc_nm.config(state="disable")
        txt_pc_nm.grid(row=1, column=1)

        txt_pf_date = tk.Entry(frm2, textvariable=self.pf_date)
        txt_pf_date.config(state="disable")
        txt_pf_date.grid(row=2, column=1)

        txt_address = tk.Entry(frm2, textvariable=self.address)
        txt_address.config(state="disable")
        txt_address.grid(row=3, column=1)

        txt_yt = tk.Entry(frm2, textvariable=self.yt)
        txt_yt.config(state="disable")
        txt_yt.grid(row=4, column=1)

        txt_bz = tk.Entry(frm2, width=50, textvariable=self.bz)
        txt_bz.config(state="disable")
        txt_bz.grid(row=5, column=1, sticky=tk.E, columnspan=3)

        txt_con_person=tk.Entry(frm2, text="联络人", textvariable=self.con_person)
        txt_con_person.config(state="disable")
        txt_con_person.grid(row=6, column=1)


        txt_sx_date=tk.Entry(frm2, text="送修日期", textvariable=self.sx_date)
        txt_sx_date.config(state="disable")
        txt_sx_date.grid(row=7, column=1)



        txt_question = tk.Text(frm2, width=50, height=5)

        txt_question.grid(row=8, column=1, columnspan=3, pady=10)




        tk.Label(frm2, text="规格").grid(row=1, column=2)
        tk.Label(frm2, text="过保日期").grid(row=2, column=2)
        tk.Label(frm2, text="保管主管").grid(row=3, column=2)
        tk.Label(frm2, text="归属分类").grid(row=4, column=2)
        tk.Label(frm2, text="联络电话").grid(row=6, column=2)
        tk.Label(frm2, text="送修厂商").grid(row=7, column=2)
        # tk.Label(frm2, text="送修日期").grid(row=7, column=2)

        txt_spec = tk.Entry(frm2, textvariable=self.spec)
        txt_spec.config(state="disable")
        txt_spec.grid(row=1, column=3)

        txt_gb_date = tk.Entry(frm2, textvariable=self.gb_date)
        txt_gb_date.config(state="disable")
        txt_gb_date.grid(row=2, column=3)

        txt_master_emp = tk.Entry(frm2, textvariable=self.master_emp)
        txt_master_emp.config(state="disable")
        txt_master_emp.grid(row=3, column=3)

        txt_gs = tk.Entry(frm2, textvariable=self.gs_type)
        txt_gs.config(state="disable")
        txt_gs.grid(row=4, column=3)

        txt_con_phone=tk.Entry(frm2, textvariable=self.con_phone)
        txt_con_phone.config(state="disable")
        txt_con_phone.grid(row=6, column=3)

        txt_sx_cust=tk.Entry(frm2, textvariable=self.sx_cust)
        txt_sx_cust.config(state="disable")
        txt_sx_cust.grid(row=7, column=3)



        frm3 = tk.Frame(self)
        tk.Label(frm3, text="回廠日期").grid(row=0, column=0)
        tk.Label(frm3, text="領取日期").grid(row=1, column=0)
        tk.Label(frm3, text="處理結果").grid(row=2, column=0)

        txt_back_factory_date = tk.Entry(frm3,textvariable=self.back_date)
        # txt_pc_no.config(state="disable")
        txt_back_factory_date.grid(row=0, column=1,sticky=tk.W,padx=10)

        txt_receive_date = tk.Entry(frm3,textvariable=self.receive_date)
        #txt_receive_date.config(state="disable")
        txt_receive_date.grid(row=1, column=1,sticky=tk.W,padx=10)



        def get_receive_date():
            print(self.repair_done.get())
            if(self.repair_done.get()=="T"):
                self.receive_date.set(str(datetime.datetime.now().strftime("%Y%m%d")))
            else:
                self.receive_date.set("")


        # txt_repair_done=tk.Checkbutton(frm3,text="維修處理完成/結案？",textvariable=self.repair_done)
        # txt_repair_done.grid(row=1, column=2,padx=10)
        ttk.Checkbutton (frm3, variable=self.repair_done, onvalue="T", offvalue="F",text="維修處理完成/結案？",command=get_receive_date).grid(row=1, column=2)


        txt_result = tk.Text(frm3, width=50, height=5)
        #txt_pf_date.config(state="disable")
        txt_result.grid(row=2, column=1,columns=3,padx=10)




        frm4 = tk.Frame(self)




        tk.Label(frm4, text="可利用").grid(row=1, column=0)
        tk.Checkbutton(frm4,variable=self.zhuban_reuse, onvalue="T", offvalue="F").grid(row=2,column=0) #主板
        tk.Checkbutton(frm4,variable=self.cpu_reuse, onvalue="T", offvalue="F").grid( row=3, column=0)#cpu
        tk.Checkbutton(frm4,variable=self.neicun_reuse, onvalue="T", offvalue="F").grid(row=4, column=0)#内存
        tk.Checkbutton(frm4,variable=self.yingpan_reuse, onvalue="T", offvalue="F").grid(row=5, column=0)#硬盘













        tk.Label(frm4,text="類型").grid(row=1, column=1)
        tk.Label(frm4,text="主板").grid( row=2, column=1)
        tk.Label(frm4,text="CPU").grid( row=3, column=1)
        tk.Label(frm4,text="內存").grid( row=4, column=1)
        tk.Label(frm4, text="硬盤").grid(row=5, column=1)

        tk.Label(frm4, text="維修前").grid(row=0, column=2,columnspan=4)
        tk.Label(frm4, text="維修後").grid(row=0, column=6,columnspan=4)



        tk.Label(frm4, text="料編").grid(row=1, column=2)
        tk.Label(frm4, text="名稱").grid(row=1, column=3)
        tk.Label(frm4, text="規格").grid(row=1, column=4)
        tk.Label(frm4, text="數量").grid(row=1, column=5)
        tk.Label(frm4, text="料編").grid(row=1, column=6)
        tk.Label(frm4, text="名稱").grid(row=1, column=7)
        tk.Label(frm4, text="規格").grid(row=1, column=8)
        tk.Label(frm4, text="數量").grid(row=1, column=9)


        #主板
        txt_zhubanpartno_before = tk.Entry(frm4, width=10, textvariable=self.zhuban_part_no)
        txt_zhubanpartno_before.grid(row=2, column=2)
        txt_zhubanpartno_before.config(state="disable")

        txt_zhubanpartnm_before = tk.Entry(frm4, width=15, textvariable=self.zhuban_nm)
        txt_zhubanpartnm_before.grid(row=2, column=3)
        txt_zhubanpartnm_before.config(state="disable")

        txt_zhubanguige_before = tk.Entry(frm4, width=15, textvariable=self.zhuban_spec)
        txt_zhubanguige_before.grid(row=2, column=4)
        txt_zhubanguige_before.config(state="disable")

        txt_zhubanqty_before = tk.Entry(frm4, width=2, textvariable=self.zhuban_qty)
        txt_zhubanqty_before.grid(row=2, column=5)
        txt_zhubanqty_before.config(state="disable")

        def zhubaninfo(event):
            part_no=self.zhuban_part_no_after.get()
            type=part_no[0:4]
            dict=sqlBase.CONDB().getEqm(part_no,'001')
            if(len(dict)>0):
                for item in dict:
                    self.zhuban_nm_after.set(item["p_stype_nm"])
                    self.zhuban_spec_after.set(item["pspec_basis"])
            else:
                messagebox.showwarning("no part_no","料編不存在")


        txt_zhubanpartno_after = tk.Entry(frm4, width=10,textvariable=self.zhuban_part_no_after)
        txt_zhubanpartno_after.grid(row=2, column=6)
        txt_zhubanpartno_after.bind('<Return>', zhubaninfo)
        # txt_zhubanpartno_after.config(state="disable")

        txt_zhubanpartnm_after = tk.Entry(frm4, width=15,textvariable=self.zhuban_nm_after)
        txt_zhubanpartnm_after.grid(row=2, column=7)
        # txt_zhubanpartnm_after.config(state="disable")


        txt_zhubanguige_after = tk.Entry(frm4, width=15,textvariable=self.zhuban_spec_after)
        txt_zhubanguige_after.grid(row=2, column=8)
        # txt_zhubanguige_after.config(state="disable")

        txt_zhubanqty_after = tk.Entry(frm4, width=2,textvariable=self.zhuban_qty_after)
        txt_zhubanqty_after.grid(row=2, column=9)
        # txt_zhubanqty_after.config(state="disable")



        #cpu
        txt_cpu_before = tk.Entry(frm4, width=10, textvariable=self.cpu_part_no)
        txt_cpu_before.grid(row=3, column=2)
        txt_cpu_before.config(state="disable")

        txt_cpu_nm_before = tk.Entry(frm4, width=15, textvariable=self.cpu_nm)
        txt_cpu_nm_before.grid(row=3, column=3)
        txt_cpu_nm_before.config(state="disable")

        txt_cpu_guige_before = tk.Entry(frm4, width=15, textvariable=self.cpu_spec)
        txt_cpu_guige_before.grid(row=3, column=4)
        txt_cpu_guige_before.config(state="disable")

        txt_cpu_qty_before = tk.Entry(frm4, width=2, textvariable=self.cpu_qty)
        txt_cpu_qty_before.grid(row=3, column=5)
        txt_cpu_qty_before.config(state="disable")

        def cpuinfo(event):
            part_no = self.cpu_part_no_after.get()
            type = part_no[0:4]
            dict = sqlBase.CONDB().getEqm(part_no, '002')
            if (len(dict) > 0):
                for item in dict:
                    self.cpu_nm_after.set(item["p_stype_nm"])
                    self.cpu_spec_after.set(item["pspec_basis"])
            else:
                messagebox.showwarning("no part_no", "料編不存在")




        txt_cpu_partno_after = tk.Entry(frm4, width=10, textvariable=self.cpu_part_no_after)
        txt_cpu_partno_after.grid(row=3, column=6)
        txt_cpu_partno_after.bind('<Return>', cpuinfo)
        # txt_cpu_partno_after.config(state="disable")

        txt_cpupartnm_after = tk.Entry(frm4, width=15, textvariable=self.cpu_nm_after)
        txt_cpupartnm_after.grid(row=3, column=7)
        # txt_cpupartnm_after.config(state="disable")

        txt_cpu_guige_after = tk.Entry(frm4, width=15, textvariable=self.cpu_spec_after)
        txt_cpu_guige_after.grid(row=3, column=8)
        # txt_cpu_guige_after.config(state="disable")

        txt_cpu_qty_after = tk.Entry(frm4, width=2, textvariable=self.cpu_qty_after)
        txt_cpu_qty_after.grid(row=3, column=9)
        # txt_cpu_qty_after.config(state="disable")

        # 内存
        txt_neicun_before = tk.Entry(frm4, width=10, textvariable=self.neicun_part_no)
        txt_neicun_before.grid(row=4, column=2)
        txt_neicun_before.config(state="disable")

        txt_neicun_nm_before = tk.Entry(frm4, width=15, textvariable=self.neicun_nm)
        txt_neicun_nm_before.grid(row=4, column=3)
        txt_neicun_nm_before.config(state="disable")

        txt_neicun_guige_before = tk.Entry(frm4, width=15, textvariable=self.neicun_spec)
        txt_neicun_guige_before.grid(row=4, column=4)
        txt_neicun_guige_before.config(state="disable")

        txt_neicun_qty_before = tk.Entry(frm4, width=2, textvariable=self.neicun_qty)
        txt_neicun_qty_before.grid(row=4, column=5)
        txt_neicun_qty_before.config(state="disable")

        def neicuninfo(event):
            part_no = self.neicun_part_no_after.get()
            type = part_no[0:4]
            dict = sql.CONDB().getEqm(part_no, '003')
            if (len(dict) > 0):
                for item in dict:
                    self.neicun_nm_after.set(item["p_stype_nm"])
                    self.neicun_spec_after.set(item["pspec_basis"])
            else:
                messagebox.showwarning("no part_no", "料編不存在")




        txt_neicun_partno_after = tk.Entry(frm4, width=10, textvariable=self.neicun_part_no_after)
        txt_neicun_partno_after.grid(row=4, column=6)
        # txt_neicun_partno_after.config(state="disable")
        txt_neicun_partno_after.bind('<Return>', neicuninfo)




        txt_neicun_partnm_after = tk.Entry(frm4, width=15, textvariable=self.neicun_nm_after)
        txt_neicun_partnm_after.grid(row=4, column=7)
        # txt_neicun_partnm_after.config(state="disable")

        txt_neicun_guige_after = tk.Entry(frm4, width=15, textvariable=self.neicun_spec_after)
        txt_neicun_guige_after.grid(row=4, column=8)
        # txt_neicun_guige_after.config(state="disable")

        txt_neicun_qty_after = tk.Entry(frm4, width=2, textvariable=self.neicun_qty_after)
        txt_neicun_qty_after.grid(row=4, column=9)
        # txt_neicun_qty_after.config(state="disable")

        # 硬盘
        txt_yingpan_before = tk.Entry(frm4, width=10, textvariable=self.yingpan_part_no)
        txt_yingpan_before.grid(row=5, column=2)
        txt_yingpan_before.config(state="disable")

        txt_yingpan_nm_before = tk.Entry(frm4, width=15, textvariable=self.yingpan_nm)
        txt_yingpan_nm_before.grid(row=5, column=3)
        txt_yingpan_nm_before.config(state="disable")

        txt_yingpan_guige_before = tk.Entry(frm4, width=15, textvariable=self.yingpan_spec)
        txt_yingpan_guige_before.grid(row=5, column=4)
        txt_yingpan_guige_before.config(state="disable")

        txt_yingpan_qty_before = tk.Entry(frm4, width=2, textvariable=self.yingpan_qty)
        txt_yingpan_qty_before.grid(row=5, column=5)
        txt_yingpan_qty_before.config(state="disable")

        def yingpaninfo(event):
            part_no = self.yingpan_part_no_after.get()
            type = part_no[0:4]
            dict = sql.CONDB().getEqm(part_no, '004')
            if (len(dict) > 0):
                for item in dict:
                    self.yingpan_nm_after.set(item["p_stype_nm"])
                    self.yingpan_spec_after.set(item["pspec_basis"])
            else:
                messagebox.showwarning("no part_no", "料編不存在")



        txt_yingpan_partno_after = tk.Entry(frm4, width=10, textvariable=self.yingpan_part_no_after)
        txt_yingpan_partno_after.grid(row=5, column=6)
        # txt_yingpan_partno_after.config(state="disable")
        txt_yingpan_partno_after.bind('<Return>', yingpaninfo)


        txt_yingpan_partnm_after = tk.Entry(frm4, width=15, textvariable=self.yingpan_nm_after)
        txt_yingpan_partnm_after.grid(row=5, column=7)
        # txt_yingpan_partnm_after.config(state="disable")

        txt_yingpan_guige_after = tk.Entry(frm4, width=15, textvariable=self.yingpan_spec_after)
        txt_yingpan_guige_after.grid(row=5, column=8)
        # txt_yingpan_guige_after.config(state="disable")

        txt_yingpan_qty_after = tk.Entry(frm4, width=2, textvariable=self.yingpan_qty_after)
        txt_yingpan_qty_after.grid(row=5, column=9)
        # txt_yingpan_qty_after.config(state="disable")

        frm1.pack(side=tk.TOP)
        frm2.pack(side=tk.TOP)
        frm3.pack(side=tk.TOP)
        frm4.pack(side=tk.TOP)


        pass