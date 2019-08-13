from  SqlDB import  CONDB
import  User
import  datetime
import  tkinter.messagebox as messagebox

class WeiXiuSql(CONDB):
    def __init__(self):
        super().__init__(None)

    # 查詢设备
    def search(self, pc_no):
        dict = {}



        cur = self.conn.cursor()
        cur.execute(" select * from ITcom_no1 a where not exists(select * from ITcom_repair b where  a.pc_no=b.pc_no and b_status  in('10','15')) and pc_no='%s'   " % (pc_no))
        c1 = cur.fetchall()
        if (len(c1) > 0):
            for item in c1:
                dict["pc_no"] = str(item["pc_no"])
                dict["pc_name"] = str(item["pc_name"])
                dict["peifa_date"] = str(item["peifa_date"])
                dict["guobao_date"] = str(item["guobao_date"])
                dict["p_spec"] = str(item["p_spec"])
                dict["use_type"] = str(item["use_type"])
                dict["own_type"] = str(item["own_type"])
                dict["address"] = str(item["address"])
                dict["master_empno"] = str(item["master_empno"])
                dict["master_deptno"] = str(item["master_deptno"])
                dict["pspec"] = str(item["pspec"])
        return dict
    #新增通知
    def insert(self,pc):
        dict=self.search_tz(pc.pc_no.get())
        if(len(dict)>0):
            messagebox.showinfo("","該設備已經產生了維修單了，目前還沒有結案")
        else:
            cur = self.conn.cursor()
            insertsql="insert into ITcom_repair(repair_no,pc_no,guobao_date,sx_date,sx_cust,upddate,updduser,b_status,con_person,con_phone,question) "\
                        "values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(pc.upddate.get(),pc.pc_no.get(),pc.gb_date.get(),
                        pc.sx_date.get(),pc.sx_cust.get(),pc.upddate.get(),User.uer_code,'10',pc.con_person.get(),pc.con_phone.get(),pc.question.get())
            cur.execute(insertsql)
            self.conn.commit()
            self.conn.close()
            messagebox.showinfo("", "保存成功")



    #更新回廠日期和處理結果---狀態為15
    def updatebackfactory(self,pc):
        cur = self.conn.cursor()
        updatesql=" update   ITcom_repair set b_status='15',back_date='%s',ask='%s',updduser='%s',upddate='%s' where pc_no='%s' and b_status='10'  "%(
            pc.back_date.get(),  pc.ask.get(), User.uer_code, pc.upddate.get(), pc.pc_no.get()
        )
        cur.execute(updatesql)
        self.conn.commit()
        self.conn.close()
        messagebox.showinfo("", "保存成功")

    #更新領取
    def updatereceive(self,pc):

        cur = self.conn.cursor()
        updatesql = " update   ITcom_repair set b_status='20',receive_date='%s',updduser='%s',upddate='%s',receive_person='%s' where pc_no='%s'   " % (
            pc.receive_date.get(),User.uer_code, pc.upddate.get(), pc.receive_person.get(),pc.pc_no.get()
        )
        cur.execute(updatesql)
        self.conn.commit()
        self.conn.close()
        messagebox.showinfo("", "保存成功")










    #查询通知
    def search_tz(self,pc_no,b_status):
        dict = {}
        cur = self.conn.cursor()
        sql='''
        select a.pc_no,b.pc_name,b.peifa_date,b.address,b.use_type,a.con_person,a.sx_date,
        a.question,b.p_spec,b.guobao_date,b.master_empno,b.own_type,a.con_phone,a.sx_cust,b.pspec,ISNULL(back_date,'') back_date
        from ITcom_repair a join ITcom_no1 b on a.pc_no=b.pc_no where a.pc_no like '%s' and a.b_status='%s'
        '''%(pc_no,b_status)
        cur.execute(sql)
        c1 = cur.fetchall()
        if (len(c1) > 0):
            for item in c1:
                dict["pc_name"] = str(item["pc_name"])
                dict["peifa_date"] = str(item["peifa_date"])
                dict["address"] = str(item["address"])
                dict["use_type"] = str(item["use_type"])
                dict["con_person"]=str(item["con_person"])
                dict["sx_date"] = str(item["sx_date"])
                dict["question"] = str(item["question"])
                dict["p_spec"] = str(item["p_spec"])
                dict["guobao_date"] = str(item["guobao_date"])
                dict["master_empno"] = str(item["master_empno"])
                dict["own_type"] = str(item["own_type"])
                dict["con_phone"] = str(item["con_phone"])
                dict["sx_cust"] = str(item["sx_cust"])
                dict["pspec"] = str(item["pspec"])
                dict["back_date"]=str(item["back_date"])
        return dict











    #查询设备主板信息
    def search_eqm_zhuban(self,pc):
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

    #查询设备CPU信息
    def search_eqm_cpu(self,pc):
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

    #查询设备内存信息
    def search_eqm_neicun(self,pc):
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


    #更新维修确认
    def comfirm_repair(self,pc):
        cur = self.conn.cursor()
        insertsql ="update  ITcom_repair set back_date='%s',receive_date='%s',ask='%s',b_status='20',updduser='%s',upddate='%s',receive_person='%s' where pc_no='%s'"%\
                   (pc.back_date.get(),pc.receive_date.get(),pc.ask.get(),User.uer_code,pc.upddate.get(),pc.receive_person.get(),pc.pc_no.get() )
        cur.execute(insertsql)
        self.conn.commit()
        self.conn.close()

