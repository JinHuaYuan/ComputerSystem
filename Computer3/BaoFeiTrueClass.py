import  tkinter as  tk
import  BaoFeiClassSqlDB as sql
import  tkinter.messagebox as messagebox
import  datetime
import tkinter.ttk as  ttk
import  SqlDB as  sqlbase


class BaoFei(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.root = master  # 定义内部变量root


        self.pc_no=tk.StringVar()
        self.pc_nm=tk.StringVar()
        self.gb_date=tk.StringVar()
        self.yt=tk.StringVar()
        self.address=tk.StringVar()
        self.pf_date=tk.StringVar()

        self.bf_reason=tk.StringVar()
        self.temp_noYn=tk.StringVar()
        self.temp_noYn.set("F")

        self.spec=tk.StringVar()
        self.pr_no=tk.StringVar()
        self.gs_type=tk.StringVar()
        self.master_emp=tk.StringVar()


        self.bf_date=tk.StringVar()
        self.upddate=tk.StringVar()



        self.repair_done = tk.StringVar()  # 維修完成
        self.repair_done.set("F")

        self.zhuban_reuse = tk.StringVar()  # 主板可以用
        self.zhuban_reuse.set("F")

        self.cpu_reuse = tk.StringVar()  # cpu可以用
        self.cpu_reuse.set("F")

        self.neicun_reuse = tk.StringVar()  # 內存可以用
        self.neicun_reuse.set("F")

        self.yingpan_reuse = tk.StringVar()  # 硬盤可以用
        self.yingpan_reuse.set("F")

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



        self.createPage()

    def createPage(self):







        frm1=tk.Frame(self)



        def reset():
            self.pc_no.set("")
            self.pc_nm.set("")
            self.gb_date.set("")
            self.yt.set("")
            self.address.set("")
            self.pf_date.set("")
            self.bf_reason.set("")
            self.temp_noYn.set("F")
            self.spec.set("")
            self.pr_no.set("")
            self.gs_type.set("")
            self.master_emp.set("")


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

            self.zhuban_reuse.set("F")
            self.cpu_reuse.set("F")
            self.neicun_reuse.set("F")
            self.yingpan_reuse.set("F")

            txt_pc_no.config(state="normal")
            btn_save.config(state="disable")  # 不可编辑
            btn_search.config(state="normal")  # 不可编辑

        def search():
            dict = sql.BaoFeiSql().search(self.pc_no.get().strip())
            if (len(dict) > 0):
                self.pc_nm.set(dict["pc_name"])
                self.gb_date.set(dict["guobao_date"])
                self.yt.set(dict["use_type"])
                self.address.set(dict["address"])
                self.pf_date.set(dict["peifa_date"])
                self.temp_noYn.set(dict["temp_noYN"])
                self.spec.set(dict["p_spec"])
                self.pr_no.set(dict["pr_no"])
                self.gs_type.set(dict["own_type"])
                self.master_emp.set(dict["master_empno"])

                sql.BaoFeiSql().search_eqm_zhuban(self)
                sql.BaoFeiSql().search_eqm_cpu(self)
                sql.BaoFeiSql().search_eqm_neicun(self)
                sql.BaoFeiSql().search_eqm_yingpan(self)

                txt_pc_no.config(state="disable")
                btn_save.config(state="normal")  # 不可编辑

                p_btype=sqlbase.CONDB().getpc_btype(self.pc_no.get())
                if(p_btype=='PC'):
                    frm3.pack(side=tk.LEFT)
                else:
                    frm3.pack_forget()


            else:
                messagebox.showinfo("", "沒有該設備編號")

        def save():
            self.bf_date.set(str(datetime.datetime.now().strftime("%Y%m%d")))
            self.upddate.set(str(datetime.datetime.now().strftime("%Y%m%d%H%M%S")))
            sql.BaoFeiSql().save(self)


        btn_reset = tk.Button(frm1, text="重置",command=reset)
        btn_reset.grid(row=0, column=0, padx=10)
        btn_search = tk.Button(frm1, text="查詢",command=search)
        btn_search.grid(row=0, column=1, padx=10)
        btn_save = tk.Button(frm1, text="保存",command=save)
        btn_save.grid(row=0, column=2, padx=10)
        btn_save.config(state="disable")  # 不可编辑





        frm2=tk.Frame(self)

        tk.Label(frm2,text="設備編號").grid(row=0,column=0)
        tk.Label(frm2,text="設備名稱").grid(row=1,column=0)
        tk.Label(frm2,text="過保日期").grid(row=2,column=0)
        tk.Label(frm2,text="用途").grid(row=3, column=0)
        tk.Label(frm2,text="地點").grid(row=4, column=0)
        tk.Label(frm2,text="配發日期").grid(row=5, column=0)
        tk.Label(frm2,text="報廢原因").grid(row=6, column=0)
        tk.Label(frm2,text="臨時編號").grid(row=0, column=2)
        tk.Label(frm2,text="規格").grid(row=1, column=2)
        tk.Label(frm2,text="請購單號").grid(row=2, column=2)
        tk.Label(frm2,text="歸屬分類").grid(row=3, column=2)
        tk.Label(frm2,text="保管主管").grid(row=4, column=2)

        def searchpc(event):
            dict = sql.BaoFeiSql().search(self.pc_no.get().strip())
            if (len(dict) > 0):
                self.pc_nm.set(dict["pc_name"])
                self.gb_date.set(dict["guobao_date"])
                self.yt.set(dict["use_type"])
                self.address.set(dict["address"])
                self.pf_date.set(dict["peifa_date"])
                self.temp_noYn.set(dict["temp_noYN"])
                self.spec.set(dict["p_spec"])
                self.pr_no.set(dict["pr_no"])
                self.gs_type.set(dict["own_type"])
                self.master_emp.set(dict["master_empno"])

                sql.BaoFeiSql().search_eqm_zhuban(self)
                sql.BaoFeiSql().search_eqm_cpu(self)
                sql.BaoFeiSql().search_eqm_neicun(self)
                sql.BaoFeiSql().search_eqm_yingpan(self)

                txt_pc_no.config(state="disable")
                btn_save.config(state="normal")  # 不可编辑

                p_btype = sqlbase.CONDB().getpc_btype(self.pc_no.get())
                if (p_btype == 'PC'):
                    frm3.pack(side=tk.LEFT)
                else:
                    frm3.pack_forget()

        txt_pc_no=tk.Entry(frm2,textvariable=self.pc_no)
        txt_pc_no.grid(row=0,column=1)
        txt_pc_no.bind("<Return>", searchpc)


        txt_pc_nm=tk.Entry(frm2,textvariable=self.pc_nm)
        txt_pc_nm.grid(row=1,column=1)
        txt_pc_nm.config(state="disable")  # 不可编辑

        txt_gb_date=tk.Entry(frm2,textvariable=self.gb_date)
        txt_gb_date.grid(row=2, column=1)
        txt_gb_date.config(state="disable")  # 不可编辑


        txt_yt=tk.Entry(frm2,textvariable=self.yt)
        txt_yt.grid(row=3, column=1)
        txt_yt.config(state="disable")  # 不可编辑



        txt_address=tk.Entry(frm2,textvariable=self.address)
        txt_address.grid(row=4, column=1)
        txt_address.config(state="disable")  # 不可编辑



        txt_pf_dat=tk.Entry(frm2,textvariable=self.pf_date)
        txt_pf_dat.grid(row=5, column=1)
        txt_pf_dat.config(state="disable")  # 不可编辑


        tk.Entry(frm2,textvariable=self.bf_reason,width=50).grid(row=6, column=1,columnspan=3)



        cbk_temp=ttk.Checkbutton(frm2,variable=self.temp_noYn, onvalue="T", offvalue="F")
        cbk_temp.grid(row=0, column=3)
        cbk_temp.config(state="disable")  # 不可编辑

        txt_spec=tk.Entry(frm2,textvariable=self.spec)
        txt_spec.grid(row=1, column=3)
        txt_spec.config(state="disable")  # 不可编辑

        txt_pr_no=tk.Entry(frm2,textvariable=self.pr_no)
        txt_pr_no.grid(row=2, column=3)
        txt_pr_no.config(state="disable")  # 不可编辑

        txt_gs_type=tk.Entry(frm2,textvariable=self.gs_type)
        txt_gs_type.grid(row=3, column=3)
        txt_gs_type.config(state="disable")  # 不可编辑

        txt_master_emp=tk.Entry(frm2,textvariable=self.master_emp)
        txt_master_emp.grid(row=4, column=3)
        txt_master_emp.config(state="disable")  # 不可编辑


        frm3=tk.Frame(self)

        tk.Label(frm3,text="可再利用").grid(row=0, column=0,sticky=tk.W)
        tk.Checkbutton(frm3, variable=self.zhuban_reuse, onvalue="T", offvalue="F").grid(row=1, column=0)  # 主板
        tk.Checkbutton(frm3, variable=self.cpu_reuse, onvalue="T", offvalue="F").grid(row=2, column=0)  # cpu
        tk.Checkbutton(frm3, variable=self.neicun_reuse, onvalue="T", offvalue="F").grid(row=3, column=0)  # 内存
        tk.Checkbutton(frm3, variable=self.yingpan_reuse, onvalue="T", offvalue="F").grid(row=4, column=0)  # 硬盘

        tk.Label(frm3,text="主板").grid(row=1, column=1)
        tk.Label(frm3,text="CPU").grid(row=2, column=1)
        tk.Label(frm3,text="內存").grid(row=3, column=1)
        tk.Label(frm3,text="硬盤").grid(row=4, column=1)

        tk.Label(frm3, text="料編").grid(row=0, column=2)
        tk.Label(frm3, text="名稱").grid(row=0, column=3)
        tk.Label(frm3, text="規格").grid(row=0, column=4)
        tk.Label(frm3, text="數量").grid(row=0, column=5)

        # 主板
        txt_zhubanpartno_before = tk.Entry(frm3, width=10, textvariable=self.zhuban_part_no)
        txt_zhubanpartno_before.grid(row=1, column=2)
        txt_zhubanpartno_before.config(state="disable")

        txt_zhubanpartnm_before = tk.Entry(frm3, width=15, textvariable=self.zhuban_nm)
        txt_zhubanpartnm_before.grid(row=1, column=3)
        txt_zhubanpartnm_before.config(state="disable")

        txt_zhubanguige_before = tk.Entry(frm3, width=15, textvariable=self.zhuban_spec)
        txt_zhubanguige_before.grid(row=1, column=4)
        txt_zhubanguige_before.config(state="disable")

        txt_zhubanqty_before = tk.Entry(frm3, width=2, textvariable=self.zhuban_qty)
        txt_zhubanqty_before.grid(row=1, column=5)
        txt_zhubanqty_before.config(state="disable")

        # cpu
        txt_cpu_before = tk.Entry(frm3, width=10, textvariable=self.cpu_part_no)
        txt_cpu_before.grid(row=2, column=2)
        txt_cpu_before.config(state="disable")

        txt_cpu_nm_before = tk.Entry(frm3, width=15, textvariable=self.cpu_nm)
        txt_cpu_nm_before.grid(row=2, column=3)
        txt_cpu_nm_before.config(state="disable")

        txt_cpu_guige_before = tk.Entry(frm3, width=15, textvariable=self.cpu_spec)
        txt_cpu_guige_before.grid(row=2, column=4)
        txt_cpu_guige_before.config(state="disable")

        txt_cpu_qty_before = tk.Entry(frm3, width=2, textvariable=self.cpu_qty)
        txt_cpu_qty_before.grid(row=2, column=5)
        txt_cpu_qty_before.config(state="disable")

        # 内存
        txt_neicun_before = tk.Entry(frm3, width=10, textvariable=self.neicun_part_no)
        txt_neicun_before.grid(row=3, column=2)
        txt_neicun_before.config(state="disable")

        txt_neicun_nm_before = tk.Entry(frm3, width=15, textvariable=self.neicun_nm)
        txt_neicun_nm_before.grid(row=3, column=3)
        txt_neicun_nm_before.config(state="disable")

        txt_neicun_guige_before = tk.Entry(frm3, width=15, textvariable=self.neicun_spec)
        txt_neicun_guige_before.grid(row=3, column=4)
        txt_neicun_guige_before.config(state="disable")

        txt_neicun_qty_before = tk.Entry(frm3, width=2, textvariable=self.neicun_qty)
        txt_neicun_qty_before.grid(row=3, column=5)
        txt_neicun_qty_before.config(state="disable")

        # 硬盘
        txt_yingpan_before = tk.Entry(frm3, width=10, textvariable=self.yingpan_part_no)
        txt_yingpan_before.grid(row=4, column=2)
        txt_yingpan_before.config(state="disable")

        txt_yingpan_nm_before = tk.Entry(frm3, width=15, textvariable=self.yingpan_nm)
        txt_yingpan_nm_before.grid(row=4, column=3)
        txt_yingpan_nm_before.config(state="disable")

        txt_yingpan_guige_before = tk.Entry(frm3, width=15, textvariable=self.yingpan_spec)
        txt_yingpan_guige_before.grid(row=4, column=4)
        txt_yingpan_guige_before.config(state="disable")

        txt_yingpan_qty_before = tk.Entry(frm3, width=2, textvariable=self.yingpan_qty)
        txt_yingpan_qty_before.grid(row=4, column=5)
        txt_yingpan_qty_before.config(state="disable")



        frm1.pack(side=tk.TOP)
        frm2.pack(side=tk.TOP)
        frm3.pack(side=tk.LEFT)