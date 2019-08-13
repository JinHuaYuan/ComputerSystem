from  SqlDB import  CONDB
import  User
import  datetime
import  tkinter.messagebox as  messagebox

class BaoFeiSql(CONDB):
    def __init__(self):
        super().__init__(None)



    # 查詢设备
    def search(self, pc_no):
        dict = {}
        cur = self.conn.cursor()
        cur.execute("select * from ITcom_no1 a where a.pc_no not in(select pc_no from  ITcom_scrap1 ) and pc_no='%s' and scrap_YN='F' " % (pc_no))
        c1 = cur.fetchall()
        if (len(c1) > 0):
            for item in c1:
                dict["pc_no"] = str(item["pc_no"])
                dict["pc_name"] = str(item["pc_name"])
                dict["guobao_date"] = str(item["guobao_date"])
                dict["use_type"] = str(item["use_type"])
                dict["address"] = str(item["address"])
                dict["peifa_date"] = str(item["peifa_date"])
                dict["temp_noYN"]= str(item["temp_noYN"])
                dict["p_spec"] = str(item["p_spec"])
                dict["pr_no"] = str(item["pr_no"])
                dict["own_type"] = str(item["own_type"])
                dict["master_empno"] = str(item["master_empno"])
        return dict

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

    #保存
    def save(self,pc):

        try:
            cur = self.conn.cursor()
            sql = ""

            #插入报废主档
            sql+='''
            insert into ITcom_scrap1 values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')
            '''%(pc.pc_no.get(),pc.pc_nm.get(),pc.gb_date.get(),pc.yt.get(),pc.address.get(),
                 pc.pf_date.get(),pc.temp_noYn.get(),pc.spec.get(),pc.pr_no.get(),pc.gs_type.get(),
                 pc.master_emp.get(),pc.bf_reason.get(),pc.bf_date.get(),User.uer_code,pc.upddate.get())
            # 插入报废尾档


            #增加可利用庫存
            if (pc.zhuban_reuse.get() == "T"):
                sql += '''
                  insert into ITcom_scrap2 values('%s','%s','%s','%s','%s')
                 update ITeqm_stock set cur_qty=cur_qty+%s,psdesc=psdesc+'%s'+'報廢入庫',upduser='%s',upddate='%s'  where part_no='%s'
                               ''' % (
                    pc.pc_no.get(),pc.zhuban_part_no.get(),pc.zhuban_qty.get(),User.uer_code, pc.upddate.get(),
                    pc.zhuban_qty.get(),pc.pc_no.get(),User.uer_code, pc.upddate.get(),pc.zhuban_part_no.get()
                )
            elif  pc.zhuban_part_no.get():
                sql += '''
                               insert into ITcom_scrap2 values('%s','%s','%s','%s','%s')
                                            ''' % (
                    pc.pc_no.get(), pc.zhuban_part_no.get(), pc.zhuban_qty.get(), User.uer_code, pc.upddate.get()
                )


            if (pc.cpu_reuse.get() == "T"):
                sql += ''' 
                 insert into ITcom_scrap2 values('%s','%s','%s','%s','%s')
                update ITeqm_stock set cur_qty=cur_qty+%s,psdesc=psdesc+'%s'+'報廢入庫',upduser='%s',upddate='%s'  where part_no='%s'
                                          ''' % (
                    pc.pc_no.get(), pc.cpu_part_no.get(), pc.cpu_qty.get(), User.uer_code, pc.upddate.get(),
                    pc.cpu_qty.get(), pc.pc_no.get(), User.uer_code, pc.upddate.get(),pc.cpu_part_no.get()
                )

            elif  pc.cpu_part_no.get():
                sql += ''' 
                        insert into ITcom_scrap2 values('%s','%s','%s','%s','%s')
                                                 ''' % (
                    pc.pc_no.get(), pc.cpu_part_no.get(), pc.cpu_qty.get(), User.uer_code, pc.upddate.get()
                )


            if (pc.neicun_reuse.get() == "T"):
                sql += '''
                 insert into ITcom_scrap2 values('%s','%s','%s','%s','%s')
                update ITeqm_stock set cur_qty=cur_qty+%s,psdesc=psdesc+'%s'+'報廢入庫',upduser='%s',upddate='%s'  where part_no='%s'
                                          ''' % (
                    pc.pc_no.get(), pc.neicun_part_no.get(), pc.neicun_qty.get(), User.uer_code, pc.upddate.get(),
                    pc.neicun_qty.get(), pc.pc_no.get(), User.uer_code, pc.upddate.get(),pc.neicun_part_no.get()
                )
            elif  pc.neicun_part_no.get():
                sql += '''
                   insert into ITcom_scrap2 values('%s','%s','%s','%s','%s')
                                            ''' % (
                    pc.pc_no.get(), pc.neicun_part_no.get(), pc.neicun_qty.get(), User.uer_code, pc.upddate.get()
                )


            if (pc.yingpan_reuse.get() == "T"):
                sql += ''' 
                 insert into ITcom_scrap2 values('%s','%s','%s','%s','%s')
                update ITeqm_stock set cur_qty=cur_qty+%s,psdesc=psdesc+'%s'+'報廢入庫',upduser='%s',upddate='%s'  where part_no='%s'
                                          ''' % (
                    pc.pc_no.get(), pc.yingpan_part_no.get(), pc.yingpan_qty.get(), User.uer_code, pc.upddate.get(),
                    pc.yingpan_qty.get(), pc.pc_no.get(), User.uer_code, pc.upddate.get(),pc.yingpan_part_no.get()
                )
            elif  pc.yingpan_part_no.get():
                sql += ''' 
                 insert into ITcom_scrap2 values('%s','%s','%s','%s','%s')p
                                          ''' % (
                    pc.pc_no.get(), pc.yingpan_part_no.get(), pc.yingpan_qty.get(), User.uer_code, pc.upddate.get()
                )


            #更新主檔資料
            sql+= '''
            delete from ITcom_no2 where pc_no='%s'
            update  ITcom_no1 set scrap_YN='T' where pc_no='%s'
            
            '''%(pc.pc_no.get(),pc.pc_no.get())


            cur.execute(sql)
            self.conn.commit()
            self.conn.close()
            messagebox.showinfo("", "保存成功")


        except Exception as e:
            messagebox.showinfo("", e)


        pass
