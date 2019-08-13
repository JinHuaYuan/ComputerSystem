import  tkinter as  tk
import  tkinter.messagebox as messagebox
import  datetime
import SqlDB as sql
import  tkinter.ttk as  ttk

class SearchMaster(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)

        self.pnodf1 = []
        self.pnodf2 = []


        self.root = master  # 定义内部变量root
        self.p_btype = tk.StringVar()
        self.p_mtype = tk.StringVar()
        self.pc_no = tk.StringVar()
        self.initPage()
        self.createPage()


    def initPage(self):
        dict = sql.CONDB().getpnodf1()
        for item in dict:
            self.pnodf1.append(str(item["p_btype"]) + "-" + str(item["p_btype_nm"]))

    def getpnoef2(self):
        dict = sql.CONDB().getpnodf2(self.p_btype.get()[0:2])
        if (len(dict) > 0):
            for item in dict:
                self.pnodf2.append(str(item["p_mtype"]) + "-" + str(item["p_mtype_nm"]))
                print(self.pnodf2)
        else:
            self.pnodf2.clear()


    def createPage(self):

        frm1=tk.Frame(self)




        tk.Label(frm1,text="大類型").grid(row=0,column=0)
        tk.Label(frm1,text="中類型").grid( row=1, column=0)
        tk.Label(frm1,text="設備編號").grid(row=2, column=0)

        cbo_pnodf1=ttk.Combobox(frm1,textvariable=self.p_btype,value=self.pnodf1,width=18)

        cbo_pnodf1.grid(row=0, column=1)




        def show_pnodf2(event):
            self.getpnoef2()
            cbo_pnodf2["value"] = self.pnodf2
        cbo_pnodf1.bind("<<ComboboxSelected>>", show_pnodf2)




        cbo_pnodf2=ttk.Combobox(frm1,textvariable=self.p_mtype,width=18)
        cbo_pnodf2.grid(row=1, column=1)


        tk.Entry(frm1,textvariable=self.pc_no).grid(row=2, column=1)

        def search():
            sql.CONDB().searchMaster(self)


        btn_search=tk.Button(frm1,text="查詢",command=search)
        btn_search.grid(row=3,column=0,columnspan=2)




        frm1.pack(side=tk.TOP)




        pass
