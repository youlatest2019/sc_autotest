#!/usr/bin/env python
# _*_ coding: utf-8 _*-
# @Time     : 2021/9/2 11:50
# @Author   : yangshukun
# @File     : DamengControl.py
import json
import os
from Common.OtherFunc import *
import dmPython

class DamengControl():

    def __init__(self, dameng_info):
        log('Dameng数据库操作初始化开始')
        dameng_dict_instance = dict_to_obj(dameng_info)
        self.user = dameng_dict_instance.user
        self.passwd = dameng_dict_instance.pswd
        self.ip_adress = dameng_dict_instance.adress
        self.port = dameng_dict_instance.port

        self.ora = dmPython.Connection(self.user, self.passwd, self.ip_adress, port=self.port)
        # self.ora = dmPython.connect('DCABWEB', '123456789', '192.168.20.157', port=5239)  # -----自测代码
        self.cur = self.ora.cursor()

    def get_data(self, sql):
        """查询数据"""
        self.cur.execute(sql)
        res = self.cur.fetchall()
        return res

    def delete_data(self, sql):
        """删除数据"""
        self.cur.execute(sql)

    def insert_data(self, sql):
        """插入数据"""
        self.cur.execute(sql)

    def exc_sql(self, sql):
        self.cur.execute(sql)

    def close(self):
        """关闭链接，避免多次调用导致数据库链接数超额定值"""
        self.ora.close()

    def commit(self):
        self.ora.commit()

    def insert_many(self, sql, params):
        self.cur.executemany(sql, params)

    def a(self):
        self.cur.callproc('DCAB_RMM_CHECK_COMMN.CHECK_MAIN', ['RFBS', '52392', '202208M4A', 'DM_RFBS_CLDWDK', 0, 2, -2])


if __name__ == '__main__':
    from Config.BaseEnv import *

    ora = DamengControl(oracle_157_dw)
    a = ora.get_data("select * from ns_install_record")
    print(a)
