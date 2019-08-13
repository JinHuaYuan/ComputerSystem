import  tkinter as  tk
import  tkinter.ttk as ttk
import  SqlDB as sql
import  datetime
from  dateutil.relativedelta import  relativedelta
import  tkinter.messagebox as messagebox
import  User
from  tkinter.filedialog import  askopenfilename
import  pandas as pd

class PiCiAdd(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.createpage()
        filename=""

    def createpage(self):
        frm1=tk.Frame(self)
        tk.Entry(frm1).pack(side=tk.LEFT)




        def getfile():
            filename=askopenfilename(filetypes=[  ('excel files', '.xlsx')  ])
            print(filename)

            upddate=str(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))


            #導入主料編
            try:
                df=pd.DataFrame(pd.read_excel(filename,sheet_name=0,dtype={'中分類':str}))#轉為文字
               # print(df["中分類"])
                df=df.applymap(lambda x:"\'"+str(x)+"\',")
                #print(df.values)

                insertsql=""
                pici_sql=""
                for item in df.values:
                    picisql_frormat = "insert into ITcom_no1 values(%s'%s','%s','%s');"
                    insertsql = ""
                    for item2 in item:
                        insertsql+=item2
                    picisql_frormat=picisql_frormat%(insertsql,User.uer_code,User.uer_code,upddate)
                    pici_sql+=picisql_frormat
                print(pici_sql)

                #導入子件
                df1 = pd.DataFrame(pd.read_excel(filename, sheet_name=1) ) # 轉為文字
                df1 = df1.applymap(lambda x: "\'" + str(x) + "\',")
                insertsql2 = ""
                pici_sql2 = ""

                #檢測是否有主鍵設備
                # arr_pc_no=df1["設備編號"].unique()



                for item in df1.values:
                    picisql_frormat2 = "insert into ITcom_no2 values(%s'%s','%s');"
                    insertsql2 = ""
                    for item2 in item:
                        insertsql2 += item2
                    picisql_frormat2 = picisql_frormat2 % (insertsql2, User.uer_code, upddate)
                    pici_sql2 += picisql_frormat2
                print(pici_sql2)


                sql.CONDB().pici_insert(pici_sql+"\n"+pici_sql2)
            except Exception as e:
                messagebox.showinfo("",e)


        tk.Button(frm1,command=getfile,text="选择文件").pack(side=tk.LEFT)






        frm1.pack()



