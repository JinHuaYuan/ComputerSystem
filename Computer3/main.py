import tkinter as  tk
import tkinter.messagebox as messagebox


class Main:
    def __init__(self, master=None):
        self.status=tk.StringVar()
        self.status.set("T")
        self.win()

    def win(self):
        main=tk.Tk()
        def hello():
            print()
        def text_change(event):
            print(txt_dafenlei.get())
            if(txt_dafenlei.get()=="71"):
                frm4.grid_forget()
        frm1=tk.Frame(main)
        lbl_dafenlei=tk.Label(frm1,text="大分類")
        lbl_dafenlei.grid(row=1,column=1)
        txt_dafenlei = tk.Entry(frm1)
        txt_dafenlei.grid(row=1, column=2)
        lbl_zhongfenlei = tk.Label(frm1, text="中分類")
        lbl_zhongfenlei.grid(row=2, column=1)
        txt_zhongfenlei = tk.Entry(frm1)
        txt_zhongfenlei.grid(row=2, column=2)
        txt_zhongfenlei.bind('<Button-1>', text_change)
        lbl_machine_no=tk.Label(frm1,text="設備編號")
        lbl_machine_no.grid(row=3, column=1)
        txt_machine_no = tk.Entry(frm1)
        txt_machine_no.grid(row=3, column=2)
        lbl_machine_nm = tk.Label(frm1, text="設備名稱")
        lbl_machine_nm.grid(row=4, column=1)
        txt_machine_nm = tk.Entry(frm1)
        txt_machine_nm.grid(row=4, column=2)
        lbl_machine_nm = tk.Label(frm1, text="過保日期")
        lbl_machine_nm.grid(row=5, column=1)
        txt_machine_nm = tk.Entry(frm1)
        txt_machine_nm.grid(row=5, column=2)
        lbl_useway = tk.Label(frm1, text="用途")
        lbl_useway.grid(row=6, column=1)
        txt_useway = tk.Entry(frm1)
        txt_useway.grid(row=6, column=2)
        lbl_address = tk.Label(frm1, text="地點")
        lbl_address.grid(row=7, column=1)
        txt_address = tk.Entry(frm1)
        txt_address.grid(row=7, column=2)
        lbl_pefa_date = tk.Label(frm1, text="配發日期")
        lbl_pefa_date.grid(row=8, column=1)
        txt_pefa_date = tk.Entry(frm1)
        txt_pefa_date.grid(row=8, column=2)
        frm1.grid(column=0,row=0,sticky=tk.W)
        frm2=tk.Frame(main)


        lbl_linshi_no = tk.Label(frm2, text="臨時編號")
        lbl_linshi_no .grid(row=1, column=1)




        chk_insi_no= tk.Checkbutton(frm2, onvalue="T", offvalue="F",variable=self.status)
        chk_insi_no.grid(row=1, column=2,sticky=tk.W)





        lbl_psec= tk.Label(frm2, text="規格")
        lbl_psec.grid(row=2, column=1)
        txt_psec= tk.Entry(frm2)
        txt_psec.grid(row=2, column=2)
        lbl_pr_no= tk.Label(frm2, text="請購單號")
        lbl_pr_no.grid(row=3, column=1)
        txt_pr_no= tk.Entry(frm2)
        txt_pr_no.grid(row=3, column=2)
        lbl_gsfenlei = tk.Label(frm2, text="歸屬分類")
        lbl_gsfenlei.grid(row=4, column=1)
        txt_gsfenlei = tk.Entry(frm2)
        txt_gsfenlei.grid(row=4, column=2)
        lbl_bg_master = tk.Label(frm2, text="保管主管")
        lbl_bg_master.grid(row=5, column=1)
        txt_bg_master = tk.Entry(frm2)
        txt_bg_master.grid(row=5, column=2)
        frm2.grid(column=3, row=0,sticky=tk.W,padx=20)
        frm3=tk.Frame(main)


        btn_cs_machine_no=tk.Button(frm3,text="產生編號",command=hello)
        btn_cs_machine_no .grid(row=1, column=1)

        btn_save = tk.Button(frm3, text="保存", command=hello,width=10)
        btn_save.grid(row=2, column=1,pady=50)

        frm3.grid(column=5, row=0,sticky=tk.N,padx=10,pady=20)



        frm4=tk.Frame(main)

        lbl_zhuban= tk.Label(frm4, text="主板/型號")
        lbl_zhuban.grid(row=1, column=1)

        lbl_zhuban = tk.Label(frm4, text="CPU")
        lbl_zhuban.grid(row=2, column=1)

        lbl_neicun = tk.Label(frm4, text="內存")
        lbl_neicun.grid(row=3, column=1)

        lbl_yingpan = tk.Label(frm4, text="硬盤")
        lbl_yingpan.grid(row=4, column=1)




        tk.Label(frm4, text="料編").grid(row=0, column=2,padx=15)


        tk.Label(frm4, text="名稱") .grid(row=0, column=3,padx=15)


        tk.Label(frm4, text="規格").grid(row=0, column=4,padx=15)

        tk.Label(frm4, text="數量").grid(row=0, column=5,padx=15)

        #主板
        txt_zhubanpartnm=tk.Entry(frm4,width=10)
        txt_zhubanpartnm.grid(row=1,column=2)

        txt_zhubanpartno = tk.Entry(frm4, width=10)
        txt_zhubanpartno.grid(row=1, column=3)

        txt_zhubanguige = tk.Entry(frm4, width=10)
        txt_zhubanguige.grid(row=1, column=4)

        txt_zhubanqty= tk.Entry(frm4, width=10)
        txt_zhubanqty.grid(row=1, column=5)

        #CPU
        txt_cpunpartnm = tk.Entry(frm4, width=10)
        txt_cpunpartnm.grid(row=2, column=2)

        txt_cpubanpartno = tk.Entry(frm4, width=10)
        txt_cpubanpartno.grid(row=2, column=3)

        txt_cpuguige = tk.Entry(frm4, width=10)
        txt_cpuguige.grid(row=2, column=4)

        txt_cpuqty = tk.Entry(frm4, width=10)
        txt_cpuqty.grid(row=2, column=5)

        # 內存
        txt_neicunnpartnm = tk.Entry(frm4, width=10)
        txt_neicunnpartnm.grid(row=3, column=2)

        txt_neicunbanpartno = tk.Entry(frm4, width=10)
        txt_neicunbanpartno.grid(row=3, column=3)

        txt_neicunguige = tk.Entry(frm4, width=10)
        txt_neicunguige.grid(row=3, column=4)

        txt_neicunqty = tk.Entry(frm4, width=10)
        txt_neicunqty.grid(row=3, column=5)

        # 硬盤
        txt_yingpannpartnm = tk.Entry(frm4, width=10)
        txt_yingpannpartnm.grid(row=4, column=2)

        txt_yingpanbanpartno = tk.Entry(frm4, width=10)
        txt_yingpanbanpartno.grid(row=4, column=3)

        txt_yingpanguige = tk.Entry(frm4, width=10)
        txt_yingpanguige.grid(row=4, column=4)

        txt_yingpanqty = tk.Entry(frm4, width=10)
        txt_yingpanqty.grid(row=4, column=5)



        frm4.grid(column=0, row=1, sticky=tk.N, padx=10, pady=20)




        main=main.mainloop()

