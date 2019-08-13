import  tkinter as tk
import  AddClass as Add
import BaoFeiClass as BaoFei
import BaoFeiComfirmClass as BaoFeiComfirm
import UpdateClass as Update
import BorrowClass as Borrow
import BackClass as  Back
import  SearchMasterClass as SearchMaster
import  BaoFeiTrueClass as  BaoFeiTrue
import  BackFactory as BackFactory
import  ReceiveClass as Receive
import User as User
import  PiCiAddClass as PiCiAdd
import  InRepairTZ as InWeiXiu
import  InRepairBack as InWeiXiuBack
import  InRepairReceive as InWeiXiuReceive

class  MainClass:
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.geometry('%dx%d' % (500, 180))  # 设置窗口大小
        self.username = tk.StringVar()
        self.username.set("ddd")
        self.password = tk.StringVar()
        self.password.set("T")
        #self.page = tk.Frame(self.root)
        #self.page.pack()



        self.inputPage = Add.Add(self.root)       #新增设备
        self.piciinputPage=PiCiAdd.PiCiAdd(self.root)#批次新增


        self.baofeiPage = BaoFei.BaoFei(self.root)  #维修通知

        self.backfactoryPage=BackFactory.BackFactory(self.root)#回廠確認
        self.receivePage=Receive.Receive(self.root)#領取確認

        # self.baofeicomfirmPage=BaoFeiComfirm.BaoFeiComfirm(self.root) #维修确认




        self.updatePage=Update.Update(self.root) #异动设备
        self.borrowPage = Borrow.Borrow(self.root)#借用
        self.backPage=Back.Back(self.root)#归还
        self.searchMasterPage=SearchMaster.SearchMaster(self.root)#库存主管
        self.baofeitruePage=BaoFeiTrue.BaoFei(self.root)#报废



        #內維修
        self.inreapirPage = InWeiXiu.InRepairTZ(self.root)  # 维修通知
        self.inrepairBackPage=InWeiXiuBack.InRepairBack(self.root)#回廠確認
        self.inrepairReceivePage=InWeiXiuReceive.InRepairReceive(self.root)#領取確認

        # self.INbackfactoryPage = BackFactory.BackFactory(self.root)  # 回廠確認
        # self.INreceivePage = Receive.Receive(self.root)  # 領取確認






        #self.weixiutzPage=WeiXiu.WeiXiu
        #self.weixiuqrPage=WeiXiu.WeiXiu
        # self.yidongPage=WeiXiu.WeiXiu



        # self.inputPage.pack_forget()
        # self.inputPage.grid_forget()
        self.createPage()
    def createPage(self):
        self.root.title("電腦管理系統" + "                  登錄者：" + User.uer_code)
        menubar = tk.Menu(self.root)

        filemenubar1 = tk.Menu(menubar, tearoff=False)
        filemenubar1.add_command(label='数据录入',command=self.createinputpage)
        filemenubar1.add_command(label='数据修改',command=self.createupdatepage)
        filemenubar1.add_command(label='批次录入', command=self.createpicipage)


        menubar.insert_cascade(2, menu=filemenubar1, label="Pc數據異動")


        filemenubar2=tk.Menu(menubar,tearoff=False)

        filemenubar2.add_command(label='送外維修',command=self.createbaofeipage)
        filemenubar2.add_command(label='回廠確認', command=self.createbackfactorypage)
        filemenubar2.add_command(label='收取確認', command=self.createreceivepage)



        # filemenubar2.add_command(label='维修确认',command=self.createbaofeicomfirmpage)



        menubar.insert_cascade(2,menu=filemenubar2,label="外维修")





        #内维修
        filemenubar3 = tk.Menu(menubar, tearoff=False)

        filemenubar3.add_command(label='維修',command=self.createInweixiuPage)
        filemenubar3.add_command(label='回廠確認',command=self.createInweixiuBackPage)
        filemenubar3.add_command(label='收取確認',command=self.createInweixiuReceivePage)

        # filemenubar2.add_command(label='维修确认',command=self.createbaofeicomfirmpage)

        menubar.insert_cascade(3, menu=filemenubar3, label="内维修")


















        menubar.insert_cascade(4,label='异动记录')
        menubar.insert_cascade(5,label='报废',command=self.createbaofeitruepage)

        menubar.delete(4)




        filemenubar5 = tk.Menu(menubar, tearoff=False)
        filemenubar5.add_command(label='借用设备',command=self.createbrorrowpage)
        filemenubar5.add_command(label='归还设备',command=self.createbackpage)
        menubar.insert_cascade(6, label='借还设备',menu=filemenubar5)

        menubar.insert_cascade(7, label='查詢庫存主管',command=self.createsearchmasterpage)





       # menubar.delete(0)  删除menubar


        self.root['menu'] = menubar  # 设置菜单栏

        # self.createinputpage()


        # self.createinputpage()


        # tk.Entry(self.page,textvariable=self.username).pack()
        # ck1=tk.Checkbutton(self.page, variable=self.password,onvalue="T",offvalue="F")
        #
        # def chang(event):
        #     print(self.password.get())
        #
        # ck1.bind("<Button-1>",chang)
        #
        # ck1.pack()

    def createInweixiuReceivePage(self):
        self.root.geometry("700x200")
        self.inrepairReceivePage.pack()
        self.inrepairBackPage.pack_forget()
        self.inreapirPage.pack_forget()
        self.piciinputPage.pack_forget()
        self.receivePage.pack_forget()
        self.backfactoryPage.pack_forget()
        # self.baofeicomfirmPage.pack_forget()
        self.baofeiPage.pack_forget()
        self.backPage.pack_forget()
        self.borrowPage.pack_forget()
        self.inputPage.pack_forget()
        self.updatePage.pack_forget()
        self.searchMasterPage.pack_forget()
        self.baofeitruePage.pack_forget()

    def createInweixiuBackPage(self):
        self.root.geometry("700x350")
        self.inrepairBackPage.pack()
        self.inreapirPage.pack_forget()
        self.piciinputPage.pack_forget()
        self.receivePage.pack_forget()
        self.backfactoryPage.pack_forget()
        # self.baofeicomfirmPage.pack_forget()
        self.baofeiPage.pack_forget()
        self.backPage.pack_forget()
        self.borrowPage.pack_forget()
        self.inputPage.pack_forget()
        self.updatePage.pack_forget()
        self.searchMasterPage.pack_forget()
        self.baofeitruePage.pack_forget()
        self.inrepairReceivePage.pack_forget()




    def createInweixiuPage(self):
        self.root.geometry("700x350")
        self.inreapirPage.pack()
        self.piciinputPage.pack_forget()
        self.receivePage.pack_forget()
        self.backfactoryPage.pack_forget()
        # self.baofeicomfirmPage.pack_forget()
        self.baofeiPage.pack_forget()
        self.backPage.pack_forget()
        self.borrowPage.pack_forget()
        self.inputPage.pack_forget()
        self.updatePage.pack_forget()
        self.searchMasterPage.pack_forget()
        self.baofeitruePage.pack_forget()
        self.inrepairBackPage.pack_forget()
        self.inrepairReceivePage.pack_forget()





    def createpicipage(self):
        self.root.geometry("700x100")
        self.piciinputPage.pack()
        self.receivePage.pack_forget()
        self.backfactoryPage.pack_forget()
        # self.baofeicomfirmPage.pack_forget()
        self.baofeiPage.pack_forget()
        self.backPage.pack_forget()
        self.borrowPage.pack_forget()
        self.inputPage.pack_forget()
        self.updatePage.pack_forget()
        self.searchMasterPage.pack_forget()
        self.baofeitruePage.pack_forget()
        self.inreapirPage.pack_forget()
        self.inrepairBackPage.pack_forget()
        self.inrepairReceivePage.pack_forget()

    def createreceivepage(self):
        self.root.geometry("700x250")
        self.receivePage.pack()
        self.backfactoryPage.pack_forget()
        # self.baofeicomfirmPage.pack_forget()
        self.baofeiPage.pack_forget()
        self.backPage.pack_forget()
        self.borrowPage.pack_forget()
        self.inputPage.pack_forget()
        self.updatePage.pack_forget()
        self.searchMasterPage.pack_forget()
        self.baofeitruePage.pack_forget()
        self.piciinputPage.pack_forget()
        self.inreapirPage.pack_forget()
        self.inrepairBackPage.pack_forget()
        self.inrepairReceivePage.pack_forget()

    def createbackfactorypage(self):
        self.root.geometry("700x500")
        self.backfactoryPage.pack()
        # self.baofeicomfirmPage.pack_forget()
        self.baofeiPage.pack_forget()
        self.backPage.pack_forget()
        self.borrowPage.pack_forget()
        self.inputPage.pack_forget()
        self.updatePage.pack_forget()
        self.searchMasterPage.pack_forget()
        self.receivePage.pack_forget()
        self.baofeitruePage.pack_forget()
        self.piciinputPage.pack_forget()
        self.inreapirPage.pack_forget()
        self.inrepairBackPage.pack_forget()
        self.inrepairReceivePage.pack_forget()



    def createbaofeitruepage(self):
        self.root.geometry("700x400")
        self.baofeitruePage.pack()
        # self.baofeicomfirmPage.pack_forget()
        self.baofeiPage.pack_forget()
        self.backPage.pack_forget()
        self.borrowPage.pack_forget()
        self.inputPage.pack_forget()
        self.updatePage.pack_forget()
        self.searchMasterPage.pack_forget()
        self.backfactoryPage.pack_forget()
        self.receivePage.pack_forget()
        self.piciinputPage.pack_forget()
        self.inreapirPage.pack_forget()
        self.inrepairBackPage.pack_forget()
        self.inrepairReceivePage.pack_forget()


    # def createbaofeicomfirmpage(self):
    #     self.root.geometry("800x600")
    #     # self.baofeicomfirmPage.pack()
    #     self.baofeiPage.pack_forget()
    #     self.backPage.pack_forget()
    #     self.borrowPage.pack_forget()
    #     self.inputPage.pack_forget()
    #     self.updatePage.pack_forget()
    #     self.searchMasterPage.pack_forget()
    #     self.baofeitruePage.pack_forget()


    def createsearchmasterpage(self):
        self.root.geometry("700x200")
        self.searchMasterPage.pack()
        self.backPage.pack_forget()
        self.borrowPage.pack_forget()
        self.inputPage.pack_forget()
        self.baofeiPage.pack_forget()
        self.updatePage.pack_forget()
        # self.baofeicomfirmPage.pack_forget()
        self.baofeitruePage.pack_forget()
        self.backfactoryPage.pack_forget()
        self.receivePage.pack_forget()
        self.piciinputPage.pack_forget()
        self.inreapirPage.pack_forget()
        self.inrepairBackPage.pack_forget()
        self.inrepairReceivePage.pack_forget()

    def createbackpage(self):
        self.root.geometry("700x300")
        self.backPage.pack()
        self.borrowPage.pack_forget()
        self.inputPage.pack_forget()
        self.baofeiPage.pack_forget()
        self.updatePage.pack_forget()
        self.searchMasterPage.pack_forget()
        # self.baofeicomfirmPage.pack_forget()
        self.baofeitruePage.pack_forget()
        self.backfactoryPage.pack_forget()
        self.receivePage.pack_forget()
        self.piciinputPage.pack_forget()
        self.inreapirPage.pack_forget()
        self.inrepairBackPage.pack_forget()
        self.inrepairReceivePage.pack_forget()

    def createbrorrowpage(self):
        self.root.geometry("700x300")
        self.borrowPage.pack()
        self.backPage.pack_forget()
        self.inputPage.pack_forget()
        self.baofeiPage.pack_forget()
        self.updatePage.pack_forget()
        self.searchMasterPage.pack_forget()
        # self.baofeicomfirmPage.pack_forget()
        self.baofeitruePage.pack_forget()
        self.backfactoryPage.pack_forget()
        self.receivePage.pack_forget()
        self.piciinputPage.pack_forget()
        self.inreapirPage.pack_forget()
        self.inrepairBackPage.pack_forget()
        self.inrepairReceivePage.pack_forget()

    def createupdatepage(self):
        self.root.geometry("700x300")
        self.updatePage.pack()
        self.backPage.pack_forget()
        self.borrowPage.pack_forget()
        self.inputPage.pack_forget()
        self.baofeiPage.pack_forget()
        self.searchMasterPage.pack_forget()
        # self.baofeicomfirmPage.pack_forget()
        self.baofeitruePage.pack_forget()
        self.backfactoryPage.pack_forget()
        self.receivePage.pack_forget()
        self.piciinputPage.pack_forget()
        self.inreapirPage.pack_forget()
        self.inrepairBackPage.pack_forget()
        self.inrepairReceivePage.pack_forget()

    def createbaofeipage(self):
        self.root.geometry("700x400")
        self.baofeiPage.pack()
        self.backPage.pack_forget()
        self.borrowPage.pack_forget()
        self.inputPage.pack_forget()
        self.updatePage.pack_forget()
        self.searchMasterPage.pack_forget()
        # self.baofeicomfirmPage.pack_forget()
        self.baofeitruePage.pack_forget()
        self.backfactoryPage.pack_forget()
        self.receivePage.pack_forget()
        self.piciinputPage.pack_forget()
        self.inreapirPage.pack_forget()
        self.inrepairBackPage.pack_forget()
        self.inrepairReceivePage.pack_forget()

    def createinputpage(self):
        self.root.geometry("700x400")
        self.inputPage.pack()
        self.backPage.pack_forget()
        self.borrowPage.pack_forget()
        self.baofeiPage.pack_forget()
        self.updatePage.pack_forget()
        self.searchMasterPage.pack_forget()
        # self.baofeicomfirmPage.pack_forget()
        self.baofeitruePage.pack_forget()
        self.backfactoryPage.pack_forget()
        self.receivePage.pack_forget()
        self.piciinputPage.pack_forget()
        self.inreapirPage.pack_forget()
        self.inrepairBackPage.pack_forget()
        self.inrepairReceivePage.pack_forget()

        #self.ccPage.pack_forget()
        #self.inputPage.pack_forget()
        #self.inputPage.grid_forget()

        #self.inputPage.pack()
        #self.page.pack_forget()
        #a=Add.Add(self.root)
        #a.pack()






    def inputdata(self):
        self.page.destroy()
        self.page = tk.Frame(self.root)
        self.page.pack()
        self.root.geometry("800x400")

        frm1 = tk.Frame(self.page)
        lbl_dafenlei = tk.Label(frm1, text="大分類")
        lbl_dafenlei.grid(row=1, column=1)
        txt_dafenlei = tk.Entry(frm1)
        txt_dafenlei.grid(row=1, column=2)
        lbl_zhongfenlei = tk.Label(frm1, text="中分類")
        lbl_zhongfenlei.grid(row=2, column=1)
        txt_zhongfenlei = tk.Entry(frm1)
        txt_zhongfenlei.grid(row=2, column=2)
        lbl_machine_no = tk.Label(frm1, text="設備編號")
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
        frm1.grid(column=0, row=0, sticky=tk.W)
        frm2 = tk.Frame(self.page)
        lbl_linshi_no = tk.Label(frm2, text="臨時編號")
        lbl_linshi_no.grid(row=1, column=1)
        chk_insi_no = tk.Checkbutton(frm2, onvalue="T", offvalue="F",variable=self.password)
        chk_insi_no.grid(row=1, column=2, sticky=tk.W)
        lbl_psec = tk.Label(frm2, text="規格")
        lbl_psec.grid(row=2, column=1)
        txt_psec = tk.Entry(frm2)
        txt_psec.grid(row=2, column=2)
        lbl_pr_no = tk.Label(frm2, text="請購單號")
        lbl_pr_no.grid(row=3, column=1)
        txt_pr_no = tk.Entry(frm2)
        txt_pr_no.grid(row=3, column=2)
        lbl_gsfenlei = tk.Label(frm2, text="歸屬分類")
        lbl_gsfenlei.grid(row=4, column=1)
        txt_gsfenlei = tk.Entry(frm2)
        txt_gsfenlei.grid(row=4, column=2)
        lbl_bg_master = tk.Label(frm2, text="保管主管")
        lbl_bg_master.grid(row=5, column=1)
        txt_bg_master = tk.Entry(frm2)
        txt_bg_master.grid(row=5, column=2)
        frm2.grid(column=3, row=0, sticky=tk.W, padx=20)
        frm3 = tk.Frame(self.page)
        btn_cs_machine_no = tk.Button(frm3, text="產生編號",)
        btn_cs_machine_no.grid(row=1, column=1)
        btn_save = tk.Button(frm3, text="保存", width=10)
        btn_save.grid(row=2, column=1, pady=50)
        frm3.grid(column=5, row=0, sticky=tk.N, padx=10, pady=20)
        frm4 = tk.Frame(self.page)
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
        txt_zhubanpartnm = tk.Entry(frm4, width=10)
        txt_zhubanpartnm.grid(row=1, column=2)
        txt_zhubanpartno = tk.Entry(frm4, width=10)
        txt_zhubanpartno.grid(row=1, column=3)
        txt_zhubanguige = tk.Entry(frm4, width=10)
        txt_zhubanguige.grid(row=1, column=4)
        txt_zhubanqty = tk.Entry(frm4, width=10)
        txt_zhubanqty.grid(row=1, column=5)
        # CPU
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

        # tk.Entry(self.page,textvariable=self.username).pack()
        # ck1=tk.Checkbutton(self.page, variable=self.password,onvalue="T",offvalue="F")
        #
        # def chang(event):
        #     print(self.password.get())
        #
        # ck1.bind("<Button-1>",chang)
        #
        # ck1.pack()

    def weixiu_tz(self):

        self.page.destroy()
        self.page = tk.Frame(self.root)
        self.page.pack()
        self.root.geometry("800x400")
        frm1=tk.Frame(self.page)
        btn_search=tk.Button(frm1,text="查询")
        btn_search.pack(side=tk.LEFT,padx=0)
        btn_save = tk.Button(frm1, text="保存")
        btn_save.pack(side=tk.LEFT,padx=10)
        frm1.grid(row=0,column=0,sticky=tk.N,rowspan=2)
        frm2=tk.Frame(self.page)
        tk.Label(frm2,text="设备编号").grid(row=0,column=0)
        tk.Label(frm2,text="设备名称").grid( row=1, column=0)
        tk.Label(frm2,text="配发日期").grid( row=2, column=0)
        tk.Label(frm2,text="地点").grid(row=3, column=0)
        tk.Label(frm2,text="用途").grid(row=4, column=0)
        tk.Label(frm2,text="联络人").grid( row=5, column=0)
        tk.Label(frm2,text="送修日期").grid( row=6, column=0)
        frm2.grid(row=1,column=0)




    def weixiu_qr(self):
        self.page.destroy()
        self.page = tk.Frame(self.root)
        self.page.pack()
        self.root.geometry("800x400")