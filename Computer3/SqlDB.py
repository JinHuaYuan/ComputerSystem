import pymssql
import decimal
import  User
import  tkinter.messagebox as messagebox
import  pandas as  pd
import datetime
import xlwings as xw
class CONDB:

    def __init__(self, master=None):
        self.conn=pymssql.connect("172.18.48.215","sa","March2010","ASDB",as_dict=True)
    def getdbcon(self):
        if self.conn:
            return self.conn

    #獲取料編大分類
    def getpc_btype(self,pc_no):
        cur = self.conn.cursor()
        cur.execute("select * from ITcom_no1 where pc_no='%s'"%(pc_no))
        c1 = cur.fetchall()
        p_btype=""
        for item in c1:
            p_btype=str(item["p_btype"])
        return p_btype


    def getpnodf1(self):
       cur= self.conn.cursor()
       cur.execute("select * from ITcom_pnodf1")
       c1=cur.fetchall()
       return  c1


    def getpnodf2(self,p_btype):
       cur= self.conn.cursor()
       cur.execute("select * from ITcom_pnodf2 where p_btype='%s' "%(p_btype))
       c1=cur.fetchall()
       return  c1
    def getyongtu(self):
        cur = self.conn.cursor()
        cur.execute("select * from ITcom_typeInfo where  type_no='Y'")
        c1 = cur.fetchall()
        return c1
    def getguishu(self):
        cur = self.conn.cursor()
        cur.execute("select * from ITcom_typeInfo where  type_no='G'")
        c1 = cur.fetchall()
        return c1
    #获取过保日期
    def getwarranty_date(self,p_btype,p_mtype):
        warranty_date=""
        cur = self.conn.cursor()
        cur.execute("select * from ITcom_pnodf2 where p_btype='%s' and p_mtype='%s'"%(p_btype,p_mtype))
        c1 = cur.fetchall()
        for item in c1:
            warranty_date=item["warranty_year"]
        return warranty_date
    #輸入職號獲取部門和名字信息
    def getEmpInfo(self,emp_no):
        dict={}
        cur = self.conn.cursor()
        cur.execute("select a.dept_no+'-'+b.dept_nm as dept ,emp_no+'-'+id_nm as emp from pompersn1 a join pomdept2 b on a.dept_no=b.dept_no  where reles_dt='' and  a.emp_no='%s'   " % (emp_no))
        c1 = cur.fetchall()
        for item in c1:
            if  (item["emp"] and item["dept"]):
                dict["emp"]=item["emp"]
                dict["dept"]=item["dept"]
        return  dict

    #获取设备
    def getEqm(self,part_no,type):
        cur = self.conn.cursor()
        cur.execute("select *  from ITeqm_stock where part_no='%s' and SUBSTRING(part_no,2,3)='%s'    "%(part_no,type))
        c1 = cur.fetchall()
        return c1

    #獲取設備編號
    def getMachine_no(self,p_btype,p_mtype):
        max_no="";
        cur = self.conn.cursor()
        cur.execute(   "select MAX(SUBSTRING(pc_no,5,4)) max_no from ITcom_no1 where p_btype='%s' and p_mtype='%s'   " % (p_btype, p_mtype))


        c1 = cur.fetchall()
        for item in c1:
            if not item["max_no"]:
                max_no=p_btype+p_mtype+'001'
            else:
                max_no = p_btype + p_mtype + str(int(item["max_no"])+1).zfill(3)
        return max_no
    #新增pc
    def insertPC(self,pc):
        cur = self.conn.cursor()
        try:
            dict=self.getEmpInfo(pc.master_emp.get()[0:5])
            if (len(dict) > 0):
                pc.master_dept.set(dict["dept"])
            cur.execute("insert into ITcom_no1   values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s') "%(
                pc.p_btype.get()[0:2],pc.p_mtype.get()[0:2],pc.machine_no.get(),pc.yongtutxt.get(),pc.guishutxt.get(),pc.machine_name.get(),pc.p_spec.get(),pc.address.get(),
                pc.master_dept.get(),pc.master_emp.get(),pc.pf_date.get(),pc.warranty_date.get(),pc.pr_no.get(),pc.tem_noYN.get(),'F',pc.bz.get(),User.uer_code,User.uer_code,pc.upddate.get()
            ))
            self.conn.commit()
            self.conn.close()
            messagebox.showinfo("","保存成功")
        except Exception as e:
             messagebox.showinfo("",e)


    #新增pc的設備
    def insertPcEqm(self,pc):
        cur = self.conn.cursor()

        str=" insert into ITcom_no2 values('%s','%s','%s','%s','%s','%s','%s') ; " %(pc.machine_no.get(),pc.zhuban_part_no.get(),pc.zhuban_nm.get(),pc.zhuban_spec.get(),pc.zhuban_qty.get(),User.uer_code,pc.upddate.get()) +\
            " insert into ITcom_no2 values('%s','%s','%s','%s','%s','%s','%s') ; "%(pc.machine_no.get(),pc.cpu_part_no.get(),pc.cpu_nm.get(),pc.cpu_spec.get(),pc.cpu_qty.get(),User.uer_code,pc.upddate.get())+\
            " insert into ITcom_no2 values('%s','%s','%s','%s','%s','%s','%s') ; "%(pc.machine_no.get(),pc.neicun_part_no.get(),pc.neicun_nm.get(),pc.neicun_spec.get(),pc.neicun_qty.get(),User.uer_code,pc.upddate.get())+ \
            " insert into ITcom_no2 values('%s','%s','%s','%s','%s','%s','%s') ; " % (pc.machine_no.get(), pc.yingpan_part_no.get(),pc.yingpan_nm.get(),pc.yingpan_spec.get(), pc.yingpan_qty.get(), User.uer_code, pc.upddate.get())

        try:
            cur.execute(str)
            self.conn.commit()
            self.conn.close()
        except Exception as e:
             messagebox.showinfo("",e)

     #查詢庫存主管
    def searchMaster(self,pc):
        searchsql='''
select a.p_btype as 大分类,d.p_btype_nm as 大分类名称,p_mtype as 中分类,p_btype_nm as 中分类名称,
a.pc_no as 设备编号,a.use_type as 用途,a.own_type as 归属分类,a.pc_name as 设备名称
,a.p_spec as 规格,a.address as 地点,a.master_deptno as 单位 ,a.master_empno as 保管主管,
a.peifa_date as 配发日期,a.guobao_date as 过保日期,a.pr_no as 请购单号, a.scrap_YN as 报废否 ,b.len_date as 借出日期,
b.ds_back_date as 计划归还日期,b.ex_back_date as 实际归还日期,b.con_person as 联系人,c.eqm_no as 子件编号,
c.eqm_nm as 子件名称,a.pspec as 备注
 from ITcom_no1 a 
left join ITcom_borrow b on a.pc_no=b.pc_no
left join ITcom_no2 c on a.pc_no=b.pc_no
left join ITcom_pnodf1 d on d.p_btype=a.p_btype
where 1=1
'''
        if(pc.p_btype.get()):
            searchsql+=" and a.p_btype='%s'"%(pc.p_btype.get()[0:2])
        if(pc.p_mtype.get()):
            searchsql += " and a.p_mtype='%s'" % (pc.p_mtype.get()[0:2])
        if (pc.pc_no.get()):
            searchsql += " and a.pc_no='%s'" % (pc.pc_no.get())

        df=pd.DataFrame(pd.read_sql(searchsql,self.conn))

        nowtime=datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        df.to_excel("查詢庫存主管"+nowtime+'.xlsx',index=False)
        print("產生報表成功報表名為" + "查詢庫存主管" + nowtime + '.xlsx')
        app = xw.App(visible=True, add_book=False)
        excel_client = app.books.open("查詢庫存主管" + nowtime + '.xlsx')




    #批次導入
    def pici_insert(self,sql):
        cur = self.conn.cursor()
        try:
            cur.execute(sql)
            self.conn.commit()
            self.conn.close()
            messagebox.showinfo("","導入成功")
        except Exception as e:
            messagebox.showinfo("", e)





















