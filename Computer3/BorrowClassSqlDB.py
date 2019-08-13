from  SqlDB import  CONDB
import  User
import  datetime
import tkinter.messagebox as  messagebox

class BorrowSql(CONDB):
    def __init__(self):
        super().__init__(None)

    #查詢
    def search(self,pc_no):
        dict={}
        cur = self.conn.cursor()
        cur.execute("  select * from ITcom_no1 a where not exists(select * from ITcom_borrow b where  a.pc_no=b.pc_no and b_status  in('10')) and pc_no='%s'        "%(pc_no))
        c1 = cur.fetchall()
        if (len(c1)>0):
            for item in c1:
                dict["pc_no"]=str(item["pc_no"])
                dict["pc_name"] = str(item["pc_name"])
                dict["guobao_date"] = str(item["guobao_date"])
                dict["address"] = str(item["address"])
                dict["temp_noYN"] = str(item["temp_noYN"])
                dict["p_spec"] = str(item["p_spec"])
                dict["master_empno"] = str(item["master_empno"])
        else:
            cur.execute("select * from  ITcom_borrow  where b_status='10' and pc_no='%s'" % (pc_no))
            c1 = cur.fetchall()
            if (len(c1) > 0):
                for item in c1:
                    if(item["b_status"]=='10'):
                        messagebox.showinfo("", "設備已經借出")
            else:
                messagebox.showinfo("", "沒有此設備編號")
        return  dict


    #新增借用通知
    def insert(self,pc):
        cur = self.conn.cursor()
        try:
            insertsql="insert into ITcom_borrow "\
                        "values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(pc.pc_no.get(),pc.pc_nm.get(),pc.con_person.get(),
                        pc.con_phone.get(),pc.len_date.get(),pc.back_date.get(),'','10',User.uer_code,pc.upddate.get()  )
            cur.execute(insertsql)
            self.conn.commit()
            self.conn.close()
            messagebox.showinfo("", "保存成功")
        except Exception as e:
            messagebox.showinfo("",e)


    #查詢是否有維修
    def search_borrow(self,pc_no):
        dict = {}
        cur = self.conn.cursor()

        sql='''
        select a.pc_no,a.pc_name,b.guobao_date,b.address,b.temp_noYN,b.p_spec,b.master_empno
        ,a.con_person,a.len_date,a.con_phone,a.ds_back_date 
        from ITcom_borrow a join ITcom_no1 b on a.pc_no=b.pc_no
        where  a.b_status='10' and a.pc_no='%s'
        '''%(pc_no)
        cur.execute(sql)
        c1 = cur.fetchall()
        if (len(c1) > 0):
            for item in c1:
                dict["pc_no"] = str(item["pc_no"])
                dict["pc_name"] = str(item["pc_name"])
                dict["guobao_date"] = str(item["guobao_date"])
                dict["address"] = str(item["address"])
                dict["temp_noYN"] = str(item["temp_noYN"])
                dict["p_spec"] = str(item["p_spec"])
                dict["master_empno"] = str(item["master_empno"])

                dict["con_person"] = str(item["con_person"])
                dict["len_date"] = str(item["len_date"])
                dict["con_phone"] = str(item["con_phone"])
                dict["ds_back_date"] = str(item["ds_back_date"])
        return dict

    #歸還確認
    def comfirm_borrow(self,pc):
        cur = self.conn.cursor()
        try:
            sql =" update ITcom_borrow set ex_back_date='%s',b_status='%s',updduser='%s',upddate='%s' where pc_no='%s' and b_status='10'   "%(
                pc.ex_back_date.get(),'20',User.uer_code,  pc.upddate.get(),pc.pc_no.get()
            )
            cur.execute(sql)
            self.conn.commit()
            self.conn.close()
            messagebox.showinfo("", "保存成功")
        except Exception as e:
            messagebox.showinfo("", e)



