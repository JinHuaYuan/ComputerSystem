from  SqlDB import  CONDB
import  User
import  datetime
import  tkinter.messagebox as messagebox

class UpdateSql(CONDB):
    def __init__(self):
        super().__init__(None)

    #查詢
    def search(self,pc_no):
        dict={}
        cur = self.conn.cursor()
        cur.execute("select * from ITcom_no1 where   scrap_YN='F' and  pc_no='%s'"%(pc_no))
        c1 = cur.fetchall()
        if (len(c1)>0):
            for item in c1:
                dict["pc_no"]=str(item["pc_no"])
                dict["pc_name"] = str(item["pc_name"])
                dict["peifa_date"] = str(item["peifa_date"])
                dict["guobao_date"] = str(item["guobao_date"])
                dict["p_spec"] = str(item["p_spec"])
                dict["use_type"] = str(item["use_type"])
                dict["own_type"] = str(item["own_type"])
                dict["address"] = str(item["address"])
                dict["master_empno"] = str(item["master_empno"])
                dict["master_deptno"] = str(item["master_deptno"])

        return  dict


    #修改
    def updat(self,pc):
        dict = self.getEmpInfo(pc.master_emp_after.get()[0:5])
        if (len(dict) > 0):
            pc.master_dpt_after.set(dict["dept"])
    #更新主檔和插入異動前後擋
        cur = self.conn.cursor()

        try:
            updateSql=""
            if  pc.pc_no_after.get():
                updateSql = "  update  ITcom_no1 set use_type='%s',own_type='%s',address='%s',master_deptno='%s',master_empno='%s',pc_no='%s'  where pc_no='%s' " \
                            % (pc.yt_after.get(), pc.gs_after.get(), pc.add_after.get(), pc.master_dpt_after.get(),
                               pc.master_emp_after.get(), pc.pc_no_after.get(),pc.pc_no.get()) + \
                            "  insert into  ITcom_no_stkchg values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" \
                            % (pc.upddate.get(), pc.pc_no_after.get(), pc.yt_before.get(), pc.yt_after.get(), pc.gs_before.get(),
                               pc.gs_after.get(), pc.add_before.get(), pc.add_after.get(),
                               pc.master_dpt_before.get(), pc.master_dpt_after.get(), pc.master_emp_before.get(),
                               pc.master_emp_after.get(), User.uer_code, pc.upddate.get())+\
                            " update ITcom_no2 set pc_no='%s' where pc_no='%s'"%(pc.pc_no_after.get(),pc.pc_no.get())
            else:
                updateSql="  update  ITcom_no1 set use_type='%s',own_type='%s',address='%s',master_deptno='%s',master_empno='%s'  where pc_no='%s' "\
                          %(pc.yt_after.get(),pc.gs_after.get(),pc.add_after.get(),pc.master_dpt_after.get(),pc.master_emp_after.get(),pc.pc_no.get())+\
                          "  insert into  ITcom_no_stkchg values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"\
                          %(pc.upddate.get(),pc.pc_no.get(),pc.yt_before.get(),pc.yt_after.get(),pc.gs_before.get(),pc.gs_after.get(),pc.add_before.get(),pc.add_after.get(),
                            pc.master_dpt_before.get(),pc.master_dpt_after.get(),pc.master_emp_before.get(),pc.master_emp_after.get(),User.uer_code,pc.upddate.get())

            cur.execute(updateSql)
            self.conn.commit()
            self.conn.close()
            messagebox.showinfo("","保存成功")
        except Exception as e:
            messagebox.showinfo("", e)




