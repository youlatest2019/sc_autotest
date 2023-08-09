#!/usr/bin/env python
# _*_ coding: utf-8 _*-
# @Time     : 2021/9/2 11:50
# @Author   : yangshukun
# @File     : OracleControl.py
import json
import os

import cx_Oracle
from Common.OtherFunc import *


class OracleControl():

    def __init__(self, oracle_info):
        log('Oracle数据库操作初始化开始')
        oracle_dict_instance = dict_to_obj(oracle_info)
        self.user = oracle_dict_instance.user
        self.passwd = oracle_dict_instance.pswd
        self.ip_adress = oracle_dict_instance.adress
        self.db_name = oracle_dict_instance.db_name

        self.ora = cx_Oracle.connect(self.user + '/' + self.passwd + '@' + self.ip_adress + '/' + self.db_name)
        # ora = cx_Oracle.connect('TA0859QXAZ_DM/123456@192.168.20.157:1521/orcl')-----自测代码
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

    ora = OracleControl(oracle_157_web)
    a = ora.get_data("select success_flag from NS_INSTALL_RECORD   where code = 'CK' and last_step = '5' and success_flag = '1' and version = '1.7.12.0'")
    print(a[0][0])
    if a[0][0] == 1 :
        print('sdsfg ')