#更新pc的设备资料和设备的库存资料
    def upd_eqm(self,pc):
        cur = self.conn.cursor()
        sql=""

        try:
        #更新主档设备
            if(pc.zhuban_reuse.get()=="T"):
                sql += '''
                  update ITcom_no2 set eqm_no='%s',eqm_nm='%s',eqm_spec='%s',eqm_qty='%s',updduser='%s',upddate='%s'   where pc_no='%s' and eqm_no='%s';
                  '''%(pc.zhuban_part_no_after.get(),pc.zhuban_nm_after.get(), pc.zhuban_spec_after.get(),pc.zhuban_qty_after.get(),User.uer_code,pc.upddate.get(),pc.pc_no.get(),pc.zhuban_part_no.get())

            if (pc.cpu_reuse.get() == "T"):
                sql += '''
                     update ITcom_no2 set eqm_no='%s',eqm_nm='%s',eqm_spec='%s',eqm_qty='%s',updduser='%s',upddate='%s' where pc_no='%s' and eqm_no='%s';
                  '''%(pc.cpu_part_no_after.get(),pc.cpu_nm_after.get(), pc.cpu_spec_after.get(),pc.cpu_qty_after.get(),User.uer_code,pc.upddate.get(),pc.pc_no.get(),pc.cpu_part_no.get())

            if (pc.neicun_reuse.get() == "T"):
                sql += '''
                     update ITcom_no2 set eqm_no='%s',eqm_nm='%s',eqm_spec='%s',eqm_qty='%s',updduser='%s',upddate='%s' where pc_no='%s' and eqm_no='%s';
                      '''%(pc.neicun_part_no_after.get(),pc.neicun_nm_after.get(), pc.neicun_spec_after.get(),pc.neicun_qty_after.get(),User.uer_code,pc.upddate.get(),pc.pc_no.get(),pc.neicun_part_no.get())

            if (pc.yingpan_reuse.get() == "T"):
                sql += '''
                     update ITcom_no2 set eqm_no='%s',eqm_nm='%s',eqm_spec='%s',eqm_qty='%s',updduser='%s',upddate='%s'  where pc_no='%s' and eqm_no='%s';
                      '''%(pc.yingpan_part_no_after.get(),pc.yingapn_nm_after.get(), pc.yingpan_spec_after.get(),pc.yingapn_qty_after.get(),User.uer_code,pc.upddate.get(),pc.pc_no.get(),pc.yingpan_part_no.get())

            #更新库存
            if(pc.zhuban_reuse.get()=="T"):
                sql += ''' update ITeqm_stock set cur_qty=cur_qty+%s,psdesc=psdesc+'%s'+'維修入庫',upduser='%s',upddate='%s'  where part_no='%s'
                        update ITeqm_stock set cur_qty=cur_qty-%s,psdesc=psdesc+'%s'+'維修領用',upduser='%s',upddate='%s'  where part_no='%s'
                    ''' % (pc.zhuban_qty.get(),pc.pc_no.get(),User.uer_code,pc.upddate.get(),pc.zhuban_part_no.get(),
                           pc.zhuban_qty_after.get(),pc.pc_no.get(),User.uer_code,pc.upddate.get(), pc.zhuban_part_no_after.get())

            if (pc.cpu_reuse.get() == "T"):
                sql += ''' update ITeqm_stock set cur_qty=cur_qty+%s,psdesc=psdesc+'%s'+'維修入庫',upduser='%s',upddate='%s'  where part_no='%s'
                                   update ITeqm_stock set cur_qty=cur_qty-%s,psdesc=psdesc+'%s'+'維修領用',upduser='%s',upddate='%s'  where part_no='%s'
                               ''' % (pc.cpu_qty.get(), pc.pc_no.get(),User.uer_code,pc.upddate.get(),    pc.cpu_part_no.get(),
                                      pc.cpu_qty_after.get(), pc.pc_no.get(),User.uer_code,pc.upddate.get(),    pc.cpu_part_no_after.get())


            if (pc.neicun_reuse.get() == "T"):
                sql += '''update ITeqm_stock set cur_qty=cur_qty+%s,psdesc=psdesc+'%s'+'維修入庫',upduser='%s',upddate='%s'  where part_no='%s'
                                   update ITeqm_stock set cur_qty=cur_qty-%s,psdesc=psdesc+'%s'+'維修領用',upduser='%s',upddate='%s'  where part_no='%s'
                               ''' % (pc.neicun_qty.get(), pc.pc_no.get(),User.uer_code,pc.upddate.get(),    pc.neicun_part_no.get(),
                                      pc.neicun_qty_after.get(), pc.pc_no.get(),User.uer_code,pc.upddate.get(),    pc.neicun_part_no_after.get())


            if (pc.yingpan_reuse.get() == "T"):
                sql += ''' update ITeqm_stock set cur_qty=cur_qty+%s,psdesc=psdesc+'%s'+'維修入庫',upduser='%s',upddate='%s'  where part_no='%s'
                           update ITeqm_stock set cur_qty=cur_qty-%s,psdesc=psdesc+'%s'+'維修領用',upduser='%s',upddate='%s'  where part_no='%s'
                               ''' % (pc.yingpan_qty.get(), pc.pc_no.get(),User.uer_code,pc.upddate.get(),    pc.yingpan_part_no.get(),
                                      pc.yingpan_qty_after.get(), pc.pc_no.get(),User.uer_code,pc.upddate.get(),    pc.yingpan_part_no_after.get())
            cur.execute(sql)
            self.conn.commit()
            self.conn.close()
            messagebox.showinfo("", "保存成功")

        except Exception as e:
            messagebox.showinfo("",e)














