from  SqlDB import  CONDB
import  User
import  datetime
import  tkinter.messagebox as messagebox


class INWeiXiuSql(CONDB):
    def __init__(self):
        super().__init__(None)


    # 查詢设备
    def search(self, pc_no,pc):
        dict = {}
        cur = self.conn.cursor()
        cur.execute('''select * from ITcom_no1 a  where scrap_YN='F'   
and not exists( select * from  ITcom_Inrepair b where a.pc_no=b.pc_no and b.b_status in('10','15') )  and a.pc_no='%s'  '''   % (pc_no))
        c1 = cur.fetchall()
        if (len(c1) > 0):
            for item in c1:
                pc.pc_no.set(str(item["pc_no"]))
                pc.pc_nm.set(str(item["pc_name"]))
                pc.spec.set(str(item["p_spec"]))

                # dict["pc_no"] = str(item["pc_no"])
                # dict["pc_name"] = str(item["pc_name"])
                # dict["peifa_date"] = str(item["peifa_date"])
                # dict["guobao_date"] = str(item["guobao_date"])
                # dict["p_spec"] = str(item["p_spec"])
                # dict["use_type"] = str(item["use_type"])
                # dict["own_type"] = str(item["own_type"])
                # dict["address"] = str(item["address"])
                # dict["master_empno"] = str(item["master_empno"])
                # dict["master_deptno"] = str(item["master_deptno"])
                # dict["pspec"] = str(item["pspec"])
        # return dict
            return True
        else:
            messagebox.showinfo("","查無此料編")
            return False

    # 查询设备主板信息
    def search_eqm_zhuban(self, pc):
        cur = self.conn.cursor()
        sql = '''
              select * from ITcom_no2 where pc_no='%s' and LEFT(eqm_no,1)='A' and LEFT(eqm_no,4)='A001'
                ''' % (pc.pc_no.get())
        cur.execute(sql)
        c1 = cur.fetchall()
        for item in c1:
            pc.zhuban_part_no.set(item["eqm_no"])
            pc.zhuban_nm.set(item["eqm_nm"])
            pc.zhuban_spec.set(item["eqm_spec"])
            pc.zhuban_qty.set(item["eqm_qty"])

        # 查询设备CPU信息

    def search_eqm_cpu(self, pc):
        cur = self.conn.cursor()
        sql = '''
              select * from ITcom_no2 where pc_no='%s' and LEFT(eqm_no,1)='A' and LEFT(eqm_no,4)='A002'
                ''' % (pc.pc_no.get())
        cur.execute(sql)
        c1 = cur.fetchall()
        for item in c1:
            pc.cpu_part_no.set(item["eqm_no"])
            pc.cpu_nm.set(item["eqm_nm"])
            pc.cpu_spec.set(item["eqm_spec"])
            pc.cpu_qty.set(item["eqm_qty"])

        # 查询设备内存信息

    def search_eqm_neicun(self, pc):
        cur = self.conn.cursor()
        sql = '''
              select * from ITcom_no2 where pc_no='%s' and LEFT(eqm_no,1)='A' and LEFT(eqm_no,4)='A003'
                ''' % (pc.pc_no.get())
        cur.execute(sql)
        c1 = cur.fetchall()
        for item in c1:
            pc.neicun_part_no.set(item["eqm_no"])
            pc.neicun_nm.set(item["eqm_nm"])
            pc.neicun_spec.set(item["eqm_spec"])
            pc.neicun_qty.set(item["eqm_qty"])

        # 查询设备硬盘信息
    def search_eqm_yingpan(self, pc):
        cur = self.conn.cursor()
        sql = '''
               select * from ITcom_no2 where pc_no='%s' and LEFT(eqm_no,1)='A' and LEFT(eqm_no,4)='A004'
                 ''' % (pc.pc_no.get())
        cur.execute(sql)
        c1 = cur.fetchall()
        for item in c1:
            pc.yingpan_part_no.set(item["eqm_no"])
            pc.yingpan_nm.set(item["eqm_nm"])
            pc.yingpan_spec.set(item["eqm_spec"])
            pc.yingpan_qty.set(item["eqm_qty"])



    #插入主檔

    def insertINReapir(self,pc):
        cur = self.conn.cursor()
        try:
            insertsql="insert into ITcom_Inrepair  values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s') "%(
                pc.upddate.get(),pc.pc_no.get(),pc.pc_nm.get(),pc.spec.get(),pc.sx_date.get(),pc.con_person.get(),pc.con_phone.get(),
                pc.question.get(),'','','','','10',User.uer_code,pc.upddate.get()
            )
            cur.execute(insertsql)
            self.conn.commit()
            self.conn.close()
            messagebox.showinfo("","保存成功")
        except Exception as e:
             messagebox.showinfo("",e)



    #查詢內維修通知主檔,10為通知，15回廠，20結案領取
    def searchITcom_Inrepair(self,pc):
        cur = self.conn.cursor()
        sql = '''
                     select * from ITcom_Inrepair where pc_no='%s' and b_status='%s'
                       ''' % (pc.pc_no.get().strip(),pc.b_status.get()  )
        cur.execute(sql)
        c1 = cur.fetchall()
        if(len(c1)>0):
            for item in c1:
                pc.pc_nm.set(str(item["pc_name"]))
                pc.spec.set(str(item["pc_spec"]))
                pc.question.set(str(item["question"]))
            return True
        else:
            messagebox.showinfo("","查無相關資料")
            return False

    #更新回廠日期和結果,狀態為15
    def updateback(self,pc):
        cur = self.conn.cursor()
        try:
            updsql = " update ITcom_Inrepair  set  back_date='%s' , ask='%s' ,b_status='15'  where pc_no='%s' and b_status='10'  " % (
                pc.back_date.get(),pc.ask.get(),pc.pc_no.get()
            )
            cur.execute(updsql)
            self.conn.commit()
            self.conn.close()
            messagebox.showinfo("", "保存成功")
        except Exception as e:
            messagebox.showinfo("", e)



    #更新領取日期和人,狀態為20
    def updatereceive(self,pc):
        cur = self.conn.cursor()
        try:
            updsql = " update ITcom_Inrepair  set  receive_date='%s' , receive_person='%s' ,b_status='20'  where pc_no='%s' and b_status='15'  " % (
                pc.receive_date.get(),pc.receive_person.get(),pc.pc_no.get()
            )
            cur.execute(updsql)
            self.conn.commit()
            self.conn.close()
            messagebox.showinfo("", "保存成功")
        except Exception as e:
            messagebox.showinfo("", e)
